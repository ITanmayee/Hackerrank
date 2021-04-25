# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

def is_array_an_factor(array , integer) :
    for i in array :
        if integer % i != 0 :
            return False
    return True


def is_integer_an_factor(array , integer) :
    for i in array :
        if i % integer != 0 :
            return False
    return True

def getTotalX(array1, array2):
   return len([i for i in range(1 , max(array2) + 1) if is_array_an_factor(array1 , i) and is_integer_an_factor(array2 , i) ])

print(getTotalX([2, 4] , [16, 32, 96]))
print(getTotalX([3, 6, 9] , [36, 72]))
