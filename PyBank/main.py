# Import modules
import csv
import os

# Set path to csv file
fileLoad = os.path.join("Resources", "budget_data.csv")

# File to hold the output
outputFile = os.path.join("analysis", "analysis.txt")

# Variables
totalMonths = 0
totalProfit_Loss = 0
monthlyChanges = []
months = [] 

# read csv file
with open(fileLoad) as Budget_Data:
    csvreader = csv.reader(Budget_Data)

    # Skip Header
    header = next(csvreader)


    firstRow = next(csvreader)
    totalMonths += 1 
    totalProfit_Loss += float(firstRow[1])
    previousProfit_Loss = float(firstRow[1]) 

    for row in csvreader:
        totalMonths += 1 
        totalProfit_Loss += float(row[1])

        # calculate the net change of Profit/Loss

        netChange = float(row[1]) - previousProfit_Loss
        monthlyChanges.append(netChange)
        months.append(row[0])
        previousProfit_Loss = float(row[1])

  
# calculate the average net change per month

averageMonthlyChange = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] 
greatestDecrease = [months[0], monthlyChanges[0]] 

# Calculate the greatest and least monthly change

for m in range(len(monthlyChanges)):

    if(monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]

    if(monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]

# Print in terminal
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${int(totalProfit_Loss)}\n"   
    f"Average Change: ${averageMonthlyChange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${int(greatestIncrease[1])})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${int(greatestDecrease[1])})"
    )

print(output)

# Export the text file
with open(outputFile, "w") as textFile:
    textFile.write(output)