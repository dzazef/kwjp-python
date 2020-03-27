import math
import os
import sys

from sympy.ntheory import isprime  # Miler - Rabin
from random import randint


class RSA:
    """Klasa obsługująca szyfrowanie RSA

    Pozwala na generowanie kluczy, jak i kodowanie/dekodowanie prostej wiadomości
    zapisanej za pomocą znaków z tabeli ASCII.
    """

    def _gen_prime(self, bits):
        """Generowanie liczby pierwszej o danej długości bitów"""
        k = 0
        while not isprime(k):
            k = randint(2 ** (bits - 1), 2 ** bits)
        return k

    def _xgcd(self, a, b):
        """Rozszerzony algorytm Euklidesa"""
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            q, a, b = b // a, b % a, a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def _mod_mult_inv(self, a, n):
        """Znajdowanie odwrotności modulo"""
        g, x, _ = self._xgcd(a, n)
        if g != 1:
            raise Exception('a and n are not coprime')
        return x % n

    def mod_power(self, x, y, p):
        """Obliczanie x**y % p"""
        res = 1
        x = x % p
        while y > 0:
            if (y & 1) == 1:
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    def gen_keys(self, bits):
        """Generowanie kluczy"""
        if bits < 8:
            raise Exception('bits should be >8')
        p = self._gen_prime(bits)
        q = self._gen_prime(bits)
        euler = (p - 1) * (q - 1)
        n = p * q
        del p, q
        e = int(math.sqrt(euler))
        e = e if e % 2 != 0 else e + 1
        while self._xgcd(e, euler)[0] != 1:
            e += 2
        d = self._mod_mult_inv(e, euler)
        return (n, e), (n, d)

    def gen_keys_to_file(self, bits, path):
        """Zapis wygenerowanych kluczy do pliku"""
        key_pub, key_prv = self.gen_keys(bits)
        with open(os.path.join(path, 'key.pub'), 'w') as f:
            f.write(str(key_pub[0]) + '\n')
            f.write(str(key_pub[1]))
        with open(os.path.join(path, 'key.prv'), 'w') as f:
            f.write(str(key_prv[0]) + '\n')
            f.write(str(key_prv[1]))

    def code(self, path, data):
        """Kodowanie ciągu znaków"""
        if not os.path.isfile(os.path.join(path, "key.pub")):  # wczytaj klucz publiczny
            raise Exception("public key not found")
        with open(os.path.join(path, "key.pub")) as f:
            n = int(f.readline())
            e = int(f.readline())
        # zamień każdy znak na liczbę o dł. 3 z zerami z przodu, dodaj 1 z przodu dla paddingu
        data = '1' + ''.join([('0' * (3 - len(str(ord(c))))) + str(ord(c)) for c in data])
        res = str(self.mod_power(int(data), e, n))
        return res

    def decode(self, path, data):
        """Dekodowanie ciągu znaków"""
        res = ''
        if not os.path.isfile(os.path.join(path, "key.prv")):  # wczytaj klucz prywatny
            raise Exception("private key not found")
        with open(os.path.join(path, "key.prv")) as f:
            n = int(f.readline())
            d = int(f.readline())
        t = str(self.mod_power(int(data), d, n))
        idx = 1
        while idx < len(t):  # Zamieniaj liczbę dł. 3 na znak
            res += chr(int(t[idx:(idx + 3)]))
            idx += 3
        return res


# Sprawdzenie poprawności parametrów i wywołanie odpowiadającej funkcji
if len(sys.argv) != 3:
    raise Exception('Incorrect number of parameters')

if sys.argv[1] == "--gen-keys":
    _bits = int(sys.argv[2])
    RSA().gen_keys_to_file(_bits, './')
elif sys.argv[1] == "--encrypt":
    _data = sys.argv[2]
    print(RSA().code('./', _data))
elif sys.argv[1] == '--decrypt':
    _data = sys.argv[2]
    print(RSA().decode('./', _data))
else:
    raise Exception('Incorrect parameter')
