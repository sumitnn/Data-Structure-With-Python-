def twoSum(arr, target, n):
    # Write your code here.
    result = []
    for i in range(n):
        if arr[0]+arr[i] == target:
            result.append((arr[0], arr[i]))

        elif arr[1]+arr[i] == target:
            result.append((arr[1], arr[i]))

        elif arr[2]+arr[i] == target:
            result.append((arr[2], arr[i]))
    return result


print(twoSum([2, 7, 11, 3], 9, 4))
