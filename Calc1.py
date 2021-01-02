#calculator -add,sub,mul,div

def Add(x,y):
    return x+y

def Sub(x,y):
    return x-y

def Mul(x,y):
    return x*y

def Div(x,y):
    return x/y


a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))

print("""
Press + for Addition
Press - for Subtraction
Press * for Multiplication
Press / for Divison
""")
choice = input("Enter Choice")
d = {"+":Add,"-":Sub,"*":Mul,"/":Div}
ls = ["+","-","*","/"]

if choice in ls:
    function = d.get(choice)
    print(function(a,b))
else:
    print("Invalid Operation")
