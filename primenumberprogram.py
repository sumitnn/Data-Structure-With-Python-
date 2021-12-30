n = int(input("enter number:"))
i = 2
while (i < n):
    if n % i == 0:
        print("Not Prime Number")
        break
    i = i+1
