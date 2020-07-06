ptr = 40
def result():
    print ptr
    ptr = 90
def func(var):
    if  var<=60:
        ptr = 30
        print ptr
    
    func(60)
    result()
