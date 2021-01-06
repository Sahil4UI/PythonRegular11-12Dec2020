def Student(id,name,*x):
    print(id,name,list(x))

Student(101,"Akash","Delhi","98766545",90)

'''
#** - keyworded argument
def Student(id,name,**x):
    print(id,name,x)

Student(101,"Akash",city = "Delhi",contct = "98766545",marks=90)
'''
