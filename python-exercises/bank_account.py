# Write code below 💖

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, balance):
    self.balance += balance
    print(f"New balance: {self.balance}")

  def withdraw(self, balance):
    if self.balance < balance:
      print("Poor ass")
    else:
      self.balance -= balance
      print(f"New balance: {self.balance}")

  def display(self):
    print("----- Account Information -----")
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")
    print(f"Balance: {self.balance}")

ac1 = BankAccount("Thinh", "Hoang", 1 , "VIP", 1111, 10)

ac1.deposit(30)
ac1.withdraw(300)
ac1.display()