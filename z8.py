maxx = -1
v = list(map(int, input().split()))

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        ch = v[i] * v[j]
        if ch > maxx and ch % 14 == 0:
            maxx = ch

print(maxx)
