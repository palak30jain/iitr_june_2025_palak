def binary_search(lst, n):
    start = 0
    end = len(lst)-1
    
    
    while start <= end:
        
        mid = (start + end) // 2
        print("loop", mid)
        if( n < lst[mid]): # left side
            end = mid - 1
        elif n > lst[mid]: # right side
            start = mid + 1
        else:
            return mid
    print("outside loop")
    return -1
