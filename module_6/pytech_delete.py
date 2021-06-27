import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.b9dss.mongodb.net/CSD?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

result = db.students.updateOne({"student_id": 1007}, {"$set": {"last_name": "Oakenshield II"}})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

beginner_line_var = "Inserted student recordinto the students collection with document id {document_id}"
print("\n--INSERT STATEMENTS--")
john = {
    "first_name": "John",
    "last_name": "Doe",
    "student_id": "1010"
}
john_document_id=db.students.insert_one(john).inserted_id
print(beginner_line_var.format(document_id = john_document_id))

print("\n\n-- DISPLAYING STUDENT TEST DOC --\nStudent ID: 1010\nFirst Name: John\nLast Name: Doe")
db.students.delete_many({"student_id": 1010})

print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")
