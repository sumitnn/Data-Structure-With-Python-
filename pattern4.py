n = int(input("enter number:"))
j = 1
i = 1
count = 1
while i <= n:
    while j <= n:
        print(count, end="  ")
        count += 1
        j += 1

    print()
    j = 1
    i += 1
