import Foundation
import nt


def ClearPYCs(dir):
	files = nt.listdir(dir)

	for f in files:
		if f[0] != '_' and f[-4:] == '.pyc':
			nt.unlink(dir + '\\' + f)

###############################################################################
## Get File Names with extension from path sFolderPath
###############################################################################
class Log:
	def __init__(self):
		self.buf = []
	def __call__(self, str):
		self.buf.append(str + '\n')
	def Dump(self, file):
		file.writelines(self.buf)

class StatLogger(Log):
	def __init__(self):
		Log.__init__(self)
		self.stats = {}
		self.fields = {}


	def Add(self, ship, sProperty, num):
		self.fields[sProperty] = 1
		if not self.stats.has_key(ship.name):
			self.stats[ship.name] = {}

		if not self.stats[ship.name].has_key(sProperty):
			self.stats[ship.name][sProperty] = (num, 1)
			return

		prevNum = self.stats[ship.name][sProperty][0]
		self.stats[ship.name][sProperty] = (prevNum + num, 1)


	def Average(self, ship, sProperty, num):
		self.fields[sProperty] = 1
		if not self.stats.has_key(ship.name):
			self.stats[ship.name] = {}

		if not self.stats[ship.name].has_key(sProperty):
			self.stats[ship.name][sProperty] = (num, 1)
			return

		prevNum = self.stats[ship.name][sProperty][0]
		prevCount = self.stats[ship.name][sProperty][1]
		num = (prevCount * prevNum + num) / float(prevCount + 1)
		self.stats[ship.name][sProperty] = (num, prevCount + 1)


	def Dump(self, file):
		lSortedShips = self.stats.keys()
		lSortedProps = self.fields.keys()
		# lSortedShips.sort()
		# lSortedProps.sort()

		self('Ship,' + string.join(lSortedProps, ','))

		for i in lSortedShips:
			lShipLine = [ i ]
			for j in lSortedProps:
				try:
					lShipLine.append(str(self.stats[i][j][0]))
				except:
					lShipLine.append('0')

			self(string.join(lShipLine, ','))

		Log.Dump(self, file)

Foundation.Log = Log
Foundation.StatLogger = StatLogger

def Dump(obj, sName):
	lsOut = []

	l = obj.__dict__.keys()
	l.sort()

	for i in l:
		try:
			sOut = str(i) + ':' + str(obj.__dict__[i].keys())
		except:
			sOut = str(i) + ':' + str(obj.__dict__[i])
		lsOut.append(sOut)

	WriteOut(lsOut, sName)


def WriteOut(lsOut, sName = 'DebugOutput'):
	file = nt.open('scripts\\Custom\\' + sName, nt.O_WRONLY|nt.O_TRUNC|nt.O_CREAT)
	for i in lsOut:
		nt.write(file, str(i) + '\n')
	nt.close(file)


def Test(sName):
	m = Foundation.BuildGameMode()
	Dump(m, sName)

Foundation.WriteOut = WriteOut
Foundation.Dump = Dump
Foundation.Test = Test

# ClearPYCs('scripts\\Custom\\FTB\\Tech')
ClearPYCs('scripts\\Custom\\Autoload')
ClearPYCs('scripts\\Custom\\FTB\\ships')
# ClearPYCs('scripts\\Custom\\FTB\\ships\\hp')
# ClearPYCs('scripts\\Custom\\FTB\\ships\\setup')
# ClearPYCs('scripts\\Custom\\FTB\\Projectiles')
