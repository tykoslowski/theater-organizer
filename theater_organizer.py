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


    # Create theater grid
    theater = [[0] * SEATS] * ROWS
    for row in theater:
        print(row)

# Main function call
if __name__ == "__main__":
    main()