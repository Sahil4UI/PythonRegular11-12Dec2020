data = [{"roll":101,"Name":"Rahul","marks":[98,42,69]},
        {"roll":102,"Name":"Mayank","marks":[93,82,67]},
        {"roll":103,"Name":"Rajesh","marks":[90,89,90]},
        {"roll":104,"Name":"Suresh","marks":[10,82,61]},
        {"roll":105,"Name":"Ramesh","marks":[5,17,60]}
    ]

"""
101 Rahul
102 Mayank
103 Rajesh
"""
#print("ROLL NO"," NAME ","AVERAGE")
for i in data:
    avg = sum(i["marks"])//(len(i["marks"]))
    print(i.get("roll"),i.get('Name'),avg)

