num = int(input("Enter student count: "))
student = []
for i in range(num):
    stu = input(f"Enter {i} student name: ")
    student.append(stu)
print(student)
