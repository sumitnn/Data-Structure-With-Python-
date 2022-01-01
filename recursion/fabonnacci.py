# fabonacci
def fun(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:

        return (fun(n-1)+fun(n-2))


print(fun(9))
