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
        user_selection = int(user_selection)
        if(user_selection >= 1 and user_selection <= 4 ):
            return user_selection
        else:
            print('Not a valid selection')
    except ValueError:
        print('Please select valid option')
    return user_selection

calculation_type = enter_selection()


if(calculation_type == 1):
    print('Your result: ',add_numbers(first_number,second_number))
elif(calculation_type == 2):
    print('Your result: ',subtract_numbers(first_number,second_number))
elif(calculation_type == 3):
    print('Your result: ',multiply_numbers(first_number,second_number))
elif(calculation_type == 4):
    print('Your result: ',divide_numbers(first_number,second_number))
