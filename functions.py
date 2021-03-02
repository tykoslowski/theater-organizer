#!/usr/bin/env python3
#
# Ty Koslowski, tykoslowski@g.ucla.edu
#
import sys

EMPTY = 0
OCCUPIED = 1
BUFFER = 2

# Used for printing to stderr easily
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Used to find an available grouping of seats
# Will mark the seats and buffer seats surrounding it as occupied and return 
# a string of the seats occupied, or will do nothing and return None
def find_and_fill(seats_req, theater_occ):
    return None