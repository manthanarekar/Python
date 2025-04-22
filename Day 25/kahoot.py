name1 = ["Amir", "Bear", "Charlton", "Daman"]
name2 = name1
name3 = name1[:]
print(id(name1), id(name2), id(name3))
name2[0] = "Alice"
name3[1] = "Bob"
sum = 0
for ls in (name1, name2, name3):
    if ls[0] == "Alice":
        sum += 1
    if ls[1] == "Bob":
        sum += 10
print(sum)
