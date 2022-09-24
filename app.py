def add_numbers(num1,num2):
    return num1 + num2

def subtract_numbers(num1,num2):
    return num1 - num2

def multiply_numbers(num1,num2):
    return num1 * num2

def divide_numbers(num1,num2):
    return num1 / num2     

def get_inputs():
    inputs_array= []
    print('Please add the first number: ')
    x = input()
    x = int(x)
    inputs_array.append(x)
    print('Please add the second number: ')
    y = input()
    y = int(y)
    inputs_array.append(y)
    return inputs_array

def do_maths(calculation_type,x,y):
    if(calculation_type == 1):
        print('Your result: ',add_numbers(x,y))
    elif(calculation_type == 2):
        print('Your result: ',subtract_numbers(x,y))
    elif(calculation_type == 3):
        print('Your result: ',multiply_numbers(x,y))
    elif(calculation_type == 4):
        print('Your result: ',divide_numbers(x,y))


def enter_selection():
    print('Welcome to the simple calculator, Please select from the following options:')
    print('1: Addition')
    print('2: Substraction')
    print('3: Multiplication')
    print('4: Division')
    print('Please enter your selection:')
    user_selection = input()
    try:
        user_selection = int(user_selection)
        if(user_selection >= 1 and user_selection <= 4 ):
            inputs =  get_inputs()
            do_maths(user_selection,inputs[0],inputs[1])
        else:
            print('Number did not match:  Not a valid calculation type, selection should be from 1 to 4')
            enter_selection()
    except:
        print('ValueError: Not able to calculate alphabets, selection should contain numbers only')
        enter_selection()
    finally:
        answer = input('continue? (yes / no). press enter to continue or type no or exit to quit: ')
        if answer.lower() in ['yes','']:
            enter_selection()
        elif answer.lower() in ['no','exit']:
            print('Thanks for using calculator') 
        else: 
            print('Not a correct response, Thanks for using calculator')

dbms = enter_selection()



