# Depdendancies
import os
import csv

# Open CSV
csv_path = os.path.join('..', 'Resources', 'election_data.csv')
with open(csv_path, newline='') as election_csv:
    election_data = csv.reader(election_csv, delimiter=',')

    # Separate header and call next line
    election_header = next(election_data)

    # Define empty dictionary
    votes = {}
    votesum = 0

    # Loop through rows of data
    for row in election_data:
        candidate = row[2]
        # If candidate name is in the dictonary, add a vote. Otherwise add entry.
        if candidate in votes:
            votes[candidate] = votes[candidate]+1
        else:
            votes[candidate] = 1
            
    # Loop through dictonary
    for key in votes:
        votesum = votesum + int(votes[key])

    # Print statments
    print(votes)
    print(votesum)

    # Export to text file
    #output = open("PyBank_Output.txt", "w")
    #output.write("Financial Analysis\n")
    #output.close()

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------