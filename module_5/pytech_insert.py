from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.b9dss.mongodb.net/CSD?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
beginner_line_var = "Inserted student record {first_name} {last_name} into the students collection with document id {document_id}"
print("--INSERT STATEMENTS--")
thorin = {
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "student_id": "1007"
}
thorin_document_id=db.students.insert_one(thorin).inserted_id
print(beginner_line_var.format(first_name = thorin["first_name"], last_name = thorin["last_name"], document_id = thorin_document_id))
bilbo = {
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "student_id": "1008"
}
bilbo_document_id=db.students.insert_one(bilbo).inserted_id
print(beginner_line_var.format(first_name = bilbo["first_name"], last_name = bilbo["last_name"], document_id = bilbo_document_id))

frodo = {
    "first_name": "Frodo",
    "last_name": "Baggins",
    "student_id": "1009"
}
frodo_document_id=db.students.insert_one(frodo).inserted_id
print(beginner_line_var.format(first_name = frodo["first_name"], last_name = frodo["last_name"], document_id = frodo_document_id))
input("\n End of program,press any key to exit... ")