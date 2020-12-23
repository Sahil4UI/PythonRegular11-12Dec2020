def calc(x,y,operator):
    result = eval(x+operator+y)
    print(result)
    
while True:
    x=input("Enter number 1:")
    y=input("Enter number 2:")
    print(
    """
    Press + to add
    Press - to subtract
    Press * to multiply
    Press / to Divide
    """)
    operator = input("Enter Operator")
    calc(x,y,operator)
