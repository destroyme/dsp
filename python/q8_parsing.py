# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import sys

data = {}

with open('football.csv', newline='') as csvfile:
    football = csv.reader(csvfile, delimiter=',')
    next(football)
    for row in football:
        data[row[0]] = {'goals' : int(row[5]),
                        'goals_allowed' : int(row[6])}

best = ('', sys.maxsize)
for k, v in data.items():
    # print(k, v)
    diff = abs(v['goals'] - v['goals_allowed'])
    if diff < best[1]:
        best = (k, diff)

print(best[0], 'has the smallest difference between goals scored and goals allowed.')
    