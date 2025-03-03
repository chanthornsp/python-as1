import csv

file_name = 'data.csv'
try:
    with open(file_name,mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Age','City'])
        writer.writerow(['John',25,'New York'])
        writer.writerow(['Jane',22,'San Francisco'])
except PermissionError as e:
    print(e)