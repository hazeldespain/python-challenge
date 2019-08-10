#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv


# In[4]:


#connect to csv file - already in same folder
budget_csv = os.path.join("budget_data.csv")
budget_csv


# In[73]:


#csv reader
with open(budget_csv, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #exclude header
    csv_header = next(csvreader)
    #define variables
    total = 0
    months = 0
    change = 0
    change_list = []
    date_list = []
    #loop through csv for total, months, and delta
    for row in csvreader:
        row[1] = int(row[1])
        total = total + int(row[1])
        months = months + 1
        #conditional to get delta 
        if row[1]>= (row[1]+1):
            change = (row[1])
            date = row[0]
        elif row[1]<= (row[1]+1):
            change = (row[1]+1)
            date = row[0]
        #append to list so you can use functions
        change_list.append(change)
        date_list.append(date)
                
    #calculate increase/decrease/average delta
    greatest_incr = max(change_list)
    greatest_decr = min(change_list)
    average_pl = sum(change_list)/len(change_list)
    a1 = change_list.index(greatest_incr)
    a2 = change_list.index(greatest_decr)
    date_g = date_list[a1]
    date_d = date_list[a2]
    
    
    print("""text
Financial Analysis
_____________________________""")
    print(f"Total Months: {months}")
    print(f"Total:{total}")
    print(f"Average Change:{average_pl}")
    print(f"Greatest Increase in Profits:{date_g}, ${greatest_incr}")
    print(f"Greatest Decrease in Profits:{date_d}, ${(greatest_decr)}")
    
    


# In[ ]:




