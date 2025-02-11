class MathOperations:
    @staticmethod 
    def add_numbers(a,b):
        return a + b

#using the static method creating an instance
#Accessing static method using class name
result = MathOperations.add_numbers(5,3)
print(result)

#Accessing static method using an object reference 
math_op = MathOperations()
print(math_op.add_numbers(10,5))