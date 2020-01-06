from random import *


def binary_search(v, L):

    low = 0
    high = len(L)-1

    while (low <= high):
        mid = (low+high)//2
        
        if L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
            
    return len(L)


def recursive_binary_search(v, L, low, high):
    
    # JE: Uncomment this next line to see the search space
    print("v(%d) L(%s) low(%d) high(%d)" %(v, str(L[low:high+1]), low, high)) 
    
    if low > high: 
        return len(L) # Not Found!

    mid = (low + high)//2

    if v == keys[mid]: # Found!
        # v is at mid in L so breakout of recursion
        return mid

    elif v < keys[mid]:
        # v is in the lower half of L so recur on L up to mid-1
        return recursive_binary_search(v, L, low, mid-1)

    # v is in the upper half of L so recur on L from mid+1
    return recursive_binary_search(v, L, mid+1, high)



# Driver code ...
keys = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
argument = int(input("Enter a target value: "))

#print(recursive_binary_search(argument, keys, 0, len(keys)-1))
result = recursive_binary_search(argument, keys, 0, len(keys)-1)
#result = binary_search(argument, keys)
if (result != len(keys)):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))

