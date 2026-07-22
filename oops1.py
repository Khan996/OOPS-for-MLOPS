# initiate a class

class employee:
    # special function/method 04 dunder method - constructor
    def __init__(self):
        print("Attributes are initiated automatically when object is created")
        self.id = 123
        self.designation = "SDE"
        self.salary = 50000
        print("Attributes/Data have been initiated")

    # creating a function (function in class is called a method)
    def travel(self, destination):
        print("This funtion is called method and is called manually after object is created")
        print(f"Sam is trvelling in {destination}")

# creating anobject/instance of employee
sam = employee()

#print(sam.salary)

# calling a method
sam.travel("Japan")
print(type(sam))