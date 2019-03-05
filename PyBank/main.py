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
    #print(len(dates))
    moneysum = sum(moneys)
    #print(moneysum)
    avgmoneys = sum(moneys)/len(moneys)
    #print(avgmoneys)
    changes = [(y - x) for (x, y) in zip(moneys[:-1], moneys[1:])]
    avgchange = sum(changes)/len(changes)
    #print(avgchange)
    max_profit = max(changes)
    #print (max_profit)
    min_profit = min(changes)
    #print (min_profit)
    #print(changes.index(max_profit))
    #print(changes.index(min_profit))
    maxind = changes.index(max_profit)
    #print(dates[maxind+1])
    minind = changes.index(min_profit)
    #print(dates[minind+1])

print('Financial Analysis')
print('--------------------------')
print(f'Total Months: {len(dates)}')
print(f'Total: ${moneysum}')
print(f'Average Change: ${round(avgchange, 2)}')
print(f'Greatest Increase in Profits: {dates[maxind+1]} (${max_profit})')
print(f'Greatest Dcrease in Profits: {dates[minind+1]} (${min_profit})')

#file = open("output.txt", "w")
#print('Financial Analysis', file='output.txt')
#print('--------------------------', file='output.txt')
#print(f'Total Months: {len(dates)}', file='output.txt')
#print(f'Total: ${moneysum}', file='output.txt')
#print(f'Average Change: ${avgchange}', file='output.txt')
#print(f'Greatest Increase in Profits: {dates[maxind+1]} (${max_profit})', file='output.txt')
#print(f'Greatest Dcrease in Profits: {dates[minind+1]} (${min_profit})', file='output.txt')
#file.close()

