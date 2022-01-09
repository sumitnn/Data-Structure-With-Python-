# swapp alternative in list
n = [2, 3, 5, 6, 7, 8, 9, 0, 1, 2]
i = 0
length = len(n)-1
while i <= length:
    n[i], n[i+1] = n[i+1], n[i]
    i += 2

print(n)
