'''
Constructor chaining is the process of calling
 one constructor from another constructor

'''
class Grandparent:
    def __init__(self):
        self.x = 100

class Parent(Grandparent):
    def __init__(self):
        self.y = 200
        super().__init__()

class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()
c = Child()
print(c.z)
print(c.y)
print(c.x)