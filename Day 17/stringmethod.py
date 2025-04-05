a = "Welcome to python"
b = "Python12"
c = ""
d = "python@123"
e = "123.89"

print(a.upper())
print(a)
print(a.lower())
print(a.isupper())  # False
print(a.islower())  # True

# checking a
print(a.isalpha())  # False Space
print(a.isalnum())  # False
print(e.isnumeric())  # False
print(e.isdigit())
print(e.isdecimal())
