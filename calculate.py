from rouge import Rouge 
import csv
import os
currentpath = os.getcwd()
print(currentpath)
i=0
f = open('영어.tsv', 'r', encoding='cp949')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)

f1 = open('save.tsv','w',encoding='cp949')

while i <495: #max 496
    rouge = Rouge()
    scores = rouge.get_scores(r[i][0], r[i][1])
    #print(scores)

    f1.write(str(i+1))
    f1.write(":")
    f1.writelines(str(scores))
    f1.write("\n")
    i+=1
