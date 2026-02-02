num1 = float(input("What's the first number? "))
operator = input("Enter an operator (+ - * / %): ")
num2 = float(input("What's the second number? "))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    if num2 == 0:
        print("You cannot divide a number by 0")
        exit()
    result = num1 / num2
    print(result)

elif operator == "%":
    result = num1 % num2
    print(result)

else:
    print(f"{operator} is not a valid operator")
    exit()

print(f"{num1} {operator} {num2} = {result}")
