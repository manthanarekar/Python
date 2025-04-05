# Traversing of string via loop
msg = "Welcome"

# for i in range(len(msg)):
# print(i , msg[i])
# i = 0
# while i < len(msg):
#     print(i , msg[i])
#     i += 1

# msg = input("Enter string: ")
# for i in range(0, len(msg), 2):
#     print(msg[i], end="")

# msg = input("Enter char: ")
# check = input("Enter check: ")
# count = 0
# charcheck = ""
# for i in range(len(msg)):
#     k = i
#     for j in range(len(check)):
#         try:
#             charcheck += msg[k]
#             k += 1
#         except:
#             None
#     if charcheck == check:
#         count += 1
#     charcheck = ""

# (
#     print(f"{check} present in {msg} for {count} time")
#     if count != 0
#     else print(f"{check} is not present in {msg}")
# )


# msg = input("Enter char: ")
# check = input("Enter check: ")
# find = ""
# for i in range(len(msg)):
#     if check == msg[i]:
#         find += f"{i} "
# if find != "":
#     print(f"{check} is present in {msg} on position : {find} ")
# else:
#     print("Not present")


msg = input("Enter char: ")
# for i in msg[::-1]:
#     print(i, end="")
# print()

# for i in reversed(msg):
#     print(i, end="")

# reverstr = ''
# for i in msg:
#     reverstr = i + 



for i in range(len(msg)):
    print(msg[int(len(msg) - i - 1)], end="")
