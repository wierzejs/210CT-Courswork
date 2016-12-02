parameter = int(input("What is your parameter?"))

n=1 #base case

#multiplying base case by itself until it will be bigger than given parameter
while n*n<=parameter:
    n=n+1
#when it becomes bigger we know that our answer is one less than n
else:
    print(n-1)
