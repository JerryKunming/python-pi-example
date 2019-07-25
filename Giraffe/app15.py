'''

employee_list = open("/home/jerry/XX-Net/pythonemployees.txt", "r")

# print(employee_list.readable())
# print(employee_list.read())
# print(employee_list.readline())
# print(employee_list.readline())
# print(employee_list.readline())
# print(employee_list.readlines())
print(employee_list.readlines()[0])

for employee in employee_list.readlines():
    print(employee)
employee_list.close()

'''
'''
employee_list = open("/home/jerry/XX-Net/pythonemployees.txt", "a")
print(employee_list.writable())
print(employee_list.write("Kelly - Customer Service\n"))
# print(employee_list.read())
employee_list.close()
employee_list = open("/home/jerry/XX-Net/pythonemployees.txt", "r")
print(employee_list.read())
employee_list.close()
'''
'''
employee_list = open("pythonemployees.txt", "w")
employee_list.write("Tom - Salesman\n")
employee_list.write("Jerry - Management\n")
employee_list.write("Mary - Accountant\n")
employee_list.close()
employee_list = open("pythonemployees.txt", "r")
print(employee_list.read())
employee_list.close()
'''

webpage01 = open("index01.html", "w")
webpage01.write("<h1> The is the title 1</h1>")
webpage01.write("<p> This is the paragraph.</p>")
webpage01.write("<footer> This is the foot area.</footer")
webpage01.close()
