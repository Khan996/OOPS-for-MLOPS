class Parent():

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Child(Parent):

    def play(self):
        print(f"{self.name} is playing")



child = Child("Alice")
child.greet()
child.play()