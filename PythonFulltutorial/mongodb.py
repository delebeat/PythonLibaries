__author__="Bamidele"

import pymongo
# uri="mongodb://localhost:27017"
uri="mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(uri)
database=client['fullstack']
collection=database['students']
students=collection.find({})


# print(students)
# students=[student['mark'] for student in collection.find({})]
# print(students)

# student_list=[]


# for student in students:
#
#     print(student['mark'])
# for content in student_list:
#     student_list.append(content)


# print(student_list)
