#calculator -add,sub,mul,div
def Calc(x,y,operator):
    return eval(x+operator+y)
    
a = input("Enter Number 1 : ")
b = input("Enter Number 2 : ")

print("""
Press + for Addition
Press - for Subtraction
Press * for Multiplication
Press / for Divison
""")
choice = input("Enter Operator : + | - | * | / :-")
print(Calc(a,b,choice))
