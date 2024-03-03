n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
for i in range(len(v)):
    for j in range(len(v)):
        if i != j:
            print(v[i], v[j], sep=" ")
