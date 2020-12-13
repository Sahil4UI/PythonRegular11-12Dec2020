Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list - python data collection
>>> x = [1,23.4,True,"Ram"]
>>> 
>>> 
>>> 
>>> 
>>> #index & slicing
>>> #indexing
>>> x
[1, 23.4, True, 'Ram']
>>> x[0]
1
>>> x[1]
23.4
>>> x[2]
True
>>> x[3]
'Ram'
>>> x[-1]
'Ram'
>>> x[-2]
True
>>> x[-3]
23.4
>>> x = [1,2,3,4,5,6,7,8,9,10]
>>> x[4:9]
[5, 6, 7, 8, 9]
>>> x =[1,2,3,4,[5,6,7,[8,9]]]]
SyntaxError: unmatched ']'
>>> x =[1,2,3,4,[5,6,7,[8,9]]]
>>> x
[1, 2, 3, 4, [5, 6, 7, [8, 9]]]
>>> x[4]
[5, 6, 7, [8, 9]]
>>> x[4][3][1]
9
>>> x = [1,2,[3,4,5],[6,7,8,[9,[10,[11,12,13,14,[15]]]]]]
>>> x[3][3][1][1][4]
[15]
>>> x[3][3][1][1][4][0]
15
>>> #methods in list
>>> #list - mutable - which can be changed - update,delete
>>> x=[]
>>> x.append(1)
>>> x
[1]
>>> x.append(2000)
>>> x
[1, 2000]
>>> x.append(3000)
>>> x
[1, 2000, 3000]
>>> x.append("hello")
>>> x
[1, 2000, 3000, 'hello']
>>> x.insert(1,"python")
>>> x
[1, 'python', 2000, 3000, 'hello']
>>> x.insert(-1,True)
>>> x
[1, 'python', 2000, 3000, True, 'hello']
>>> x.insert(-2,"hi")
>>> x
[1, 'python', 2000, 3000, 'hi', True, 'hello']
>>> x[0]= 200000
>>> x
[200000, 'python', 2000, 3000, 'hi', True, 'hello']
>>> x
[200000, 'python', 2000, 3000, 'hi', True, 'hello']
>>> x.pop()#last value
'hello'
>>> x
[200000, 'python', 2000, 3000, 'hi', True]
>>> x.pop()
True
>>> x
[200000, 'python', 2000, 3000, 'hi']
>>> x.pop(0)
200000
>>> x
['python', 2000, 3000, 'hi']
>>> x.remove('hi')
>>> x
['python', 2000, 3000]
>>> del x[0]
>>> x
[2000, 3000]
>>> x.clear()
>>> x
[]
>>> x = [1,2]
>>> y = [3,4]
>>> x+y
[1, 2, 3, 4]
>>> x.extend(y)
>>> x
[1, 2, 3, 4]
>>> y
[3, 4]
>>> x = [1,2]
>>> y = [3,4]
>>> y.extend(x)
>>> y
[3, 4, 1, 2]
>>> x= [1,2]
>>> y = [3,4]
>>> x+y
[1, 2, 3, 4]
>>> x-y
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> x*y
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'list'
>>> x
[1, 2]
>>> x*5
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> x
[1, 2]
>>> x = [1,99,98,89,65,67,43,21,0]
>>> x.sort()
>>> x
[0, 1, 21, 43, 65, 67, 89, 98, 99]
>>> x.sort(reverse=True)
>>> x
[99, 98, 89, 67, 65, 43, 21, 1, 0]
>>> x = [1,2]
>>> y= x.copy()
>>> x
[1, 2]
>>> y
[1, 2]
>>> x
[1, 2]
>>> y=x
>>> id(x)
140307475701888
>>> id(y)
140307475701888
>>> x
[1, 2]
>>> y
[1, 2]
>>> x.pop()
2
>>> x
[1]
>>> y
[1]
>>> x
[1]
>>> x = [1,2,3,4]
>>> y = x.copy()
>>> id(x)
140307475703104
>>> id(y)
140307475704576
>>> x.pop()
4
>>> x
[1, 2, 3]
>>> y
[1, 2, 3, 4]
>>> 