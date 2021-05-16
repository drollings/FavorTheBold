#!/usr/bin/env python

import string
import re
import os


# A generic regular expression meant to match strings like "thing.Function(1.0)"
# simpleExpression = re.compile(r'^(\s*)(\S*)\.(.*)\((\s*\d+.*)\)(.*)$')


# A base class for
class LineRevisor:
	def __init__(self, dict, expr):
		self.dict = dict
		self.expression = expr

	def __call__(self, lineIn, dictargs):
		matching = self.expression.match(lineIn)
		if matching is None:
			return lineIn

		leading = matching.group(1)		# 0: Leading space
		item = matching.group(2)		# 1: Item
		dictargs['func'] = matching.group(3)		# 2: Function
		dictargs['args'] = matching.group(4)		# 3: Arguments
		trailing = matching.group(5)	# 4: Trailing characters

		str = self.ReviseMatch(dictargs)
		if str:		return '%s%s.%s(%s)%s' % (leading, item, dictargs['func'], str, trailing)
		else:		return lineIn

	def ReviseMatch(self, dictargs):
		func, args = dictargs['func'], dictargs['args']
		if self.dict.has_key(func):
			return self.dict[func](args)
		return None

	def Exclude(self, lineIn):
		pass


# Goes through a whole hardpoints file passing each line to a LineRevisor
class FileRevisor:
	def __init__(self, defaultLineRevisor):
		self.defaultLineRevisor = defaultLineRevisor

	def __call__(self, fileName):
		print 'Revising', fileName
		file = open (fileName)
		lines = file.readlines()
		file.close()

		linesOut = []
		self.Process(lines, linesOut)

		try:				os.mkdir('new')
		except OSError:		pass

		fileName = os.path.join('new', fileName)
		file = open(fileName, 'w')
		file.writelines(linesOut)
		file.close()

	def Process(self, lines, linesOut):
		for i in lines:
			i = string.rstrip(i)
			self.ReviseLine(i, linesOut)

	def ReviseLine(self, line, linesOut):
		linesOut.append(self.defaultLineRevisor(line, {}) + '\n')

