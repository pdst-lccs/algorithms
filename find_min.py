
def find_smallest(a):

    smallest = a[0]

    for idx in range(1, len(a)):
        if a[idx] < smallest:
            smallest = a[idx]
            
    return smallest

ages = [18, 27, 15, 13, 22, 14, 12, 21]
print("Smallest:", find_smallest(ages))

'''
ages = [18, 27, 15, 13, 22, 14, 12, 21]

smallest = ages[0] # 18

for idx in range(1, len(ages)):
    if ages[idx] < smallest:
        smallest = ages[idx]

print("Smallest:", smallest)
'''

'''
smallest = ages[0] # 18
if ages[1] < smallest:
    smallest = ages[1]
if ages[2] < smallest:
    smallest = ages[2]
if ages[3] < smallest:
    smallest = ages[3]
if ages[4] < smallest:
    smallest = ages[4]
if ages[5] < smallest:
    smallest = ages[5]
if ages[6] < smallest:
    smallest = ages[6]
if ages[7] < smallest:
    smallest = ages[7]

'''