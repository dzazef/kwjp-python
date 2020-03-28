def flatten(list_):
    """Generator for flattening a list"""
    for elem in list_:
        if type(elem) != list:
            yield elem
        else:
            yield from flatten(elem)


gen = flatten([[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7,
               [[9, [123, [[123]]]], 10]])
for e in gen:
    print(e)
