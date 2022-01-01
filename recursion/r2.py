# print 1 to n integer using recursion
n = int(input("enter number:"))


def fun(x):
    if x == 0:
        return 1
    else:

        fun(x-1)
        print(x)


fun(n)
