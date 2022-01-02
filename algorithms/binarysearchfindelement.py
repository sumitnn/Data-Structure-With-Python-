arr = [7, 10, 2, 18, 11, 21, 3, 44, 3, 222, 66, 24, 45, 63, 64, 87, 98]
arr.sort()
low = 0
high = len(arr)-1
search = 11
while low <= high:
    mid = (low+high)//2
    if arr[mid] == search:
        print(f"found at index of {mid-1}")
        break
    elif arr[mid] < search:
        low = mid+1
    else:
        high = mid-1
    print("*")
