import os
import math

mathematical_operations = ['+','-','*','/']

def application_name():
    print('''
          
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
          ''')

def options_menu():
    display_option_title('Choosing an option')
    print("[+] Plus")
    print("[-] Minus")
    print("[*] Times")
    print("[/] Divided by")
    print('[0] Exit...')


def display_option_title(text):
    os.system('cls')
    application_name()
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()
    
def choose_option():
        operation = input("\nchoose the option: ")
        if operation == '0':
            exit_program()
            return False
        if operation not in mathematical_operations:
            print('#ERROR! Invalid Option')
            return_to_menu()
            return
        try:
            first_number = float(input('Enter the first number: ')) 
            second_number = float(input('Enter the second number: '))
        except ValueError:
            print('\nERROR: Invalid input. Enter only numbers.')
            return_to_menu()
            return
        
        if not math.isfinite(first_number) or not math.isfinite(second_number):
            print('ERROR: Please enter finite numbers.')
            return_to_menu()
            return
        
        if operation == '+':
            add_numbers(first_number, second_number)
        elif operation == '-':
            subtract_numbers(first_number, second_number)
        elif operation == '*':
            multiply_numbers(first_number, second_number)
        elif operation == '/':
            divide_numbers(first_number, second_number)
        
    
def return_to_menu():
    input('Press ENTER to return to the menu.')


def add_numbers(numb_1, numb_2):
    result = numb_1 + numb_2
    display_option_title('Result of the sum')
    print(f'Result: {result}')
    return_to_menu()

def subtract_numbers(numb_1, numb_2):
    subtraction = numb_1 - numb_2
    display_option_title('Result of the subtraction')
    print(f'Result: {subtraction}')
    return_to_menu()   

def divide_numbers(numb_1, numb_2):
    if numb_2 == 0:
        print('ERROR. Division by zero is not allowed.')
        return_to_menu()
    else:
        division = numb_1 / numb_2
        display_option_title('Result of the division')
        print(f'Result: {division}') 
        return_to_menu()  
    
def multiply_numbers(numb_1, numb_2):
    multiplication = numb_1 * numb_2
    display_option_title('Result of the multiplication')
    print(f'Result: {multiplication}')
    return_to_menu()
    
    
def exit_program():
    os.system('cls')
    print('Exiting the calculator. Bye-bye!\n')
        
    

def main():
    while True:
        options_menu()
        if choose_option() is False:
            break

if __name__ == '__main__':
    main()