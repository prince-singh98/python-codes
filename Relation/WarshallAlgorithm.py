import numpy as np

M = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])
x = len(M)


def warshall(M):
    assert(len(row) == len(M) for row in M)
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = M[i][j] or (M[i][k] and M[k][j])
    return M


print("The given relation is: ")
print(M)
print("Transitive Closure is: ")
print(warshall(M))
