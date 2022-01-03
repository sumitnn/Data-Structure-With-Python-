# square find using binary search
# 36 return 6

def find_square(n):
    s = 0
    e = n
    mid = s+(e-s)//2
    while s <= e:
        if (mid*mid) == n:
            return mid
        elif (mid*mid) >= n:
            e = mid-1
        else:
            s = mid+1
        mid = s+(e-s)//2

    return mid


def find_decimal(n, u, actual):
    if n*n == actual:
        return n
    increment = 0.1
    ans = n
    for i in range(u):

        while ans*ans <= n:
            ans = ans+increment
        ans = ans-increment
        increment = increment/10
    return ans


n = 63
result = find_square(n)
result = find_decimal(result, 3, n)
print(result)
