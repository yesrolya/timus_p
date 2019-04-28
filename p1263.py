x = input().split()

N = int(x[0])
M = int(x[1])

A = []
B = []
for i in range(0, N):
    A.append(0)

for i in range(0, M):
    y = int(input())
    A[y - 1] += 1

for i in range(0, N):
    print("%.2f" % (A[i]*100/M) + '%')

x = int(input())
if x % 4 == 1 or x % 4 == 2:
    print("grimy")
else:
    print("black")