#!/usr/bin/env python
# Dasher42's ship revisor for Bridge Commander


import FileRevisor
import re
import string
import Registry

# Global variables
# raceList = Registry.Registry()
# propertyList = Registry.Registry()
# shipList = Registry.Registry()

import BCShipRecords
import BCPropertyRecords

propertyInit = re.compile(r'^(\S*)\s\=\sApp\.(\S+)Property\_Create\(\"(.+)\"\)')
propertyRegister = re.compile(r'^App\.g\_kModelPropertyManager\.RegisterLocalTemplate')
propertyLoadSet = re.compile(r'^def LoadPropertySet')
powerReq = re.compile(r'^\s*\S*\.SetNormalPowerPerSecond\(\s*(.*)\s*\)')
radius = re.compile(r'^\s*\S*\.SetRadius\(\s*(.*)\s*\)')

propertyList = Registry.Registry()
# A regular expression for matching property
basicExpression = re.compile(r'^(\s*)(\S*)\.(.*)\(\s*(.*)\s*\)(.*)$')



class Log:
	def __init__(self):
		self.buf = []
	def __call__(self, str):
		self.buf.append(str + '\n')
	def Dump(self, file):
		file.writelines(self.buf)

log = Log()


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


hardSet = [
	re.compile(r'\.SetPosition'),
	re.compile(r'\.SetPosition2D'),
	re.compile(r'\.SetWeaponID'),
	re.compile(r'\.SetGroups'),
	re.compile(r'\.SetIconNum'),
	re.compile(r'\.SetIconPositionX'),
	re.compile(r'\.SetIconPositionY'),
	re.compile(r'\.SetIconAboveShip'),
	re.compile(r' = App\.'),
	re.compile(r'\.SetXYZ'),
	re.compile(r'\.SetDirection'),
	re.compile(r'\.SetRight'),
	re.compile(r'\.SetOrientation'),
	re.compile(r'\.SetArcWidthAngles'),
	re.compile(r'\.SetArcHeightAngles'),
	re.compile(r'\.SetWidth'),
	re.compile(r'\.SetLength')
]


# An intended base class for properties in BCPropertyRecords.py
class BCProperty(FileRevisor.LineRevisor):
	def __init__(self, name):
		self.name = name
		self.expression = basicExpression
		BCPropertyRecords.propertyList.Register(self, name)

	# def HardSet(lineIn):
	# 	for i in hardSet:
	# 		if i.match(lineIn):
	# 			return 1

	def ReviseMatch(self, dict):
		str = None
		func, args, ship, pStats = dict['func'], dict['args'], dict['ship'], dict['pStats']
		if ship == None:
			raise 'ERROR:  No ship!'
		evalStr = 'str = self.%s(args, ship, pStats)' % (func)
		try:
			# print args, evalStr
			try:	exec(evalStr)
			except SyntaxError:
				raise SyntaxError, evalStr
			return str
		except AttributeError:
			return None

	def StaticLines(self, ship, name, linesOut):
		pass


class BCShipRevisor(FileRevisor.FileRevisor):
	def __init__(self):
		FileRevisor.FileRevisor.__init__(self, None)

		self.property = None
		self.propertyName = None
		self.propertyType = None
		self.propertyStats = None
		self.numWeaponSystems = 0

	def Process(self, lines, linesOut):
		self.shipProperties = {}
		self.powerRequired = {'red': 0, 'yellow': 0, 'green': 0 }
		FileRevisor.FileRevisor.Process(self, lines, linesOut)

	# This is run over every line in the file after it is loaded
	def ReviseLine(self, lineIn, linesOut):
		matching = propertyInit.match(lineIn)
		if matching:
			# This is a property being initialized
			(self.property, self.propertyStats) = ship.GetProperty(matching.group(2), matching.group(3))
			self.propertyName = matching.group(1)
			self.propertyType = matching.group(2)
			self.AppendPropertyLine(lineIn)

			dict = self.propertyStats
			if self.propertyType == 'Phaser' or self.propertyType == 'PulseWeapon':
				terawattRatio = 1.0
				if dict is not None and dict.has_key('terawatts'):
					terawattRatio = dict['terawatts']

				ship.chargeCount = ship.chargeCount + terawattRatio
				log(string.join((ship.name, self.propertyType, str(ship.chargeCount)), ', '))
			elif self.propertyType == 'WeaponSystem' and self.propertyName[:7] != 'Tractor':
				ship.numWeaponSystems = ship.numWeaponSystems + 1
			return

		matching = propertyRegister.match(lineIn)
		if matching:
			# Property definition is done
			if self.property:
				staticLines = []
				self.property.StaticLines(ship, self.propertyName, staticLines)
				for i in staticLines:
					self.AppendPropertyLine(i)
			self.AppendPropertyLine(lineIn)
			return

		matching = propertyLoadSet.match(lineIn)
		if matching:
			# The properties are done, it's loading them to the set
			self.property = None
			self.propertyName = None
			self.propertyType = None
			self.properyStats = None
			self.WriteProperties(ship, linesOut)
			linesOut.append(lineIn + '\n')
			return

		# Regular line, just append
		if self.propertyName:
			if not (self.property and self.property.Exclude(lineIn)):
				if self.property and self.property.RelyStaticLines():
					matching = powerReq.match(lineIn)
					if self.propertyType == 'TorpedoSystem' and matching:
						ship.stats['torpedopower'] = matching.group(1)
				else:
					self.AppendPropertyLine(lineIn)
				matching = radius.match(lineIn)
				if matching:
					size = matching.group(1)
					ship.subsystems[self.propertyName] = {'size': size }
					if size > ship.stats['sizeIndex']:
						ship.stats['sizeIndex'] = size
		else:
			linesOut.append(lineIn + '\n')

	def AppendPropertyLine(self, lineIn):
		type = self.propertyType
		name = self.propertyName
		try:
			self.shipProperties[type][name][0].append(lineIn)
		except KeyError:
			if not self.shipProperties.has_key(type):
				self.shipProperties[type] = Registry.Registry()
			self.shipProperties[type].Register( ([ lineIn ], self.property, self.propertyStats), name)


	def WriteProperties(self, ship, linesOut):
		# We do this here so that the stock weapon system is guaranteed to come last
		ship.SetProperty('WeaponSystem', '.*', BCPropertyRecords.propertyList['WeaponSystem'])
		ship.SetupPowerLevels()

		for type in self.shipProperties.keys():
			typeList = self.shipProperties[type]
			for system in typeList._arrayList:
				prop = self.shipProperties[type][system][1]
				pLines = self.shipProperties[type][system][0]
				pStats = self.shipProperties[type][system][2]
				if prop:
					pStats['shipSize'] = float(ship.stats['sizeIndex'])

					if ship.subsystems.has_key(system):
						size = ship.subsystems[system]['size']
						pStats['sizeRatio'] = float(size) / float(ship.stats['sizeIndex'])
						pStats['size'] = float(size)
						# print system, size


					for i in pLines:
						out = prop(i, { 'ship': ship, 'pStats': pStats } )
						if out:
							linesOut.append( '%s\n' % (out) )
				else:
					for i in pLines:
						linesOut.append( '%s\n' % (i) )


def InputLoop():
	while 1:
		input = string.strip(raw_input(' > '))
		if not len(input):
			continue
		exec input




# Command-line utility use
if __name__ == '__main__':
	import sys
	import os

	try:
		prefix = sys.argv[1]
	except:
		prefix = ''

	print prefix

	# Set up the objects
	fRevisor = BCShipRevisor()

	# Parse the arguments
	pwd = os.getcwd()
	list = os.listdir(pwd)
	for file in list:
		s = string.split(string.lower(file), '.')
		if s[-1] == 'py':
			if prefix != '' and s[0][:len(prefix)] != prefix:
				continue
			name = string.lower(s[0])
			detail = string.split(name, '_')
			if len(detail) > 1:
				name = string.join(detail[1:])

			try:
				ship = BCShipRecords.shipList[name]
			except KeyError:
				print 'No ship listing for', file, name
				continue

			linesOut = []
			fRevisor(file)

	f = open('ShipRevisor.log', 'w+')
	log.Dump(f)
	f.close()

	f = open('ShipRevisor.csv', 'w')
	BCPropertyRecords.statLog.Dump(f)
	f.close()