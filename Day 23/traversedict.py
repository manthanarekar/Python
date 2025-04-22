# students = {"sid": 101, "sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]}
# for i in students:
#     print(i)

# for i in students.items():
#     print(i)

# for i in students.keys():
#     print(i)

# for i in students.values():
#     print(i)

# students = {
#     {"sid": 101, "sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
#     {"sid": 101, "sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
#     {"sid": 101, "sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
# }

# for k, v in students.items():
#     print(k, "=", v)

# students = {
#     101: {"sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
#     102: {"sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
#     103: {"sname": "raj", "grade": "A", "subject": ["py", "js", "sql"]},
# }

# for i in students.items():
#     print(i)

# for i, j in students.items():
#     print(i, j)

# for i, j in students.items():
#     print(i, ":", end=" ")
#     for k, v in j.items():
#         print(v, end=" ")
#     print()

# students = {
#     101: {"sname": "raj", "subject": {"py": 90, "js": 80, "sql": 67}},
#     102: {"sname": "komal", "subject": {"py": 78, "js": 88, "sql": 97}},
#     103: {"sname": "pooja", "subject": {"py": 98, "js": 60, "sql": 67}},
# }
# marks = []
# for i, j in students.items():
#     print(i, end=" ")
#     for k, v in j.items():
#         print(v, end=" ")
#         if k == "sunjects":
#             for m in j[k].values():
#                 marks.append(m)
#     print()
#     totalmarks = sum(marks)
#     print("Total Marks : ", totalmarks)
#     per = totalmarks / len(j[k])
#     print(f"{per:0.2f}")
#     marks.clear()
#     print()


library = {}
count = int(input("Enter count for books : "))
for i in range(count):
    isbn = input(f"Enter {i+1} book isbn : ")
    title = input(f"Enter {i+1} book title : ")
    author = input(f"Enter {i+1} book author : ")
    price = input(f"Enter {i+1} book price : ")
    library.update(
        {isbn: {"isbn": isbn, "title": title, "author": author, "price": price}}
    )

# print(library)

for k, v in library.items:
    print(k, end=" ")
    for val in v.values():
        print(val, end=" ")
    print()
    
    
    

