# Import Modules
import operator
import os
import csv

# Set Variables
total_votes = 0
candidates= []
poll = []
candidate_votes = []
candidate_percent = []
winner = ""


# Set Path For File
election_csv = os.path.join('.','Resources', 'election_data.csv')

# Open & Read CSV File
with open(election_csv, 'r') as csvfile:
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read The Header
    header = next(csvreader)

    # Iterate through every row
    for row in csvreader:
        # The total number of votes cast
        total_votes += 1
        candidates.append(row[2])
        
# A complete list of candidates who received votes
candidates = sorted(candidates)

# Revised list of candidates
for i in range(total_votes):
    if candidates[i-1] != candidates[i]:
        poll.append(candidates[i])

# Calculate total number of votes each candidate won
for j in range(len(poll)):
    vote_count = candidates.count(poll[j])
    candidate_votes.append(vote_count)

# The percentage of votes each candidate won
for k in range(len(candidate_votes)):
    percent = ("{0:.3f}".format((candidate_votes[k]/total_votes)*100))
    candidate_percent.append(percent)
    
# The winner of the election based on popular vote.
popular_vote = candidate_votes.index(max(candidate_votes))
winner = poll[popular_vote]
poll_results = zip(poll, candidate_percent, candidate_votes)
poll_results = sorted(poll_results, key = operator.itemgetter(2), reverse = True)

# Print the Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {(total_votes)}")
print("-------------------------")
for row in poll_results:
    print(f"{row[0]}: {str(row[1])}% ({str(row[2])})")
print("-------------------------")
print(f"Winner: {(winner)}")
print("-------------------------")

# Output file
output_file = os.path.join('.', 'Resources', 'analysis.text')

# Open output file to write to
with open(output_file, 'w',) as txtfile:

# Write the Analysis
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {(total_votes)}\n")
    txtfile.write("-------------------------\n")
    for row in poll_results:
        txtfile.write(f"{row[0]}: {str(row[1])}% ({str(row[2])})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {(winner)}\n")
    txtfile.write("-------------------------\n")
        

