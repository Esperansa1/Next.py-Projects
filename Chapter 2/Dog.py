from Animal import Animal
class Dog(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def get_type(self):
        return "Dog"

    def talk(self):
        return "woof woof"
    
    def fetch_stick(self):
        print("There you go, sir")
    
    def super_ability(self):
        self.fetch_stick()
