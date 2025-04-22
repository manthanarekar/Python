# print(help(list))

# print(bin(12345))

# print(hex(90))

# print(oct(1230))

# print(pow(2,4))

# print(round(1234.678))

# print(divmod(123,4))

# zip() -> packing data into one element
# name = ["raj", "pooja", "komal"]
# grade = ["A", "O", "B"]
# per = [89, 90]

# print(list(zip(name, grade)))  # [('raj', 'A'), ('pooja', 'O'), ('komal', 'B')]
# print(list(zip(name, grade, per)))  # [('raj', 'A', 89), ('pooja', 'O', 90)]

# per = [89, 90, None]

# for i in name, grade, per:
#     print(i)

# for i in name, grade, per:
#     print(i[0])

# print(list(zip(name, grade, per)))
# print(set(zip(name, grade, per)))
# print(tuple(zip(name, grade, per)))
# print(tuple(zip(name, grade)))


# student = [("raj", "A", 89), ("pooja", "O", 90), ("komal", "B", None)]
# # zip(*variable) = unzip of data onto seperate elements
# print(student)
# print(list(zip(*student)))
# print(tuple(zip(*student)))
# print(set(zip(*student)))
# print(dict(zip(*student))) # error

# enumerate

# a = {"a,", "e", "i", "o", "u"}
# print(list(enumerate(a)))


# # iter()
# colors = ["red", "green", "blue"]
# print(colors)
# newcolors = iter(colors)

# first = next(newcolors)
# print(first)

