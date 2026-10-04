# Instance and Class Variables

class Student:

    college = "ABC Engineering College"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("College:", Student.college)


student1 = Student("Namratha", "CSE")
student2 = Student("Rahul", "CSE")

student1.display()
print()

student2.display()