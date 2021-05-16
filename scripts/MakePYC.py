import nt
import compileall

def Go(sPath = None):
	if not sPath:
		sPath = nt.getcwd()

	# Remove any old .pyc's.
	nt.path.walk(sPath, DeleteFiles, ".pyc")

	# Compile any .py files.
	print "Compiling all .py's"
	compileall.compile_dir(sPath)

	# Remove any .py's.
	nt.path.walk(sPath, DeleteFiles, ".py")

def DeleteFiles(sExtension, sDir, lsFiles):
	print "Removing %s's from %s" % (sExtension, sDir)

	# Remove any files that end in the specified extension.
	for sFile in lsFiles:
		sFile = nt.path.join(sDir, sFile)

		# Make sure the file isn't read-only.
		nt.chmod(sFile, 0x0999)

		try:
			if sFile[-len(sExtension):] == sExtension:
				nt.remove(sFile)
		except IOError:
			print "Unable to remove file: %s" % sFile

if __name__ == "__main__":
	import sys
	print "MakePYC: %s" % sys.argv
	try:
		sPath = sys.argv[1]
	except IndexError:
		sPath = None

	Go(sPath)
