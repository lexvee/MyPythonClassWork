class Customer(): #this can as well be class Customer(object)

    def __init__(self,name):
            self.name=name
            
    def set_balance(self,balance):
            self.balance=balance
            return None
        
    def deposit(self,amount):
            self.balance+=amount
            return self.balance
        
    def withdraw(self,amount):
            if not amount>self.balance:
                self.balance-=amount
            else:
                raise RuntimeError("insufficient balance")
            return self.balance

    def get_balance(self):
            return self.balance

new_customer=Customer("James")
print(new_customer.name)

new_customer.set_balance(25000)
print("acct bal: ",new_customer.get_balance())

new_customer.deposit(50000)
print("new acct bal: ",new_customer.get_balance())

new_customer.withdraw(30000)
print("acct bal: ",new_customer.get_balance())




