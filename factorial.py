fac = 1
num = int(input("Enter a Number :"))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fac = fac*i
print("The factorial of",num,"is",fac)
