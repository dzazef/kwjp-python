from random import randint, random


def gen_rand_full_tree(height):
    """Generate random full binary tree of given height"""
    return (None if height == 0
            else [randint(0, 100),
                  gen_rand_full_tree(height - 1),
                  gen_rand_full_tree(height - 1)])


def gen_new_value(last_leafs, only_leafs, density=0.9):
    """Generate value of new leaf."""
    if len(last_leafs) > 1 or not only_leafs:
        return randint(0, 100) if density > random() else None
    else:
        return randint(0, 100)


def create_new_leaf(new_value, new_last_leafs, only_leafs):
    """Create new leaf."""
    if new_value is None:
        return (None, True) if only_leafs else (None, False)
    else:
        new_leaf = [new_value, None, None]
        new_last_leafs.append(new_leaf)
        return new_leaf, False


def gen_rand_tree(height, density=0.9):
    """Generate random not full binary tree of given height."""
    tree = [randint(0, 100), None, None]
    last_leafs = [tree]
    for i in range(height - 1):
        only_leafs = True  # True if all generated value are leafs
        new_last_leafs = []
        while len(last_leafs):
            c_leaf = last_leafs.pop()
            # Create left child
            new_value_l = gen_new_value(last_leafs, only_leafs, density)
            new_leaf_l, only_leafs = \
                create_new_leaf(new_value_l, new_last_leafs, only_leafs)
            c_leaf[1] = new_leaf_l
            # Create right child
            new_value_r = gen_new_value(last_leafs, only_leafs, density)
            new_leaf_r, only_leafs = \
                create_new_leaf(new_value_r, new_last_leafs, only_leafs)
            c_leaf[2] = new_leaf_r
        last_leafs = new_last_leafs
    return tree


def bfs(tree):
    """Generator for BFS. Works only for trees (no cycle)."""
    queue = [tree]
    while len(queue):
        elem = queue.pop(0)
        yield elem[0]
        if elem[1] is not None:
            queue.append(elem[1])
        if elem[2] is not None:
            queue.append(elem[2])


def dfs(tree):
    """Generator for DFS. Works only for trees (no cycle)."""
    stack = [tree]
    while len(stack):
        elem = stack.pop(-1)
        yield elem[0]
        if elem[2] is not None:
            stack.append(elem[2])
        if elem[1] is not None:
            stack.append(elem[1])


if __name__ == '__main__':
    _tree = gen_rand_tree(4)
    print(_tree)
    for node in bfs(_tree):
        print(node, end=' ')
    print()
    for node in dfs(_tree):
        print(node, end=' ')
