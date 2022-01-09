# element present in list or not

n = [3, 5, 4, 6, 2, 6, 0]
# target = 0
# target = 3
target = 64
# target = 6
# target = 5
for i, value in enumerate(n):
    if value == target:
        print(f"present at index {i}")
        break
