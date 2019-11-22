import csv 
import pprint as p
import os

csv_path = os.path.join('budget_data.csv')

print(csv_path)

with open(csv_path, 'r') as infile: # not sure on language for this one
    in_c = csv.reader(infile)   #or this one :(

    header = next(in_c)  #gets the first item out(list format) 
                            #and look through row
    data = list(in_c)  #formats rows in lists and embeds in list

#total month count
    months = 0
    for i in data:
        months += 1
       
    
    

    print('Timeframe of analysis:  ' + str(months) + ' months')
    p.pprint(data)