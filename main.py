import BankAccount() from classes.py

Bobs_Account = BankAccount("Bob",0.02, "Checking")
try:
    print(Bobs_Account.__account_balance)
except AttributeError:
    print("Cannot access private data.")

print(Bobs_Account._account_holder)
print(Bobs_Account._account_number)
print(Bobs_Account.__account_balance)
# print(Bobs_Account.deposit(2.00))
# print(Bobs_Account.get_balance())
# print(Bobs_Account.withdraw(1000))