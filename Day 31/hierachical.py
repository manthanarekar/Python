class Vehical:
    companyname = input("Enter company name : ")


class Twoweheeler(Vehical):
    vehicalname = input("Enter tow wheeler vehical name : ")
    medelnum = input("Enter tow wheeler vehical numer : ")

    def twowheelerdata(self):
        print("Two wheeler vehical company name : ", self.companyname)
        print("Two wheeler vehical name : ", self.vehicalname)
        print("Two wheeler vhical model name : ", self.medelnum)


class Fourwheeler(Vehical):
    # vehicalname = input("Enter four wheeler vehical name : ")
    # medelnum = input("Enter four wheeler vehical numer : ")123

    def __init__(self, vehicalname, modelnum):
        self.vehicalname = vehicalname
        self.modelnum = modelnum
        print(self.vehicalname, self.modelnum)

    def fourwheelerdata(self):
        print("four wheeler vehical company name : ", self.companyname)
        print("four wheeler vehical name : ", self.vehicalname)
        print("four wheeler vhical model name : ", self.modelnum)


t = Twoweheeler()
t.twowheelerdata()
f = Fourwheeler("Suzuki", 121)
f.fourwheelerdata()
