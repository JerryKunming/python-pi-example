num1 = float(input("Please input your first number: "))
op = input("please input your operator(valid operators: + - * /): ")
num2 = float(input("please input your second number: "))

if op == "+":
    print("The sum of your numbers is: ")
    print(num1 + num2)
elif op == "-":
    print("The subtraction of your numbers is: ")
    print(num1 - num2)
elif op == "*":
    print("The product of your numbers is: ")
    print(num1 * num2)
elif op == "/":
    print("The division of your numbers is: ")
    print(num1 /num2)
else:
    print("The operator you input is not valid.")