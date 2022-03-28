from src.classes.land import Land

class Bicycle(Land):

    def __init__(self, name, price, hasMotor, exerciseBike):
        super().__init__(name, price, hasMotor)
        self.exerciseBike = exerciseBike

    def displayData(self):
        super().Displaydata()
        print(self.exerciseBike)
