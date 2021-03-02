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

# Used to find an available grouping of seats, returns None if none found, or 
# a list of row, column pairs if found
def find(seats_req, theater_occ):
    # Check edges of every other row first
    row_index = len(theater_occ) - 1 # Start at back of theater
    while row_index >= 0:
        if theater_occ[row_index][0] == EMPTY:
            seat_index = 1
            while seat_index <= seats_req
        row_index -= 1

# Used to fill the theater seats specified and to turn the filled seats into 
# a string for output processing, returns a list of seats filled in format 
# ROWSEAT where ROW is a letter A-J and SEAT is a number 1-20
def fill(seats_to_be_filled, theater_occ):
    return 

# Used to find an available grouping of seats
# Will mark the seats and buffer seats surrounding it as occupied and return 
# a string of the seats occupied, or will do nothing and return None
def find_and_fill(seats_req, theater_occ):
    seats_to_be_filled = find(seats_req, theater_occ)
    if seats_to_be_filled is not None:
        seats_filled = fill(seats_to_be_filled, theater_occ)
        return_str = ""
        for seat in seats_filled:
            return_str += (seat + ",")
        return_str = return_str[:len(return_str) - 1] # Strip last comma off
        return return_str
    return None