from Animal import Animal
class Dragon(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def get_type(self):
        return "Dragon"

    def talk(self):
        return "Raaaawr"
    
    def breath_fire(self):
        print("$@#$#@$")
    
    def super_ability(self):
        self.breath_fire()
