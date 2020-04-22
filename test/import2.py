import csv
csv1 = 'D:\DOCS\python3\ook1.csv'
csv2 = 'D:\DOCS\python3\ook2.csv'
with open(csv1) as f1:
    reader = csv.reader(f1)
    set1 = (list(reader))
set2 = (str(set1))
set3 = (set2.strip("'["))
set4 = (set3.strip("]'"))
set5 = set(set4.split("'], ['"))

with open(csv2) as f2:
    reader2 = csv.reader(f2)
    set12 = (list(reader2))
set22 = (str(set12))
set32 = (set22.strip("'["))
set42 = (set32.strip("]'"))
set52 = set(set42.split("'], ['"))
set6 = sorted(list(set5.intersection(set52)))
for i in range((len(set6))):
    print(set6[i])


