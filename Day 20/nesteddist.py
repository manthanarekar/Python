studentdb = [
    ["id", "name", "grade"],
    [101, "raj", "A"],
    [102, "pooja", "O"],
    [103, "komal", "B"],
]

# for j in studentdb:
#     for i in j:
#         print(i, end="\t")
#     print()

# WAP to tabke student id , name , grade from user as per the count user and show in table formate
# studentdb = [["id", "name", "grade"]]
# count = int(input("Enter count for student : "))
# for i in range(count):
#     id = int(input(f"Enter {i+1} student id : "))
#     name = input(f"Enter {i+1} student name : ")
#     grade = input(f"Enter {i+1} student grade : ")
#     studentdb.append([id, name, grade])

# for i in studentdb:
#     for j in i:
#         print(j, end="\t")
#     print()

# Search by ID

stuid = int(input("Enter student id to get details : "))
flag = False
for i in studentdb:
    if i[0] == stuid:
        flag = True
        for j in studentdb[0]:
            print(j, end="\t")
        print()
        for j in i:
            print(j, end="\t")

if flag == False:
    print("Student not fount")

# Delete
studid = int(input("\nEnter student id for delete : "))
flag = False
for i in studentdb:
    if i[0] == studid:
        flag = True
        studentdb.pop(studentdb.index(i))
        print("Delete Done!")

if flag == False:
    print("student data not found")
