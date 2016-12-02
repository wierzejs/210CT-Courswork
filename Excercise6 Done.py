def sentenceReverse(lst):      
    lst = lst.split()
    length = len(lst)             
    lastPostion = length - 1
    n = length//2                #How many times will the functions go
    for n in range(0, n):    
        temp = lst[lastPostion]     # Creating temporary postion for incoming swap
        lst[lastPostion] = lst[n]   #swap
        lst[n] = temp               #assining temp back to sequence
        lastPostion -= 1           #leaving changed number at the end and going one lower
        
    return lst
lst = "This Is an amazing nonfuctional list wannabe"

print(sentenceReverse(lst))

#O(n), for n is the variable 'n' aka how many times will fuction run

