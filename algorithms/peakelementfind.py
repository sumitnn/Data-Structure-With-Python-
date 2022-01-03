def find(arr):
    s = 0
    l = len(arr)-1
    mid = (s+l)//2

    while s <= l:
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            s = mid + 1
        else:
            l = mid-1

        mid = (s+l)//2
    return s


a = [0, 1, 2, 44, 4, 3, 2, 100]

result = find(a)
print(result)
