del7 = del2 = del14 = nn = 0
name_f = input()
f = open(name_f, mode='r')
n = int(f.readline())

for i in range(n):
    a = int(f.readline())
    if a % 14 == 0:
        del14 += 1
    elif a % 7 == 0:
        del7 += 1
    elif a % 2 == 0:
        del2 += 1
    else:
        nn += 1
itog = 0

itog += del2 * del7
itog += del14 * (del14 - 1) // 2
itog += del14 * (n - del14)
print(itog)
