#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Instructions
# Your task is to create a Python script that analyzes the records to calculate each of the following:
  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

 # ```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Pseudo code
# Open the file
# Read all of the file's rows
# Pass the contents of each row into a list, with
    # each column as a separate list
# Check the length of the list to determine total months
# Sum the profit/loss field of the list to determine total profit/loss
# Calculate the average of the profit/loss field of
    # the list
# Find:
    # 1)The greatest increase in profit
    # 2) The greatest decrease in losses
# Use a function to print the results


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Begin actual code


# Module for setting filepaths in all operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')



# Open the file
with open(csvpath, mode='r', newline='') as csvfile:
    # Read the content
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)


# --------------------------------------------------------------------------------------------------
# Read the CSV and determine the output values

    # Initialize profitlossSum as an integer
    profitLossSum = 0
    profitLossGreatest = 0
    lastProfitLoss = 0


    # Loop to pull source data into two separate lists
    month = []
    profitLoss = []
    for row in csvreader:
        # print the row as a proof of concept
        #print(row)

        row[1] = int(row[1])
        month.append(row[0])
        profitLoss.append(row[1])

        # print the results initially as a proof of concept
        #print(row[1])

        #Add this row's profit/loss to the current total
        profitLossSum = int(profitLossSum)+int(row[1])

        # Check whether this row is the greatest increase in profits
            # Defined as the largest increase from one month to the next
        if row[1] > lastProfitLoss:
            profitLossGreatestMonth = row[0]
            profitLossGreatest = row[1]

        # Check whether this row is the greatest decrease in losses
            # Defined as the smallest change in a single month where the resulting profit/loss  was still less than that of the prior month
        if row[1] < lastProfitLoss and row[1] < 0:
            profitLossLeastMonth = row[0]
            profitLossLeast = row[1]

        # Set ProfitLoss to reference in next run
        lastProfitLoss = row[1]

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Final Calculations

    # Calculate total number of months' data included
    totalMonths = len(month)

    # Calculate the average change
    profitLossAverage = profitLossSum/len(month)
    # Round this to eliminate decimal noise
    profitLossAverage = round(profitLossAverage)


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Print the analysis
    print(f"\n Financial analysis \n --------------------- \n Total Months: {totalMonths} \n Total: ${profitLossSum} \n The average change was: ${profitLossAverage} \n Greatest Increase in Profits: ${profitLossGreatest} in {profitLossGreatestMonth} \n Greatest Decrease in Profits: ${profitLossLeast} in {profitLossLeastMonth} \n ---------------------")

# Write the analysis to a TXT file
analysis = open("analysis.txt","w+")
analysis.write(f"\n Financial analysis \n --------------------- \n Total Months: {totalMonths} \n Total: ${profitLossSum} \n The average change was: ${profitLossAverage} \n Greatest Increase in Profits: ${profitLossGreatest} in {profitLossGreatestMonth} \n Greatest Decrease in Profits: ${profitLossLeast} in {profitLossLeastMonth} \n ---------------------")
