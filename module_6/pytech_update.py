import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.b9dss.mongodb.net/CSD?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

result = db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Oakenshield II"}})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")


print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n\n\n")
input("End of program, press any key to continue...")