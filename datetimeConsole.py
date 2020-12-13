Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> datetime = datetime.now()
>>> datetime.strftime("%d/%m/%y")
'12/12/20'
>>> datetime.strftime("%d/%m/%y , %p")
'12/12/20 , AM'
>>> datetime.strftime("%d/%m/%y , %a")
'12/12/20 , Sat'
>>> #%a - > day
>>> datetime.strftime("%H:%M:%S")
'11:43:24'
>>> datetime.strftime("%H:%M:%S,%p")
'11:43:24,AM'
>>> #%H  -> 24hr
>>> #%l -> 12hrs
>>> 