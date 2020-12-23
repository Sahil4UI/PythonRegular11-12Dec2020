def f1():
    print("f1 called....")
    def f2():
        print("f2 called...")
    def f3():
        print("f3 called...")
    def f4():
        print("f4 called...")

    return f2,f3,f4

x,y,z = f1()
x()
y()
z()
'''
#return statement
def sum(x,y):
    return x+y

res = sum(12,12)
print(res)
'''
