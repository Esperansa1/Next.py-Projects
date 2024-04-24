from Animal import Animal
class Cat(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)
    
    def get_type(self):
        return "Cat"

    def talk(self):
        return "meow"
    
    def chase_laser(self):
        print("Meeeeow")

    def super_ability(self):
        self.chase_laser()
