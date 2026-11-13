print("************************** WELCOME TO OUR SCHOOL **************************")
print("")

# Subjects
subjects = ["Mathematics", "Biology", "Physics"]

studentNumber = int(input("Please enter the number of students present: "))

listOfStudents = []

# Collect student information
for i in range(studentNumber):

    studentName = input("Enter student name: ")

    scores = []

    # Collect scores for each subject
    for j in range(len(subjects)):

        score = int(input(f"Enter the score for {subjects[j]} for {studentName}: "))

        if score >100 or score<0:
            print("Invalid value")
            break

        scores.append(score)

    # Store student and their scores together
    student = {
        "name": studentName,
        "scores": scores
    }

    listOfStudents.append(student)




# Display all students and their scores
print("\n*************** STUDENT RESULTS ***************")
for student in listOfStudents:

    print(f"\nStudent: {student['name']}")

    for j in range(len(subjects)):
        print(f"{subjects[j]}: {student['scores'][j]}")