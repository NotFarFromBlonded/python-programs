import random
def create(m):
    l=[[random.random()for column in range(m)]for row in range (m)]
    for i in range(m):
        for j in range(m):
            val=input("enter element of matrice: ")
            l[i][j]=val
    return l
def display(l,m):
    for i in range(m):
        for j in range(m):
            print l[i][j],'',
        print
def rotate(l,m):
    for i in range(0, m/2):
        for j in range(i,m-1-i):
            k=l[i][j]
            l[i][j]=l[m-1-j][i]
            l[m-1-j][i]=l[m-1-i][m-1-j] 
            l[m-1-i][m-1-j]=l[j][m-1-i] 
            l[j][m-1-i]=k
    return l

def main():
    n=input("enter order of matrix: ") 
    li=create(n) 
    display(li,n)
    newMatrix=rotate(li,n)
    print "the matrix when rotated by 90 looks like this: "
    display(newMatrix,n)
main()