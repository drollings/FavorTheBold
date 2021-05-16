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

ship = None

propertyInit = re.compile(r'^(\S*)\s\=\sApp\.(\S+)Property\_Create\(\"(.+)\"\)')
propertyRegister = re.compile(r'^App\.g\_kModelPropertyManager\.RegisterLocalTemplate')
propertyLoadSet = re.compile(r'^def LoadPropertySet')
property3DPos = re.compile(r'^\s*\S*\.SetPosition\(\s*(.*),\s*(.*),\s*(.*)\s*\)')

property2DPos = re.compile(r'^(\s*\S*).SetPosition2D\(\s*(.*),\s*(.*)\s*\)')
pSetIconPositionX = re.compile(r'^(\s*\S*).SetIconPositionX\(\s*(.*)\s*\)')
pSetIconPositionY = re.compile(r'^(\s*\S*).SetIconPositionY\(\s*(.*)\s*\)')
pSetIconAboveShip = re.compile(r'^(\s*\S*).SetIconAboveShip\(\s*(.*)\s*\)')
pSetIndicatorIconPositionX = re.compile(r'^(\s*\S*).SetIndicatorIconPositionX\(\s*(.*)\s*\)')
pSetIndicatorIconPositionY = re.compile(r'^(\s*\S*).SetIndicatorIconPositionY\(\s*(.*)\s*\)')


dIconNums = {
	# Forward beam
	'364' : [ -13, -20, 1, 0 ],
	'510' : [ -20, -10, 1, 0 ],

	# Port beam
	'361' : [ -29, -4, 20, 0 ],
	'508' : [ -16, -11, 20, 0 ],

	# Star beam
	'362' : [  12, -4, 20, 0 ],
	'509' : [  -6, -11, 20, 0 ],

	# Aft beam
	'363' : [ -14, 16, 1, 0 ],
	'511' : [ -23,  6, 1, 20 ],

	# Forward Port beam					# Forward Starboard beam
	'350' : [  -1, -8, 1, 0 ],			'330' : [ -57, -8, 1, 0 ],
	'502' : [   2, -4, 1, -10 ],		'501' : [ -49, -4, 1, -10 ],
	'506' : [   2,  0, 1, 5 ],			'505' : [ -49,  0, 1, 5 ],

	# Port beam							# Starboard beam
	'340' : [ -67,  12, 1, 0 ],			'360' : [  32,  12, 1, 0 ],
	'500' : [ -49,  16, 1, -10 ],		'503' : [  13,  16, 1, -10 ],
	'504' : [ -49,  20, 1, 5 ],			'507' : [  13,  20, 1, 5 ],

	# -28,0		0,0
	# -12,-26	24,-26


	# Complete arc
	# Dasher's all-around
	# kTextureHandle = kIcons.LoadIconTexture('Data/Icons/PhaserArcsWide.tga')
	# kIcons.SetIconLocation(550, kTextureHandle, 0, 0, 126, 70)
	# kIcons.SetIconLocation(555, kTextureHandle, 0, 0, 128, 64)

	# kTextureHandle = kIcons.LoadIconTexture('Data/Icons/PhaserFieldsWide.tga')
	# kIcons.SetIconLocation(551, kTextureHandle, 2, 2, 83, 59)
	# kIcons.SetIconLocation(552, kTextureHandle, 2, 60, 83, 54)

	# kIcons.SetIconLocation(556, kTextureHandle, 93, 24, 36, 25)
	# kIcons.SetIconLocation(557, kTextureHandle, 93, 24, 34, 22)

	'550' : [ -63, -35, 0, 0 ],		# 126 x 70
	'551' : [ -41, -30, 0, -10 ],	# 83 x 59
	'552' : [ -41, -27, 0, 5 ],		# 83 x 54

	'555' : [ -25, -15, 0, 0 ],		# 49 x 29
	'556' : [ -18, -13, 0, -10 ],	# 36 x 25
	'557' : [ -17, -11, 0, 5 ],		# 34 x 22


	# Pulse
	'365' : [ -2, -5, 1, 0 ],
	'512' : [ -20, -8, 1, 0 ],	# Port
	'513' : [ -20, -8, 1, 0 ],	# Starboard

	# Torpedo
	'370' : [  -2, -2, 1, 0 ]

}

pSetIconNum = re.compile(r'^(\s*\S*).SetIconNum\(\s*(.*)\s*\)')
pSetIndicatorIconNum = re.compile(r'^(\s*\S*).SetIndicatorIconNum\(\s*(.*)\s*\)')


propertyList = Registry.Registry()
# A regular expression for matching property

basicExpression = re.compile(r'^(\s*)(\S*)\.(.*)\(\s*(.*)\s*\)(.*)$')


def abs(i):
	if i < 0:
		i = i * -1
	return i

# An intended base class for properties in BCPropertyRecords.py
class BCProperty(FileRevisor.LineRevisor):
	def __init__(self, name):
		self.name = name
		BCPropertyRecords.propertyList.Register(self, name)

	def HardSet(lineIn):
		pass

	def __call__(self, lineIn, dictargs):
		matching = basicExpression.match(lineIn)
		if matching is None:
			return lineIn

		leading = matching.group(1)		# 0: Leading space
		item = matching.group(2)		# 1: Item
		dictargs['func'] = matching.group(3)		# 2: Function
		dictargs['args']  = matching.group(4)		# 3: Arguments
		trailing = matching.group(5)	# 4: Trailing characters

		str = self.ReviseMatch(dictargs)
		if str:		return '%s%s.%s(%s)%s' % (leading, item, dictargs['func'], str, trailing)
		else:		return lineIn

	def ReviseMatch(self, dict):
		str = None
		func, args, ship, pStats = dict['func'], dict['args'], dict['ship'], dict['pStats']
		if ship == None:
			raise 'ERROR:  No ship!'
		evalStr = 'str = self.%s(args, ship, pStats)' % (func)
		try:
			# print evalStr
			exec(evalStr)
			return str
		except AttributeError:
			return None

	def StaticLines(self, ship, name, linesOut):
		pass


class BCIconPlacer(FileRevisor.FileRevisor):
	def __init__(self):
		FileRevisor.FileRevisor.__init__(self, None)

		self.property = None
		self.propertyName = None
		self.propertyType = None
		self.propertyStats = None

	def Process(self, lines, linesOut):
		self.max3DExtent = 0
		self.shipProperties = {}
		self.powerRequired = {'red': 0, 'yellow': 0, 'green': 0 }
		FileRevisor.FileRevisor.Process(self, lines, linesOut)

	# This is run over every line in the file after it is loaded
	def ReviseLine(self, lineIn, linesOut):
		matching = propertyInit.match(lineIn)
		if matching:
			# This is a property being initialized
			# (self.property, self.propertyStats) = ship.GetProperty(matching.group(2), matching.group(3))
			self.propertyName = matching.group(1)
			self.propertyType = matching.group(2)
			self.AppendPropertyLine(lineIn)
			return

		matching = property3DPos.match(lineIn)
		if matching:
			for i in range(1, 4):
				j = abs(matching.group(i))
				if self.max3DExtent < j:
					self.max3DExtent = j
			self.AppendPropertyLine(lineIn)
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
			linesOut.append(lineIn + '\n\n')
			return

		# Regular line, just append
		if self.propertyName:
			if not (self.property and self.property.Exclude(lineIn)):
				self.AppendPropertyLine(lineIn)
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
		x = 0
		y = 0
		tmp = 0
		numFTorp = 0
		numATorp = 0
		for type in self.shipProperties.keys():
			typeList = self.shipProperties[type]
			for system in typeList._arrayList:
				prop = self.shipProperties[type][system][1]
				pLines = self.shipProperties[type][system][0]
				pStats = self.shipProperties[type][system][2]


				# Perform the actual 2D revision
				# First, we need to get the XYZ coordinates
				for lineIn in pLines:
					matching = property3DPos.match(lineIn)
					if matching:
						x = float(matching.group(1)) / (float(self.max3DExtent) + 0.001)
						y = float(matching.group(2)) / (float(self.max3DExtent) + 0.001)
						z = float(matching.group(3)) / (float(self.max3DExtent) + 0.001)
						# print system, "XYZ", x, y, z, "MAX", self.max3DExtent
						y = y + z * 0.7
						# print type
						x128 = 64 + 128 * x
						y128 = 64 + 128 * y * (z * 0.7)

						x64 = 80 * x * 0.7
						y64 = 72 * y * 0.7

						xSpaceOut = 20
						ySpaceOut = 25

						if type == 'Phaser':
							xSpaceOut = 5
							ySpaceOut = 10
							if abs(x64 - 80) < 10:
								xSpaceOut = 20
								ySpaceOut = 20

						if abs(x64) > abs(y64):
							x64 = x64 * 0.75
							if x64 > 0:
								x64 = x64 + xSpaceOut
							else:
								x64 = x64 - xSpaceOut
						else:
							if y64 > 0:
								y64 = y64 * 0.5 + ySpaceOut
							else:
								y64 = y64 * 0.2 - ySpaceOut * 1.1

						x64 = int(80 + x64)
						y64 = int(72 - y64)

						x64i = x64
						y64i = y64

					matching = pSetIconNum.match(lineIn)
					if matching:
						tmp = matching.group(2)
						if dIconNums.has_key(tmp):
							x64 = x64 + dIconNums[tmp][0]
							if x64 >= 80:
								x64 = x64 + dIconNums[tmp][2]
							else:
								x64 = x64 - dIconNums[tmp][2]
							y64 = y64 + dIconNums[tmp][1]
						continue

					matching = pSetIndicatorIconNum.match(lineIn)
					if matching:
						tmp = matching.group(2)
						if dIconNums.has_key(tmp):
							x64i = x64i + dIconNums[tmp][0]
							y64i = y64i + dIconNums[tmp][1] + dIconNums[tmp][3]
							y64 = y64 + dIconNums[tmp][3]
							if x64 >= 80:
								x64i = x64i + dIconNums[tmp][2]
							else:
								x64i = x64i - dIconNums[tmp][2]

						continue

				for lineIn in pLines:
					matching = property2DPos.match(lineIn)
					if matching:
						lineIn = "%s.SetPosition2D(%s, %s)" % (matching.group(1), x128, y128)
						linesOut.append( '%s\n' % (lineIn) )
						continue

					matching = pSetIconPositionX.match(lineIn)
					if matching:
						lineIn = "%s.SetIconPositionX(%s)" % (matching.group(1), x64)
						linesOut.append( '%s\n' % (lineIn) )
						# print x64, y64

						continue

					matching = pSetIconPositionY.match(lineIn)
					if matching:
						lineIn = "%s.SetIconPositionY(%s)" % (matching.group(1), y64)
						linesOut.append( '%s\n' % (lineIn) )
						continue

					matching = pSetIconAboveShip.match(lineIn)
					if matching:
						if z > 0:
							lineIn = "%s.SetIconAboveShip(%s)" % (matching.group(1), 1)
						else:
							lineIn = "%s.SetIconAboveShip(%s)" % (matching.group(1), 0)
							if abs(y64 - 72) < 20:
								y64 = y64 + 10
								y64i = y64i + 10
						linesOut.append( '%s\n' % (lineIn) )
						continue

					matching = pSetIndicatorIconPositionX.match(lineIn)
					if matching:
						lineIn = "%s.SetIndicatorIconPositionX(%s)" % (matching.group(1), x64i)
						linesOut.append( '%s\n' % (lineIn) )
						continue

					matching = pSetIndicatorIconPositionY.match(lineIn)
					if matching:
						lineIn = "%s.SetIndicatorIconPositionY(%s)" % (matching.group(1), y64i)
						linesOut.append( '%s\n' % (lineIn) )
						continue

					linesOut.append( '%s\n' % (lineIn) )

		self.shipProperties = {}



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

	# Set up the objects
	fRevisor = BCIconPlacer()

	# ship = BCShipRecords.shipList['defiant']
	# fRevisor('admiral_defiant.py')
	# raise ''

	# Parse the arguments
	pwd = os.getcwd()
	list = os.listdir(pwd)
	for file in list:
		s = string.split(file, '.')
		name = string.lower(s[0])
		detail = string.split(name, '_')
		author = detail[0]
		if len(detail) > 1:
			name = string.join(detail[1:])
		if s[-1] == 'py':
			if prefix != '' and s[0][:len(prefix)] != prefix:
				continue
			linesOut = []
			fRevisor(file)

	# InputLoop()
