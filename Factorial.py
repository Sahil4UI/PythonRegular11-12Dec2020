#find the factorial of a number
# 5-> 5*4*3*2*1
#import math
#x = int(input("Enter a number :"))
'''
print(math.factorial(x))
'''
'''
factorial = 1
for i in range(1,x+1):
    factorial = factorial*i
print(factorial)

'''
#fibonacci series->0 1 1 2 3 5 8 13....
firstNum = 0
secondNum= 1
print(firstNum)
print(secondNum)

for i in range(8):
    thirdNum = firstNum+secondNum
    print(thirdNum)
    firstNum,secondNum = secondNum,thirdNum

