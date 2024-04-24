from Animal import Animal
class Skunk(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)
        self._stink_count = 6
        self._color = "Green"

    def get_type(self):
        return "Skunk"

    def talk(self):
        return "tsssss"
    
    def stink(self):
        print("Dear lord!")

    def super_ability(self):
        self.stink()
