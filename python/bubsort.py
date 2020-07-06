def create(n):
    l = []
    for i in range (n):
        v = input("enter list elements: ")
        l = l+ [v]
    return l
def bub_s_asc(l):
    for i in range (len(l)-1):
        for j in range (len(l)-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        print "list at",i+1,"position",l
    print "final list",l
def bub_s_dsc(l):
    for i in range (len(l)-1):
        for j in range (len(l)-1-i):
            if l[j]<l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
                
        print "list at",i+1,"position",l
    print "final list",l
def main():
    x = input ("enter list size: ")
    y = create(x)
    print y
    print "sorting - 1.ascending, 2.descending"
    c = input ("enter choice: ")
    if c == 1:
        bub_s_asc(y)
    elif c == 2:
        bub_s_dsc(y)
    else:
        print "invalid choice"
main()
        
