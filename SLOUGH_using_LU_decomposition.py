import numpy as np


def lu_solve(A, b):
    n = A.shape[0]

    # LU разложение
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n):
        U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
        L[(k + 1):, k] = (A[(k + 1):, k] - L[(k + 1):, :k] @ U[:k, k]) / U[k, k]

    # Решение СЛАУ Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - L[i, :i] @ y[:i]

    # Решение СЛАУ Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]

    return x


# Пример использования
A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

b = np.array([1, 0, 1])

x = lu_solve(A, b)
print("Решение СЛАУ с помощью LU разложения:")
print(x)

