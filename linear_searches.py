

def linear_search_v1(v, L):
    i = 0
    while i < len(L): # more?
        if L[i] == v: # match?
            return i # successful

        i = i + 1

    return i # unsuccessful


def linear_search_v2(v, L):
    i = 0
    match = False
    
    while not match and i < len(L):
        if L[i] == v: # match?
            match = True
        else:
            i = i + 1

    return i


def linear_search_v3(v, L):
    i = 0
    while i < len(L) and L[i] != v: # more? and match?
        i = i + 1

    return i



def linear_search_v4(v, L):
    for i in range(len(L)):
        if L[i] == v:
            return i
        
    return len(L)

def linear_search_v5(v, L):
    i = 0
    for element in L:
        if element == v:
            return i
        i = i + 1
        
    return len(L)


def linear_search_v6(v, L, index=0) :
    if len(L) != 0:
        if L[0] == v:
            return index

        r =  linear_search_v6(v, L[1:], index+1)
        if r != -1:
            return r

    return -1

# Driver code ...
keys = [15, 4, 41, 13, 24, 14, 12, 21]
argument = int(input("Enter a target value: "))
print(linear_search_v1(argument, keys))
print(linear_search_v2(argument, keys))
print(linear_search_v3(argument, keys))
print(linear_search_v4(argument, keys))
print(linear_search_v5(argument, keys))
print(linear_search_v6(argument, keys))

'''
result = linear_search_v1(argument, keys)

if (result != len(keys)):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))
'''