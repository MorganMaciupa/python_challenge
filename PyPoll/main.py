import os
import csv

# Path to collect data from the Resources folder
polling_csv = os.path.join("Resources", "election_data.csv")

# Define the variables
total_votes = []

# # Open the csv
with open(polling_csv) as csvfile:
    
#  # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
# # Read the header row first
    csv_header = next(csvreader)
    
# Loop through each row in the file
    for row in csvreader: 
        
# The total number of votes cast
        total_votes.append(row[0])
print("Election Results")
print("-------------------------")
print(f'Total Votes: {len(total_votes)}')
print("-------------------------")

# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.




