a = [2, 4, 54, 33, 22, 11, 7, 6]
i = 0
j = 1
while i <= len(a)-1:
    while j <= len(a)-1:
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
        j += 1
    j = i+1
    i += 1
print(a)
