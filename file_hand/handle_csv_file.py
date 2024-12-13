import csv

f = open("first_csv.csv", "w")
csv_w = csv.writer(f)
# csv_w.writerow(["Name", "Class", "Address", "Email", "PhoneNo"])
# csv_w.writerow(["venkey", "python", "xxxx", "venkey_phonenum@gmail.com", "xxxxxxxx"])
# csv_w.writerow(["venkey", "python", "xxxx", "venkey_phonenum@gmail.com", "xxxxxxxx"])
data = [
    ["Name", "Age", "City", "Occupation"],  # Header
    ["Alice", 30, "New York", "Engineer"],
    ["Bob", 28, "San Francisco", "Designer"],
    ["Charlie", 25, "Chicago", "Data Scientist"],
    ["Diana", 32, "Los Angeles", "Manager"]
]
csv_w.writerow(data[0])
for row in data[1:]:
    if row[1] >= 30:
        csv_w.writerow(row)


fff = open("first_csv_rows.csv", "w")
csv_ww = csv.writer(fff)
# csv_w.writerow(["Name", "Class", "Address", "Email", "PhoneNo"])
# csv_w.writerow(["venkey", "python", "xxxx", "venkey_phonenum@gmail.com", "xxxxxxxx"])
# csv_w.writerow(["venkey", "python", "xxxx", "venkey_phonenum@gmail.com", "xxxxxxxx"])
data_r = [
    ["Name", "Age", "City", "Occupation"],  # Header
    ["Alice", 30, "New York", "Engineer"],
    ["Bob", 28, "San Francisco", "Designer"],
    ["Charlie", 25, "Chicago", "Data Scientist"],
    ["Diana", 32, "Los Angeles", "Manager"]
]
csv_ww.writerows(data_r)
