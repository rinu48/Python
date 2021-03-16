import csv
with open('student2.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("Student Name & Dept")
 print("---------------------------------")
 for row in data:
   print(row['s_name'], row['s_dept'])