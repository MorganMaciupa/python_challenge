import os
import csv

# Set path to collect data from the Resources folder
budgetcsv = os.path.join("Resources", "budget_data.csv")
# Set path to write data to text file
results = os.path.join("Analysis", "Results.txt")

# Define the variables
months = []
total = []
change = []

# Open the csv
with open(budgetcsv) as csvfile:
    
# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first
    csv_header = next(csvreader)
    # Loop through each row in the file
    for row in csvreader:
        
        # Count each row as a new month by adding each to a list
        months.append(row[0])
        
        # Add each total amount of "Profit/Losses" over the entire period to a list
        total.append(float(row[1]))
        
    #Print table title    
    print("Financial Analysis")
    print("-----------------------------------")
    #Print the total number of months
    print(f'Total months: {len(months)}')
    
#Open text file to save results
with open(results, 'w') as txtfile:
    
    # Write results to txt file
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------------\n")
    txtfile.write(f'Total months: {len(months)}\n')
    txtfile.write("-----------------------------------\n")

    #Create a loop to calculate the differences between each month and the one previous
    for i in range(1, len(months)):
        #
        change.append(total[i] - total[i-1])
        avg_change = round(sum(change)/len(change), 2)
        
        #Find the month with the highest increase in revenue
        max_increase = max(change)
        month_max = (months[change.index(max(change))])
        
        #Find the month with the largest decrease in revenue (ie the biggest loss)
        max_decrease = min(change)
        month_min = (months[change.index(min(change))])

    #Sum the total of all revenue
    print(f'Total: ${sum(total)}')
    #Print the average change, greatest increase and decrease with index months
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {month_max} (${max_increase})')
    print(f'Greatest Decrease in Profits: {month_min} (${max_decrease})')
    
    #Print to the txt file
    txtfile.write(f'Total: ${sum(total)}\n')
    #Print the average change, greatest increase and decrease to txt file
    txtfile.write(f'Average Change: ${avg_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {month_max} (${max_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {month_min} (${max_decrease})\n')