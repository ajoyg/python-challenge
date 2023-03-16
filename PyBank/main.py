import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')

#open the budget_data.csv file
with open(csvpath, encoding='utf8') as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=',')
   
    #Get the data into a list
    budgetrows=[row for row in csvreader]
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

# write the results into the analysis file and print it on the terminal  
analysisoutput = os.path.join('analysis','FinancialAnalysis.txt')
with open(analysisoutput,'w') as analysiswriter:
    analysiswriter.write("```text\n")
    print("```text")
    analysiswriter.write("Financial Analysis\n")
    print("Financial Analysis")
    analysiswriter.write("----------------------------\n")
    print("----------------------------")
    analysiswriter.write(f"Total Months: {total_months}\n")
    print(f"Total Months: {total_months}")
    analysiswriter.write(f'Total: {"${:.0f}".format(total_profit_loss)}\n')
    print(f'Total: {"${:.0f}".format(total_profit_loss)}')
   
    analysiswriter.write(f'Average change: {"${: .2f}".format(total_change/(len(budgetrows)-1))}\n')
    print(f'Average change: {"${:.2f}".format(total_change/(len(budgetrows)-1))}')
   
    analysiswriter.write(f'Greatest Increase in Profits: {max(change_dict, key=lambda key:change_dict[key])}  ({"${:.0f}".format(change_dict[max(change_dict, key=lambda key:change_dict[key])])})\n')
    print(f'Greatest Increase in Profits: {max(change_dict, key=lambda key:change_dict[key])}  ({"${:.0f}".format(change_dict[max(change_dict, key=lambda key:change_dict[key])])})')
   
    analysiswriter.write(f'Greatest Decrease in Profits: {min(change_dict, key=lambda key:change_dict[key])}  ({"${: .0f}".format(change_dict[min(change_dict, key=lambda key:change_dict[key])])})\n')
    print(f'Greatest Decrease in Profits: {min(change_dict, key=lambda key:change_dict[key])}  ({"${: .0f}".format(change_dict[min(change_dict, key=lambda key:change_dict[key])])})')
   
    analysiswriter.write("```\n")
    print("```")