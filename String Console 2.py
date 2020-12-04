Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "Python is a Programming Language"
>>> x.lower()
'python is a programming language'
>>> x.upper()
'PYTHON IS A PROGRAMMING LANGUAGE'
>>> x.swapcase()
'pYTHON IS A pROGRAMMING lANGUAGE'
>>> x.casefold()
'python is a programming language'
>>> x.capitalize()
'Python is a programming language'
>>> x.title()
'Python Is A Programming Language'
>>> x.replace("Python","Java")
'Java is a Programming Language'
>>> x.count('a')#frequency
4
>>> x
'Python is a Programming Language'
>>> x.index('a')
10
>>> x.index('a',0)
10
>>> x.index('a',11)
17
>>> x.index('a',-1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x.index('a',-1)
ValueError: substring not found
>>> x.index('a',18)
25
>>> x.find('a')
10
>>> x.index('a',11)
17
>>> 
>>> x.index('x')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x.index('x')
ValueError: substring not found
>>> x.find('x')
-1
>>> #-1 -> value not found in the string
>>> x
'Python is a Programming Language'
>>> x = "Python"
>>> len(x)
6
>>> x.center(6)
'Python'
>>> x.center(5)
'Python'
>>> x.center(1)
'Python'
>>> x.center(7)
' Python'
>>> x.center(8)
' Python '
>>> x.center(20)
'       Python       '
>>> x.center(20,"*")
'*******Python*******'
>>> x.center(20,"-")
'-------Python-------'
>>> x.center(20,"@")
'@@@@@@@Python@@@@@@@'
>>> #strip
>>> x = '       Python       '
>>> x.lstrip()
'Python       '
>>> x.rstrip()
'       Python'
>>> x
'       Python       '
>>> x.strip()
'Python'
>>> x = '@@@@@@@Python@@@@@@@'
>>> x.strip()
'@@@@@@@Python@@@@@@@'
>>> x.strip("@")
'Python'
>>> x = '@@@@@@@Pyt@hon@@@@@@@'
>>> x.strip('@')
'Pyt@hon'
>>> #z-fill - zero fill
>>> x = "Python"
>>> x.zfill(6)
'Python'
>>> x.zfill(20)
'00000000000000Python'
>>> x = "Welcome to our class"
>>> x.split()
['Welcome', 'to', 'our', 'class']
>>> x
'Welcome to our class'
>>> x.split(o)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x.split(o)
NameError: name 'o' is not defined
>>> x.split('o')
['Welc', 'me t', ' ', 'ur class']
>>> #ASCII(American standard code for information interchange) values
>>> #A - 65
>>> #ord,chr
>>> ord('A')
65
>>> ord('@')
64
>>> ord('%')
37
>>> #chr ->character
>>> chr(65)
'A'
>>> chr(92)
'\\'
>>> chr(98)
'b'
>>> chr(97)
'a'
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> 22/7
3.142857142857143
>>> 22//7
3
>>> 5/2
2.5
>>> 5//2
2
>>> 