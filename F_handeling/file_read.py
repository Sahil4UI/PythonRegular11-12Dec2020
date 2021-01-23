file = open('mydata.txt','r')
# data = file.read()
# data = file.read(20)
# data = file.readline()
data = file.readlines()
print(data)
for line in data:
    print(line,end="")
file.close()




#1. create a textfile named as abc.txt,
#2. read it 
#3. replace all 'a' with 'x' in the file.