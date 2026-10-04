# Constructor

class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)


student1 = Student("Namratha", 21, "CSE")

student1.display()