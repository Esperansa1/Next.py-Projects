from Animal import Animal
class Skunk(Animal):
    def __init__(self, name, hunger, stink_count = 6):
        super().__init__(name, hunger)
        self._stink_count = 6
        self._color = "Green"
        self._stink_count = self._stink_count

    def get_type(self):
        return "Skunk"

    def get_stink_count(self):
        return self._stink_count

    def talk(self):
        return "tsssss"
    
    def stink(self):
        print("Dear lord!")

    def super_ability(self):
        self.stink()
