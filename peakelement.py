#arr = [1,2,4,5,7,8,3]
def peak(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
            
    left = 1
    right = n - 2
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[mid-1]:
            left = mid + 1
        else:
            right = mid - 1
            
arr = [1,2,4,5,7,8,3]
print(peak(arr)) # here the output is 8 because it is greater than neighbours
        