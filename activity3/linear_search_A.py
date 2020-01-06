import random

def linear_search(v, L):
    global comparisons

    for index in range(len(L)):
        comparisons = comparisons + 1
        if L[index] == v:
            return index
            
    return -1

# Driver code ...
print("%s\t\t %s\t\t %s" %("List Size", "Found Index", "#Comparisons"))
for list_size in [1, 10, 1000, 10000, 100000, 1000000]:
    some_list = list(range(list_size))
    random.shuffle(some_list) # randomise the list
    comparisons = 0
    # target = random.randrange(len(some_list)) # average case
    target = -1 # worst case because -1 never exists
    pos = linear_search(target, some_list)
    print("%d\t\t %d\t\t %d" %(len(some_list), pos, comparisons))

