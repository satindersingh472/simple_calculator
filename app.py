#add numbers takes 2 arguments and add them
def add_numbers(num1,num2):
    return num1 + num2
# substract function will take 2 arguments and substract num2 from num1
def subtract_numbers(num1,num2):
    return num1 - num2
#multiply numbers will multiply the 2 numbers getting from arguments
def multiply_numbers(num1,num2):
    return num1 * num2
#divide numbers will divide the argument num1 with the argument num2
def divide_numbers(num1,num2):
    return num1 / num2     

#get inputs will ask the user to input 2 numbers seperately
def get_inputs():
    inputs_array= []
    print('Please enter the first number: ')
    x = input()
    #it will convert the number into an integer
    x = int(x)
    #and then append it to the end of the inputs_array list
    inputs_array.append(x)
    print('Please enter the second number: ')
    y = input()
    #after the input it will convert the input into an integer
    y = int(y)
    #after that it will append it to the end of the inputs_array list
    inputs_array.append(y)
    #the function will return the inputs array
    return inputs_array

#do maths will take three arguments , calculation type and numbers to calculate
#it will execute the function based on the option selected by the user
def do_maths(calculation_type,x,y):
    if(calculation_type == 1):
        print('Your result: ',add_numbers(x,y))
    elif(calculation_type == 2):
        print('Your result: ',subtract_numbers(x,y))
    elif(calculation_type == 3):
        print('Your result: ',multiply_numbers(x,y))
    elif(calculation_type == 4):
        print('Your result: ',divide_numbers(x,y))

#enter selection will ask for the user input 
def enter_selection():
    while(True):
        print('Welcome to the simple calculator, Please select from the following options:')
        print('1: Addition')
        print('2: Substraction')
        print('3: Multiplication')
        print('4: Division')
        print('Please enter your selection:')
        #user selection will store the user input from 1 to 4 for calculation type
        user_selection = input()
        try:
            #need to convert to int because if not and if there is wrong number entered
            #it will still show the error from else statment
            #and the value error will not get displayed in the except statement
            user_selection = int(user_selection)
            #user selection must be between integer 1 and 4
            if(user_selection >= 1 and user_selection <= 4 ):
                #if option selected is 1 to 4 then inputs will store the return value from get_inputs
                #and use that value as an argument inside the do_maths function
                inputs =  get_inputs()
                #do_maths will get its arguments from user_selection and return values from get_inputs()
                do_maths(user_selection,inputs[0],inputs[1])
            else:
                #if option selected is not between 1 and 4 but still a number else statement will get true
                #and will let the function continue
                print('Number did not match:  Not a valid calculation type, selection should be from 1 to 4')
                continue
        except:
            #if any other value other than the number or integer is entered the function will show error
            #from this except statement and continue the statement
            print('ValueError: wrong value entered instead of a number, selection should contain numbers only')
            continue
        finally:
            #finally at the end of every calculation or failed code this block of code
            #will get executed and ask for the user input
            answer = input('continue? (yes / no). press enter to continue or type no or exit and then press enter to quit: ')
            #if the user input is yes or enter or y then the function will continue
            if answer.lower() in ['yes','y','']:
                continue
            #else if the input is no or exit or n then the loop will break
            elif answer.lower() in ['no','n','exit']:
                print('Thanks for using calculator')
                break 
            #if not the correct option is entered then the loop will break as well
            else: 
                print('Not a correct response, Thanks for using calculator')
                break

enter_selection()



