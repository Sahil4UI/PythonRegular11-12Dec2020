def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))
print(
"""
Press 1 to add
Press 2 to subtract
Press 3 to multiply
Press 4 to Divide
""")
choice = int(input("Enter choice:"))

if choice ==1:
    add(x,y)
elif choice ==2:
    sub(x,y)
elif choice ==3:
    mul(x,y)
elif choice ==4:
    div(x,y)
else:
    print("invalid choice")


    




