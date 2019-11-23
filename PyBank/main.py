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

#Mst answer average change greatest increase and greatest decrease then done :)
#left off in min 21:46

#attempt for average change
    total_diff = 0
    for i in range(1, len(data)):
        num1 = int(data[i-1][1])
        num2 = int(data[i][1])
        diff = num2 - num1
        total_diff += int(diff)

#max/min
    maxminlist = []
    for i in range(0, len(data)):
        num = int(data[i][1])
        maxminlist.append(num)

    maxnum = max(maxminlist)
    minnum = min(maxminlist)

    maxindex = maxminlist.index(maxnum)
    minindex = maxminlist.index(minnum)

print('Timeframe of analysis:  ' + str(months) + ' months')
print('Total profit:  $' + str(profit))
print('Average Change: $' + str(format(float(total_diff / 85), '.2f')))
print('Greatest Increase in Profits: ' + str(data[maxindex][0]) + ' $' + str(maxnum))
print('Greatest Decrease in Profits: ' + str(data[minindex][0]) + ' $' + str(minnum))