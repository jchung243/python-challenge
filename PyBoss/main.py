# Dependencies
import os
import csv

# Open CSV
csv_path = os.path.join('..', 'Resources', 'employee_data.csv')
with open(csv_path, newline='') as employee_csv:
    employee_data = csv.reader(employee_csv, delimiter=',')

    # Separate header and call next line
    employee_header = next(employee_data)

    #For loop to cycle through data
    for row in employee_data:
        print('hi')