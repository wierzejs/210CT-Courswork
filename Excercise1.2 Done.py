import random

def shuffle(x):
    arrayRange = len(x)
    if not arrayRange > 2:  #checking if array has more than two elements and prints an error if it doesn't
        raise AssertionError('Array is too short to shuffle!')
    for i in range(arrayRange):
        swap = random.randrange(arrayRange - 1)
        swap += swap >= i
        x[index], x[swap] = x[swap], x[i]
    return Array
Array = [1,2,3,4,5,6,7,8,9,10]
print (shuffle(Array))


#O(n), where n is the amount of elements in the array
