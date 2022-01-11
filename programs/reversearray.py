a = [2, 3, 4, 63, 33, 2, 42, 1]
s, e = 0, len(a)-1
while s < e:
    a[s], a[e] = a[e], a[s]
    s += 1
    e -= 1
print(a)
