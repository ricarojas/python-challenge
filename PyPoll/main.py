import os

import csv
#import default dict to allow for analysis
from collections import defaultdict
#locate path to data
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open("output_pypoll.txt", "w") as output_pypoll:
    with open(csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        print(csv_reader.line_num)

    #ensure that VS is able to read data and has the correct datasheet
        csv_header = next(csv_reader)
        #print(f"CSV Header: {csv_header}")

        #row_count = sum(1 for row in csv_reader)
        total_votes = 0
        candidates = []
        d = defaultdict(int)
    #loop through data, adding candidates to dictioanry and counting their votes
        for row in csv_reader:
            total_votes += 1
            d[row[2]] +=1
            if row[2] not in candidates:
                candidates.append(row[2])
    #print results
        print(candidates)
        print(d)
        Charles_total = d["Charles Casper Stockham"]
        Diana_total = d["Diana DeGette"]
        Raymon_total = d["Raymon Anthony Doane"]

        Charles_per = (Charles_total / total_votes)
        Diana_per = (Diana_total / total_votes)
        Raymon_per = (Raymon_total / total_votes)

        Charles_per_rounded = round(Charles_per * 100, 3)
        Diana_per_rounded = round(Diana_per * 100, 3)
        Raymon_per_rounded = round(Raymon_per * 100, 3)
        line = "{} testing\n".format(Charles_per_rounded)

    #print Header
        output_pypoll.write (f"Election Results" + "\n")
        output_pypoll.write (f"----------------------------------------------------" + "\n")
    #print Total Votes
        output_pypoll.write ("Total votes: "+ str(total_votes)+ " \n")
        output_pypoll.write (f"----------------------------------------------------"+ "\n")
    #print candidates, percentages and votes using dictionary key and formatting
        
        line = "Charles Casper Stockam : {}% ({})\n".format(Charles_per_rounded, Charles_total)
        output_pypoll.write (line)
        line = "Diana DeGette: {}% ({})\n".format(Diana_per_rounded, Diana_total)
        output_pypoll.write (line)
        line = "Raymon Anthony Doane: {}% ({})\n".format(Raymon_per_rounded, Raymon_total)
        output_pypoll.write (line)
        #output_pypoll.write (f"Charles Casper Stockam :" + str(Charles_per_rounded) +str(Charles_total) + "\n")
        #print(f"Diana DeGette: {Diana_per:.3%}", Diana_total)
        #print(f"Raymon Anthony Doane: {Raymon_per:.3%}", Raymon_total)
        output_pypoll.write (f"----------------------------------------------------" + "\n")
    
    #print the winner by overall votes, using max function
    output_pypoll.write (f"Winner: "+ (max(d, key=d.get)) + "\n")
    output_pypoll.write (f"----------------------------------------------------")

    output_pypoll.close()