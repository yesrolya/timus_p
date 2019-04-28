def find_numbers (A, N1, B, N2, sum):
    i = 0
    j = 0
    while i < N1 and j < N2:
        if A[i] + B[j] == sum:
            return True
        while i < N1 and j < N2 and A[i] + B[j] < sum:
            i += 1
        if i >= N1:
            return False
        while i < N1 and j < N2 and A[i] + B[j] > sum:
            j += 1
        if j >= N2:
            return False
        if A[i] + B[j] == sum:
            return True
    return False


sum = 10000
N1 = int(input())
A = []
for i in range(0, N1):
    A.append(int(input()))
N2 = int(input())
B = []
for i in range(0, N2):
    B.append(int(input()))
can = find_numbers(A, N1, B, N2, sum)
if can:
    print('YES')
else:
    print('NO')
