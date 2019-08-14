n = int(input("Enter a Number :"))
s=0
a=n
c=str(n)
l=len(c)

while a!=0 :
    r = a % 10
    s += (r ** l)
    a = a // 10


if s==n :
    print ( n, " is an Armstrong Number. ")
else :
    print ( n, " is not a Armstrong Number. ")
