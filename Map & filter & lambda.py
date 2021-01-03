#Map , filter
def Conversion(cm):
    return 0.01*cm

#print(Conversion(99))
list1 = [1,100,25.6,300,500,90.45,345.76,42345]
'''
result = []
for i in list1:
    result.append(Conversion(i))
print(result)
result = list(map(Conversion,list1))
print(result)

'''
#lambda Funtion - single line function
'''
def Conversion(cm):
    return 0.01*cm

x = lambda cm : 0.01*cm
print(x(345))
'''
'''
def Even(x):
    if x%2==0:
        return True
    else:
        return False

x=[1,2,3,4,5,6]
result = list(filter(Even,x))
print(result)
'''
'''
result = list(map(Even,x))
for i in range(len(result)):
    if result[i]==True:
        print(x[i])
'''
'''
import functools
list1=[1,2,3,4,5]
x =functools.reduce(lambda a,b:a+b,list1)
print(x)
'''

d = {k:v for k,v in ('a1','b2')}
d['a1']=1
d['b2']=2


















































