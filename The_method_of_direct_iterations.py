import numpy as np

# Определение размерности СЛАУ
n = 3

# Определение матрицы коэффициентов размерности n x n
A = np.array([[2, 1, -1],
              [3, 2, 1],
              [1, -1, 2]])

# Определение вектора свободных членов размерности n
b = np.array([4, 2, 3])

# Максимальное число итераций
max_iter = 100
# Порог сходимости
tolerance = 1e-6

# Начальное приближение
x = np.zeros(n)

# Прямые итерации
for i in range(max_iter):
    x_new = np.zeros(n)
    for j in range(n):
        x_new[j] = (b[j] - np.dot(A[j, :j], x[:j]) - np.dot(A[j, j + 1:], x[j + 1:])) / A[j, j]
    if np.linalg.norm(x_new - x) < tolerance:
        break
    x = x_new

# Вывод решения
print("Метод прямых итераций:")
print(x)

