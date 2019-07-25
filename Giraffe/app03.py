def say_hi():
    print("Hello Dear User")

print("Top")
say_hi()
print("Bottom")

def say_hi01(name, age):
    print("Hello Dear " + name + ". You are " + age + " years old.")

say_hi01("Mike", "35")
say_hi01("Mary", "23")

def cube(num):
    return num*num*num

print(cube(5))
result = cube(4)
print(result)