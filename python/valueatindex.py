def creat_l(n,p):
    l =[]
    for i in range (n):
        y = input ("enter value ")
        l = l+[y]
    if p<n:
        print "list at", p ,"position: ",l[p-1]
    else:
        print "index out of range"
def main():
    n = input ("enter list size: ")
    
    creat_l(n,p)
    p = input ("enter position")
main()
