def creat_l(n):
    l = []
    for i in range (n):
        y = input ("enter value ")
        l = l + [y]
    return l
def search_l(l,val):
    ctr = 0
    for i in range (len(l)):
        if l[i] == val:
            ctr+=1
            print "match found at",i+1,"position"
    if ctr == 0:
        print "No match found "
    else:
        print "No. of matches found-",ctr
def main():
    n = input ("enter list size: ")
    l = creat_l(n)
    c = 'y'
    while c == 'y' or c == 'Y':
        val = input ("enter value to search: ")
        search_l(l,val)
        c = raw_input('Do you want to continue? ')
main()
    
    
