#function->User Defined functions and PRedefined functions
#def -define
#function definition
#global variables
'''
x  =10
y = 20

def Add():
    #local variable
    x = 90
    y = 30
    print(f"the Sum of {x} and {y}={x+y}")

Add()
print("Sum=",x+y)
'''

#parameterized function
#arguments
'''
def Add(x,y):
    print(f"the Sum of {x} and {y}={x+y}")
#parameters
Add(90,90)
'''
'''
def Add(x,y):
    return x+y
res = Add(90,90)
print(res)
'''
#None
#recursive Function
'''
def f1(x):
    #base case - condition
    if x>20:
        return#break
    print(x)
    f1(x+2)

f1(2)
'''
'''
def f1(x):
    #base case - condition
    if x<1:
        return#break
    print(x)
    f1(x-1)

f1(10)
'''
#factorial of a number:5 ->
'''
def Fact(x):
    if x==1:
        return 1
    return x*Fact(x-1)

print(Fact(5))
'''

def SOD(x):
    if x==0:
        return 0
    rem = x%10    
    return rem+SOD(x//10)


print(SOD(123))



























