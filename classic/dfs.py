"""
Depth first search
"""

from utils import adj_matrix_to_tree
import numpy as np
from collections import deque

adj_mat = np.zeros((7, 7))
adj_mat[0] = [0, 1, 1, 0, 1, 0, 0]
adj_mat[1] = [0, 0, 0, 1, 0, 1, 0]
adj_mat[2] = [0, 0, 0, 0, 0, 0, 1]
G = adj_matrix_to_tree(adj_mat)
print("Graph", G)

S = deque([G])
visited = set()
while len(S) != 0:
    v = S.pop()
    if v not in visited:
        visited.add(v)
        print(f"Visited {v.val}")
        for w in v.children:
            S.append(w)
