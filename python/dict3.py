def display (g):
    print "name",'\t',"phone no."
    for i in (g):
        print i,'\t',g[i]
def create(n):
    d = dict()
    for i in range (n):
        val = raw_input("Enter Name: ")
        val1 = input("Enter phone no.: ")
        d[val] = val1
    return d
def main():
    m = input ("enter no. of entries: ")
    d = create(m)
    display(d)
    h = 'y'
    while h == 'y' or h== 'Y':
        print "1. display keys , 2. display values"
        g = input ("enter choices: ")
        if g == 1:
            print d.keys()
        elif g == 2:
            print d.values()
        else:
            print " invalid option "
    h = raw_input ("do you want to continue?: ")
main()
        

        
        
        
        
