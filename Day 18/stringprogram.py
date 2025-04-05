"""
user = input('Enter : ')
for i in range(len(user)):
    try:
        if user[i] in 'aeiou':
            user = user.replace(user[i],'')
    except:
        pass
print(f'{user}')



str = input('Enter string: ')
vowels = ''
count = 0
for i in str:
    if i in 'aeiou':
        vowels += i
        count += 1

print('Vowels are : ',vowels )
print('Volwels count are : ', count)



str = input('Enter string: ')
vcount = 0
ccount = 0
for i in str:
    if i.lower() in 'aeiou':
        vcount += 1
    else:
        ccount += 1

print('Consonnet count are : ', ccount)
print('Volwels count are : ', vcount)


"""

user = input("Enter : ")
char = input("Enter char to find: ")
final = ""
flag = False
for i in user:
    if i.lower() == char.lower():
        if flag == False:
            print(f"{i} find in {user}")
            new = input("Enter char to replace: ")
            flag = True
        final += new
    else:
        final += i
print(f"Done {final} string")
