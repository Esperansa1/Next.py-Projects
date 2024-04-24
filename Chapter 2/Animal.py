
class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    
    def get_name(self):
        return self._name
    
    def is_hungry(self):
        return self._hunger > 0
    
    def feed(self):
        self._hunger -= 1

    def get_type(self):
        raise NotImplementedError    
    
    def talk(self):
        raise NotImplementedError
    
    def super_ability(self):
        raise NotImplementedError