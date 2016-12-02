def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def trailingZeroes(factorialResult):
    stringConverted = str(factorialResult)
    return len(stringConverted)-len(stringConverted.rstrip('0'))

n=int(input("Please enter a number"))
print("There are ",trailingZeroes(factorial(n))," trailing zeroes from ", n,"*",n ," which results in ", factorial(n))


#O(n), each line of code is being run once
