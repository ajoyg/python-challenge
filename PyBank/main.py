import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')

#open the budget_data.csv file
with open(csvpath, encoding='utf8') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')
   
    #Get the data into a list
    budgetrows=[r for r in csvreader]
    budgetrows.pop(0) # Remove the header
    
    total_change=0
    change_dict={}
    for i in range(len(budgetrows)):
        profit_loss_this_mth=budgetrows[i]
        if i > 0:
            profit_loss_lst_mth = budgetrows[i-1]
            profit_loss_change=  int(profit_loss_this_mth[1]) - int(profit_loss_lst_mth[1])
            change_dict[profit_loss_this_mth[0]]= profit_loss_change
            total_change = total_change+profit_loss_change
             
    total_months=len(budgetrows) #Total number of months, exclude the header

    total_profit_loss=0
    for monthly_budget in budgetrows:
        total_profit_loss = total_profit_loss+int(monthly_budget[1]) # Total profit/loss
    
    # Get the greatest increase and decrease
    greatest_increase = 0
    greatest_decrease = -1
    for month, change in change_dict.items():
        if change >0:
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_mth = month
        else:
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_mth = month

# write the results into the analysis file   
analysisoutput = os.path.join('analysis','FinancialAnalysis.txt')
with open(analysisoutput,'w') as analysiswriter:
    analysiswriter.write("```text\n")
    analysiswriter.write("Financial Analysis\n")
    analysiswriter.write("----------------------------\n")
    analysiswriter.write(f"Total Months: {total_months}\n")
    analysiswriter.write(f'Total Profit/Loss: {"${:.0f}".format(total_profit_loss)}\n')
    analysiswriter.write(f'Average change: {"${: .2f}".format(total_change/(len(budgetrows)-1))}\n')
    analysiswriter.write(f'Greatest Increase in Profits: {greatest_increase_mth}  ({"${:.0f}".format(greatest_increase)})\n')
    analysiswriter.write(f'Greatest Decrease in Profits: {greatest_decrease_mth}  ({"${: .0f}".format(greatest_decrease)})\n')