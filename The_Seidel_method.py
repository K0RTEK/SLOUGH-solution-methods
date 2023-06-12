import numpy as np


def seidel_solve(A, b, max_iterations=100, tolerance=1e-6):
    n = A.shape[0]
    x = np.zeros(n)  # Начальное приближение

    for _ in range(max_iterations):
        x_new = np.copy(x)

        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, (i + 1):], x[(i + 1):])) / A[i, i]

        if np.linalg.norm(x_new - x) < tolerance:
            break

        x = x_new

    return x


# Пример использования
A = np.array([[4, 1, -1],
              [2, 7, 1],
              [1, 1, 3]])

b = np.array([3, 19, 1])

x = seidel_solve(A, b)
print("Метод Зейделя:")
print(x)

