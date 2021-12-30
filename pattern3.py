# using while loop
rows = int(input("enter rows:"))
i = 1
j = 1
r = 0
while i <= rows:
    while j <= rows:
        print(rows-r, end=" ")
        r += 1
        j += 1
    print()
    j = 1
    i += 1
    r = 0
