data = [{"id":101,"name":"Rahul","addr":"Delhi"},
        {"id":102,"name":"mukesh","addr":"Gujrat"},
        {"id":103,"name":"Lokesh","addr":"Delhi"},
        {"id":104,"name":"Rahul","addr":"Delhi"},
        {"id":105,"name":"Rahul","addr":"Delhi"}]

import csv
#csv-comma separated values-excel file
file = open("xyz.csv",'w')
writer = csv.writer(file)
writer.writerow(data[0].keys())
for i in data:
    writer.writerow(i.values())
file.close()

file = open("xyz.csv","r")
reader = csv.reader(file)
for i in reader:
        print(i)
