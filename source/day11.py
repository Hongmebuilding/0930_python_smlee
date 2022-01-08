"""
    Day1 File
    Version : 1.0
    Created : 2021.12.07
    Updated : 2021.12.07
    Author  : S.M.Lee
"""
import csv

print("Python")

s1 = 'We are studying Python'
s2 = '이것은 한글이죠'


f = open("../memo/test1.txt", "wt", encoding='cp949')  # directory 한 칸 올라갈때마다 ../
f.write(s1)
f.write('\n')
f.write(s2)
f.close()

f = open("../memo/test2.txt", "wt", encoding='utf-8')
f.write(s1)
f.write('\n')
f.write(s2)
f.close()


# rf = open("../memo/test1.txt", "rt", encoding='cp949')
rf = open("../memo/test2.txt", "rt", encoding='utf-8')
while True:
    readstr = rf.read(10)
    if readstr == '':
        break
    print(readstr)
rf.close()

rf = open("../memo/test2.txt", "rt", encoding='utf-8')
while True:
    readstr = rf.readline()
    if readstr == '':
        break
    print(readstr, end="")
rf.close()

print()
rf = open("../memo/test2.txt", "rt", encoding='utf-8')
readstr = rf.readlines(10000)  # readlines는 각 줄을 하나씩 list에 분리하여 반환
print(readstr)
for str in readstr:
    print(str, end="")

csvf = open("../memo/test3.csv","wt")
csv_writer = csv.writer(csvf, delimiter='|')
# csv_writer = csv.writer(csvf)
csv_writer.writerow([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
csvf.close()

csvf = open("../memo/test3.csv","rt")
csv_reader = csv.reader(csvf, delimiter='|')
# print(list(csv_reader))
for list in csv_reader:
    print(list)

from myutils import *

cprintTitle("Day1")