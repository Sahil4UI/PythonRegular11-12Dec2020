Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arithmetical,comparison,logical
>>> #logical - and , or , not
>>> #and - if all conditions are true then result is true
>>> 4>=10 and 45 <= 100
False
>>> 40>=10 and 45 <= 100
True
>>> #or - atleast one conditions must be true for true as a result
>>> 1 >= 4  or 40==10 or 45 <= 100
True
>>> #not-> true ->false
>>> #false -> true
>>> 5 > = 10
SyntaxError: invalid syntax
>>> 5 >= 10
False
>>> not 5 >= 10
True
>>> not 5 >= 10 and not 5<=10
False
>>> (not 5>=10) and (not 5<=10)
False
>>> #bitwise operators-> bits(binary)
>>> 10 & 17
0
>>> 25 & 10
8
>>> #bitwise or
>>> 49 | 22
55
>>> #bitwise not
>>> ~ 12
-13
>>> ~ -12
11
>>> ~ 19
-20
>>> ~ -19
18
>>> #bitwise (left shift or right shift operator)
>>> 12 << 1 #1 bit shift
24
>>> 12 << 2
48
>>> 17 << 2
68
>>> 17 >> 1
8
>>> 17 >> 2
4
>>> #membership operator
>>> #in , not in
>>> vowels = "aeiouAEIOU"
>>> 'z' in vowels
False
>>> 'A' in vowels
True
>>> 'z' not in vowels
True
>>> x = "1234"
>>> 1 in x
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    1 in x
TypeError: 'in <string>' requires string as left operand, not int
>>> '1' in x
True
>>> x = [1,2,3,4,5]
>>> 5 in x
True
>>> #Assignment operator
>>> x = 5
>>> x += 5
>>> #x = x+5
>>> x =+ 5
>>> x
5
>>> x+=5
>>> x
10
>>> x = 0
>>> x+=5
>>> x
5
>>> x =10
>>> x=0
>>> x=+5
>>> x
5
>>> x -= 5
>>> x
0
>>> x =10
>>> x *=5
>>> x
50
>>> x/=5
>>> x
10.0
>>> x %= 2
>>> 
>>> x
0.0
>>> x = 5
>>> x **= 2
>>> x &=10
>>> x
8
>>> x |= 2
>>> x
10
>>> #identity operator
>>> x = 5
>>> y = 5
>>> x is y
True
>>> x is not y
False
>>> # == ,is
>>> x = [1,2,3,4,5]
>>> y = [1,2,3,4,5]
>>> x is y
False
>>> x==y
True
>>> # == -> value
>>> # is -value and memory
>>> x = [1,2,3,4,5]
>>> y=x
>>> x is y
True
>>> del x[0]
>>> x
[2, 3, 4, 5]
>>> y
[2, 3, 4, 5]
>>> x = 12
>>> 