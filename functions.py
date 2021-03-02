#!/usr/bin/env python3
#
# Ty Koslowski, tykoslowski@g.ucla.edu
#
import sys

EMPTY = 0
OCCUPIED = 1
BUFFER = 2

ROWS = 10
SEATS = 20

# Used for printing to stderr easily
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Used to find an available grouping of seats, returns None if none found, or 
# a list of row, column pairs if found
def find(seats_req, theater_occ):
    ret_list = []
    # Check edges of every other row first
    row_index = ROWS - 1 # Start at back of theater
    while row_index >= 0:
        # Empty on left edge
        if theater_occ[row_index][0:seats_req] == [EMPTY] * seats_req:
            seat_index = 0
            while seat_index < seats_req:
                ret_list.append((row_index, seat_index))
                seat_index += 1
            return ret_list
        # Empty on right edge
        elif theater_occ[row_index][SEATS - seats_req:SEATS] == [EMPTY] * seats_req:
            seat_index = SEATS - seats_req
            while seat_index < SEATS:
                ret_list.append((row_index, seat_index))
                seat_index += 1
            return ret_list
        row_index -= 2
    
    # If no edges open, move to greedy algorithm
    row_index = ROWS - 1 # Start at back of theater again
    while row_index >= 0:
        
        seat_index = 0 # Iterate through all seats in each row (in amounts of seats_req)
        while seat_index + seats_req <= SEATS:
            continue_flag = False
            
            if theater_occ[row_index][seat_index:(seat_index + seats_req)] == [EMPTY] * seats_req:
                # Check above if not at row 0
                if row_index != 0:
                    for i in range(seat_index, seat_index + seats_req):
                        if theater_occ[row_index - 1][i] == OCCUPIED:
                            continue_flag = True
                            break
                    if continue_flag is True:
                        seat_index += 1
                        continue
                # Check below if not at last row
                if row_index != ROWS - 1:
                    for i in range(seat_index, seat_index + seats_req):
                        if theater_occ[row_index + 1][i] == OCCUPIED:
                            continue_flag = True
                            break
                    if continue_flag is True:
                        seat_index += 1
                        continue
                # Check left three spaces or amount of spaces 
                # between start of seating and left edge
                if seat_index != 0:
                    if seat_index < 3:
                        for i in range(0, seat_index):
                            if theater_occ[row_index][i] == OCCUPIED:
                                continue_flag = True
                                break
                    else:
                        for i in range(seat_index - 3, seat_index):
                            if theater_occ[row_index][i] == OCCUPIED:
                                continue_flag = True
                                break
                    if continue_flag is True:
                        seat_index += 1
                        continue
                # Check right three spaces or amount of spaces
                # between end of seating and right edge
                if seat_index + seats_req < SEATS:
                    if SEATS - (seat_index + seats_req) < 3:
                        for i in range(seat_index + seats_req, SEATS):
                            if theater_occ[row_index][i] == OCCUPIED:
                                continue_flag = True
                                break
                    else:
                        for i in range(seat_index + seats_req, seat_index + seats_req + 3):
                            if theater_occ[row_index][i] == OCCUPIED:
                                continue_flag = True
                                break
                    if continue_flag is True:
                        seat_index += 1
                        continue
                # Seats are valid, return row and seat values
                temp_seat_index = seat_index
                while temp_seat_index < seat_index + seats_req:
                    ret_list.append((row_index, temp_seat_index))
                    temp_seat_index += 1
                return ret_list
            
            seat_index += 1
        row_index -= 1
    
    # No valid seats, we have to return None
    return None

# Used to fill the theater seats/set buffer seats specified and to turn the 
# filled seats into a string for output processing, returns a string filled 
# in format "ROWSEAT,ROWSEAT,..." where ROW is a letter A-J and SEAT is a 
# number 1-20, and the number ROWSEATs is equal to the number of seats filled
def fill(seats_to_be_filled, theater_occ):
    return_str = ""
    
    # Loop through seats to be filled and fill them, 
    # fill buffer seats, then add to string
    for i in range(len(seats_to_be_filled)):
        
        row = seats_to_be_filled[i][0]
        seat = seats_to_be_filled[i][1]
        theater_occ[row][seat] = OCCUPIED
        
        # Buffer three to the left if this is first seat
        if i == 0:
            if seat < 3:
                for j in range(0, seat):
                    theater_occ[row][j] = BUFFER
            else:
                for j in range(seat - 3, seat):
                    theater_occ[row][j] = BUFFER
        # Buffer three to the right if this is last seat
        elif i == (len(seats_to_be_filled) - 1):
            if SEATS - (seat + 1) < 3:
                for j in range(seat + 1, SEATS):
                    theater_occ[row][j] = BUFFER
            else:
                for j in range(seat + 1, seat + 4):
                    theater_occ[row][j] = BUFFER
        # Buffer above if not in first row
        if row != 0:
            theater_occ[row - 1][seat] = BUFFER
        # Buffer below if not in last row
        elif row != ROWS - 1:
            theater_occ[row + 1][seat] = BUFFER
        # Format into substring and append to return string
        seat_str = chr(row + 65) + str(seat + 1)
        return_str += (seat_str + ",")

    return return_str[:-1] # Strip last comma off

# Used to find an available grouping of seats
# Will mark the seats and buffer seats surrounding it as occupied and return 
# a string of the seats occupied, or will do nothing and return None
def find_and_fill(seats_req, theater_occ):
    # Check if seats required in reasonable range
    if seats_req < 0 or seats_req > SEATS:
        return None
    
    # Find seats
    seats_to_be_filled = find(seats_req, theater_occ)
    
    if seats_to_be_filled is not None:
        # Fill seats and return string
        return fill(seats_to_be_filled, theater_occ)
    else: 
        # Fill no seats and return None
        return None