# Assignment Handout: Designing and Implementing a Simple Bank Account Management System

## Objective:
In this assignment, you will apply the Object-Oriented Programming (OOP) concepts learned in the lesson to design and implement a simple bank account management system. You will demonstrate your understanding of classes, objects, attributes, methods, encapsulation, and abstraction.

## Problem Statement:
You are tasked with creating a basic bank account management system using OOP principles. The system should allow users to create bank accounts, perform transactions, and view account
details.

## Requirements:
### 1. Design a BankAccount class with the following attributes:
- accountNumber (string): Unique identifier for the bank account
- accountHolder (string): Name of the account holder
- balance (float): Current balance of the account
### 2. Implement the following methods within the BankAccount class:
- __init__(self, accountNumber, accountHolder, initialBalance): Constructor to initialize the
bank account with the provided account number, account holder name, and initial balance.
- deposit(self, amount): Method to deposit a specified amount into the account and update the
balance accordingly.
- withdraw(self, amount): Method to withdraw a specified amount from the account and update
the balance accordingly. If the withdrawal amount exceeds the current balance, display an error
message.
- getBalance(self): Method to retrieve and return the current balance of the account.
- displayAccountInfo(self): Method to display the account number, account holder name, and
current balance.
### 3. Encapsulate the attributes of the BankAccount class by using appropriate access modifiers
- (e.g., private or protected) to ensure data integrity and prevent direct access from outside the
class.
### 4. Create a main program that demonstrates the usage of the BankAccount class:
- Instantiate multiple bank account objects with different account numbers, account holder
names, and initial balances.
- Perform deposit and withdrawal transactions on the bank account objects.
- Display the account information and current balance of each bank account.
### 5. Implement appropriate error handling and input validation:
- Ensure that the deposit and withdrawal amounts are positive numbers.
- Handle the case where the withdrawal amount exceeds the current balance by displaying an
error message.
### 6. Write clear and concise documentation for your code, including:
- A brief description of the BankAccount class and its purpose
- Explanation of each attribute and method within the class
- Instructions on how to run the main program and interact with the bank account objects
### 7. Test your implementation thoroughly to ensure that all the requirements are met and the program functions as expected.

**Accreditation Notes:**

- I worked on this assignment with my breakout room group of Bryan Garret & Darien Davis.

- I used Google Gemini Advanced to help me debug some of the traceback calls that I could not solve using online resources in addition to the course materials such as Stack Overflow, and to help me with the details for this readme file and the documentation.

- I use Stack Overflow & W3 Schools as a resource in most of my coding, mostly to help understand what is happening in the terminal errors when I cannot find the information in the course materials.