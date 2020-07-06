def creat_l(n):
    l = []
    for i in range (n):
        y = input("enter value ")
        l = l + [y]
    return l
def max_min(l):
    max = l[0]
    min = l[0]
    for i in range (len(l)):
        if l[i]>max:
            max = l[i]
    for j  in range (len(l)):
        if l[j]<min:
            min = l[j]
    print "largest value = ", max
    print "smallest value = ", min
def main():
    n = input ("enter list size ")
    l = creat_l(n)
    max_min(l)
main()
