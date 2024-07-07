'''
Module: classes

This module defines the `BankAccount` class, a fundamental building block for representing and managing bank accounts.

Classes:
    BankAccount: Represents a bank account with attributes like account number, holder name, and balance. It provides methods for deposit, withdrawal, balance inquiry, and displaying account information.
'''

class BankAccount():
    '''
        Represents a bank account.

        Attributes:
            _account_number (str): The unique identifier for the bank account.
            _account_holder (str): The name of the account holder.
            __account_balance (float): The current balance in the account (private).

        Methods:
            __init__(self, account_holder, account_balance, account_number): 
                Initializes a new BankAccount instance.
            
            deposit(self, amount): 
                Deposits the specified amount into the account.

            withdraw(self, amount): 
                Withdraws the specified amount from the account, if sufficient funds are available.

            get_balance(self): 
                Retrieves the current account balance.

            display_account_info(self): 
                Displays the account holder's name, account number, and current balance.
        '''
    def __init__(self, account_holder: str, account_balance: float, account_number: str):
        self._account_number = account_number
        self._account_holder = account_holder
        self.__account_balance = account_balance
        

    def deposit(self, amount):
        if amount > 0:
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
        return f"Hello {self._account_holder}, your current balance for account number {self._account_number} is ${self.__account_balance:.2f}" 