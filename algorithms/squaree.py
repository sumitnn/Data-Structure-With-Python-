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


n = 64
result = find_square(n)
print(result)
