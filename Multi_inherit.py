class GrandParent():

    def __init__(self, name):
        self.name = name

    def tell_a_story(self):
        print(f"{self.name} tells a story.")

class Parent(GrandParent):

    def work(self):
        print(f"{self.name} is working.")

class Child(Parent):

    def play(self):
        print(f"{self.name} is playing.")


child = Child("John")
child.tell_a_story()
child.work()
child.play()