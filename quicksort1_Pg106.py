# A quicksort algorithm that doesn't use in place partioning

def quick_sort(L):
    left_list = []
    middle_list = []
    right_list = []

    # JE: Uncomment the next line to see debug info.
    #print("Input:", L)
    
    # Base case 
    if len(L) <= 1:
        return(L)

    # Set pivot to the last element in the list
    pivot = L[len(L)-1] 

    # Iterate through all elements (keys) in L
    for key in L:
        if key < pivot:
            left_list.append(key)
        elif key == pivot:
            middle_list.append(key)
        else:
            right_list.append(key)

    # JE: Uncomment the next line to see debug info.
    #print("Left (%s) Pivot (%s) Right (%s):" %(str(left_list), str(middle_list), str(right_list)))

    # Repeat the quicksort on the sub-lists and combine the results
    return quick_sort(left_list) + middle_list + quick_sort(right_list)
    #sorted_left_lists = quick_sort(left_list)
    #print("Lefts", sorted_left_lists)
    #sorted_right_lists = quick_sort(right_list)
    #print("Rights", sorted_right_lists)
    #return sorted_left_lists + middle_list + sorted_right_lists

# Driver code
aList = [88, 46, 25, 11, 18, 12, 22]
#aList = [85, 24, 63, 45, 17, 31, 96, 50]
print("INPUT (initial list): ", aList)
print("OUTPUT (sorted list): ", quick_sort(aList))



