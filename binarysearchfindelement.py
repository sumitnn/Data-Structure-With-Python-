# sort the list then find low,mid,high values
search = 44
a = [2, 2, 3, 3, 5, 6, 8, 23, 34, 35, 43, 44, 55, 66, 77, 99]
low = 0
high = len(a)-1
print(high)
mid = high//2
if a[mid] == search:
    print(mid)
elif a[mid] < element:
