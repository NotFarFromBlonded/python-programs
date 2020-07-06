import random
def create(m):
    l = [[random.random()for row in range (m)]for column in range (m)]
    for i in range (m):
        for j in range (m):
            val = input ("enter value: ")
            l[i][j] = val
    return l
def display (l,m):
    for i  in range (m):
        for j in range (m):
            print l[i][j],
        print
def sum_up_tri(l,m,n):
    s = 0
    print "the elements are: "
    for i in range (m):
        for j in range (n):
            if i+j>m-1:
                print l[i][j]
                s+=l[i][j]
    print "sum= ",s
def sum_dw_tri(l,m,n):
    s =0
    print "the elements are: "
    for i in range (m):
        for j in range (n):
            if i+j<=m-1:
                print l[i][j]
                s+=l[i][j]
    print "sum= ",s
def main():
    x = input("enter no. of rows/columns: ")
    l = create(x)
    print "the matrix is "
    display(l,x)
    print "sum - 1. sum of upper triangle,2. sum of lower triangle"
    c = input ("enter choice: ")
    if c == 1:
        sum_up_tri(l,x,x)
    elif c == 2:
        sum_dw_tri(l,x,x)
    else:
        print "invalid choice"
main()
        

                
        
                    
