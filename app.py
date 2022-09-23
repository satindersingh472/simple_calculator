def add_numbers(num1,num2):
    return num1 + num2

def subtract_numbers(num1,num2):
    return num1 - num2

def multiply_numbers(num1,num2):
    return num1 * num2

def divide_numbers(num1,num2):
    return num1 / num2     


print('Welcome to the simple calculator, Please select from the following options:')
print('1: Addition')
print('2: Substraction')
print('3: Multiplication')
print('4: Division')

def enter_selection():
    print('Please enter your selection:')
    user_selection = input()
    try:
        if(user_selection > 4 or user_selection < 1):
            user_selection = int(user_selection)
    except:
        print('Please enter a valid selection from 1 to 4')
        print('Please enter your first number:')
        num1 = input()
        num1 = int(num1)
        print('Please enter your second number: ')
        num2 = input()
        num2 = int(num2)
    return [user_selection , num1, num2]

values = enter_selection()

calculation_type = values[0]
first_number = values[1]
second_number = values[2]

if(calculation_type == 1):
    print('Your result: ',add_numbers(first_number,second_number))
elif(calculation_type == 2):
    print('Your result: ',subtract_numbers(first_number,second_number))
elif(calculation_type == 3):
    print('Your result: ',multiply_numbers(first_number,second_number))
elif(calculation_type == 4):
    print('Your result: ',divide_numbers(first_number,second_number))
