from rouge import Rouge 
import csv
import os
currentpath = os.getcwd()
print(currentpath)
i=1
f = open('summay.tsv', 'r', encoding='cp949')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)


while i <496:
    rouge = Rouge()
    scores = rouge.get_scores(r[i][0], r[i][1])
    print(scores)
