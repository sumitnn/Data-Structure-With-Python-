a = [4, 3, 2, 6, 8, 10, 22]
i = 0
j = 0
while i < len(a)-1:
    while j < len(a)-1-i:
        if a[j] > a[j+1]:
            a[i], a[j] = a[j], a[i]
        j += 1
    j = 0
    i += 1
print(a)
