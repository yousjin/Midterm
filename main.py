# Program make a simple calculator

import logging

import Add
import Sub
import Mul
import Div

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if (num1!='1' and num1!='2' and num1!='3' and num1!='4') or (num2!='1' and num2!='2' and num2!='3' and num2!='4'):
            logger.warning('Invalid INPUT')



        if choice == '1':
            print(num1, "+", num2, "=", Add.add(num1, num2))
            logger.info('%f + %f = %f', num1, num2, Add.add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Sub.subtract(num1, num2))
            logger.info('%f - %f = %f', num1, num2, Sub.subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Mul.multiply(num1, num2))
            logger.info('%f * %f = %f', num1, num2, Mul.multiply(num1,num2))

        elif choice =='4':
            
            try:
                print(num1, "/", num2, "=", Div.divide(num1,num2))
                logger.info('%f / %f = %f', num1, num2, Div.divide(num1,num2))
            except(ZeroDivisionError):
                logger.warning('Divide by ZERO')
                print('warning : Divide by Zero')
                
            
        # check if user wants another calculation
        # break the while loop if answer is no

        #End Loop
        ISDone = False
        while True:

            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower()

            if next_calculation == "no":
                no_check = input('Are you sure? (yes/no): ')
                no_check = no_check.lower()
                if no_check=='yes':
                    ISDone = True
                    break
                elif no_check=='no':
                    continue
            elif next_calculation == "yes":
                break
            elif next_calculation == "why?":
                continue
            else:
                break
            
        if ISDone:
            break


    else:
        print("Invalid Input")
