#Dependencies
import csv

#files to load and output
file_to_load = "C:\\Users\\larab\\OneDrive\\Documents\\GitHub\\election_data.csv"
file_to_output = "C:\\Users\\larab\\OneDrive\\Documents\\GitHub\\payroll_analysis.txt"

#total vote counter
total_votes = 0

#candidate options and vote counters
candidate_options = []    #list of available candidates
candidate_votes = {}      #key= candidate name, values= number of votes

#winning candidates and winning count tracker
winning_candidate = ""    #string-name of winner
winning_count = 0         #number of votes

#read in csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    #for each row
    for row in reader:
       
        #add to the total vote count
        total_votes = total_votes +1

        #extract the candidate name from each row
        candidate_name = row["Candidate"]

        #if the candidate doesn't match any existing candidate..
        if candidate_name not in candidate_options:

            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            #and begin tracking that  candidate's voter count
            candidate_votes[candidate_name]=0

        #then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1

    #Determine the winner by looping through the counts
    for candidate in candidate_votes:

        #retrieve the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) *100

        #determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    
#format the results
    result=f'''
    Election Results
    ------------------------

    Total Votes: {total_votes}
    ------------------------
    Charles Casper Stockham: {round(100*candidate_votes['Charles Casper Stockham']/total_votes,3) }% ({candidate_votes['Charles Casper Stockham']})
    Diana DeGette: {round(100*candidate_votes['Diana DeGette']/total_votes,3) }% ({candidate_votes['Diana DeGette']})
    Raymon Anthony Doane: {round(100*candidate_votes['Raymon Anthony Doane']/total_votes,3) }% ({candidate_votes['Raymon Anthony Doane']})
    ------------------------
    Winner: {winning_candidate}
    ------------------------
    '''
    print(result)

#print the results and export the data to our text file
with open(file_to_output, "w") as f:
    f.write(result)
    








