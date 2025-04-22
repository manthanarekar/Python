user = str(input("Enter string : "))
# flipstr = user[::-1]
# if len(flipstr) >= 3:
#     final = flipstr[:3]
#     final = final[::-1]
#     if final[:3] == "ing":
#         user += "ly"
#     else:
#         user += "ing"
#     print(user)
# else:
#     print("Lenth of string is less than 3 ")

check = user[:1]
final = check
i = 1
while i < len(user):
    if user[i] == check:
        final += "$"
    else:
        final += user[i]
    i += 1
print(f"final string : {final}")
