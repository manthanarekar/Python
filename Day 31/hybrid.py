class Vehical:
    companyname = "Tata"


class Twoweheeler(Vehical):
    def __init__(self, t_vehicalname, t_medelnum):
        self.t_vehicalname = t_vehicalname
        self.t_medelnum = t_medelnum

    def twowheelerdata(self):
        print("Two wheeler vehical company name : ", self.companyname)
        print("Two wheeler vehical name : ", self.t_vehicalname)
        print("Two wheeler vhical model name : ", self.t_medelnum)


class Fourwheeler(Vehical):
    def __init__(self, f_vehicalname, f_modelnum):
        self.f_vehicalname = f_vehicalname
        self.f_modelnum = f_modelnum

    def fourwheelerdata(self):
        print("four wheeler vehical company name : ", self.companyname)
        print("four wheeler vehical name : ", self.f_vehicalname)
        print("four wheeler vhical model name : ", self.f_modelnum)


t = Twoweheeler("Honda", 1111)
t.twowheelerdata()
f = Fourwheeler("Suzuki", 2222)
f.fourwheelerdata()
