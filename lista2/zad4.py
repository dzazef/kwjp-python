import sys
import os
import hashlib


class RepChecker:
    """Klasa wypisujący zbiory plików o tej samej zawartości"""

    def __init__(self):
        """Sprawdza poprwaność parametrów"""
        if len(sys.argv) != 2:
            raise Exception('Incorrect number of parameters')
        else:
            _dir = sys.argv[1]
            self.dir = _dir if _dir[-1] == '/' else _dir + '/'

    def _pretty_print(self, res):
        """Wypisuje wynik w ładnym formacie"""
        for _list in res:
            if len(_list) > 1:
                print("-----------------------")
                for elem in _list:
                    print(elem)

    def _check_equal(self, file1, file2):
        """Sprawdza czy dane pliki mają taką samą zawartość"""
        f1_size = os.stat(file1).st_size
        f2_size = os.stat(file2).st_size
        with open(file1) as f1:
            f1_data = f1.read()
            f1_hash = hashlib.md5(f1_data.encode()).hexdigest()
        with open(file2) as f2:
            f2_data = f2.read()
            f2_hash = hashlib.md5(f2_data.encode()).hexdigest()
        equals = (f1_size == f2_size) and (f1_hash == f2_hash)
        return equals

    def _find(self, lists, elem):
        """Zwraca na którym miejscu w wyniku znajduje sie lista zawierająca element"""
        for i in range(len(lists)):
            if elem in lists[i]:
                return i
        return -1

    def _union(self, lists, elem1, elem2):
        """Łączy zbiory zawierające pliki o tej samej zawartości"""
        idx1 = self._find(lists, elem1)
        idx2 = self._find(lists, elem2)
        assert idx1 >= 0 and idx2 >= 0
        if idx1 != idx2:
            lists[idx1].append(elem2)
            lists[idx2].remove(elem2)

    def check(self):
        """Znajduje zbiory plików o tej samej zawartości"""
        for curr_dir, dir_names, file_names in os.walk(self.dir):
            cur_res = [[os.path.join(curr_dir, fn)] for fn in file_names]
            for fn1 in file_names:
                full_fn1 = os.path.join(curr_dir, fn1)
                for fn2 in file_names:
                    full_fn2 = os.path.join(curr_dir, fn2)
                    if self._check_equal(full_fn1, full_fn2):
                        self._union(cur_res, full_fn1, full_fn2)
            self._pretty_print(cur_res)


RepChecker().check()
