#!/usr/bin/env python3
#
# Ty Koslowski, tykoslowski@g.ucla.edu
#
import sys
import os
from os import path
from functions import *

ROWS = 10
SEATS = 20
SEPARATOR = " "

# Main function
def main():
    # Argument checking
    if len(sys.argv) != 2: # Exit if number of arguments isn't 1
        eprint("Exited with 1: Correct usage is ./theater_oranizer [FILENAME]")
        sys.exit(1)
    if path.exists(sys.argv[1]) is not True: # Exit if file is invalid
        eprint("Exited with 1: File does not exist")
        sys.exit(1)
    
    # Gather data from file
    data_file = open(sys.argv[1], "r")
    lines = data_file.readlines()
    
    reservations = []
    for line in lines: # Grab reservation from each line
        reservations.append(line.split(SEPARATOR))
    for res in reservations: # Get rid of unnecessary chars and convert to ints
        res[0] = int(res[0][1:])
        res[1] = int(res[1].rstrip("\n"))

    # Create an output file
    output_file = open("result.txt", "w")

    # Create theater grid
    theater = [[0] * SEATS] * ROWS

    # For each reservation, reserve seats and mark buffer seats as occupied,
    # note the completed reservation in results.txt or note the reservation as 
    # unfulfilled if it is not possible
    for res in reservations:
        output_str = find_and_fill(res[1], theater)
        if output_str is not None:
            output_file.write("R" + str(res[0]).zfill(3) + " " + output_string + "\n")
        else:
            output_file.write("R" + str(res[0]).zfill(3) + " Unfulfilled\n")

    # Return path to output file
    return os.path.abspath(output_file.name)

# Main function call
if __name__ == "__main__":
    main()