def find(arr):
    s = 0
    l = len(arr)-1
    mid = (s+l)//2

    while s < l:
        if arr[mid] > arr[0]:
            s = mid + 1
        else:
            l = mid

        mid = (s+l)//2
    return s


a = [3, 8, 10, 17, 23, 1]

result = find(a)
print(result)
