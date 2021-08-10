#!/usr/bin/env python3
# NDE CHALLENGE #2 - LISTS

#Take the following list

dogs = ["1 dalmation", 5, "3 huskies", ["spot", "toto", "kujo", "dex", "fred"], "1 St. Bernard"]

#Print out the following sentences. The {} show you where the variables should go.

#I have {5} dogs. My {3 huskies} are {spot}, {kujo}, and {dex}. My {1 dalmation} is {toto} and my {1 St. Bernard} is {fred}.

print(f'I have {dogs[1]} dogs. My {dogs[2]} are {dogs[3][0]}, {dogs[3][2]}, and {dogs[3][3]}. My {dogs[0]} is {dogs[3][1]} and my {dogs[4]} is {dogs[3][4]}.')
