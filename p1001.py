A = []
N = int(input())
K = int(input())
A.append(0)
A.append(K - 1)
for i in range(2, N):
    A.append((A[i-2] + A[i - 1])  * (K - 1))
print(A[N] + A[N-1])
