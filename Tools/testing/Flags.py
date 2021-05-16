class Flags:
	"""A generic long bitvector.  Accessors maintain integrity of the >32 bit size.
	"""
	def __init__(self, val = 0):
		self._value = long(val)

	def __repr__(self):
		return str(self._value)

	def __long__(self):
		return self._value

	def __int__(self):
		return self._value

	def List(self, registry):
		out = []
		for i in range(0, len(registry)):
			if self[i]:
				out.append(registry[i])
		return string.join(out, ', ');

	def __iand__(self, other):
		return self._value & long(other)

	def __ixor__(self, other):
		return self._value ^ long(other)

	def __ior__(self, other):
		return self._value | long(other)

	def Toggle(self, num):
		if long(num) >= 4096:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value ^ long(1 << long(num))

	def Set(self, num):
		if long(num) >= 4096:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value | long(1 << long(num))

	def UnSet(self, num):
		if long(num) >= 4096:	# Manual limits imposed because extremely high precisions cause slowdown
			raise IndexError	# and could be a sign of buggy code.
		self._value = self._value & long(1 << long(num))

	def __getitem__(self, i):
		return self._value & long(1 << long(i))
	def __setitem__(self, i, val):
		if val:
			self._value = self._value | long(1 << long(i))
		else:
			self._value = self._value & long(1 << long(i))
		return self._value


# import Foundation
# Foundation.Flags = Flags