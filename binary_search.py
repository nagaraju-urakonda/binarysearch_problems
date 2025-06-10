def binary_search(arr,target):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # if target not found
arr=[1,2,3,4,5,6]
target = 5
print(binary_search(arr,target)) # here output is 4 target 5 is in index 4

    