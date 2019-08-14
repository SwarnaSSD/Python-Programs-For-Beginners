def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

n = int(input("Enter A Number  : "))
a=n
s =0
while n>0:
    r = n % 10
    s = s + fact(r)
    n = n // 10
    
if  s==a:
    print (a , " is a KrishnaMurty Number.")
else:
    print(a , " is not a KrishnaMurty Number.")

