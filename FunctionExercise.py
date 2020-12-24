'''
def Even(x):
    if x%2==0:
        return True
    else:
        return False
    
x= [1,2,3,4,5,6,7,8,9,10]
x
res= []

for i in x:
    value = Even(i)
    if value==True:
        print(i)
'''
'''
def Show(x):
    x.sort()
    return x[-1],x[-2],x[-3]

x = [1,2,90,87,34,23,67,89]
a,b,c = Show(x)
print(a)
print(b)
print(c)
'''






