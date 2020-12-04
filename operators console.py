Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Comparison Operators  > < >= <= != ==
>>> 5 > 10
False
>>> 10 < 5
False
>>> 10 >= 10
True
>>> 5 <= 10
True
>>> 10 != 10
False
>>> #== - equality operator
>>> 5 == 10
False
>>> 10 = 10
SyntaxError: cannot assign to literal
>>> # = -> asignment operator
>>> x = 5
>>> #logical Operators-> and, or , not
>>> #and -all conditions are true -> result - true
>>> 5 >= 10 and 10 > = 5
SyntaxError: invalid syntax
>>> 5 >= 10 and 10 >= 5
False
>>> 5 >= 5 and 10 > = 5 and 1==1
SyntaxError: invalid syntax
>>> 5 >= 5 and 10 >= 5 and 1==1
True
>>> #or -if atleast one conditon is true, then overall answer is true
>>> 5 >= 50 or 10 >= 5 or 1==1
True
>>> #not-True->false,false-True
>>> 5>=50
False
>>> not 5>=50
True
>>> 