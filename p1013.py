def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


#V = []2 10
N = int(input())
K = int(input())
M = int(input())
#V.append(0)#0
#V.append(K - 1)#1
#for i in range(2, N+1):
#    V.append((V[0] + V[1]) * (K - 1))
#    V.pop(0)
print(fib(N)*(K-1))

