class mobile:
    shop_name='steve jobs'
    def _init_(self,company=None,model=None,price = 0.0,colour = None):
        self.company=company
        self.model = model
        self.price = price
        self.colour = colour
    def disp_data(self):
        print self.company,'\t',self.model,'\t',self.price,'\t',self.colour
    def get_data(self):
        self.company=raw_input("enter company - ")
        self.model = raw_input("enter model - ")
        self.price = input("enter price - ")
        self.colour = raw_input("enter colour - ")
phones = []
def making_database():
    ch = 'Y'
    print 'phone details'
    while ch == 'y' or ch == 'Y':
        a = mobile()
        a.get_data()
        phones.append(a)
        ch = raw_input ('More phones - ')
    return phones
def disp_database():
    for i in phones:
        i.disp_data()
        print
def  main():
    making_database()
    print '''steve jobs
1. enter new phone
2. view'''
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        choice = input ("enter choice - ")
        if choice ==1:
            making_database()
        elif choice ==2:
            print 'Phones available from ',mobile.shop_name,'\n'
            print 'Company','\t','Model','\t','Price','\t','colour'
            disp_database()
        else:
            print "please enter a valid choice"
        ch = raw_input ("do something else ?(y/n) ")
    print 'Thanks for coming '
main()

    
                 
