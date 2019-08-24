# Import Modules
import os
import csv

# Set Variables
months = []
pnl = []
total_change = []
avg_change = 0
profit = 0
loss = 0
# Set Path For File
budget_csv = os.path.join('.','Resources', 'budget_data.csv')

# Open & Read CSV File
with open(budget_csv, 'r') as csvfile:
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read The Header
    header = next(csvreader)
    # Read The Rirst Row
    row = next(csvreader)

    # Append to months and pnl list
    months.append(row[0])
    pnl.append(int(row[1]))
    # Set Current Row as previous
    previous = int(row[1])

    # Iterate through every row
    for row in csvreader:
        # Append to months and pnl list
        months.append(row[0])
        pnl.append(int(row[1]))
        # Find the monthly change and append to total_change
        change = int(row[1])-previous
        total_change.append(int(change))
        # Set Current Row as previous
        previous = int(row[1])
# Calculate avg_change and format to two decimal points
avg_change = float("{0:.2f}".format(sum(total_change)/len(total_change)))
# Find the Greatest Increase 
profit = max(pnl)
# Find the Greatest Decrease
loss = min(pnl)
# Find the Corresponding Month to the Greatest Increase and Greatest Decrease (Indexes)
profit_month = pnl.index(max(pnl))
loss_month = pnl.index(min(pnl))

# Print the Analysis
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(pnl)}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {months[profit_month]} (${profit})")
print(f"Greatest Decrease in Profits: {months[loss_month]} (${loss})")

# Output file
output_file = os.path.join('.', 'Resources', 'analysis.text')

# Open output file to write to
with open(output_file, 'w',) as txtfile:

# Write the Analysis
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months:{len(months)}\n")
    txtfile.write(f"Total: ${sum(pnl)}\n")
    txtfile.write(f"Average Change: {avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {months[profit_month]} (${profit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {months[loss_month]} (${loss})\n")
        
        
