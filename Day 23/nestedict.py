students = {
    "sid": [1, 2, 3],
    "names": ["raj" "pooja", "komla"],
    "grade": ["A", "A+", "B"],
}

s = []
for i in students.values():
    print(i)
    s.append(i)

print(s)

# First student details
print("Sid : ", s[0][0])
print("Name : ", s[1][0])
print("Grade : ", s[2][0])
