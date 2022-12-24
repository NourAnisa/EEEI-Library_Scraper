from DatabaseAPI import *
from IEEEDatabaseAPI import *

# -------------------------------------------------
# ENTER YOUR SEARCH TERM HERE
# -------------------------------------------------
SEARCH_TERM = input("Masukkan Kata kunci pencarian Anda: ")

# API Objects
ieee = IEEEDatabaseAPI()

# Runs the Query and Returns a Dictionary Containing the Results
# We can modify this function to return whatever we want
result = ieee.run_query(SEARCH_TERM)

# Writes a CSV Containing the Results
output_file = open(SEARCH_TERM + "_result.csv", "w", encoding="utf-8")

if result != None:
    for key in result:
        output_file.write(key + "," + str(result[key]))
        output_file.write('\n')
    output_file.close()

print("Job Complete")
        




