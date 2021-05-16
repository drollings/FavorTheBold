grep FindByName $1.py | sort > out; grep FindByName ftb_$1.py | sort > outftb; joe out*
