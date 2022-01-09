# reverse a list

# n = [3, 5, 3, 53, 5, 2, 6, 7, 8]
n = [1, 2, 3, 4, 4, 4, 4, 7, 8, 1, 1]

i = 0
length = len(n)-1
while i <= length:
    if i == length-i:
        break

    n[i], n[length-i] = n[length-i], n[i]

    i += 1
print(n)
