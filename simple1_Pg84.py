# Simple Sort v1

unsorted_list = [9, 6, 10, 4, 8, 5, 7] # the list to be sorted
sorted_list = [] # the initial (empty) sorted list

# Loop over every element in the unsorted list
for i in range(len(unsorted_list)):
    smallest = min(unsorted_list) # min returns the smallest
    sorted_list.append(smallest) # append the smallest to the sorted list
    unsorted_list.remove(smallest) # remove the smallest from unsorted_list

print(sorted_list)