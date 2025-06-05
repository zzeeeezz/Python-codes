students_full_name = input("student's full name: ")
print(students_full_name.title())
student_age = eval(input("student's age: "))
course_name = input("course name: ")
ä,ö,ü = map(eval, input("three test scores: ").split())
ß = ä + ö + ü
print(f"Average score: {ß / 3}")
if ß / 3 >= 60:
    print("Passed, True")
else:
    print("Failed, False")









