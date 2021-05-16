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

ship = None

propertyInit = re.compile(r'^(\S*)\s\=\sApp\.(\S+)Property\_Create\(\"(.+)\"\)')
propertyRegister = re.compile(r'^App\.g\_kModelPropertyManager\.RegisterLocalTemplate')
propertyLoadSet = re.compile(r'^def LoadPropertySet')

propertyList = Registry.Registry()
# A regular expression for matching property

basicExpression = re.compile(r'^(\s*)(\S*)\.(.*)\(\s*(.*)\s*\)(.*)$')


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
		BCPropertyRecords.propertyList.Register(self, name)

	def HardSet(lineIn):
		for i in hardSet:
			if i.match(lineIn):
				return 1

	# def Process(backLog, linesOut, ship):
	# 	for i in backLog:
	# 		linesOut.append(self(ship, i) + '\n')


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


class BCShipRevisor(FileRevisor.FileRevisor):
	def __init__(self):
		FileRevisor.FileRevisor.__init__(self, None)

		self.property = None
		self.propertyName = None
		self.propertyType = None
		self.shipProperties = {}
		self.propertyStats = None
		self.powerRequired = 0

	def Process(self, lines, linesOut):
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
			if self.property:
				self.powerRequired = self.powerRequired + self.property.SetNormalPowerPerSecond('', ship, self.propertyStats)
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
		for type in self.shipProperties.keys():
			typeList = self.shipProperties[type]
			for system in typeList._arrayList:
				prop = self.shipProperties[type][system][1]
				pLines = self.shipProperties[type][system][0]
				pStats = self.shipProperties[type][system][2]
				for i in pLines:
					linesOut.append( '%s\n' % (i) )
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

	# Set up the objects
	fRevisor = BCShipRevisor()

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
			try:
				ship = BCShipRecords.shipList[name]
			except KeyError:
				print 'No ship listing for', file, name
				continue

			linesOut = []
			fRevisor(file)

	# InputLoop()
