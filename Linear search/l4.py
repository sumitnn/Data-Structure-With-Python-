# find unique elements in list
n = [5, 4, 3, 3, 2, 66, 66, 3, 2, 8, 9, 0]
result = []
for i in n:
    if i not in result:
        result.append(i)
print(result)
