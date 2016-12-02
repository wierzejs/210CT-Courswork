def primeCheck(val,maxRange):
    maxRange= maxRange-1 #setting a divisor

    if maxRange <0:
        print ("Please enter value higher than 0")
        return None
    elif maxRange == 0 or maxRange == 1:
        print ("This is prime number")
        return True
    elif val%maxRange==0:
        print ("this is not prime nubmer, the number '", val,"' is dividable by", maxRange)
        return False
    else:
         return primeCheck(val,maxRange)
    

val=int(input("what nubmer do you wish to check?"))
maxRange=val

print(primeCheck(val,maxRange))

#O(n), the worst case is the amount of iterations equal to variable 'maxRange'
