from random import randint, random


class NodeTypeError(Exception):
    """Error raised when type of child is incorrect"""
    pass


class Node:
    """Node of tree"""

    def __init__(self, value=None):
        """Set initial values"""
        self._value = value
        self._children = []

    @property
    def value(self):
        """Get value of node"""
        return self._value

    @value.setter
    def value(self, value):
        """Set value of node"""
        self._value = value

    @property
    def children(self):
        """Get children of node"""
        return self._children

    @children.setter
    def children(self, nodes):
        """Set children of node"""
        self._children = []
        self.append_children(nodes)

    def append_children(self, *nodes):
        """Append children of node"""
        for node in nodes:
            if not isinstance(node, Node):
                raise NodeTypeError()
            self._children.append(node)


class Tree:
    """Class representing tree"""

    def __init__(self):
        self._tree = None

    @property
    def tree(self):
        return self._tree

    def _gen_new_value(self, last_leafs, only_leafs, density=0.9):
        """Generate value of new leaf."""
        if len(last_leafs) > 1 or not only_leafs:
            return randint(0, 100) if density > random() else None
        else:
            return randint(0, 100)

    def gen_rand_tree(self, height, max_children=2, density=0.9):
        """Generate random not full binary tree.

        :param height: height of tree
        :param max_children: max. number of children
        :param density: density of tree
        """
        t = Node(randint(0, 100))
        last_leafs = [t]
        for i in range(height - 1):
            only_leafs = True
            new_last_leafs = []
            while len(last_leafs):
                c_leaf = last_leafs.pop()
                for j in range(max_children):
                    new_value = \
                        self._gen_new_value(last_leafs, only_leafs, density)
                    if new_value is not None:
                        only_leafs = False
                        new_leaf = Node(new_value)
                        new_last_leafs.append(new_leaf)
                        c_leaf.append_children(new_leaf)
            last_leafs = new_last_leafs
            self._tree = t
        return t

    def bfs(self):
        """Generator for BFS. Works only for trees (no cycle)."""
        if self._tree is None:
            raise Exception('Tree not created')
        queue = [self._tree]
        while len(queue):
            node = queue.pop(0)
            yield node.value
            queue += node.children

    def dfs(self):
        """Generator for DFS. Works only for trees (no cycle)."""
        if self._tree is None:
            raise Exception('Tree not created')
        stack = [self._tree]
        while len(stack):
            node = stack.pop(-1)
            yield node.value
            stack += node.children


if __name__ == '__main__':
    tree = Tree()
    tree.gen_rand_tree(4, max_children=3, density=0.9)
    for _node in tree.bfs():
        print(_node, end=' ')
    print()
    for _node in tree.dfs():
        print(_node, end=' ')
