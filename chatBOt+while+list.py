helloList=["hello","hi","hey"]
byeList = ["bye","see you later"]
chat = True
while chat:
    msg = input("Enter Message").lower()
    if msg in helloList:
        print("Hello Sir...")
    elif msg in byeList:
        print("Good Bye...")
        chat =False
