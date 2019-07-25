try:
    num = int(input("Enter a number: "))

    print(num)

    num_il = 10 / 0

except ValueError:
    print("The number you input is invalid.")

except ZeroDivisionError:
    print("You have number divided by zero.")