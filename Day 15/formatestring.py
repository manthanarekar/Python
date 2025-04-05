name = "Rohit"
place = "Mumbai"
ans1 = "My name is", name, "and I am from", place
formate = name, place, "Pune"
# print(ans1)

# print("My name is", name, "and I am from", place )

# f string
# print("My name is {name} and I am from  {place} ")

# %s string specifier
ans2 = "My name is %s and I am from %s " % (name, place)
print(f"ans2 : {ans2}")

# .format()
ans4 = "My name is {0} and I am from {1} and {2}".format(formate)

