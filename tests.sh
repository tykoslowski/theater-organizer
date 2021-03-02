#!/bin/sh
#
# Testing script for Movie Theater Seating Challenge
#   zip file extractable
#   has expected files
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
SOURCEFILE="theater_organizer.py"
FUNCTIONFILE="functions.py"
RUNFILE="run.sh"
TESTSFILE="tests.sh"
TESTSDIR="tests"

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

# check for README
if [ ! -f $README ]
then
    echo README not found
    errors=$((errors+1))
fi

# check for Makefile
if [ ! -f $MAKEFILE ]
then
    echo Makefile not found
    errors=$((errors+1))
fi

# check for main source file
if [ ! -f $SOURCEFILE ]
then
    echo "Main source file not found"
    errors=$((errors+1))
fi

# check for functions file
if [ ! -f $FUNCTIONFILE ]
then
    echo Function file not found
    errors=$((errors+1))
fi

# check for run shell script
if [ ! -f $RUNFILE ]
then
    echo Run shell script not found
    errors=$((errors+1))
fi

# check for testing shell script (this script!)
if [ ! -f $TESTSFILE ]
then
    echo Tests shell script not found
    errors=$((errors+1))
fi

# check for tests directory
if [ ! -d $TESTSDIR ]
then
    echo Tests folder not found
    errors=$((errors+1))
fi

# remove the test directory and its contents
echo Removing $TEMP
cd ..
rm -rf $TEMP

# display number of errors
echo ---------------------
echo " Number of errors: $errors"
echo ---------------------