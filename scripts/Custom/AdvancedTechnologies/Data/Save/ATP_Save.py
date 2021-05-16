import nt

FALSE	= 0
TRUE	= 1
FILE	= 0
INDENT	= 1

dfile   = 0
indent  = 0

def open_save_file(sfilename="Save_00.py",sfilepath="scripts\\Custom\\AdvancedTechnologies\\Data\\Save"):
	global dfile
	global indent
	close_save_file()
	sfullpath = sfilepath + "\\" +sfilename
	dfile = nt.open(sfullpath,nt.O_WRONLY|nt.O_TRUNC|nt.O_CREAT)
	indent = 0

def write_save_file(s,rel_indent=0):
	global dfile
	global indent

	if not dfile:
		return
	indent = indent + rel_indent
	if indent < 0:
		indent = 0

	nt.write(dfile,"\t"*indent+s+"\n")

def write_vector(s,V):
	write_save_file(s+" = App.TGPoint3()")
	write_save_file("s.SetX("+str(V.GetX())+")")
	write_save_file("s.SetY("+str(V.GetY())+")")
	write_save_file("s.SetZ("+str(V.GetZ())+")")

def close_save_file():
	global dfile
	global indent
	if dfile:
		nt.close(dfile)
		dfile = 0
		indent = 0
