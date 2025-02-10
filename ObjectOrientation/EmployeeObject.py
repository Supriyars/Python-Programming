class Employee:
    company_name = 'code' #class based variable
    def __init__(self,name,age,desig): #instance based variable
        self.name = name
        self.age = age
        self.desig = desig

    def login(self,time):
        print(f"{self.name} logged in at {time}")

    def logout(self,time):
        print(f"{self.name} logged out at {time}")

    def work(self,hours):
        print(f"{self.name} worked for {hours}")
    
    def get_details(self):
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee designation: " , self.desig)

e1 = Employee('Ak', 24, "SDE")
e2 = Employee('PK', 25, "Manager")
e3 = Employee('RK', 26, "Developer")
e1.get_details()
e2.get_details()
e3.get_details()
