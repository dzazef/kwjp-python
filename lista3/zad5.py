def powerset(set_):
    """Powerset using map and lambda"""
    return (powerset(set_[1:]) +
            list(map(lambda x: x + [set_[0]], powerset(set_[1:])))
            if len(set_) > 0 else [[]])


print(powerset([1, 2, 3, 4]))
