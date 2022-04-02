import os
import csv

# Path to collect data from the Resources folder
budgetcsv = os.path.join("Resources", "budget_data.csv")

#Define the variables:
months = []
total = []
totals_change = []

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
# # # Add each total amount of "Profit/Losses" over the entire period to a list
        total.append(float(row[1]))

    #create a loop to total differences between rows
    for i in range(1,len(total)):
        totals_change.append(total[i] - total[i-1])
        avg_change = round(sum(totals_change)/len(totals_change), 2)
        
        max_increase = max(totals_change)
        
        max_decrease = min(totals_change)
        
        
    print("Financial Analysis")
    print("-----------------------------------")
    print(f'Total months: {len(months)}')
    print(f'Total: ${sum(total)}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: (${max_increase})')
    print(f'Greatest Decrease in Profits: (${max_decrease})')
    
# # Add greatest increase in profits (date and amount) over the entire period to a list
    

# # # The greatest decrease in losses (date and amount) over the entire period
#         