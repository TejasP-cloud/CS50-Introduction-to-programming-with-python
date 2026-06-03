CLI Calculator

Video Demo: https://youtu.be/XyW9LzobNO0

Description

CLI Calculator is a command-line calculator written in Python that performs four basic arithmetic operations: addition, subtraction, multiplication, and division. The application runs entirely in the terminal and allows users to repeatedly perform calculations without restarting the program.

The goal of this project was to apply several concepts learned throughout CS50's Introduction to Programming with Python, including functions, loops, exception handling, input validation, conditionals, and program organization. While the calculator itself is a simple application, it demonstrates how multiple programming concepts can be combined to create a complete and user-friendly program.

When the program starts, the user is prompted to enter two numbers. After entering the numbers, the user selects an arithmetic operator from the available options: addition (+), subtraction (-), multiplication (*), or division (/). The program then performs the requested operation and displays the result. Once the calculation is complete, the user is asked whether they would like to perform another calculation. This process continues until the user chooses to exit the program.

Features
Addition of two numbers
Subtraction of two numbers
Multiplication of two numbers
Division of two numbers
Validation of numeric input
Validation of operator input
Division-by-zero protection
Ability to perform multiple calculations in a single session
Clear and user-friendly error messages
Program Structure

The program is divided into four functions, each with a specific responsibility.

get_number(prompt)

This function repeatedly asks the user for a number until a valid numeric value is entered. It uses a try/except block to catch ValueError exceptions that occur when the user enters invalid input such as letters or symbols.

Separating this functionality into its own function improves readability and prevents code duplication.

get_operator()

This function prompts the user to enter an operator. Only the following operators are accepted:













/

If the user enters an invalid operator, an error message is displayed and the function continues asking until a valid operator is entered.

calculate(num1, num2, op)

This function performs the arithmetic operation selected by the user. It receives two numbers and an operator as arguments.

A match/case statement is used to determine which operation should be performed. This approach keeps the code organized and easy to understand.

The function also handles division by zero. If the user attempts to divide by zero, an error message is displayed and the function returns None instead of causing the program to crash.

main()

The main function controls the overall flow of the application.

It displays the welcome message, collects user input, calls the necessary functions, displays the result, and asks the user whether another calculation should be performed.

The program continues running until the user enters "n" when prompted to calculate again.

Design Choices

One of the main design decisions was to separate the program into multiple functions rather than placing all logic inside a single block of code. This makes the program easier to read, maintain, and expand in the future.

Input validation was isolated into dedicated functions because validation is required multiple times throughout the program. By creating separate functions for numbers and operators, the code becomes more modular and reusable.

I also chose to use Python's match/case statement in the calculate() function because it provides a clean and readable alternative to multiple if/elif statements when handling different arithmetic operations.

Error Handling

The calculator is designed to handle common user errors gracefully.

The program handles:

Invalid numeric input
Invalid operator input
Division by zero

Instead of terminating unexpectedly, the program displays a helpful error message and allows the user to continue using the calculator.

Example Usage

Enter first number: 10

Enter second number: 5

Enter operator (+, -, *, /): +

10 + 5 = 15

Calculate again? (y/n): y

Enter first number: 20

Enter second number: 0

Enter operator (+, -, *, /): /

Error: Cannot divide by zero.

What I Learned

This project helped reinforce several important programming concepts introduced throughout CS50P. These include functions, loops, exception handling, user input validation, program organization, and writing clean and maintainable code.

Building the project also provided experience in breaking a larger problem into smaller functions, with each function having a specific responsibility. This made the program easier to develop, test, and understand.

Requirements

This project uses only Python's built-in features and does not require any external libraries.

To run the program:

python calculator.py