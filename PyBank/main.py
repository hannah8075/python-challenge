#import packages
import os
import csv

#create file path for csv file
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#open and read csv file
with open(csvpath) as budget_data:

    csvreader = csv.reader(budget_data, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #define lists needed for analysis
    month_list = []
    profit_loss_list=[]

    # Read each row of data after the header
    for row in csvreader:
        month_list.append(row[0])
        profit_loss_list.append(int(row[1]))
    
    #print(profit_loss_list)

    # FIND NUMBER OF MONTHS
    num_of_months = len(month_list)
    #print(f"Total Months: {num_of_months}")

    # FIND TOTAL AMOUNT OF PROFIT/LOSS
    total_profit_loss = sum(profit_loss_list)
    #print(f"Total: ${total_profit_loss}")

    # FIND AVERAGE CHANGE OF PROFIT/LOSS
    #define average function
    def average(lst):
        return round(sum(lst)/len(lst),2)

    profit_loss_change = []

    for i, num in enumerate(profit_loss_list):
        #print(i,num); max index is 85
        if i == 85:
            break
        profit_loss_change.append(profit_loss_list[i+1] - profit_loss_list[i])
        
    avg_change = (average(profit_loss_change))
    #print(f"Average Change: ${avg_change}")

    # FIND GREATEST INCREASE IN PROFIT/LOSS
    
    #for i, month in enumerate(month_list):
        #print(i, month); max index is 85
    #for i, num in enumerate(profit_loss_change):
        #print(i, num); max index is 84; index + 1 is the month change number references to
    max_month_num = max(profit_loss_change)
    max_month_idx = profit_loss_change.index(max(profit_loss_change))+1
    max_month = month_list[max_month_idx]
    #print(f"Greatest Increase in Profits: {max_month} (${max_month_num})")

    # FIND GREATEST DECREASE IN PROFIT/LOSS
    min_month_num = min(profit_loss_change)
    min_month_idx = profit_loss_change.index(min(profit_loss_change))+1
    min_month = month_list[min_month_idx]
    #print(f"Greatest Decrease in Profits: {min_month} (${min_month_num})")

# PRINT RESULTS
print('''Financial Analysis
_____________________________________''')
print(f"Total Months: {num_of_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_month_num})")
print(f"Greatest Decrease in Profits: {min_month} (${min_month_num})")


# CREATE TEXT FILE IN ANALYSIS FOLDER

# Specify the file to write to
output_path = os.path.join("analysis", "PyBankResults.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("_____________________________________")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {num_of_months}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${total_profit_loss}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${avg_change}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${max_month_num})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${min_month_num})")