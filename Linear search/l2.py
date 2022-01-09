# reverse a number

n = 12453
reverse_num = 0
while n != 0:
    mod = n % 10
    reverse_num = reverse_num*10+mod
    n = n//10


print(reverse_num)
