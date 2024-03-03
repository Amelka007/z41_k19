n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
for i in range(len(v)):
    for j in range(i, len(v)):
        print(v[i], v[j], sep=" ")
