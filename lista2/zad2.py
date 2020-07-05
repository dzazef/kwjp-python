import binascii
import sys


class Base64:
    """Klasa kodująca/dekodująca do kodu Base64"""
    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __init__(self):
        """Sprawdzanie poprawności parametrów"""
        if len(sys.argv) != 4:
            raise Exception('Incorrect number of parameters')
        else:
            if sys.argv[1] == '--encode':
                self.encode_mode = True
            elif sys.argv[1] == '--decode':
                self.encode_mode = False
            else:
                raise Exception('incorrect parameter, choose \'--encode\' or \'--decode\'')
            self.file_read = sys.argv[2]
            self.file_write = sys.argv[3]

    def _ascii_to_8bin(self, _asc):
        """Zamienia znak na 8bitowy ciąg zer i jedynek"""
        f = format(_asc, 'b')
        res = '0' * (8 - len(f)) + f
        assert len(res) == 8
        return res

    def _dec_to_6bin(self, _dec):
        """Zamienia liczbę na 6bitowy ciąg zer i jedynek"""
        s = "{0:b}".format(_dec)
        res = '0' * (6 - len(s)) + s
        assert len(res) == 6
        return res

    def _file_to_binstr(self, _file):
        """Zamienia dane z pliku na ciąg zer i jedynek"""
        with open(_file, 'rb') as f:
            data = f.read()
            bin_str = ''.join(self._ascii_to_8bin(x) for x in data)
        return bin_str

    def _file_to_str(self, _file):
        """Czyta dane z pliku"""
        with open(_file, 'r') as f:
            data = f.read()
        return data

    def encode(self):
        """Zamienia dane z pliku na kod Base64"""
        res = ''
        bin_str = self._file_to_binstr(self.file_read)
        idx = 0
        while idx < len(bin_str):
            curr_str = bin_str[idx:(idx + 6)]
            curr_int = int(curr_str, 2)
            res += self.base64[curr_int]
            idx += 6
        return res

    def decode(self):
        """Odszyfrowuje dane z pliku, które są zapisane w kodzie Base64"""
        res = ''
        enc_str = self._file_to_str(self.file_read)
        bin_str = ''.join(self._dec_to_6bin(self.base64.find(c)) for c in enc_str)
        idx = 0
        while idx < len(bin_str):
            curr_str = bin_str[idx:(idx + 8)]
            res += chr(int(curr_str, 2))
            idx += 8
        return res

    def code(self):
        """Wywyołuje odpowiednią metodę i zapisuje dane do pliku"""
        res = self.encode() if self.encode_mode else self.decode()
        with open(self.file_write, 'w') as f:
            f.write(res)


Base64().code()
