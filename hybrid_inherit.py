class Animal():

    def __init__(self, name):
        self.name = name 

    def sound(self):
        print(f"{self.name} makes a sound")

class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is fedding milk")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} flies")

class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)
    def nocturnal(self):
        print(f"{self.name} is nocturnal")


bat = Bat("Bruce")
bat.nocturnal()
bat.fly()
bat.feed()
bat.sound()