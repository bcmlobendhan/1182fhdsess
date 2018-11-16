import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["database"]
collection = db["tableinputs"]

user_name = input("Enter user name : ")
p_word = input("Enter password : ")
for x in collection.find({},{"user":1,"pass":1}):
	name = str(x["user"])
	password=str(x["pass"])
if user_name==name and p_word==password:
	print("login successful")
else:
	print("login failed")