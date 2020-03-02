from random import randint

_n = 10


def generate_string(n):
    value = ""
    for i in range(n):
        r = randint(0, 2)
        if r is 0:
            value += 'a'
        elif r is 1:
            value += 'b'
        else:
            value += 'c'
    return value


def generate_list(n, k):
    values = []
    for i in range(n):
        values.append(generate_string(k))
    return values


def string_to_dict(s):
    _dict = {}
    for i in range(len(s)):
        if s[i] != '*':
            _dict[i] = s[i]
    return _dict


def find_matches(patt_dict, value_list):
    matches = []
    for val in value_list:
        flag_match = True
        for idx in patt_dict:
            if patt_dict[idx] != val[idx]:
                flag_match = False
        if flag_match:
            matches.append(val)
    return matches


def run(n, k):
    rand_str_list = generate_list(n, k)
    print(rand_str_list)

    x = input('\033[0;36m$:\033[0m ')
    for c in x:
        if (c is not 'a' and c is not 'b' and c is not 'c' and c is not '*') \
                or len(x) != _n:
            raise Exception('Incorrect string')

    patt_dict = string_to_dict(x)
    matches = find_matches(patt_dict, rand_str_list)
    print(matches)


run(_n, _n)
