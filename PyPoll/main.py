import csv
import sys 
poll_csv = 'election_data.csv'

def print_and_file(statement, file_pointer) :
    print (statement)
    file_pointer.write(str(statement) + "\n")

with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Prompt the user for what wrestler they would like to search for
    next(csvreader)

    # Loop through the data
    total_votes = 0
    total_candidates  = {}

    for row in csvreader:
        total_votes += 1 
        if row[2] not in total_candidates :
            total_candidates[row[2]] = 1 
        else :
            total_candidates[row[2]] += 1 

lead_votes = 0
winner = ""
with open('my_file.txt', 'w' )as f :
    #sys.stdout = f
    print_and_file ('Election Results ',f)
    print_and_file("-------------------------",f)
    print_and_file(str("Total Votes : " + str(total_votes)),f)
    for key, value in total_candidates.items() :
        round_val = format(float(value * 100/total_votes  ), ".2f" )
        print_and_file (str( str(key) + "  " +str (value) + " " + \
                        round_val + "%" ),f)
        if value > lead_votes :
            lead_votes = value
            winner = key
    print_and_file ('-----------------------',f)
    print_and_file(str('winner:' + str(winner)),f )
    f.close()