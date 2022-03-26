from src.classes.land import Land

class Car(Land):
    def __init__(self, name, price, hasMotor, useGas):
        super().__init__(name,price,hasMotor)
        self.useGas = useGas

    def displayData(self):
        super().Displaydata()
        print(self.useGas)