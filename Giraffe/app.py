character_name = "Tom"
character_age = "50"
is_male = True
is_female = False
print("There once was a man\ named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print(character_name.upper().isupper())
print(len("character_name"))
character_name = "Mike"
print(character_name[0])
print(character_name.index("k"))
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

print(character_name.lower().islower())
phrase = "Giraffe Academy"
print(phrase)
print(phrase.replace("Giraffe","Elephant"))

print(2)
print(3.1415926)
print(-10.4)
print(3 + 4.521)
print(3 - 4.5)
print(3 * 4.5)
print(3 / 4.5)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)
my_num = 1.7321
print("This is a number: ")
print(my_num)
print("This is a string: ")
print(str(my_num))
print(str(my_num) + " is my favorite number.")
my_num = -10
print("-10 的绝对值：")
print(abs(my_num))
print(pow(3, 4))
print(max(3.4, 5.6, 9.8, -3.4))
print(min(3.4, 5.6, 9.8, -3.4))
print(round(3.14))
print(round(3.44))
print(round(3.55))

from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(37.8))

name = input("Enter you full name: ")
age = input("Tell me your age please: ")
print("Hello " + name + "! You are " + age + " years old. ")

print("Now there is a calculator below:")
num1 = input("Enter the first number: ")
print("The first number you input is: " + num1)
num2 = input("Enter the second number: ")
print("The second number you input is: " + num2)
result = float(num1) + float(num2)
print("The sum of your numbers is: " + str(result))
print("\n")
print("\n")
print("\n")
print("Madlib")
flower = input("Enter the flower you like best:")
color = input("Enter the color you like best: ")
thing = input("The name of thing you like best: ")
nature = input("Why you like it because it is: ")
celebrity = input("The famous person you love most: ")
print(flower + " is " + color.lower() + ".")
print(thing + " is " + nature.lower() + ".")
print("I love " + celebrity + ".")