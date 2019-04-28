x = input().split()

N = int(x[0])
M = int(x[1])
Y = int(x[2])
finded = False
A = []
for i in range(0, M):
    if pow(i, N) % M == Y:
        finded = True
        A.append(i)

if not finded:
    A.append(-1)

print(*A)