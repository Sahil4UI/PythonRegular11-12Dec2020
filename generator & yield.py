#Return vs Yield
'''
def f1(x):
	for i in range(1,x+1):
		return i
f1(10)
'''
'''
def f1(x):
	for i in range(1,x+1):
	    yield(i)
gen_obj = f1(10)
#print(list(gen_obj))
for data in gen_obj:
    print(data)

'''

def f1():
    yield(1,2,3)

x = f1()
for i in x:
    print(i)
'''
def Square():
    for i in range(1,11):
        yield(i**2)

obj=Square()
'''
