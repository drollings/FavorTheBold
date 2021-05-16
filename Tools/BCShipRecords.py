import re
import Registry
import BCPropertyRecords
import string

propertyList = BCPropertyRecords.propertyList
raceList = Registry.Registry()
shipList = Registry.Registry()


# Class definitions
class Race:
	def __init__(self, name):
		self.name = name
		raceList.Register(self, name)
		self.engineSound = "'%s Engines'" % (self.name)


# Some miscellaneous math functions
def WeightedAverage(num, tally, count = 2):
	return (num + float(tally * (count - 1))) / count

def DegradedArc(x, rate = 2, minimum = 4):
	if x <= 1:
		return x
	d = x - (x * (rate * x / 100))
	return max([d, x / minimum])


class Ship:
	def __init__(self, name):
		self.name = name
		self.race = None
		self.stats = {'sensorIndex': 1000, 'maneuverThrustIndex': 1000, 'sizeIndex': 1000, }
		self.properties = {}
		self.shields = {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 }
		# self.shieldCharge = {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 }
		self.chargeCount = 0.0
		self.numWeaponSystems = 0
		self.powerRequired = {'red': 0, 'yellow': 0, 'green': 0 }
		# self.powerPercent = ('red', 0.9514)
		self.powerPercent = ('red', 0.55)
		self.battery = 250
		self.bakBattery = 80
		self.conduit = 1.2
		self.bakConduit = 0.4
		self.sFiringString = ''
		self.lTorpTypes = [ ['FTBPhotonTorpedo', 100] ]
		self.subsystems = {}

		shipList.Register(self, name)
		self.SetProperty('Engine', '.*', propertyList['Engine'])
		self.SetProperty('WarpEngine', '.*', propertyList['WarpEngine'])
		self.SetProperty('Hull', '.*', propertyList['HullElement'])
		self.SetProperty('Hull', '.*Hull.*', propertyList['Hull'])
		self.SetProperty('Hull', '.*Bridge.*', propertyList['Bridge'])
		self.SetProperty('Hull', '.*Battle Bridge.*', propertyList['HullElement'])
		self.SetProperty('Ship', '.*', propertyList['Ship'])
		self.SetProperty('Sensor', '.*', propertyList['Sensor'])
		self.SetProperty('Power', '.*', propertyList['Power'])
		self.SetProperty('ImpulseEngine', '.*', propertyList['ImpulseEngine'])
		self.SetProperty('Shield', '.*', propertyList['Shield'])
		self.SetProperty('TractorBeam', '.*', propertyList['TractorBeam'])
		self.SetProperty('RepairSubsystem', '.*', propertyList['RepairSystem'])
		# self.SetProperty('Torpedo', '.*', propertyList['TorpedoSystem'])
		self.SetProperty('TorpedoSystem', '.*', propertyList['TorpedoSystem'])
		self.SetProperty('WeaponSystem', '.*', propertyList['PhaserSystem'])
		self.SetProperty('WeaponSystem', '.*Tractor.*', propertyList['TractorWeaponSystem'])
		self.SetProperty('CloakingSubsystem', '.*', propertyList['CloakingDevice'])



	def Mass(self):
		# d = float(int(self.stats['mass'] / 42708)) + 1
		d = float(int(self.stats['mass'] / 10250)) + 1
		BCPropertyRecords.statLog.Average(self, 'Mass', d)
		return d

	def RotationalInertia(self):
		# d = float(int(self.stats['mass'] / 342))
		d = float(int(self.stats['mass'] / 20)) + 1
		BCPropertyRecords.statLog.Average(self, 'Rotational Inertia', d)
		return d

	def RepairIndex(self):
		return 1.0

	def StructureIndex(self):
		return (self.stats['hullIndex'] + 1000.0) / 2000.0

 	def SensorIndex(self):
		return self.stats['sensorIndex'] / 1000.0

	def SizeIndex(self):
		l = self.stats['length']
		w = self.stats['width']
		h = self.stats['height']
		s = max(max(l, w), h)
		return s / 641.0

	def MassIndex(self):
		return self.stats['mass'] / 5125000.0

	def ManeuverAccelIndex(self):
		# i = DegradedArc(self.stats['maneuverIndex'] / 1000.0, 3.15, 2.75)
		i = DegradedArc(self.stats['maneuverIndex'] / 1000.0, 15.0, 4.0)
		# if i > 1.0:
		# 	i = WeightedAverage(i, 1, 2.75)
		# print self.stats['maneuverThrustIndex'], 'Accel', i
		return i

	def ManeuverMaxIndex(self):
		i = DegradedArc(self.stats['maneuverIndex'] / 1000.0, 11, 6)
		# if i > 1.0:
		# 	i = i + WeightedAverage(i, 1, 3)
		# print self.stats['maneuverIndex'], 'MAX', i
		return i

	def AccelIndex(self):
		# return WeightedAverage(self.stats['maneuverThrustIndex'] / 1000.0, 0.75, 4)
		return WeightedAverage(self.stats['maneuverThrustIndex'] / 1000.0, 0.3, 4)

	def SpeedMaxIndex(self):
		i = DegradedArc(self.stats['maxVelocity'] / 400.0, 15.0, 3.0)
		return WeightedAverage(i, 1.0, 1.25)

	def EngineSound(self):
		return "'Federation Engines'"

	def GetProperty(self, type, name):
		expr = re.compile(name)
		if self.properties.has_key(type):
			for i in self.properties[type]:
				if i[0].match(name):
					# print 'Looked up type', type, 'with name', name, i[1]
					return (i[1], i[2])
		return (None, None)

	def SetProperty(self, type, expression, property, dict = {}):
		if self.properties.has_key(type):
			self.properties[type].insert(0, ( re.compile(expression), property, dict) )
		else:
			self.properties[type] = [ ( re.compile(expression), property, dict) ]

	def HullIndex(self):
		# A 1.5x integer adjustment of the strength of hull structures
		# return (self.stats['hullIndex'] / 1000) * self.MassIndex() * 2.0
		return (self.stats['hullIndex'] + 1000.0) / 2000.0

	# The actual overall strength of the hull
	def HullStrength(self):
		# return self.HullIndex() * WeightedAverage(1.0, self.MassIndex(), 3.0)
		# return self.HullIndex() * WeightedAverage(self.MassIndex(), 1.0, 3.0)
		# return self.HullIndex() * WeightedAverage(self.MassIndex(), 1.0, 2.0)
		# return (self.MassIndex() * 3.0 + self.HullIndex() * 2.0) / 5.0
		return self.MassIndex() * self.HullIndex()

	def SetShields(self, dict):
		tally = 0.0
		for i in dict.values():
			tally = tally + 1
		try:
			charge = self.stats['shieldIndex']
		except KeyError:
			charge = 0
		# average = (54000.0 * charge / 1000) / tally
		average = (75000.0 * charge / 1000) / tally
		for i in dict.keys():
			self.shields[i] = average * dict[i]

	def SetShieldCharge(self, dict):
		tally = 0.0
		for i in dict.values():
			tally = tally + 1
		try:
			charge = self.stats['shieldChargeIndex']
		except KeyError:
			try:
				charge = self.stats['shieldIndex']
			except KeyError:
				charge = 0
		average = (72.0 * charge / 1000) / tally

		sizeFactor = 1 / WeightedAverage(self.MassIndex(), 1, 2)
		average = average * sizeFactor

		self.shieldCharge = {}

		for i in dict.keys():
			self.shieldCharge[i] = average * dict[i]

	def GetShields(self, dir):
		dir = string.lower(dir)
		d = self.shields[dir]
		BCPropertyRecords.statLog.Average(self, 'Shield', d)
		return d


	def GetShieldRecharge(self, dir):
		dir = string.lower(dir)
		return self.shieldCharge[dir]

	def RepairPower(self):
		return 0.1

	def RepairRate(self):
		return 50.0 * self.HullStrength()  # * (self.stats['crew'] / 1000.0)

	def SensorPower(self):
		# return 800.0 * ((self.SensorIndex() + 2.0) / 3.0)
		return 1200.0 * ((self.SensorIndex() + 2.0) / 3.0)

	def EnginePower(self):
		return 3000.0 * (self.ManeuverAccelIndex() + 1.5) / 2.5	 * (self.MassIndex() + 1.0) / 2.0

	def ShieldPower(self):
		return 2500.0 * self.stats['shieldIndex'] / 1000.0

	def WeaponPower(self):
		retval = float(int(self.stats['terawatts'] / 15.0 + 0.5))
		if self.stats.has_key('torpedopower'):
			retval += float(self.stats['torpedopower'])
		return retval

	def SetupPowerLevels(self):
		# print self.SensorPower(), self.RepairPower(), self.EnginePower(), self.ShieldPower(), self.WeaponPower()
		self.powerRequired['green'] = int(self.SensorPower() + self.RepairPower() + self.EnginePower() + 0.5)
		self.powerRequired['yellow'] = int(self.powerRequired['green'] + self.ShieldPower() + 0.5)
		self.powerRequired['red'] = int(self.powerRequired['yellow'] + self.WeaponPower() + 0.5)
		# print self.powerRequired.items()

	def TractorDamage(self):
		s = 1.0
		try:
			s = self.stats['tractorDamage']
		except KeyError:
			pass

		m = (self.stats['mass'] / 225000) + 1.0

		return float(int(m * s + 3.0))


import ShipClasses

ShipClasses.Initialize(Race, Ship, raceList, propertyList)