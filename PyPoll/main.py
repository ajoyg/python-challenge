import os
import csv


csvpath = os.path.join('Resources','election_data.csv')
candidates=set()
candidates_votes=[]
candidate_total_votes={}
#open the election_data.csv file
with open(csvpath, encoding='utf8') as electiondata:
    electionreader = csv.reader(electiondata, delimiter=',')
    next(electionreader) # skip the title
    # get the distinct candidates and the candidates vote
    for voterrow in electionreader:
        candidates_votes.append((voterrow[2]))
        candidates.add(voterrow[2])

# get the total votes for each candidate and put it a dictionary
for this_candidate in candidates:
    candidate_total_votes[this_candidate]=candidates_votes.count(this_candidate)

# write the results into the analysis file and print it on the terminal
analysisoutput = os.path.join('analysis','ElectionResults.txt')
with open(analysisoutput,'w') as analysiswriter:
    analysiswriter.write("```text\n")
    print("```text")
    analysiswriter.write("Election Results\n")
    print("Election Results")
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write(f"Total Votes: {len(candidates_votes)}\n")
    print(f"Total Votes: {len(candidates_votes)}") 
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    for candidate, total_votes in sorted(candidate_total_votes.items()):
        analysiswriter.write(f'{candidate}: {"{0:.3f}%".format((total_votes*100)/len(candidates_votes))} {"({0:.0f})".format(total_votes)}\n')
        print(f'{candidate}: {"{0:.3f}%".format((total_votes*100)/len(candidates_votes))} {"({0:.0f})".format(total_votes)}')
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write(f'Winner: {max(candidate_total_votes, key=lambda key:candidate_total_votes[key])}\n')
    print(f'Winner: {max(candidate_total_votes, key=lambda key:candidate_total_votes[key])}')
    analysiswriter.write("-------------------------\n")
    print("-------------------------")
    analysiswriter.write("```\n")
    print("```")
