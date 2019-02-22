# Depdendancies
import os
import csv

# Open CSV
csv_path = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csv_path, newline='') as budget_csv:
    budget_data = csv.reader(budget_csv, delimiter=',')

    # Separate header and call next line
    budget_header = next(budget_data)

    # Loop through data
    for row in budget_data:
        tot_months = row

# Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.