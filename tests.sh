#!/bin/sh
#
# Testing script for Movie Theater Seating Challenge
#   zip file extractable
#   has expected files
#   make default
#   make clean
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
TESTINPREF="in"
TESTOUTPREF="out"
TESTINEXT=".txt"
TESTOUTEXT=".txt"

TESTNUM=7
OUTPUTFILE="result.txt"

EXIT_OK=0
EXIT_ERR=1

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

# check make
make
echo "... checking make"
if [ ! -f $SOLUTION ]
then
    echo Error with make
    errors=$((errors+1))
fi

# check make clean
echo "... checking make clean"
make clean
if [ -f $SOLUTION ]
then
    echo Error with make clean
    errors=$((errors+1))
fi

# make again and do tests
make

# test with bogus arguments
./$SOLUTION > /dev/null 2>STDERR
if [ ! -s STDERR ]
then
    echo "No error message for usage"
    errors=$((errors+1))
fi
rm -f STDERR

./$SOLUTION $TESTSDIR/"bogus"$TESTINEXT > /dev/null 2>STDERR
if [ ! -s STDERR ]
then
    echo "No error message for bad file"
    errors=$((errors+1))
fi
rm -f STDERR

./$SOLUTION $TESTSDIR/$TESTINPREF"1"$TESTINEXT \
            $TESTDIR/$TESTINPREF"2"$TESTINEXT > /dev/null 2>STDERR
if [ ! -s STDERR ]
then
    echo "No error message for too many files"
    errors=$((errors+1))
fi
rm -f STDERR

# run all tests on solution
echo -----------------
echo " Beginning tests"
echo -----------------

i=1
while [ $i -le $TESTNUM ]
do
    echo "... testing input $i"
    ./$SOLUTION ./$TESTSDIR/$TESTINPREF$i$TESTINEXT
    DIFF=$(diff ./$OUTPUTFILE ./$TESTSDIR/$TESTOUTPREF$i$TESTOUTEXT)
    if [ "$DIFF" != "" ]
    then
        echo "test $i failed"
        errors=$((errors+1))
    fi

    i=$((i+1))
done

# remove the test directory and its contents
echo Removing $TEMP
cd ..
rm -rf $TEMP

# remove other files created by the testing script
make clean

# display number of errors
echo ---------------------
echo " Number of errors: $errors"
echo ---------------------