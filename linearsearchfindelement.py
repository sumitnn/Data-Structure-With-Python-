a = [2, 4, 5, 3, 6, 8, 4, 16, 3, 33, 36, 7, 22, 66]
i = 0
n = 8
while i < len(a):
    if a[i] == n:
        print(f"found at index {i}=> value {a[i]} !!")
    i += 1
