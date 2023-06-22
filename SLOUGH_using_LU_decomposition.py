def LU(A, L, U, n):
    for i in range(n):
        for j in range(i, n):
            L[j][i] = U[j][i] / U[i][i]

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]

        for i in range(k, n):
            for j in range(k - 1, n):
                U[i][j] = U[i][j] - L[i][k - 1] * U[k - 1][j]


def proisv(A, B, R, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += A[i][k] * B[k][j]


def solve(A, B, X, n):
    L = [[0] * n for _ in range(n)]
    U = A.copy()

    # LU разложение
    for i in range(n):
        for j in range(i, n):
            L[j][i] = U[j][i] / U[i][i]

        for k in range(i + 1, n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]

            for j in range(i + 1, n):
                U[k][j] = U[k][j] - L[k][i] * U[i][j]

    # Прямой ход
    Y = [0] * n
    for i in range(n):
        Y[i] = B[i]
        for j in range(i):
            Y[i] -= L[i][j] * Y[j] 

    # Обратный ход
    for i in range(n - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, n):
            X[i] -= U[i][j] * X[j]
        X[i] /= U[i][i]


def show(A, n):
    for i in range(n):
        for j in range(n):
            print("\t", A[i][j], "\t", end="")
        print()


n = 3
L = [[0] * n for _ in range(n)]
R = [[0] * n for _ in range(n)]

A = [[2, -1, 0],
     [-1, 2, -1],
     [0, -1, 2]]

print("First matrix:")
show(A, n)
U = A.copy()
LU(A, L, U, n)
print("U matrix:")
show(U, n)
print("L matrix:")
show(L, n)
proisv(L, U, R, n)
print("L*U matrix:")
show(R, n)

B = [1, 1, 1]  # Вектор свободных членов
X = [0] * n    # Вектор неизвестных

solve(A, B, X, n)

print("Solution:")
for i in range(n):
    print("x{} = {}".format(i+1, X[i]))
