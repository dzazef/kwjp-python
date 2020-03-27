import os
import sys


class WordCount:
    """Klasa obliczająca zadane właśności pliku"""

    def __init__(self):
        """Sprawdza poprawność parametrów"""
        if len(sys.argv) != 2:
            raise Exception('Incorrect number of parameters')
        else:
            self.file = sys.argv[1]

    def count(self):
        """Oblicza zadane właśności pliku"""
        max_line = 0
        lines = 0

        bytes_ = os.stat(self.file).st_size  # liczba bajtów
        with open(self.file) as f:
            words = len(f.read().split())  # liczba słów
        with open(self.file) as f:
            for line in f:
                lines += 1  # zliczanie linii
                if len(line) > max_line:
                    max_line = len(line)  # aktualizacja dł. maks. linii
        return lines, max_line, words, bytes_


_lines, _max_line, _words, _bytes = WordCount().count()
print(f'lines: {_lines}\nmax line: {_max_line}\nwords: {_words}\nbytes: {_bytes}')
