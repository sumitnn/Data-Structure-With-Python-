# print n to 1 integer using recursion
n = int(input("enter number:"))


def fun(x):
    if x == 0:
        return 1
    else:
        print(x)
        fun(x-1)


fun(n)
