# Depdendancies
import os
import csv

# Open CSV
csv_path = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csv_path, newline='') as budget_csv:
    budget_data = csv.reader(budget_csv, delimiter=',')

    # Separate header and call next line
    budget_header = next(budget_data)

    # Define lists and variables to append budget values and store values
    profit_tracker = [0.0]
    profit_change = [0.0]
    increase = 0.0
    decrease = 0.0
    x = 0

    # Loop through data
    for row in budget_data:
        #Advance counter
        x = x + 1 
        #Store date string in placeholder
        date = row[0]

        # Store profit value in tracker list
        profit_tracker.append(float(row[1]))
        #Store change from previous value to current value in list.
        profit_change.append(float(profit_tracker[x]-profit_tracker[x-1]))

        if profit_change[x] > increase:
            increase = profit_change[x]
            increase_date = date
        if profit_change[x] < decrease:
            decrease = profit_change[x]
            decrease_date = date
    
    #Remove initial 0 value from list
    del profit_tracker[0]
    del profit_change[0]

    #Total number of months displayed:
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(profit_tracker)}")
    print(f"Total: ${sum(profit_tracker)}")
    print(f"Average Change: ${sum(profit_change)/len(profit_change)}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

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