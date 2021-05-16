all : ShipRevisor.csv

clean :
	rm -f new/* *.csv *.log

ShipRevisor.csv : ../../../Tools/ShipClasses.py ../../../Tools/BCPropertyRecords.py ../../../Tools/BCShipRecords.py
	python ../../../Tools/ShipRevisor.py

icons :
	python ../../../Tools/IconPlacer.py

install :
	mv -f new/* .

scale :
	python ../../../Tools/

order :
	python ../../../Tools/ShipOrderRevisor.py