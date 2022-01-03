# first and last occurrence program using binarysearch
# 1234557  input
# firstoccurence=4 lastoccurence=5 of 5 value return index
def first_occ(n, find):
    s = 0
    r = 0
    l = len(n)-1
    mid = (s + l)//2
    while s <= l:
        if n[mid] == find:
            r = mid

            l = mid-1
        elif n[mid] < find:
            l = mid-1
        else:
            s = mid+1
        mid = (s + l)//2

    return r


def last_occ(n, find):
    s = 0
    r = 0
    l = len(n)-1
    mid = (s + l)//2
    while s <= l:
        if n[mid] == find:
            r = mid
            s = mid+1
        elif n[mid] < find:
            l = mid-1
        else:
            s = mid+1
        mid = (s + l)//2

    return r


arr = [2, 3, 3, 5, 4, 4, 4, 4, 5, 6]
result1 = first_occ(arr, 4)
result = last_occ(arr, 4)
print(result1, result)
