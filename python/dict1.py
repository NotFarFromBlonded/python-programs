def display(g):
    print "Name",'\t',"Phonr No."
    for i in range (g):
        print i,'\t',g[i]
def creat(n):
    d = dict()
    for i in range (n):
        val = raw_input("Enter Name: ")
        val1 = raw_input ("Enter phone no.: ")
        d[val] = val1
    return d
def main():
    m = input ("No. of Entries in dictionary: ")
    d = d.append(m)
    display (d)
    h = 'y'
    while h=='y' or h == 'Y':
        m = raw_input ("enter phone no. you want to search for: ")
        flag = 0
        for i in d:
            if d[i] == m:
                print "entry found: "
                print "Name",'\t',"Phone No."
                print i,'\t',d[i]
                flag = 1
        if flag == 0:
            print "entry not found"
        h = raw_input ("Do you want to continue? ") 
main()
    
