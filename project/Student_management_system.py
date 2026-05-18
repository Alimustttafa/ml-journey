students_db = {
    "Ali" : [90, 85, 80],
    "Omer" : [85, 80, 75]
}

def add_student():
    student_name = input("ُEnter student name: ").strip().capitalize()
    students_db[student_name] = []
    for i in range(3):
        mark = int(input(f"Enter mark {i + 1}: "))
        students_db[student_name].append(mark)
    print(f"student {student_name} are added successfully")
    
def delete_student(name):
    if name in students_db:
        del students_db[name]
        print(f"student {name} are deleted successfully")
    else:
        print(f"Student {name} are not found")
    
def update_student():
    student_name = input("ُEnter student name: ").strip().capitalize()
    if student_name in students_db:
        students_db[student_name] = []
        for i in range(3):
            mark = int(input(f"Enter mark {i + 1}: "))
            students_db[student_name].append(mark)
        print(f"student {student_name} are updated successfully")
    else:
        print(f"Student {student_name} are not found")
    
def calculate_average(name):
    if name in students_db:
        average = sum(students_db[name]) / len(students_db[name])
        print(f"student {name} average is {average}")
    else:
        print(f"Student {name} are not found")

while True:
    choose = input("choose an option: \n 1- add student \n 2- delete student \n 3- update student \n 4- calculate average \n 5- exit \n").strip()
    
    if choose == "1":
        add_student()
    elif choose == "2":
        student_name = input("ُEnter student name you want to delete: ").strip().capitalize()
        delete_student(student_name)
    elif choose == "3":
        update_student()
    elif choose == "4":
        student_name = input("ُEnter student name you want to calculate average: ").strip().capitalize()
        calculate_average(student_name)
    elif choose == "5":
        break
        