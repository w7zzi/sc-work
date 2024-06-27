import json

class_data = {
  "class": {
    "pupils": [
      {
        "name": "John Doe",
        "grades": {
          "Maths": 85,
          "English": 78,
          "Sciences": 92
        }
      },
      {
        "name": "Jane Smith",
        "grades": {
          "Maths": 90,
          "English": 88,
          "Sciences": 94
        }
      },
      {
        "name": "Tom Brown",
        "grades": {
          "Maths": 75,
          "English": 64,
          "Sciences": 70
        }
      },
      {
        "name": "Emily White",
        "grades": {
          "Maths": 92,
          "English": 95,
          "Sciences": 98
        }
      },
      {
        "name": "Michael Green",
        "grades": {
          "Maths": 80,
          "English": 82,
          "Sciences": 85
        }
      },
      {
        "name": "Sarah Johnson",
        "grades": {
          "Maths": 88,
          "English": 91,
          "Sciences": 89
        }
      },
      {
        "name": "David Lee",
        "grades": {
          "Maths": 76,
          "English": 85,
          "Sciences": 78
        }
      },
      {
        "name": "Laura Adams",
        "grades": {
          "Maths": 84,
          "English": 79,
          "Sciences": 86
        }
      },
      {
        "name": "Robert Brown",
        "grades": {
          "Maths": 93,
          "English": 92,
          "Sciences": 90
        }
      },
      {
        "name": "Lisa Davis",
        "grades": {
          "Maths": 81,
          "English": 80,
          "Sciences": 82
        }
      },
      {
        "name": "Kevin Harris",
        "grades": {
          "Maths": 77,
          "English": 76,
          "Sciences": 75
        }
      },
      {
        "name": "Karen Young",
        "grades": {
          "Maths": 89,
          "English": 87,
          "Sciences": 90
        }
      },
      {
        "name": "Daniel King",
        "grades": {
          "Maths": 95,
          "English": 94,
          "Sciences": 97
        }
      },
      {
        "name": "Nancy Clark",
        "grades": {
          "Maths": 79,
          "English": 83,
          "Sciences": 85
        }
      },
      {
        "name": "Patrick Lee",
        "grades": {
          "Maths": 72,
          "English": 74,
          "Sciences": 70
        }
      },
      {
        "name": "Jessica Turner",
        "grades": {
          "Maths": 91,
          "English": 89,
          "Sciences": 93
        }
      },
      {
        "name": "Brian Scott",
        "grades": {
          "Maths": 78,
          "English": 77,
          "Sciences": 76
        }
      },
      {
        "name": "Rachel Hall",
        "grades": {
          "Maths": 85,
          "English": 88,
          "Sciences": 84
        }
      },
      {
        "name": "Steven Walker",
        "grades": {
          "Maths": 90,
          "English": 91,
          "Sciences": 92
        }
      },
      {
        "name": "Megan Lewis",
        "grades": {
          "Maths": 83,
          "English": 81,
          "Sciences": 84
        }
      },
      {
        "name": "Aaron Robinson",
        "grades": {
          "Maths": 82,
          "English": 79,
          "Sciences": 81
        }
      },
      {
        "name": "Michelle Allen",
        "grades": {
          "Maths": 87,
          "English": 86,
          "Sciences": 88
        }
      },
      {
        "name": "Justin Carter",
        "grades": {
          "Maths": 75,
          "English": 73,
          "Sciences": 74
        }
      },
      {
        "name": "Emma Evans",
        "grades": {
          "Maths": 93,
          "English": 94,
          "Sciences": 96
        }
      },
      {
        "name": "Scott Mitchell",
        "grades": {
          "Maths": 70,
          "English": 72,
          "Sciences": 71
        }
      },
      {
        "name": "Rebecca Baker",
        "grades": {
          "Maths": 88,
          "English": 89,
          "Sciences": 91
        }
      },
      {
        "name": "Andrew Nelson",
        "grades": {
          "Maths": 86,
          "English": 87,
          "Sciences": 85
        }
      },
      {
        "name": "Emily Roberts",
        "grades": {
          "Maths": 92,
          "English": 93,
          "Sciences": 94
        }
      },
      {
        "name": "Joshua Parker",
        "grades": {
          "Maths": 80,
          "English": 81,
          "Sciences": 79
        }
      },
      {
        "name": "Sophia Edwards",
        "grades": {
          "Maths": 84,
          "English": 85,
          "Sciences": 87
        }
      }
    ]
  }
}

def display_all_grades():
    for student in class_data["class"]["pupils"]:
        print(f"Name: {student['name']}")
        for subject, grade in student["grades"].items():
            print(f"{subject}: {grade}")

def average_grade_subject():
    subjects = ["Maths", "English", "Sciences"]
    for subject in subjects:
        total = 0
        count = 0
        for student in class_data["class"]["pupils"]:
            total += student["grades"][subject]
            count += 1
            average = total / count
            print(f"Average grade for {subject}: {average:.2f}")

def average_grade_per_student():
    for student in class_data["class"]["pupils"]:
        total = 0
        count = 0
        for grade in student["grades"].values():
            total += grade
            count += 1
            average = total / count
            print(f"Average grade for {student['name']}: {average:.2f}")
  
def add_student():
    name = input("Enter student name: ")  
    maths_grade = int(input("Enter maths grade: "))
    english_grade = int(input("Enter english grade: "))
    sciences_grade = int(input("Enter sciences grade: "))    
    new_student = {
        "name": name,
        "grades": {
            "Maths": maths_grade,
            "English": english_grade,
            "Sciences": sciences_grade
        }
    }
    class_data["class"]["pupils"].append(new_student)

def count_students_above_average_grade():
    total = 0
    count = 0
    for student in class_data["class"]["pupils"]:
        for grade in student["grades"].values():
            total += grade
            count += 1
            average = total / count
    above_average = 0
    for student in class_data["class"]["pupils"]:
        total_student = 0
        count_student = 0
        for grade in student["grades"].values():
            total_student += grade
            count_student += 1
            average_student = total_student / count_student
            if average_student > average:
                above_average += 1
    print(f"Number of students above average grade: {above_average}")

def search_students_by_name():
    name = input("Enter student name: ")
    for student in class_data["class"]["pupils"]:
        if student["name"] == name:
            print(f"Student found: {student['name']}")
            print(f"Maths grade: {student['grades']['Maths']}")
            print(f"English grade: {student['grades']['English']}")
            print(f"Sciences grade: {student['grades']['Sciences']}")

# main program
print("Menu:")
print("1 - Show all grades for all subjects and students, sorted alphabetically by name")
print("2 - Show the average grade for each subject")
print("3 - Show the average grade for each student, sorted descendant (top students first)")
print("4 - Add a new student")
print("5 - Count students above an average grade")
print("6 - Search for students by name")
print("7 - Exit program")

operation = input("Enter your choice (1/2/3/4/5/6/7): ")
if operation == '1':
    display_all_grades()
elif operation == '2':
    average_grade_subject()
elif operation == '3':
    average_grade_per_student()
elif operation == '4':
    add_student()
elif operation == '5':
    limit = int(input("Enter the average grade above limit: "))
    count_students_above_average_grade()
elif operation == '6':
    name = input("Enter the name of the student to search: ")
    search_students_by_name()
elif operation == '7':
    print("Exiting program")