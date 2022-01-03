n = 10
i, j, z, k = 1, 1, 1, n
while i <= n:
    while j <= n+1-i:
        print(j, end=" ")
        j += 1
    if i > 1:
        while z <= i*2-2:
            print("*", end=" ")
            z += 1
        z = 1
    k = n-i+1
    while k >= 1:
        print(k, end=" ")
        k -= 1
    k = n

    j = 1

    print()
    i += 1
