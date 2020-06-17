

def sum_of_last_columns(file):
    """Returns sum of last columns in file"""
    with open(file) as f:
        bytes_ = sum([int(line.split(' ')[-1]) for line in f.readlines()])
        print(f'Całkowita liczba bajtów: {bytes_}')


sum_of_last_columns('assets/zad3.txt')
