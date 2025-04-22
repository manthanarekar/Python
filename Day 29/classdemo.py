# Empty class
# class Colege:
#     pass


# class College:
#     collegeid = 111
#     collegename = "reparel"
#     address = "matunga"


# print(College)
# print(College.collegeid, College.collegename, College.address)


# col1 = College()
# print(col1.collegeid, col1.collegename, col1.address)


class College:
    collegeid = 111
    collegename = "reparel"
    address = "matunga"

    def colllegedata(self):  # self parameter used to refer class
        collegeid = 222
        collegename = "ACHARYA"
        address = "chembur"
        print(collegeid, collegename, address)


col1 = College()
print(col1.collegeid, col1.collegename, col1.address, col1.colllegedata())
# College.colllegedata()

College.address = "Borivali"
print(col1.collegeid, col1.collegename, col1.address, col1.colllegedata())  # Borivali
print(College.collegeid, College.collegename, College.address)  # Borivali

col1.address = "Dadar"
print(col1.collegeid, col1.collegename, col1.address, col1.colllegedata())  # Borivali
print(College.collegeid, College.collegename, College.address)  # Dadar
