import random
def create(r,c):
    l =[[random.random()for column in range (c)]for row in range (r)]
    for i in range (r):
        for j in range (c):
            val = input ("enter element of matrice: ")
            l[i][j] = val
    return l
def display(lis,r,c):
    print "the matrix is "
    for i in range (r):
        for j in range (c):
            print lis[i][j],'',
        print
def multi(list1,a,b,list2,m,n):
    if b == m:
        l = [[random.random()for i in range (a)]for j in range (n)]
        for i in range (a):
            for j in range (n):
                l[i][j]=0
                for k in range (b):
                    l[i][j]=l[i][j]+list1[i][k]*list2[k][j]
    return l
def main():
    a = input ("enter no. of rows: ")
    b = input ("enter no.of columns: ")
    list1 = create(a,b)
    m = input ("enter no. of rows: ")
    n = input ("enter no. of columns: ")
    list2 = create(m,n)
    display(list1,a,b)
    display(list2,m,n)
    matrix=multi(list1,a,b,list2,m,n)
    display(matrix,a,n)
main()
