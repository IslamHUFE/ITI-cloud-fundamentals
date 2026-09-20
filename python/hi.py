n = 0
student = {
    "ID" : [0,{
        "Name"    : "name",
        "Age"     :      0,
        "Courses" :     [],
    }],
}
students = []

while True:
    print("Press A and Enter to enter a new student")
    print("Press V and Enter to view all students")
    print("Press S and Enter to search for a student by name")
    print("Press U and Enter to update a student infromation")
    print("Press D and Enter to delet a student")
    key = input("Press X and Enter to Exit\n\n")

    if key == "A" or key == "a":
        students.append(student.copy())
        students[n]["ID"][0]         = input("\n\nID: ")
        students[n]["ID"][1]["Name"] = input("\nName: ")
        students[n]["ID"][1]["Age"]  = input("\nAge: ")
        print("Enter courses and enter X when you are done")
        i = 1
        while True:
            course = input(f"\nCourse {i}: ")
            if course == "x" or course == "X":
                break
            else:
                students[n]["ID"][1]["Courses"].append(course)
            i =+ 1
        n =+ 1

    if key == "V" or key == "v":
        for i in n:
            print(f"\nID: {students[i]["ID"][0]}")
            print(f"\nName: {students[i]["ID"][1]["Name"]}")
            print(f"\nAge: {students[i]["ID"][1]["Age"]}")
            print(f"\n Courses:{students[i]["ID"][1]["Courses"]}")
            print("\n\n")

    if key == "S" or key == "s":
        search = input("Type student name: ")

