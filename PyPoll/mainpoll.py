import csv 
import os

path = os.path.join('..','..', '..',
                    'UT-MCB-DATA-PT-11-2019-U-C', 'Homework',
                    '02-Python', 'Instructions', 'PyPoll', 'Resources',
                    'election_data.csv'
                    )

with open(path, 'r') as infile:

    csv_reader = csv.reader(infile)
    raw = list(csv_reader)

    header = raw.pop(0)  ##could also do """header = next(csv_reader)"""

total_votes = len(raw)


nam = [row[2] for row in raw]
cand_name = [raw[0][2]]
for name in nam:
    if name not in cand_name:
        cand_name.append(name)
