n = int(input("enter number:"))
i = 1
j = 1
while i <= n:
    while j < i + 1:
        print("*", end=" ")
        j += 1
    j = 1
    i += 1
    print()
