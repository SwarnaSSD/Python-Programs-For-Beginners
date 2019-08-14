s = input("Enter a String: ")
l = len(s)
s = s.upper()
c=0
for i in range(0 , l):
    ch = s[i]
    if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" :
        c = c + 1

print (" No. of Vowels = ", c)
