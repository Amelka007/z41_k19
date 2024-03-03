v = []
n = int(input())
for _ in range(n):
    v.append(int(input()))
k = v[-1]
for i in v:
    print(i + k)