#!/bin/sh
#
# Testing script for Movie Theater Seating Challenge
#   extracted zip file
#   has README
#   make default
#   make dist
#   make clean
#   make default, success, creates program
#   unrecognized parameters
#   error for nonexistent input file
#   check expected outputs
#
SOLUTION="theater_organizer"
ZIPNAME="movie_theater_seating_challenge-Ty_Koslowski.zip"
README="README"
MAKEFILE="Makefile"

EXIT_OK=0
EXIT_ERR=1

TIMEOUT=1

errors=0

# read the zip into a test directory
TEMP=`pwd`/"theater_organizer_test"
if [ -d $TEMP ]
then
    echo Deleting old $TEMP
    rm -rf $TEMP
fi
mkdir $TEMP
unzip $ZIPNAME -d $TEMP
cd $TEMP

# check for 


# remove the test directory and its contents
echo Removing $TEMP
rm -rf $TEMP