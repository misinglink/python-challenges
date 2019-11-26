import csv 
import pprint as p
import os

csv_path = os.path.join('budget_data.csv')

with open(csv_path, 'r') as infile: # not sure on language for this one
    in_c = csv.reader(infile)   #or this one :(

    header = next(in_c)  #gets the first item out(list format) 
                            #and look through row
    data = list(in_c)  #formats rows in lists and embeds in list

#total month count
    months = 0
    for i in data:
        months += 1

#net profit
    profit = 0
    for i in range(0, len(data)):
        num = data[i][1]
        profit += int(num)

#attempt for average change
    total_diff = 0
    for i in range(1, len(data)):
        num1 = int(data[i-1][1])
        num2 = int(data[i][1])
        diff = num2 - num1
        total_diff += int(diff)

#max/min findin 
    maxminlist = []
    for i in range(0, len(data)):
        num = int(data[i][1])
        maxminlist.append(num)

    maxnum = max(maxminlist)
    minnum = min(maxminlist)

    maxindex = maxminlist.index(maxnum)
    minindex = maxminlist.index(minnum)

#write results to file
with open('Financial Analysis', 'r+') as out_file:
    out_file.write('Timeframe of analysis:  ' + str(months) + ' months \n')
    out_file.write('Total profit:  $' + str(profit) + '\n')
    out_file.write('Average Change: $' + str(format(float(total_diff / 85), '.2f')) + '\n')
    out_file.write('Greatest Increase in Profits: ' + str(data[maxindex][0]) +' $' + str(maxnum) + '\n')
    out_file.write('Greatest Decrease in Profits: ' + str(data[minindex][0]) + ' $' + str(minnum) + '\n')

#prints results in terminal :)
    for line in out_file:
        print(line)
    out_file.close()
