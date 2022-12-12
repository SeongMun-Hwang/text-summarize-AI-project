# -*- coding: utf-8 -*-
import pandas as pd #pip install pandas
from rouge import Rouge #pip install rouge
import os

currentpath = os.getcwd()
print(currentpath)
i=1

f = open('save.tsv', 'w', encoding='cp949') #저장할 파일 이름

filename='summary.xlsx' #요약문 담긴 엑셀 이름
df=pd.read_excel(filename,engine='openpyxl')

original=df['original'] #[1행 1열 문자] -> 1행 2열부터 1차원 배열로 저장
model=df['model'] #[행 2열 문자] ->  2행 2열부터 1차원 배열로 저장ㅍ

while i <496: #max 496 //라우지 계산해서 save.tsv로 저장
    rouge = Rouge()
    scores = rouge.get_scores(original[i], model[i])
    #print(scores)

    f.write(str(i+1))
    f.write(":")
    f.writelines(str(scores))
    f.write("\n")
    i+=1