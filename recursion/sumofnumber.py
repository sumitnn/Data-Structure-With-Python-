def fun(n):
    if n == 0:
        return 0
    else:
        return (n + fun(n-1))


print(fun(6))
