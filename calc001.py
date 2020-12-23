def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

while True:
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    print(
    """
    Press + to add
    Press - to subtract
    Press * to multiply
    Press / to Divide
    """)
    choice = input("Enter choice:")
    d = {"+":add,"-":sub,"*":mul,"/":div}
    function = d.get(choice)
    function(x,y)
