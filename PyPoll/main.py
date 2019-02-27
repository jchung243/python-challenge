# Depdendancies
import os
import csv

# Open CSV
csv_path = os.path.join('..', 'Resources', 'election_data.csv')
with open(csv_path, newline='') as election_csv:
    election_data = csv.reader(election_csv, delimiter=',')

    # Separate header and call next line
    election_header = next(election_data)

    # Define empty dictionary and placeholder variables
    votes = {}
    votesum = 0
    votecount = 0

    # Loop through rows of data
    for row in election_data:
        candidate = row[2]
        # If candidate name is in the dictonary, add a vote. Otherwise add entry.
        if candidate in votes:
            votes[candidate] = votes[candidate]+1
        else:
            votes[candidate] = 1
            
    # Loop through dictonary to tally sum of votes and find winner
    for key in votes:
        votesum = votesum + int(votes[key])
        if votes[key] > votecount:
            winner = key
            votecount = votes[key]

    # Print header and total votes
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votesum}")
    print("-------------------------")
    
    # Loop though dictonary to print election results
    for key in votes:
        print(f"{key}: {round(100*(votes[key]/votesum),3)}% ({votes[key]})")
    
    # Print winner
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    with open("PyPoll_Output.txt", "w") as output:
        #Print header and total votes to CSV
        output.write("Election Results\n")
        output.write("-------------------------\n")
        output.write(f"Total Votes: {votesum}")
        output.write("-------------------------\n")

        # Loop though dictonary to print election results
        for key in votes:
            output.write(f"{key}: {round(100*(votes[key]/votesum),3)}% ({votes[key]})\n")
        
        # Print winner
        output.write("-------------------------\n")
        output.write(f"Winner: {winner}\n")
        output.write("-------------------------\n")
        output.close()