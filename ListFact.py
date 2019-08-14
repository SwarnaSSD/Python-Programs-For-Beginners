def fact(n):
    f=1
    for i in range(1,(n+1)):
        f=f*i
    return f

for i in range(1,6):
    print ("Factorial of ", i , " is ", fact(i))

