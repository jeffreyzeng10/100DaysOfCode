import os
clear = lambda: os.system('cls')

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def start_calculator():
    print(logo)
    num1 = input("What's the first number?: ")
    print('+')
    print('-')
    print('*')
    print('/')
    calculator(num1)

def calculator(num1):
    operation = input("Pick an operation: ")
    num2 = input("What is the next number?: ")
    answer = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {answer}")
    continue_flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
    if continue_flag == 'y':
        return calculator(answer)
    elif continue_flag == 'n':
        clear()
        start_calculator()

def calculate(n1, n2, op):
    n1 = float(n1)
    n2 = float(n2)

    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return

start_calculator()
