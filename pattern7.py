n = int(input("enter number:"))
i = 1
j = 1
z = 1
while i <= n:
    cond = n-i
    while z <= cond:
        # print(" ", end=" ")   for right angled traingle
        print("", end=" ")  # for traingle

        z += 1
    z = 1
    while j <= i:
        print("*", end=" ")
        j += 1

    j = 1
    i += 1
    print()
