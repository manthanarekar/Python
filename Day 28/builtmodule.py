# from datetime import datetime
# print(datetime.now())

# import random

# print(random.randrange(1, 50))  # random interger number
# print(random.randrange(1, 51, 2))  # odd interger between 1 to 50
# print(random.randint(1, 50))  # work only for integer
# print(random.choice(range(1, 50)))  # work as per sequence

# name = ["jeet", "rahul", "rohit"]
# print(random.choice(name))
# print(random.choices(name, k=2))
# print(random.sample(name, k=2))


# WAP ti generate random password
# import string
# import random

# allcharaters = (
#     string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits
# )

# # print(allcharaters)
# length = int(input("Enter length for password : "))
# password = "".join(random.choices(allcharaters, k=length))
# print(password)


# import os

# print(os.getcwd())
# print(os.listdir())
# # os.mkdir("dir1")
# # os.rmdir("dir1")
# print(dir(os))

import sys

# print(sys.platform)
# print(sys.version)
# print(sys.version_info)
# print(sys.modules)

# sys.stdout.write("welcome")

print("enter name : ", sys.argv)
print("name : ", sys.argv[1])
