# Bubble Sort works by repeatedly swapping adjacent elements if they are in wrong order.
# Bubble Sort v1

# 1. Initialise an unsorted list
aList = [5, 7, 3, 6, 2]

print("INPUT (initial list): ", aList)

# 2. Traverse across every element in the list
for i in range(len(aList)):
    #print("BEFORE PASS %d: %s " %(i+1, aList))
    # 3. Compare all adjacent elements starting from the beginning
    for j in range(len(aList)-1):
        # 4. if the elements are out of order, then swap them
        #print("%s " %aList, end="-> ")
        if aList[j] > aList[j+1]:
            temp = aList[j+1]
            aList[j+1] = aList[j]
            aList[j] = temp
        #print("%s " %aList)
        
    #print("AFTER PASS %d: %s " %(i+1, aList))

print("OUTPUT (sorted list): ", aList)

# NOTE:
# The canonical way to swap two variables in Python is
# a, b = b, a

