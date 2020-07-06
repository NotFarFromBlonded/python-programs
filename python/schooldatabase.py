class school:
    school_name = 'school data'
    def _init_(self, rno = 0,admno = 0,cl = 0,tm = 0, grade = None):
        self.rno= rno
        self.admno = admno
        self.cl = cl
        self.tm = tm
        
    def cal_gr(self,x):
        if x >= 75:
            return 'A'
        elif x >= 60:
            return 'B'
        elif x >= 50:
            return 'C'
        else :
            return 'Fail'
    def disp_data(self):
        print self.rno,'\t',self.admno,'\t',self.cl,'\t',self.tm,'\t',self.gr
    def get_data(self):
        self.rno = input ("enter roll no. - ")
        self.admno = input ("enter admission no. - ")
        self.cl = input ("enter class - ")
        self.tm = input ("enter total marks - ")
        self.gr = school.cal_gr(self,self.tm)
m_l = []
def main():
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        m_obj=school ()
        m_obj.get_data()
        m_l.append(m_obj)
        ch = raw_input ("more schools? ")
    print "Rno",'\t',"admno",'\t',"cl",'\t',"tm",'\t',"gr",'\t'
    for i in range (len(m_l)):
        m_l[i].disp_data()
    return m_l
main()
        
        
       
