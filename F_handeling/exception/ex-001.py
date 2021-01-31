
try:
    x=int(input("Enter no 1 : "))
    y=int(input("Enter no 2 : "))
    print(x/y)
    
except BaseException as be:
    print(be)
finally:
    print(x+y)
    print(x-y)
    print(x*y)
    