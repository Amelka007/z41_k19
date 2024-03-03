a = int(input())
del6 = del3 = del2 = maxx = k = 0
while a != 0:
    if a % 6 == 0 and a > del6:
        del6 = a
    elif a > maxx:
        maxx = a
    if a % 2 == 0 and a > del2:
        del2 = a
    elif a % 3 == 0 and a > del3:
        del3 = a
    k += 1

    a = int(input())

r = int(input())
if del6 * maxx > del2 * del3:
    r_it = del6 * maxx
else:
    r_it = del2 * del3
if r == r_it:
    print(k, r_it, "yes", sep='\n')
else:
    print(k, r_it, "no", sep='\n')
