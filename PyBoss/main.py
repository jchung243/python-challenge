# Dependencies
import os
import csv

# State Dictionary
us_state = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# CSV Paths
csv_path = os.path.join('..', 'Resources', 'employee_data.csv')
write_path = os.path.join(".", "employee_data_OUTPUT.csv")

with open(csv_path, newline='') as employee_csv:
    employee_data = csv.reader(employee_csv, delimiter=',')

    # Separate header and call next line
    employee_header = next(employee_data)

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(write_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        output = csv.writer(csvfile, delimiter=',')

        # Write headers
        output.writerow(['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    
        # For loop to cycle through data
        for row in employee_data:
        
            # Separate first and last name
            first,last = row[1].split(" ")
            row[1] = first
            row.insert(2, last)

            # Change DOB
            year,month,day = row[3].split("-")
            row[3] = f"{month}/{day}/{year}"

            # Change SSN
            first,second,third = row[4].split("-")
            row[4] = f"***-***-{third}"

            # Lookup State and change
            row[5] = us_state[row[5]]

            # Write row to CSV
            output.writerow(row)