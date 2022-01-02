def fun(x, n):
    if n == len(x):
        return 1
    if x[n] < x[n+1]:
        return -1
    else:

        return fun(x, n+1)


x = [1, 2, 3, 7, 33]
result = fun(x, 0)
if result == 1:
    print("sorted")
else:
    print("not sorted")
