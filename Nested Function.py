def f1():
    def f2():
        print("Function 2 called")

    def f3():
        print("Function 3 called")

    def f4():
        print("Function 4 called")

    return "f1 called",f2,f3,f4

a,x,y,z = f1()
x()
y()
z()
print(a)
