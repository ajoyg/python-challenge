# python-challenge
Repo for python challenge, module 3 of the UCB Data Analytics &amp; Visualization Bootcamp.
This repo has two folders, PyBank and PyPoll. The python script in PyBank summarizes finanacial information of a company's performance while the python script in PyPoll analyzes the election results from voting data across counties.

PyBank<br>
The main.py python script reads a csv file - budget_data.csv located in the Resources folder within the PyBank folder. The script analyzes the financial records from [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". The script calculates the following - 
The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

The above data is written into a file called FinancialAnalysis.txt in the analysis folder [PyBank/analysis/Financialanalysis.txt], the output is also printed on the terminal.

PyPoll<br>
The main.py python script in the PyPoll directory analyzes the election results from a csv file called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The script calculates the following - 
* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

The above data is written into a file called ElectionResults.txt in the analysis folder [PyPoll/analysis/ElectionResults.txt], the output is also printed on the terminal.
