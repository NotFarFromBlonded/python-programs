def create(n):
    l = []
    for i in range (n):
        v = input ("enter list elements: ")
        l = l+[v]
    return l
def in_sort_asc(l):
    for i in range (1,len(l)):
        val = l[i]
        j = i
        while ((val<l[j-1]) and (j>=1)):
            l[j] = l[j-1]
            j-=1
        l[j]=val
        print l
def in_sort_dsc(l):
    for i in range (1,len(l)):
        val = l[i]
        j = i
        while ((val<l[j-1]) and (j>=1)):
            l[j-1] = l[j]
            j+=1
        l[j]=val
        print l
def main():
    x = input ("enter list size: ")
    y = create (x)
    print y
    print " sort - 1.ascending, 2.descending"
    c = input ("enter choice")
    if c == 1:
        in_sort_asc(y)
    elif c == 2:
        in_sort_asc(y)
    else:
        "invalid choice"
main()
        
    
