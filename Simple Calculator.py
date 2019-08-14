print("Select  1. Addition   2. Difference   3. Multiplication   4. Division ")
ch = int(input("Enter Your Choice : "))
if ch==1:
    a = int(input(" Enter a : "))
    b = int(input(" Enter b : "))
    print ("Sum = ", a ," + ", b , " = ", (a+b))
elif ch==2:
    a = int(input(" Enter a : "))
    b = int(input(" Enter b : "))
    if a>b:
         print ("Difference = ", a ," - ", b , " = ", (a-b))
    else:
            print ("Difference = ", b ," - ", a , " = ", (b-a))
            
elif ch==3:
    a = int(input(" Enter a : "))
    b = int(input(" Enter b : "))
    print ("Product = ", a ," * ", b , " = ", (a*b))
elif ch==4:
    a = int(input(" Enter a : "))
    b = int(input(" Enter b : "))
    print ("Quotient = ", a ," / ", b , " = ", (a//b))
else:
    print("Invalid Input! ")
