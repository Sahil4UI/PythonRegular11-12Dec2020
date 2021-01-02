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
'''
result = list(map(Conversion,list1))
print(result)

#lambda Funtion - single line function
x = lambda cm : 0.01*cm
print(x(345))

