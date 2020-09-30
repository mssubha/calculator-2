"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    user_prompt = input("Enter Equation : ")
    user_tokens = user_prompt.split(" ") # user_tokens = ["+", "2","4"]

    if user_tokens[0]  == 'q':
        break

    elif len(user_tokens) == 2 and user_tokens[1].isdigit() == True:
        num1 = user_tokens[1]
        operator = user_tokens[0]
        if operator == 'square':
            output = square(float(num1))
        elif operator =='cube':
            output = cube(float(num1))
    elif len(user_tokens) == 3 and user_tokens[1].isdigit() and user_tokens[2].isdigit():
        operator = user_tokens[0]
        num1 = user_tokens[1]
        num2 = user_tokens[2]
    
        if operator == '+':
            output = add(float(num1), float(num2))
        elif operator == '-':
            output = subtract(float(num1), float(num2))
        elif operator == '*':
            output = multiply(float(num1), float(num2))
        elif operator == '/':
            output = divide(float(num1), float(num2))

        elif operator == 'power':
            output = power(float(num1), float(num2))
        elif operator == 'mod':
            output = mod(float(num1), float(num2))
    else:
        output = 'Error'

    print(output)
