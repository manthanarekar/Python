students = (11, "raj", "A+", "mumbai", 963852)
"""
for i in students:
    print(i)
    
i = 0
while i < len(students):
    print(i, students[i])
    i += 1 
    
"""

color = ("red", "green", "blue", "white", "black", "red", "pink")
user = input("Enter to check in tuple: ")
count = 0
find = ""
for i in color:
    if i == user:
        count += 1
if count != 0:
    print(f"{user} found for {count} times")
else:
    print("Not found")

flag = False

for i in range(len(color)):
    if color[i] == user:
        if flag == False:
            find = i
            flag = True
            
if find != "":
    print(f"{user} found on {find} position")
else:
    print("Not found")
