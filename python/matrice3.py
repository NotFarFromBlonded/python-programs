import random
def create(rw,cn):
    l = [[random.random()for row in range (rw)]for column in range (cn)]
    for i in range (rw):
        for j in range (cn):
            val = input("enter values: ")
            l[i][j]=val
    return l
def disp(lis,ro,co):
    for i in range (ro):
        for j in range (co):
            print lis[i][j],
        print
def sum_row(lis,ro,co):
    for i in range (co):
        s = 0
        for j in range (ro):
            s+=lis[i][j]
        print "sum of row",i+1,"is",s
def sum_cmn(lis,ro,co):
    for i in range (ro):
        s = 0
        for j in range (co):
            s+=lis[i][j]
        print "sum of column",i+1,"is",s
def main():
    row = input("Enter no. of rows: ")
    col = input("Enter no. of columns: ")
    list1 = create(row,col)
    disp(list1,row,col)
    print "sum- 1. Row, 2. Column"
    f = input ("enter choice: ")
    if f == 1:
        sum_row(list1,row,col)
    elif f == 2:
        sum_cmn(list1,row,col)
    else:
        print "invalid choice"
main()
            
            
