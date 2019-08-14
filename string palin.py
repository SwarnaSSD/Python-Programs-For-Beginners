st = input("Enter a Word : ")
st_rev = reversed(st)
if list(st) == list(st_rev) :
    print (st , " is a Palindrome Word. ")
else :
    print (st , " is not a Palindrome Word. ")
