import csv
import os

# creates variables
total_votes = 0
votes = 0
winner_votes = 0
candidate_votes = {}
candidates = []
candidate_voter_pct = 0
candidates_name = 0
results = ""
winner = ""

 # path to pull data from
csvpath = "Resources/election_data.csv"

# open and read from it as dictionary
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

# Loop for total number of votes and candidate names
    for row in csvreader:
        total_votes = total_votes + 1
        candidates_name = row["Candidate"]

        # loop for different names in the csv & create a dictionary with votes and names
        if candidates_name not in candidates:
                candidates.append(candidates_name)
                candidate_votes[candidates_name] = 1
            
        candidate_votes[candidates_name] = candidate_votes[candidates_name] + 1

# write the results to output file and write to that file

# write the results to output file then print it
output_file = "output.txt"
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    print ("Election Results")
    print ("-------------------------------")
    print ("")
    print (f'Total Votes:  {total_votes}')
    print ("")
    print ("-------------------------------")
    print ("")
    writer.writerow(["Election Results"])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow([])
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow([])   
    
    #For loop to compare candidates votes and get the winner then print out the results and winner to screen and output file
    for candidates_name in candidate_votes:
        votes = candidate_votes[candidates_name]
        candidate_voter_pct = float(votes)/float(total_votes)*100
        if (votes > winner_votes):
            winner_votes = votes
            winner = candidates_name
        Results = f'{candidates_name}: {candidate_voter_pct:.2f}% ({votes})'
        print(f'{candidates_name}: {candidate_voter_pct:.2f}% ({votes})')
        print ("")
        writer.writerow([Results])
        writer.writerow([])
    print ("-------------------------------")
    print ("")
    print (f'Winner: {winner}')
    print ("")
    print ("-------------------------------")
    writer.writerow(["-------------------------------"])
    writer.writerow([]) 
    writer.writerow(["Winner: " + winner]) 
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    
