def creat_l(n):
    l=[]
    for i in range (n):
        y = input ("enter value ")
        l = l+[y]
    return l
def disp_l(ll,n):
    for i in range (n):
        print "ll[",i,"]=",ll[i]
def main():
    n = input ("enter list size ")
    print '''1. create list
2. display list'''
    c = 'y'
    while c == 'y' or c == 'Y':
        ch = input ("enter choice ")
        if ch == 1:
            l = creat_l(n)
        elif ch==2:
            disp_l(l,n)
        else:
            print "invalid input"
        c = raw_input ("do you want to continue? ")
main()
