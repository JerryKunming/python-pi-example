from student import Student

student1 = Student("Tom", "Chemistry", 3.5, False)
student2 = Student("Sally", "Physics", 2.5, True)
print(student1.is_on_probation)
print(student1.name)
print(student2.major)
print(student1.on_honor_roll())
print(student2.on_honor_roll())
