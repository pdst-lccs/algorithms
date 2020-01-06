# Bubble Sort works by repeatedly swapping adjacent elements if they are in wrong order.
# Bubble Sort v2

# 1. Initialise an unsorted list
aList = [1, 2, 3, 4]
#aList = [5, 7, 3, 6, 2]

exchange = True
i = 0
# 2. Traverse across every element as long as there are exchanges
while (i < len(aList)) and  exchange:
    exchange = False # assume that there will be no exchanges
    # 3. Compare all adjacent elements starting from the beginning
    for j in range(len(aList)-1):
        # 4. if the elements are out of order, then swap them
        print("%s " %aList, end="-> ")
        if aList[j] > aList[j+1]:
            temp = aList[j+1]
            aList[j+1] = aList[j]
            aList[j] = temp
            exchange = True # we've done an exchange!
            
    i = i+1 # increment the loop counter
    
print("OUTPUT (sorted list): ", aList)
