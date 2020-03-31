import os
import csv

bank_csv = os.path.join('..', 'Resources', 'PyBank_File.csv')

ProfitLoss = []

Average = 0

Lines = 0

Lastmonth = []

date= []

with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        ProfitLoss.append(float(row[1]))
        Lines += 1
        date.append(row[0])
       
    for i in range(1,Lines):
        Lastmonth.append(ProfitLoss[i] - ProfitLoss[i-1])   
        Average = round(sum(Lastmonth)/(Lines-1),2)

        max_date = str(date[Lastmonth.index(max(Lastmonth))])
        min_date = str(date[Lastmonth.index(min(Lastmonth))])


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {str(Lines)}')
print(f'Total: ${sum(ProfitLoss)}')
print(f'Average Change: ${str(Average)}')
print(f'Greatest increase in profits: {max_date} (${max(Lastmonth)})')
print(f'Greatest decrease in profits: {min_date} (${min(Lastmonth)})')

output_file = os.path.join("analysis_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Financial Analysis\n')
    datafile.write(f'Total Months: {str(Lines)}\n')
    datafile.write(f'Total: ${sum(ProfitLoss)}\n')
    datafile.write(f'Average Change: ${str(Average)}\n')
    datafile.write(f'Greatest increase in profits: {max_date} (${max(Lastmonth)})\n')
    datafile.write(f'Greatest decrease in profits: {min_date} (${min(Lastmonth)})\n')




