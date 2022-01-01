n = int(input("enter number:"))
i = 1
j = 1
count = 1
while i <= n:
    while j < i + 1:
        print(count, end=" ")
        count += 1
        j += 1
    j = 1
    i += 1
    print()
