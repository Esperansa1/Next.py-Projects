from Animal import Animal
class Unicorn(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)


    def get_type(self):
        return "Unicorn"

    def talk(self):
        return "Good day, darling"

    def sing(self):
        print("""
I don't care about your modern time preacher
Welcome boys, too much noise, I will teach ya
Pam pam pa hoo, turram pam pa hoo
Hey, I think you forgot how to play
My teddy bear's running away
The Barbie got something to say
Hey, hey, hey, hey
My "Simon says" leave me alone
I'm taking my Pikachu home
You're stupid just like your smartphone
Wonder Woman don't you ever forget
You're divine and he's about to regret
He's a bucka-mhm-buckbuckbuck-mhm boy
Bucka-mhm-buckbuckbuck
I'm not your bucka-mhm-buck-mhm-buck-mhm
I'm not your toy (not your toy)
You stupid boy (stupid boy)
I'll take you down now, make you watch me
Dancing with my dolls on the motha-bucka beat
Not your toy (cululoo, cululoo)
(Cululoo, cululoo)
A-a-a ani lo buba
Don't you go and play with me boy!
A-a-a ani lo buba
Don't you go and play, shake!
Hey! Wedding bells ringing
(Cululoo, cululoo) Hey! Money men bling-bling
I don't care about your stefa, baby
Pam pam pa hoo, turram pam pa hoo
Wonder Woman don't you ever forget
You're divine and he's about to regret
He's a bucka-mhm-buckbuckbuck-mhm boy
Bucka-mhm-buckbuckbuck
I'm not your bucka-mhm-buck-mhm-buck-mhm
I'm not your toy (not your toy)
You stupid boy (stupid boy)
I'll take you down now, make you watch me
Dancing with my dolls on the motha-bucka beat
Not your toy (not your toy)
You stupid boy (stupid boy)
I'll t-t-t-take you now w-w-w-with me now, boy
I'm not your toy
You stupid boy
I'll take you down now, make you watch me
Dancing with my dolls on the motha-bucka beat
Look at me, I'm a beautiful creature
(You stupid boy)
I don't care about your modern time preacher
(I'm not your toy)
Not your toy, not your toy, not your toy, toy
I'm not your toy, not your toy, not your toy, toy
        """)

    def super_ability(self):
        self.sing()
