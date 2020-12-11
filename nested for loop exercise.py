'''
for i in range(1,5):
    for j in range(i):
        print(i,j)
'''

'''
*
**
***
****
*****
for i in range(1,6):
    print("*"*i)
'''

'''
    *
   ***
  *****
 *******
*********

for i in range(1,6):
    print(" "*(5-i)+"*"*(2*i-1))
'''
#draw this using nested for loop
"""
*
**
***
****
*****
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in reversed(range(1,6)):
    for j in range(i):
        print("*",end="")
    print()

"""
'''
******
*    *
*    *
*    *
*    *
******
'''
for i in range(1,7):
    for j in range(1,7):
        if (i==1 or i==6) or (j==1 or j==6):
            print("*",end="")
        else:
            print(" ",end="")
    print()
#Homework
"""
    *
   **
  ***
 ****
*****

    *
   * *
  * * *
 * * * *
* * * * *


1
12
123
1234
12345

1
10
101
1010
10101

1
23
456
78910
"""


















