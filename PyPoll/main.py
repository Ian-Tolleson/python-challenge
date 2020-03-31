import os
import csv

poll_csv = os.path.join('..', 'Resources', 'PyPoll_File.csv')

votes = []
candidates = []
candidate_votes = {}
Total_votes = 0

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        Total_votes += 1
        name = row[2]
        
        if name not in candidates:
            candidates.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] +=1



print("Election Results")
print("--------------------")
print(f'Total votes: {Total_votes}')
print("--------------------")
for key in candidate_votes:
    print(key," : ", round(candidate_votes[key]/Total_votes*100,2),"% (",candidate_votes[key],")")
print(candidates)


output_file = os.path.join("election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('-------------------------\n')
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {Total_votes}\n')
    datafile.write('-------------------------\n')



            
