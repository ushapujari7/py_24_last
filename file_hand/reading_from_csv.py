import csv

f_o = open("first_csv_rows.csv")
csv_r = csv.reader(f_o, delimiter=",")
header = next(csv_r)
# line1 = next(csv_r)
# line2 = next(csv_r)

for row in csv_r:
    if row:
        if int(row[1]) >= 30:
            print(row)