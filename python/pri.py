n = input ("enter no. " )
while n>0:
    for i in range (2,n+1):
        for j in range (1,i):
            if i%j!=0:
                print i
