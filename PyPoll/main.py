import os
import csv

csv_path = os.path.join('election_data.csv')

with open(csv_path) as pollCSV:
    csvreader = csv.reader(pollCSV, delimiter=',')
    csv_header = next(pollCSV)
    voter_ids = []
    countys = []
    candidates = []
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        voter_ids.append(voter_id)
        countys.append(county)
        candidates.append(candidate)
    total_votes = len(voter_ids)
    #print(total_votes)
    candidate_names = set(candidates)
    #print (candidate_names)
    OTooleyCount = candidates.count("O'Tooley")
    #print(OTooleyCount)
    CorreyCount = candidates.count('Correy')
    KhanCount = candidates.count('Khan')
    LiCount = candidates.count('Li')
    OTooleyPercent = OTooleyCount / total_votes *100
    #print(OTooleyPercent)
    CorreyPercent = CorreyCount / total_votes *100
    KhanPercent = KhanCount / total_votes *100
    LiPercent = LiCount / total_votes *100
    final_count = [OTooleyCount, CorreyCount, KhanCount, LiCount]
    winner_list = ["O'Tooley", 'Correy', 'Khan', 'Li']
    #print(final_count)
    winnerindex = final_count.index(max(final_count))
    #print(winnerindex)
    winner = winner_list[winnerindex]
    #print(winner)

print('Election Results')
print('----------------------')
print(f'Total Votes: {total_votes}')
print('----------------------')
print(f'Khan: %{round(KhanPercent, 3)} ({KhanCount})')
print(f'Correy: %{round(CorreyPercent, 3)} ({CorreyCount})')
print(f'Li: %{round(LiPercent, 3)} ({LiCount})')
print(f"O'Tooley: %{round(OTooleyPercent, 3)} ({OTooleyCount})")
print('----------------------')
print(f'Winner: {winner}')
print('----------------------')
