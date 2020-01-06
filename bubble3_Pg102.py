# Bubble Sort works by repeatedly swapping adjacent elements if they are in wrong order.
# Bubble Sort v3

# 1. Initialise an unsorted list
aList = [5, 7, 3, 6, 2, 4, 1]

print("INPUT (initial list): ", aList)

exchange = True
n = len(aList)
i = 0
# 2. Traverse across every element as long as there are exchanges
while (i < n) and  exchange:
    print("BEFORE PASS %d: %s " %(i+1, aList))
    exchange = False # assume that there will be no exchanges
    # 3. Compare all unsorted adjacent elements
    for j in range(n-i-1):
        # 4. if the elements are out of order, then swap them
        print("%s " %(aList), end="-> ")
        if aList[j] > aList[j+1]:
            aList[j], aList[j+1] = aList[j+1], aList[j] # Canonical swap!
            exchange = True # we've done an exchange!
            
        print("%s " %aList)
    
    print("AFTER PASS %d: %s " %(i+1, aList))
    i = i+1 # increment the loop counter
    
print("OUTPUT (sorted list): ", aList)
