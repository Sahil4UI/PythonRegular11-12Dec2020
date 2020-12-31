'''
def f1(x):
    if x>5:
        return
    f1(x+1)
    print(x)

f1(1)
'''
'''
def Mul(a,b):
    if b==1:
        return a
    if a==0:
        return 0
    return a+Mul(a,b-1)

print(Mul(9,6))
'''
'''
def f1(string,size):
    if size==0:
        return string[0]
    return ""+string[size]+f1(string,size-1)

x = "abcdef"
size = len(x)-1
print(f1(x,size))

'''


def Prime(n,i):
    if n<=2:
        return True if n==2 else False
    if n==i:
        return True


    if n%i==0:
        return False
    
    return Prime(n,i+1)




n = int(input("Enter a number"))
print(Prime(n,2))

















