# find all duplicates in an array
n = [2, 4, 5, 5, 8, 8, 2, 3, 6, 9, 0]
r = []
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] == n[j]:
            r.append(n[i])

print(r)
