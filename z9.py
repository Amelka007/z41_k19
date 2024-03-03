k = 0
name_f = input()
f = open(name_f, mode='r')
v = f.readlines()
del v[0]

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        ch = int(v[i]) * int(v[j])
        if ch % 14 == 0:
            k += 1

print(k)
