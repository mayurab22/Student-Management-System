# Import the csv module for working with CSV files
import csv

# Open the 'student.csv' file in write mode with newline handling
with open('student.csv', 'w', newline='') as file:
    # Create a CSV writer object to write data to the file
    writer = csv.writer(file)

    # Define the field names for the CSV data
    field = ["name", "age", "grade"]

    # Write the field names as the first row of the CSV file
    writer.writerow(field)

    # Write additional data rows to the CSV file
    writer.writerow(["test1", "40", "A"])
    writer.writerow(["test2", "23", "E"])
    writer.writerow(["test3", "50", "C"])
    writer.writerow(["test4", "40", "B"])
    writer.writerow(["test5", "23", "D"])
    writer.writerow(["test6", "50", "A"])
    writer.writerow(["test7", "40", "F"])
    writer.writerow(["test8", "23", "E"])
    writer.writerow(["test9", "50", "F"])