#!/usr/bin/env python

# P81 -> Dolph is 1.469

import FileRevisor
import re


# Revisor functions
class rf_Scale:
	def __init__(self, scaleBy):
		self.scaleBy = float(scaleBy)
	def __call__(self, x):
		return float(x) * self.scaleBy

class rf_Scale3:
	def __init__(self, scaleBy):
		self.scaleBy = float(scaleBy)
		self.exp = re.compile(r'^\s*(.*)\s*\,\s*(.*)\s*\,\s*(.*)')
	def __call__(self, arg):
		matching = self.exp.match(arg)
		if matching is None:
			return arg
		x = (float(matching.group(1)) * self.scaleBy)
		y = (float(matching.group(2)) * self.scaleBy)
		z = (float(matching.group(3)) * self.scaleBy)
		return '%f, %f, %f' % (x, y, z)


# Command-line utility use
if __name__ == '__main__':
	import sys

	# Parse the arguments
	try:
		scale, ships = sys.argv[1], sys.argv[2:]
	except IndexError:
		print "Usage:  Rescale.py <scale> <ship> [<ship>...]\n"
		sys.exit()

	# Setup for the line revisor
	scaler = rf_Scale(scale)
	scaler3 = rf_Scale3(scale)
	functions = {
		'SetPosition': scaler3,
		'SetWidth': scaler,
		'SetLength': scaler,
		'SetRadius': scaler
	}

	basicExpression = re.compile(r'^(\s*)(\S*)\.(.*)\(\s*(.*)\s*\)(.*)$')

	# Set up the objects
	lRevisor = FileRevisor.LineRevisor(functions, basicExpression)
	fRevisor = FileRevisor.FileRevisor(lRevisor)

	for i in ships:
		linesOut = []
		fRevisor(i)

