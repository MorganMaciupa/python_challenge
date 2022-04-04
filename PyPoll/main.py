import os
import csv

# Path to collect data from the Resources folder
polling_csv = os.path.join("Resources", "election_data.csv")
# Path to save data to text file
text_results = os.path.join("Analysis", "Results.txt")

# Define variables
total_votes = 0
candidate_votes = {}
candidate_list = []
vote_percentage = 0
winning_candidate = {}
winning_count = 0

# # Open the csv
with open(polling_csv, "r") as csvfile:
    
#  # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
# # Read the header row first
    csv_header = next(csvreader)
    
# Loop through each row in the file
    for row in csvreader: 
        
# The count each row as a new vote
        total_votes += 1
    
    #Define the candidate names
        candidate_name = row[2]
        
     #Create conditional for finding unique candidate names from the list
        if candidate_name not in candidate_list: 
            #Add it to the list of candidates 
            candidate_list.append(candidate_name)
            #Start at zero and add one to their vote count 
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1
     
     #Print to terminal
    print("Election Results")
    print("-----------------------------------")
    print(f'Total Votes: {total_votes}')
    print("-----------------------------------")
     
#Open text file to save results
with open(text_results, 'w') as txtfile:
    # Write results to txt file
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write("-----------------------------------\n")
        
    #Run a for loop for each candidate in the list
    for candidate_name in candidate_votes: 
        #Take the total votes for each candidate
        c_votes = candidate_votes[candidate_name]
        #Calculate their percentage of total votes 
        vote_percentage = round((int(c_votes) / int(total_votes) * 100), 3)
        #Define the results for the candidate 
        candidate_results = (f"{candidate_name}: {vote_percentage}% ({c_votes})\n")
        #Print each candidates results to termainal
        print(candidate_results)
        #Write the results to txt file
        txtfile.write(candidate_results)
        
#Find the winning candidate with if statement
        if (c_votes > winning_count):
            #then set winning_count
             winning_count = c_votes
             winning_candidate = candidate_name
    
    #print winning candidate to termainl
    print("-----------------------------------")
    print(f'Winner: {winning_candidate}')
    print("-----------------------------------")
    
    #Write results to txt file
    txtfile.write("-----------------------------------\n")
    txtfile.write(f'Winner: {winning_candidate}\n')
    txtfile.write("-----------------------------------\n")
