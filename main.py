''' Main module to demonstrate bank account management. '''

from classes import BankAccount

def main():
    ''' Creates and manages multiple bank account objects. '''

    # Create two bank accounts
    bobs_account = BankAccount("Bob", 1000.0, "123456789")
    alice_account = BankAccount("Alice", 500.0, "987654321") 

    # Display initial account information
    print("Initial account information:")
    print(bobs_account.display_account_info())
    print(alice_account.display_account_info())

    # Perform transactions
    bobs_account.deposit(500.0)
    alice_account.deposit(250.0)
    bobs_account.withdraw(200.0)
    alice_account.withdraw(100.0)
    # Display updated account information
    print("\nUpdated account information:")
    print(bobs_account.display_account_info())
    print(alice_account.display_account_info())
    
if __name__ == "__main__":
    main()