def max_rot(n):
    a, rot, b = list(str(n)), 0, []
    while rot < len(a):
        b.append(int(''.join(a)))
        a.append(a[rot])
        del a[rot]
        print(n, max(b))
        rot += 1

    return max(b)