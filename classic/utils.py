class Node:
    def __init__(self, val, children=None, parent=None):
        if children is None:
            children = []
        self.val = val
        self.children = children
        self.parent = parent

    def __repr__(self):
        if len(self.children) == 0:
            return self.val
        else:
            return f"{self.val}: {self.children}"


def adj_matrix_to_tree(adj_matrix, alphabetical=True):
    N, M = adj_matrix.shape
    assert N == M

    def get_code(x):
        if alphabetical:
            return chr(x + 65)
        else:
            return f"N{x}"

    nodes = {i: Node(get_code(i)) for i in range(N)}
    for i in range(N):
        for j in range(M):
            if adj_matrix[i, j] != 0.0:
                nodes[i].children.append(nodes[j])
                nodes[j].parent = nodes[i]
    ret_node = None
    # Find parentless node
    for node in nodes.values():
        if node.parent is None:
            if ret_node is not None:
                raise ValueError("Cannot convert to tree")
            ret_node = node
    return ret_node
