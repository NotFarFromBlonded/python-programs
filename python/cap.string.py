def creat_l(n):
    l = []
    for i in range (n):
        y = raw_input("enter string ")
        l = l+[y]
    return(l)
def str_cap(l):
    d = len (l)
    print "element starting with capital letter "
    for i in range (d):
        str = l[i]
        if str[0].isupper:
            print str
def main():
    n = input ("enter list size ")
    ll = creat_l(n)
    str_cap(ll)
main()
