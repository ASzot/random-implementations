"""
Breadth first search
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

Q = deque([G])
visited = set([G])
while len(Q) != 0:
    v = Q.popleft()
    print(f"Visited {v.val}")
    for w in v.children:
        if w not in visited:
            visited.add(w)
            Q.append(w)
