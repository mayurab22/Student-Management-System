import csv

# Define a dictionary to map grades to numerical values for comparison
grade_to_value = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1
}

# Function to read the CSV file and return the student data
def read_student_csv(file_path):
    students = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append({
                'name': row['name'],
                'age': int(row['age']),
                'grade': row['grade']
            })
    return students

# Function to calculate the average grade
def calculate_average_grade(students):
    total_grade_value = 0
    for student in students:
        total_grade_value += grade_to_value[student['grade']]
    
    average_grade_value = total_grade_value / len(students)
    
    # Find the grade that corresponds to the average value
    for grade, value in grade_to_value.items():
        if value == round(average_grade_value):
            return grade

# Function to find the student(s) with the highest grade
def find_highest_grade_students(students):
    highest_grade_value = max(grade_to_value[student['grade']] for student in students)
    
    # Find all students with the highest grade
    highest_grade_students = [
        student for student in students 
        if grade_to_value[student['grade']] == highest_grade_value
    ]
    
    return highest_grade_students

# Main function to run the script
def main():
    file_path = r'student.csv'  # File path for the student CSV
    
    # Read the student data from the CSV
    students = read_student_csv(file_path)
    
    # Calculate the average grade
    average_grade = calculate_average_grade(students)
    print(f"The average grade is: {average_grade}")
    
    # Find and print the student(s) with the highest grade
    highest_grade_students = find_highest_grade_students(students)
    
    if len(highest_grade_students) == 1:
        print(f"Student with the highest grade is: {highest_grade_students[0]['name']} with grade {highest_grade_students[0]['grade']}")
    else:
        print("Students with the highest grade are:")
        for student in highest_grade_students:
            print(f"{student['name']} with grade {student['grade']}")

# Run the script
main()
