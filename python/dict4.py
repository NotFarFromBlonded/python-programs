def create(n):
    d = dict()
    for i in range (n):
        val = raw_input ("enter name: ")
        val1 = input ("enter phone no.: ")
        d[val]=val1
    return d
def main():
    m = input ("enter no.of entries: ")
    d = create(m)
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        print "choices - 1.Add a new entry,2.Delete an entry,3.Modify an entry"
        g = input ("enter an option: ")
        if g == 1:
            val = raw_input("enter name: ")
            val1 = input("enter phone no.: ")
            d[val]=val1
            print d
        elif g==2:
            val2 = raw_input ("enter name you want to delete")
            if val2 in d:
                d.pop(val2)
                print d
            else:
                print "name not found"
        elif g == 3:
            val3 = raw_input ("enter name: ")
            val4 = input ("enter new phone no.: ")
            if val3 in d:
                d[val3]=val4
                print d
            else:
                print "match not found"
        else:
            print "invalid option"
        ch = raw_input ("do you wantto continue? ")
main()
        
        
