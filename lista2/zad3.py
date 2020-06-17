import sys
import os


class FileRenamer:
    """Klasa obsługująca zamianę plików na z małej litery rekursywnie w danym katalogu"""

    def __init__(self):
        """Sprawdza poprawność parametrów"""
        if len(sys.argv) != 2:
            raise Exception('Incorrect number of parameters')
        else:
            _dir = sys.argv[1]
            self.dir = _dir if _dir[-1] == '/' else _dir + '/'

    def small_case(self):
        """Zamienia wszystkie nazwy na z małej litery rekursywnie w danym katalogu"""
        for curr_dir, dir_names, file_names in os.walk(self.dir):
            for f_name in file_names:
                fn_split = f_name.split('.')
                new_fn = fn_split[0].lower() + f_name[len(fn_split[0]):]  # zachowaj rozszerzenie
                old_path, new_path = os.path.join(curr_dir, f_name), os.path.join(curr_dir, new_fn)
                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f'Renamed \'{os.path.join(curr_dir, f_name)}\' '
                          f'to \'{os.path.join(curr_dir, new_fn)}\'')


FileRenamer().small_case()
