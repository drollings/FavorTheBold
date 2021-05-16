import whrandom



class SystemPlacer:
	def __init__(self, diameterRoot, distX = 5, distY = 5):
		self.diameter = diameterRoot * diameterRoot
		extraX = self.diameter * distX
		extraY = self.diameter * distY
		extraZ = whrandom.random() * self.diameter * 2
		if whrandom.random() > 0.5:
			extraZ = extraZ * -1.0

		self.planeX = whrandom.random() * diameterRoot
		self.planeX = self.planeX * self.planeX + extraX
		if whrandom.random() > 0.5:
			self.planeX = self.planeX * -1.0

		self.planeY = self.diameter - self.planeX + extraY
		if whrandom.random() > 0.5:
			self.planeY = self.planeY * -1.0

		self.planeZ = whrandom.random()
		self.planeZ = self.diameter * 2 * self.planeZ
		if whrandom.random() > 0.5:
			self.planeZ = self.planeZ * -1.0

	def __call__(self, orbitRoot = 0):
		if orbitRoot:
			orbit = orbitRoot * orbitRoot
			self.planeX
			self.planeY
			X = orbitRoot * whrandom.random()
			X = X * X + self.planeX

			Y = orbitRoot * whrandom.random()
			Y = Y * Y + self.planeY

			Z = whrandom.random()
			Z = self.diameter * 2 * Z
			if Z % 2:
				Z = Z * -1.0

			return (X, Y, Z)
		else:
			return (self.planeX, self.planeY, self.planeZ)


placer = SystemPlacer(90.39)

print placer()
print placer(155.29)
