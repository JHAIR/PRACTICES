from src.classes.transport import Transport

class Land(Transport):

    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self.hasMotor = hasMotor

    def Displaydata(self):
        print( super(Land, self).getprice())
        print(super(Land, self).getname())
        print(self.hasMotor)
