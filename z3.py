n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
for i in v:
    for j in v:
        print(i, j, sep=" ")
