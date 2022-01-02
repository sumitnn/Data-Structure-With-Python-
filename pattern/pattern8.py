n = 4
# n=int(input("enter number:"))
i, j, z, x = 1, 1, 1, 1

while i <= n:
    while z <= n-i:
        print(" ", end=" ")
        z = z+1
    z = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    while x <= i-1:
        print(i-x, end=" ")
        x += 1
    x = 1
    print()
    j = 1
    i += 1
