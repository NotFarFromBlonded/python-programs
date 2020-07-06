def display(g):
    print "name",'\t',"Phone NO."
    for i in g :
        print i,'\t',g[i]
def create(n):
    d = dict()
    for i in range (n):
        val = raw_input("Enter name: ")
        val1 = raw_input("Enter phone no.: ")
        d[val]=val1
    return d
def main():
    m = input ("no.of entries in dictionary: ")
    d = create(m)
    display(d)
main()
