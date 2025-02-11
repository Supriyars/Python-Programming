class Student:
    def cook(self):
        print('Student is cooking')
    def play(self):
        print('Playing cricket')

class Employee(Student):
    def work(self):
        print('Employee is working')
    def cook(self):
        print('Employee is cooking')

e = Employee()
e.play()

'''
work(): Specialized method are the methods only present in child class
play(): inherited methods are the methods from parent class used as it is in child class
cook(): Overidden method  are the methods where we can change the implimentation of the method in child class
'''