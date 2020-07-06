str=raw_input("enter a string: ")
l=len(str)
ctr=0
i=0
y=0
b=0
while i<1:
    T=str[i]
    print str[i]
    ctr=ctr+1
    i=i+1
    if T=='e' or T=='E':
        y=y+1
    elif T=='':
        b=b+1
print "no. of characters ",ctr
print "no. of occurences of 'e' or 'E'= ",y
print "no. of words= ",b+1
