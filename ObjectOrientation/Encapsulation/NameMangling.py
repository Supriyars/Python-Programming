class Demo1:
    def __init__(self,name):
        self.__name = name  #Private Variable
d1 = Demo1('Akash')
print(d1._Demo1__name) # Name Mangling git
'''
1.  Name Mangling is a process of providing new name to  the private variables
2. These new names will be provided automatically by python for all private members
3. New name will be provided in the format 
objectName._className__variableName
'''