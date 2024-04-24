from Animal import Animal
from Cat import Cat
from Dog import Dog
from Skunk import Skunk
from Unicorn import Unicorn
from Dragon import Dragon

def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcFly = Dragon("McFly", 80)


    zoo_lst = [dog, cat, skunk, unicorn, dragon, doggo, kitty, stinky, clair, mcFly]


    for animal in zoo_lst:
        print(animal.get_type(), animal.get_name())

        while animal.is_hungry():
            animal.feed()

        print(animal.talk())
        animal.super_ability()
    
    print(Animal.zoo_name)

if __name__ == "__main__":
    main()