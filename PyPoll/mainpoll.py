import csv 
import os
import pprint

path = os.path.join('..','..', '..',
                    'UT-MCB-DATA-PT-11-2019-U-C', 'Homework',
                    '02-Python', 'Instructions', 'PyPoll', 
                    'Resources','election_data.csv'
                    )

with open(path, 'r') as infile:

    csv_reader = csv.reader(infile)
    raw = list(csv_reader)

    header = raw.pop(0)  ##could also do """header = next(csv_reader)"""

total_votes = len(raw)


nam = [row[2] for row in raw]
cand_name = []
for name in nam:
    if name not in cand_name:
        cand_name.append(name)

khan_c = 0
corr_c = 0
li_c = 0
tool_c = 0

for i in nam:
    if i == cand_name[0]:
        khan_c += 1
    elif i == cand_name[1]:
        corr_c += 1
    elif i == cand_name[2]:
        li_c += 1
    elif i == cand_name[3]:
        tool_c += 1


per_kh = float(format(((khan_c/total_votes) * 100), '.3f'))
per_co = float(format(((corr_c/total_votes) * 100), '.3f'))
per_li = float(format(((li_c/total_votes) * 100), '.3f'))
per_ot = float(format(((tool_c/total_votes) * 100), '.3f'))

the_list = []
the_list = [cand_name[0], khan_c, per_kh], [cand_name[1], corr_c, per_co], \
    [cand_name[2], li_c, per_li], [cand_name[3], tool_c, per_ot]

#select winner
max_list = []
for i in range(0, len(the_list)):
    max_list.append(the_list[i][1])
max = max(max_list)
maxindex = max_list.index(max)

#results in vars

a = 'Election Results\n'
b = '------------------------\n'
c = the_list[0][0] + '\n Votes: ' + str(the_list[0][1]) +\
     '  (' + str(the_list[0][2]) + '%)\n'
d = the_list[1][0] + '\n Votes: ' + str(the_list[1][1]) +\
     '  (' + str(the_list[1][2])+ '%)\n'
e = the_list[2][0] + '\n Votes: ' + str(the_list[2][1]) +\
     '  (' + str(the_list[2][2])+ '%)\n'
f = the_list[3][0] + '\n Votes: ' + str(the_list[3][1]) +\
     '  (' + str(the_list[3][2])+ '%)\n'
w = 'Winner: ' + str(cand_name[maxindex])
t = 'Total Votes: ' + str(total_votes) + '\n'

with open('election_results', 'w') as outfile:
    outfile.write(a + b + t + b + c + d + e +  f + b + w)
    outfile.close()

readd = open('election_results', 'r')
print (readd.read())
readd.close()

