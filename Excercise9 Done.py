def binarySearch(aList, x, y):
    if len(aList)==0:
        return False
    else:
        middle = len(aList)//2
        if aList[middle]>x and aList[middle]<y:
            return True
        else:
            if aList[middle]<x:
                return binarySearch(aList[middle+1:], x, y)
            else:
                return binarySearch(aList[:middle], x, y)
theList = [1,2,3,4,5,6,7,8,9,10,11,12]
print (binarySearch(theList, 8, 10))



#O(n), n depends on the amount of numbers in a list
