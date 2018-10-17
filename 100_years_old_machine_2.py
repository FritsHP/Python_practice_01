import datetime

name = raw_input("Tell me your name: ")
age = input("Tell me your age: ")
whatup = datetime.datetime.now()
diff = 100 - age

#show exactly the year you turn 100
print("Hello" + name + ", you will be 100 years in ",whatup.year+diff)
