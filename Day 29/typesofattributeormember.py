# Type of memeber / attribte in class
# 1) class
# 2) instance
# 3) static
# 4) local


# class TypeofMember:
#     id = 111

#     def getid(self):
#         id = 222
#         print(id)


# t = TypeofMember()
# print("id : ", TypeofMember.id)
# print("id : ", t.id)
# t.getid()

# 3) Instance

class Area:
    radius = 4.5
    
    def __init__(self):
        print('init-1')


    def areaofcircle(self):
        self.b = 'JOjo'
        return 3.14 * self.radius * self.radius
    
a = Area()
print(list(map()))