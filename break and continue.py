#break,continue
'''
for i in range(1,10000):
    print(i)
    if i==100:
        break
'''
#print 1-20 excluding numbers multiple of 3
'''
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
'''
#take a number as an input from user,check wether its prime or not
'''
x=int(input("enter number :"))

for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")

'''
#find the sum of digits of number->123->1+2+3
