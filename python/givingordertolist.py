def creat_l(n):
    l = []
    for i in range (n):
        val = input ("enter list elements: ")
        l.append(val)
    return l
def main():
    n = input ("enter list size ")
    l = creat_l(n)
    print l
    print '''1. reverse the list
2. Insert avalue
3. Arrange in descending order
4. arrange in ascending order'''
    c = 'y'
    while c == 'y' or c == 'Y':
        ch = input ("enter choice ")
        if ch == 1:
            l.reverse()
            print "reverse list"
            print l
        elif ch == 2:
            i = input ("enter index ")
            if i >= len(l):
                print "index out of range "
            else:
                v = input ("enter value to be inserted ")
                l.insert(i-1,v)
                print "modified list"
                print l
        elif ch == 3:
            l.sort()
            l.reverse()
            print l
        elif ch == 4:
            l.sort()
            print l
        else:
            print "invalid choice"
        c = raw_input ("do you want to cont.? ")
main()
        
