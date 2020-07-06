def creat_l(n):
    l =[]
    for i in range (n):
        y = raw_input("enter string ")
        l.append(y)
    return l
def str_d(l):
    d = len (l)
    print "element starting with 'd' or 'D'"
    for i in range (d):
        str = l[i]
        if str[0] == 'd' or str[0] == 'D':
            print str
def main():
    n = input ("enter list size ")
    ll = creat_l(n)
    str_d(ll)
main()
        
    

    
