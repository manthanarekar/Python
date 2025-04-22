from abc import ABC, abstractmethod


class CAR(ABC):
    @abstractmethod
    def milage(self):
        print("Final 9-abstract method ")


class Tesla(CAR):
    def milage(self):
        return super().milage()

    def mil(self):
        print("Tesla has 50Kmph milage")


t = Tesla()
t.milage()
t.mil()
