#linear search
def linear_search(values,target):
    n = len(values)
    for i in range(n):
        if values[i] == target:
            return i
    return -1

#recursive binary search
def binarySearchRecursive(arr,low,high,x):
    if  high >= low:
        mid = (high + low) // 2 # floor division for eg 7//2 = 2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr,low,mid-1,x)
        
        else:
            return binarySearchRecursive(arr,mid+1,high,x)
        
    return -1

#iterative bina