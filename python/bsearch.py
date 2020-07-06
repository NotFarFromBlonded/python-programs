def creat_l(n):
    l = []
    for i in range (n):
        y = input ("enter value ")
        l = l+[y]
    return l
def b_search(l,v):
    p = -1
    low = 0
    high = len(l)-1
    while (high>=low):
        mid = (low +high)/2
        if l[mid]==v:
            p = mid
            break
        elif l[mid]>v:
            high = mid - 1
        else:
            low = mid +1
    if p == -1:
        print "no match found"
    else:
        print "match found at ",p+1,"position"
def main():
    n = input ("enter list size ")
    l = creat_l(n)
    c = 'y'
    while c == 'y' or c =='Y':
        val = input ("enter value to be searched ")
        b_search(l,val)
        c = raw_input("do you want to continue? ")
main()
               
        
