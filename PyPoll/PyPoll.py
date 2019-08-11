#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import os


# In[ ]:


poll_csv = os.path.join("election_data.csv")


# In[ ]:


#csv reader
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #exclude header
    csv_header = next(csvreader)
    #define variables
    total = 0
    candidates = []
    #loop through csv for total votes, list of candidates, % of votes 
        #per candidate, total number of votes per candidate, winner
    for row in csvreader:
        # The total number of votes cast
        total = (total + 1)
        print(total)
        # A complete list of candidates who received votes
        from collections import Counter
        candidates = [row[2]]
        # The total number of votes each candidate won
        Khan_votes = print(candidates.count("Khan")) 
        Correy_votes = print(candidates.count("Correy"))
        Li_votes = print(candidates.count("Li"))
        OTooley_votes = print(candidates.count("O'Tooley"))
        print(f"Khan Total Votes:{Khan_votes}")
        print(f"Correy Total Votes:{Correy_votes}")
        print(f"Li Total Votes:{Li_votes}")
        print(f"O'Tooley Total Votes:{OTooley_votes}")
        #The total number of votes each candidate won
        Khan_percent = Khan_votes/total
        Correy_percent = Correy_votes/total
        Li_percent = Li_votes/total
        OTooley_percent = OTooley_votes/total
        print(f"Khan Percent of Votes:{Khan_percent}")
        print(f"Correy Percent of Votes:{Correy_percent}")
        print(f"Li Percent of Votes:{Li_percent}")
        print(f"O'Tooley Percent of Votes:{OTooley_percent}")
        #The winner of the election based on popular vote.
        winner_result = ({Khan_percent, Correy_percent, Li_percent, OTooley_percent}).max
        print(winner_result)
        
    
    print("""text
Election Results
__________________""")
    (f" Total Votes:{total}")
print("""
______________________
""")
    (f" Khan:{Khan_percent}%,{(Khan_votes)}")
    (f" Correy:{Correy_percent}%,{(Correy_votes)}")
    (f" Li:{Li_percent}%,{(Li_votes)}")
    (f" O'Tooley:{OTooley_percent}%,{(OTooley_votes)}")
print("""
______________________
""")
    (f"Winner{winner_result}")
print("""
______________________
""")


# In[ ]:


#not working...
#output into a text file
output_path = os.path.join("poll_output.csv")

with open('election_data.csv', 'w', newline='') as csvfile:
    text_file= csv.writer(csvfile)
    text_file.writerows(csvreader)

