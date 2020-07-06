def create(n):
    l = []
    for i in range (n):
        v = input ("enter elements: ")
        l = l+[v]
    return l
def sel_sort_asc(l):
    for i in range (len(l)-1):
        min = l[i]
        for j in range (i,len(l)):
            if min >l[j]:
                min,l[j]=l[j],min
    print "final list: ",l
def sel_sort_dsc(l):
    for i in range (len(l)-1):
        max = l[i]
        for j in range (i,len(l)):
            if max <l[j]:
                l[j],max=max,l[j]
    print "final list: ",l
def main():
    x = input ("enter list size: ")
    y = create(x)
    print y
    print "sort - 1.ascending, 2.descending"
    c = input ("enter choice: ")
    if c == 1:
        sel_sort_asc(y)
    elif c == 2:
        sel_sort_dsc(y)
    else:
        print "invalid choice"
main()

        
