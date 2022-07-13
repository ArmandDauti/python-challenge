# import modules
import csv
import os

# Set path to csv file
fileLoad = os.path.join("Resources", "election_data.csv")

# File to hold the output 
outputFile = os.path.join("analysis", "analysis.txt")

# Variables
totalVotes = 0     
candidateList = [] 
candidateVotes = {} 
winningCount = 0 
winningCandidate = ""

# read CSV file
with open(fileLoad) as Election_Data:
    csvreader = csv.reader(Election_Data)

    # Skip header
    header = next(csvreader)

    firstRow = next(csvreader)
    totalVotes += 1

    for row in csvreader:
        totalVotes += 1

        if row[2] not in candidateList:
            candidateList.append(row[2])
            candidateVotes[row[2]] = 1
        
        else:
            candidateVotes[row[2]] += 1  
            voteOutput = ""

    for candidate in candidateVotes:
        votes = candidateVotes.get(candidate)
        votePct = (float(votes) / float(totalVotes)) * 100.00
        voteOutput += f"{candidate}: {votePct:,.3f}% ({votes:,})\n"

        # compare the votes to the winning count
        if votes > winningCount:
            winningCount = votes
            winningCandidate = candidate

    winningCandidateOutput = f"Winner: {winningCandidate}\n"


    # Print in terminal
    output = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes:,}\n"
        f"-------------------------\n"
        f"{voteOutput}"
        f"-------------------------\n"
        f"{winningCandidateOutput}"
        f"-------------------------\n"
    )

print(output)

# Export the text file
with open(outputFile, "w") as textFile:
    textFile.write(output)