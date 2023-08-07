def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

choice = int(input('select operation: 1 to add, 2 to subtract, 3 to multiply and 4 to divide'))
if choice == 1:
    num1 = int(input('enter 1st number'))
    num2 = int(input('enter 2nd number'))
    answer = add(num1, num2)
    print(num1, '+', num2, '=', answer)

elif choice == 2:
    num1 = int(input('enter 1st number'))
    num2 = int(input('enter 2nd number'))
    answer = subtract(num1, num2)
    print(num1, '-', num2, '=', answer)    

elif choice == 3:
    num1 = int(input('enter 1st number'))
    num2 = int(input('enter 2nd number'))
    answer = multiply(num1, num2)
    print(num1, '*', num2, '=', answer) 

elif choice == 4:
    num1 = int(input('enter 1st number'))
    num2 = int(input('enter 2nd number'))
    answer = divide(num1, num2)
    print(num1, '/', num2, '=', answer) 

else:
    print('invalid input')           








