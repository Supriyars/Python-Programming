class Bank:
    bank_name = "SBI"
    def __init__(self,name,age,bal):
        self.name = name
        self.age = age
        self.bal = bal

    def display_info(self):
        print(f'''User name is: {self.name} and 
              age is: {self.age} and balance is {self.bal}''')

b1 = Bank("Pooja", 25, 25000)
print(b1.bank_name)
print(Bank.bank_name)
b1.display_info()