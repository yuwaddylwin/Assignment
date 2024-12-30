import csv

def load_students(filename):
    try:
        mylist=[]
        with open(filename) as csv_file:
            students_data = csv.DictReader(csv_file)
            for row in students_data:
                mylist.append(row)
            print("Loaded data:", mylist)
            return mylist
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except IOError:
        print(f"Error: Unable to read from file '{filename}'.")
        return []



def save_students(filename, students):
    try:
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["StudentID", "FirstName", "LastName","Major", "Gender", "DateOfBirth", "Email", "Address","Ph_no","Nationality"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except IOError:
        print("Error: Unable to write to file")

def display_all_students(filename):
    students = load_students(filename)
    print("Loaded data:", students)
    for index, student in enumerate(students, start=1):
        print(f"Student {index}:")
        for field, value in student.items():
            print(f"{field}: {value}")
        print()


def display_total_number_of_students(filename):
    students = load_students(filename)
    total_students = len(students)
    print(f"Total number of students: {total_students}")

def add_new_student(filename):
    StudentID = input("Enter student ID: ")
    FirstName = input("Enter first name: ")
    LastName = input("Enter last name: ")
    Major = input("Enter major: ")
    Gender = input("Enter gender: ")
    DateOfBirth = input("Enter date of birth (eg, 1 Sept 2004): ")
    Email = input("Enter email: ")
    Address = input("Enter address: ")
    Ph_no = input("Enter Ph_no (eg,###-###-###): ")
    Nationality = input("Enter Nationality: ")


    student = {
        "StudentID": StudentID,
        "FirstName": FirstName,
        "LastName": LastName,
        "Major": Major,
        "Gender": Gender,
        "DateOfBirth": DateOfBirth,
        "Email": Email,
        "Address": Address,
        "Ph_no": Ph_no,
        "Nationality": Nationality
    }

    students = load_students(filename)
    students.append(student)
    save_students(filename, students)
    print("Student added successfully!")

def search_student_by_id(filename, StudentID):
    students = load_students(filename)
    found_students = [student for student in students if student['StudentID'] == StudentID]
    return found_students

def delete_student_by_id(filename, StudentID):
    students = load_students(filename)
    updated_students = [student for student in students if student['StudentID'] != StudentID]
    save_students(filename, updated_students)
    print("Student deleted successfully!")

def update_student_by_id(filename, StudentID):
    students = load_students(filename)
    updated_students = []
    for student in students:
        if student['StudentID'] == StudentID:
            student['FirstName'] = input("Enter new first name: ")
            student['LastName'] = input("Enter new last name: ")
            student['Major'] = input("Enter new major: ")
            student['Gender'] = input("Enter new gender: ")
            student['DateOfBirth'] = input("Enter new date of birth: ")
            student['Email'] = input("Enter new email: ")
            student['Address'] = input("Enter new address: ")
            student['Ph_no'] = input("Enter new ph number: ")
            student['Nationality'] = input("Enter Nationality: ")
            print("Student updated successfully!")
        updated_students.append(student)
    save_students(filename, updated_students)

def main():
    filename = 'python5.csv'
    while True:
        print("\n1. Display all students")
        print("2. Display total number of students")
        print("3. Add new student")
        print("4. Search student by ID")
        print("5. Delete student by ID")
        print("6. Update student by ID")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_students(filename)
        elif choice == '2':
            display_total_number_of_students(filename)
        elif choice == '3':
            add_new_student(filename)
        elif choice == '4':
            StudentID = input("Enter student ID to search: ")
            found_students = search_student_by_id(filename, StudentID)
            if found_students:
                for student in found_students:
                    for key, value in student.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print("Student not found.")
        elif choice == '5':
            StudentID = input("Enter student ID to delete: ")
            delete_student_by_id(filename, StudentID)
        elif choice == '6':
            StudentID = input("Enter student ID to update: ")
            update_student_by_id(filename, StudentID)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
