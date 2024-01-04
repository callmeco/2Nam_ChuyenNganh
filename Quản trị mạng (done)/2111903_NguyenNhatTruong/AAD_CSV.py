import csv
import AAD_CLIENT


with open('sample.csv', mode='r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        username = row['username']
        employee_id = row['employee_id']
        official_name = row['official_name']
        print(username, employee_id, official_name)
        AAD_CLIENT.create_user(username, employee_id, official_name, active=True)
        #AAD_CLIENT.manage_user(username, mode='delete')