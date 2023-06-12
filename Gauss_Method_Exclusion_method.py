import numpy as np

def gaussian_elimination(A, b):
    n = A.shape[0]  # Размерность матрицы A
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)  # Объединяем матрицу A и вектор b

    for i in range(n - 1):
        # Поиск ведущего элемента по столбцам
        max_index = np.argmax(np.abs(Ab[i:, i])) + i
        if max_index != i:
            Ab[[i, max_index]] = Ab[[max_index, i]]  # Меняем строки местами

        # Приведение матрицы к треугольному виду
        pivot = Ab[i, i]
        if pivot == 0:
            raise ValueError("Матрица A вырождена, нет решений")

        Ab[i] /= pivot  # Деление строки на ведущий элемент

        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]  # Множитель для преобразования строк
            Ab[j] -= factor * Ab[i]

    # Обратный ход
    x = np.zeros(n)
    x[n - 1] = Ab[n - 1, n]
    for i in range(n - 2, -1, -1):
        x[i] = Ab[i, n] - np.dot(Ab[i, i + 1:n], x[i + 1:n])

    return x

# Пример использования
A = np.array([[2, 1, -1],
              [3, 2, 1],
              [1, -1, 2]], dtype=float)

b = np.array([4, 2, 3], dtype=float)

x = gaussian_elimination(A, b)
print("Метод Гаусса: метод исключения (правило прямоугольника), выбор ведущего элемента по столбцам:")
print(x)

