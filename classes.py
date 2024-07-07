''' A file to hold the Parent class and all child classes'''

class BankAccount():
    def __init__(self, account_holder: str, account_balance: float, account_number: str):
        self._account_number = account_number
        self._account_holder = account_holder
        self.__account_balance = account_balance
        

    def deposit(self, amount):
        if amount < 0:
            self.__account_balance = amount + self.__account_balance
            return self.__account_balance
        else:
            return "Your deposit must be greater than zero."
    
    def withdraw(self, amount):
        if (self.__account_balance < amount):
            return "Insufficient Funds"
        else:
            self.__account_balance = self.__account_balance - amount
            return self.__account_balance
        
    def get_balance(self):
        return f" {self.__account_balance}" 

    def display_account_info(self):
        return f"Hello ${self.account_holder}, your current balance for account number ${self.account_number} is $${self.account_balance}."