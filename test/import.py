import csv

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        return(row)
        #print(" ".join(row))
        #print(row)


csv_path = 'D:\DOCS\python3\ook1.csv'
with open(csv_path) as f_obj:
    set1 = set(csv_reader(f_obj))

#csv_path2 = 'D:\DOCS\python3\ook2.csv'
#with open(csv_path2) as f_obj2:
  #  set2 = set(csv_reader(f_obj2))

print(set1.intersection(set2))
