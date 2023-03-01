#linear search
def linear_search(values,target):
    n = len(values)
    for i in range(n):
        if values[i] == target:
            return i
    return -1

# note that binary search assumes the given array or list as already sorted
#recursive binary search
def binarySearchRecursive(arr,low,high,x): # binary search implemented using Recursion
    if  high >= low:
        mid = (high + low) // 2 # floor division for eg 7//2 = 2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr,low,mid-1,x)
        
        else:
            return binarySearchRecursive(arr,mid+1,high,x)
        
    else:
        return -1



#iterative binary search
def binarySearchIterative(arr,x): # binary search implemented using Iteration
    low = 0
    high= len(arr)-1
    while low <= high:
        mid = (high + low)//2
        if arr[mid]> x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            return mid
    return -1

