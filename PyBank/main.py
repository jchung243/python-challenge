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
        # Advance counter
        x = x + 1 
        # Store date string in placeholder
        date = row[0]

        # Store profit value in tracker list
        profit_tracker.append(float(row[1]))
        # Store change from previous value to current value in list.
        profit_change.append(float(profit_tracker[x]-profit_tracker[x-1]))

        # Increase/decrease logic
        if profit_change[x] > increase:
            increase = profit_change[x]
            increase_date = date
        if profit_change[x] < decrease:
            decrease = profit_change[x]
            decrease_date = date
    
    # Remove initial value from lists and additional value from profit change list
    del profit_tracker[0]
    del profit_change[0]
    del profit_change[0]

    # Print statments
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(profit_tracker)}")
    print(f"Total: ${sum(profit_tracker)}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change), 2)}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

    # Export to text file
    output = open("PyBank_Output.txt", "w")
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {len(profit_tracker)}\n")
    output.write(f"Total: ${sum(profit_tracker)}\n")
    output.write(f"Average Change: ${round(sum(profit_change)/len(profit_change), 2)}\n")
    output.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
    output.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})\n")
    output.close()