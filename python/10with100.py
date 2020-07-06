def creat_l(n):
    l = []
    for i in range (n):
        val = input ("enter value ")
        l.append(val)
    return l
def update(l):
    print "original list: "
    for x in range (len(l)):
        print l[x],
    print
    for i in range (len(l)):
        if l[i]==10:
            l[i]=100
    print "modified list: "
    for j in range (len(l)):
        print l[j],
def main():
    n = input("enter list size ")
    l = creat_l(n)
    update (l)
main()
            
        
