# Simple (Selection) Sort v1

# 1. Initialise an unsorted list
aList = [9, 6, 10, 4, 8, 5, 7]
# 2. Initialise a marker
marker = 0 

# 3. Traverse through all list items
while marker < len(aList):
    # 4. Find the minimum element to the right of the marker
    index_of_min = marker
    for j in range(marker+1, len(aList)): 
        if aList[index_of_min] > aList[j]: 
            index_of_min = j

    # 5. Exchange the smallest item with the item at the marker
    temp = aList[marker] # save the item at the marker
    aList[marker] = aList[index_of_min] # copy 1
    aList[index_of_min] = temp # copy 2
    
    # 6. Advance the marker to the right by 1 position
    marker = marker+1

# 7. Stop

print(marker, aList)

'''
# aList = [9, 8, 7, 6, 5, 4, 3]
aList = [3, 4, 5, 6, 7, 8, 9]
'''