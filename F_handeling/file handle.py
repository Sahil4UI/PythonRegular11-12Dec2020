'''
file  = open('xyz.txt','w')
file.write("hi")
file.close()
'''
file =open('img.jpg','rb')
data = file.read()
print(data)
file.close()

file =open('img-copy.jpg','wb')
file.write(data)
file.close()
