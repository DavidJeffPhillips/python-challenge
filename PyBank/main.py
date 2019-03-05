import os
import csv

csv_path = os.path.join('budget_data.csv')

with open(csv_path) as bankCSV:
    csvreader = csv.reader(bankCSV, delimiter=',')
    csv_header = next(bankCSV)
    dates=[]
    moneys=[]
    for row in csvreader:
        date=row[0]
        money=row[1]
        dates.append(date)
        moneys.append(int(money))
    print(len(dates))
    moneysum = sum(moneys)
    print(moneysum)
