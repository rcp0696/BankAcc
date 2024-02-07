class bankAccount:
    def __init__(self, name, accountID, age, balance=0):
        self.name = name
        self.accountID = accountID
        self.age = age
        self.balance = balance

    def display_balance(self):
        print(self.balance)
  
    def withdraw(self, amount):
        self.amount = amount
        if self.balance <= self.amount:
          print(f"{self.name}, you do not have enough money to withdraw!")
        else:
          self.balance -= self.amount
          print(f"Your new balance is {self.balance}")


    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount

    @property
    def age(self):
        return self.name
    @age.setter
    def age(self, new_age):
        if new_age < 11 or new_age > 80:
            self.age = new_age
        #else:
            #raise ValueError("Age must be between 11 and 80")

b1 = bankAccount("Rishi", 2005,16, 1000)
b2 = bankAccount("Vidhi", 2010,12, 1000)


def main():
  path = int(input("What would you like to do?: \n(1) Display Balance \n(2) Withdraw \n(3) Deposit: \n"))

  if path == 1:
    b1.display_balance()

  elif path == 2:
      mons = int(input("How much you wanna withdraw: "))
      b1.withdraw(mons)
  elif path == 3:
      b1.deposit()
  else:
      print("Not an option mate")

main()
