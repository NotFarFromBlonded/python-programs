def creat_l(n):
    l=[]
    for i in range (n):
        val = input("enter value")
        l = l+[val]
    return l
def rev(l):
    print "original list-"
    n = len(l)
    for i in range (n):
        print l[i],
    print
    print "reverse list-"
    for i in range (-1,-n-1,-1):
        print l[i],
    print
def main():
    n = input("enter list size: ")
    print '''1.Create list
2. Reverse list'''
    c = 'y'
    while c == 'y' or c == 'Y':
        ch = input("enter choice: ")
        if ch == 1:
            l = creat_l(n)
        elif ch == 2:
            l = rev(l)
        else:
            print "invalid choice"
        c = raw_input("do you want to continue? ")
main()
        
