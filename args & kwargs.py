#* arguments , ** keyworded arguments
'''
def Student(id,name,*args):
    print(id,name,args)

Student(101,"Lokesh","Delhi","987655432",98)
'''

#** keyworded argument
def Student(id,name,**kwargs):
    print(id,name,kwargs)
Student(101,"Lokesh",city ="Delhi",contactNo="987655432",marks=98)
