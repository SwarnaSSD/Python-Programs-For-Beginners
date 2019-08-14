n = int(input ("Enter a number : "))
f=0
for i in range(2,n-1):
    if n%i==0:
        f=f+1

if f==0 :
    print (n,"is a Prime Number.")
else :
    print (n,"is not a Prime Number.")

