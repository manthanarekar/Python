# String Method
# a = 'Java'
# b = 'Html'
# a += b
# print(a)

s = "Welcome to Python"

"""
print("----- COUNT ------")
print(s.count("o"))
print(s.count(""))  # 18 | len(s) + 1
s1 = ""
print(s1.count(""))  # 1
print(s.count("om"))  # 1
print(s.count("jhkjde"))  # if not present
print(s.count("o", 4, 12))  # 2


print("---- FIND -----")  # First index number
print(s.find("o"))  # 4
print(s.find(""))  # 0
print(s.find("om"))  # 4 first char position
print(s.find("ot"))  # -1 if not present
print(s.find("kjefb"))  # -1 if not present
print(s.count("o", 5, 12))  # 9

print("----- INDEX ------")
print(s.index("o"))  # 4
print(s.index(""))  # 0
print(s.index("om"))  # 4
# print(s.index('ot')) # if not present then error
# print(s.index('z')) # error
print(s.index("o", 4, 12))

"""

print("----- replcae -----")
print(s.replace("o", "z"))  # Welczme tz Pythzn
print(s.replace("o", "z", 1))  # Welczme to Python
print(s.replace("q", "z"))  # if not present nothing will be change
print(s.replace("", "z"))  # write z after every char

print("----- join -----")
print(s.join("java"))
print(s.join("x"))
print("x".join(s))
print(" ".join(s))
str = "ceabd"
print("".join(sorted(str)))  # here help to conver list to str

print("----- split -----")
print(s.split())  # spliting as per space
s1 = "Python,Java,html,css,bootstrap"
print(s.split(" ", 1))
print(s.split(" ", 0))
print(s.split(" ", 2))
print(s.split(" ", 5))
print(s1.split(",", 2))
print(s1.split(","))

print("----- splitlines -----")
print(s.splitlines())
s3 = "h1\nhow r u?"
print(s3)
print(s3.split())
print(s3.splitlines())

print("----- zfill -----")
print(s.zfill(25))
print(s.zfill(5))

print("----- strip -----")
z = "           Mango             "
print(z.strip())
