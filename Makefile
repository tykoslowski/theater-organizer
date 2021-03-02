# Ty Koslowski, tykoslowski@g.ucla.edu
# 
# Makefile for creation, testing, and distribution of theater_organizer 
# solution.
#
default: theater_organizer

theater_organizer: theater_organizer.py run.sh clean
	ln -T ./run.sh ./theater_organizer

clean:
	rm -f *.zip theater_organizer 

dist: theater_organizer
	zip movie_theater_seating_challenge-Ty_Koslowski.zip theater_organizer.py functions.py run.sh tests.sh Makefile README

tests: dist
	./tests.sh