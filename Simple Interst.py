p=int(input("Enter Principal Amount = Rs."))

t=int(input("Enter Time = "))

r=int(input("Enter Rate = "))

SI = (p * r * t) / 100

amt = p + SI

print("Simple Interest = Rs. %d     Maturity  Amount = Rs. %d" %(SI,amt))
