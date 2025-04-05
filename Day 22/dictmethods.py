# without methos add,update and delete on dictionary

# books = {}
# print(books)
# books["isbn"] = 1111
# print(books)
# books["isbn"] = 5555
# print(books)
# books["title"] = "python"
# print(books)
# books["authors"] = "rossom", "smith"
# print(books)


# methos
# update()
# students = {}
# print(students)
# students.update({"sid": 101})
# print(students)
# students.update({"sid": 101, "sid": 201})
# print(students)
# students.update({"name": "Pooja", "grade": "A+"})
# print(students)
# students.update({"subject": ["py", "js", "sql"]})
# print(students)
# students["sid"] = 101
# print(students)
# students.update({"city": "mumbai"})
# print(students)

# # removing pop(),popitem()
# students.pop("city")
# print(students)
# # students.pop('per') # KeyError : per
# # print(students)

# students.popitem()  # last key and value
# students.popitem()
# print(students)

# # clear()
# students.clear()

# # del()
# del students


# copy()
number = {1: 100, 2: 200, 3: 300}
print(number)
x = number.copy()
print(x)

# values(), get(), keys(), item()
print(number.values())

print(number.get(2))
print(number.get(200))  # None if key not exists

print(number.keys())

print(number.items())

# formkey()
n = [1, 3, 45, 3]
print(n)
n = dict.fromkeys(n, "itv")
print(n)

# setdefault()
movies = {"name": "kgf", "start": 5}
print(movies)
x = movies.setdefault("duration", "2.10mins")
print(x)
movies.update({"duration": "3hrs"})
print(movies)
movies.update({"duration": x})
print(movies)
