#Import module

import csv


# Variables

Votes = []
Candidates = []
County = []
Charles =[]
Diana =[]
Raymon =[]
Percent_of_Charles = []
Percent_of_Diana = []
Percent_of_Raymon = []

Votes_for_Charles = 0
Votes_for_Diana =0
Votes_for_Raymon =0


# Open the path to read the file

csvpath = ('Resources/election_data.csv')
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip Header

        csvheader = next(csvreader)
              
        for row in csvreader:
            Votes.append(row[0])
            County.append(row[1])
            Candidates.append(row[2])
            total_votes = (len(Votes))
               
        for candidate in Candidates:
            if candidate == "Charles Casper Stockham":
                Charles.append(Candidates)
                Votes_for_Charles = len(Charles)
        
            elif candidate == "Diana DeGette":
                Diana.append(Candidates) 
                Votes_for_Diana = len(Diana) 
            
            else:
                Raymon.append(Candidates)
                Votes_for_Raymon = len(Raymon)
        
        # Calculate percentage votes for each candidate 

        Percent_of_Charles = round(((Votes_for_Charles/total_votes)*100),3) 
        Percent_of_Diana = round(((Votes_for_Diana/total_votes)*100),3)
        Percent_of_Raymon = round(((Votes_for_Raymon/total_votes)*100), 3)


        # Winner
        if Percent_of_Charles > max(Percent_of_Diana,Percent_of_Raymon):
            winner = "Charles Casper Stockham"  
        
        elif Percent_of_Diana > max(Percent_of_Raymon, Percent_of_Charles):
            winner = "Diana DeGette"      

        else:    
            winner = "Raymon Anthony Doane" 

  # Print results to terminal

        election_results = f'''
                Election Results
                -----------------------------
                Total Votes: {str(total_votes)}
                -----------------------------
                Charles Casper Stockham: {str(Percent_of_Charles)}% ({str(Votes_for_Charles)})
                Diana DeGette: {str(Percent_of_Diana)}% ({str(Votes_for_Diana)})
                Raymon Anthony Doane: {str(Percent_of_Raymon)}% ({str(Votes_for_Raymon)})
                -------------------------------- 
                Winner: {winner} 
                '''
        print(election_results)
                

        # Export results to txt file.
with open("Analysis/election_data.txt", "w") as election_analysis:
    election_analysis.write(election_results)