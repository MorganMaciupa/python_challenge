import os
import csv

# Path to collect data from the Resources folder
budgetcsv = os.path.join("Resources", "budget_data.csv")

#Define the variables:
months = []
total = []
largest_increase = []
smallest_increase = []

# # Open the csv

with open(budgetcsv) as csvfile:
    
#  # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
# # Read the header row first
    csv_header = next(csvreader)
# Loop through each row in the file
    for row in csvreader:
        
# # # Add total number of months included in the dataset to a list
        months.append(row[0])
        total.append(int(row[1]))
    
    #Calculate the total of months in the list
    print(f'Total months: {len(months)}')
    
# # # Add each total amount of "Profit/Losses" over the entire period to a list
        
    
    #Sum the totals from the list
    print(f'Total: ${sum(total)}')

# # Add average of the changes in "Profit/Losses" over the entire period to a list
        

# # Add greatest increase in profits (date and amount) over the entire period to a list
    #largest_increase.append(row[1])
        # lgst_inc = 

# # The greatest decrease in losses (date and amount) over the entire period