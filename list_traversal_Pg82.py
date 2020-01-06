L = [18, 27, 15, 13, 22]

# Traverse the list displaying one element a time
for index in range(len(L)):
    print(L[index])

temp = L[2]
L[2] = L[1]
L[1] = temp

print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])