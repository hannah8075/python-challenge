#import packages
import os
import csv

#create file path for csv file
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#open and read csv file
with open(csvpath) as poll_data:

    csvreader = csv.reader(poll_data, delimiter=',')

    csv_header = next(csvreader)

    #define lists needed for analysis
    voter_id_list = []
    candidate_list=[]

    # Read each row of data after the header
    for row in csvreader:
        candidate_list.append(row[2])
    
#print(candidate_list[:10])

#find unique candidates; ['Khan', 'Correy', 'Li', "O'Tooley"]
def unique(lst): 
    unique_list = [] 
    for x in lst: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

unique_candidates = unique(candidate_list)

# COUNT VOTE
khan = 0
correy= 0
li = 0
otooley = 0
total_vote = 0

for name in candidate_list:
    if name == 'Khan':
        khan += 1
    elif name == 'Correy':
        correy += 1
    elif name == 'Li':
        li += 1
    elif name == "O'Tooley":
        otooley += 1

total_vote = khan + correy + li + otooley

# CALCULATE PERCENTAGE OF VOTES
khan_percent = (khan/total_vote) * 100
correy_percent = (correy/total_vote) * 100
li_percent = (li/total_vote) * 100
otooley_percent = (otooley/total_vote) * 100

# FIND WINNER
#print(unique_candidates)
all_count_list = [khan, correy, li, otooley]

votes_dict = dict(zip(unique_candidates, all_count_list))
#print(votes_dict) 

winner = max(votes_dict, key=votes_dict.get)
#print(winner)

# PRINT RESULTS
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_vote}")
print("------------------------")
print(f'Khan: {khan_percent:.3f}% ({khan})')
print(f'Correy: {correy_percent:.3f}% ({correy})')
print(f'Li: {li_percent:.3f}% ({li})')
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
print("------------------------")
print(f'Winner: {winner}')
print("------------------------")


# CREATE TEXT FILE IN ANALYSIS FOLDER

# Specify the file to write to
output_path = os.path.join("analysis", "PyPollResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_vote}")
    txtfile.write("\n")
    txtfile.write("------------------------")
    txtfile.write("\n")
    txtfile.write(f'Khan: {khan_percent:.3f}% ({khan})')
    txtfile.write("\n")
    txtfile.write(f'Correy: {correy_percent:.3f}% ({correy})')
    txtfile.write("\n")
    txtfile.write(f'Li: {li_percent:.3f}% ({li})')
    txtfile.write("\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
    txtfile.write("\n")
    txtfile.write("------------------------")
    txtfile.write("\n")
    txtfile.write(f'Winner: {winner}')
    txtfile.write("\n")
    txtfile.write("------------------------")