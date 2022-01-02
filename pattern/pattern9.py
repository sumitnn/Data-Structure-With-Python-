n = 5
i, j, z = 1, 1, 1
while i <= n:
    while j <= n+1-i:
        print(j, end=" ")
        j += 1
    j = 1
    while z <= n:

        print("*", end=" ")
        z += 1
    z = 1

    # while z <= n:
    # print(z, end=" ")
    # z += 1
    # z = 1
    print()
    i += 1
