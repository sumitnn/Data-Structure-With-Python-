# using while loop
rows = int(input("enter rows:"))
i = 1
j = 1
while i <= rows:
    while j <= rows:
        print(i, end=" ")
        j += 1
    print()
    j = 1
    i += 1
