import Registry
import ShipRevisor
import string
import re

propertyList = Registry.Registry()
statLog = ShipRevisor.StatLogger()


class Component(ShipRevisor.BCProperty):
	def __init__(self, name):
		ShipRevisor.BCProperty.__init__(self, name)

	def RelyStaticLines(self):
		return 0

	def _SetMaxCondition(self, args, ship, pStats):
		mult = self.HullStrengthFactor(args, ship, pStats)
		# size = pStats['size']
		# sizeFactor = (size * 1.25 + 3.2) / 2.25
		# d = mult * sizeFactor * ship.HullIndex() * 2000
		# d = float(int(d)) + (2000.0 * ship.HullIndex())
		# if self.name == 'Hull':
		# 	print sizeFactor, ship.HullIndex(), d
		return d

	def SetMaxCondition(self, args, ship, pStats):
		mult = self.HullStrengthFactor(args, ship, pStats)
		size = pStats['size']

		sizeFactor = (size+0.8) * (size+0.8)
		d = sizeFactor * ship.HullIndex() * 1400.0	# This value should be at least half the hole value in FTB_Support.py
		d = float(int(d)) + (mult * 1000.0 * ship.HullIndex())
		# if self.name == 'Hull':
		# 	print sizeFactor, ship.HullIndex(), d
		return d

	def HullStrengthFactor(self, args, ship, pStats):			return 1.0
	def SetCritical(self, args, ship, pStats):					return '0'
	def SetTargetable(self, args, ship, pStats):				return '0'
	# def SetPrimary(self, args, ship, pStats):					return '0'
	def SetRepairComplexity(self, args, ship, pStats):			return 3.0 * ship.RepairIndex()
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.5
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return '0.0'


class TargettableComponent(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def SetMaxCondition(self, args, ship, pStats):
		d = Component.SetMaxCondition(self, args, ship, pStats)
		statLog.Average(ship, self.name + ' HP', d)
		return d

	def SetTargetable(self, args, ship, pStats):				return 1
	def SetRepairComplexity(self, args, ship, pStats):			return 3.0 * ship.RepairIndex()


class Hull(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def SetMaxCondition(self, args, ship, pStats):
		d = int(Component.SetMaxCondition(self, args, ship, pStats))
		d = d + 2000.0
		statLog.Average(ship, self.name + ' HP', d)
		return d

	def HullStrengthFactor(self, args, ship, pStats):			return 3.0
	def SetCritical(self, args, ship, pStats):					return 1
	def SetTargetable(self, args, ship, pStats):				return 1
	def SetPrimary(self, args, ship, pStats):					return 1
	def SetRepairComplexity(self, args, ship, pStats):			return 3.0 * ship.RepairIndex()
	def SetDisabledPercentage(self, args, ship, pStats):		return '0.0'


class SolidMass(Hull):
	def __init__(self, name):
		Component.__init__(self, name)

	def SetMaxCondition(self, args, ship, pStats):
		mult = self.HullStrengthFactor(args, ship, pStats)
		size = pStats['size'] + 1.0

		sizeFactor = size * size * size
		d = sizeFactor * ship.HullIndex() * 1400.0	# This value should be at least half the hole value in FTB_Support.py
		d = float(int(d))
		# if self.name == 'Hull':
		# 	print sizeFactor, ship.HullIndex(), d
		return d

	def HullStrengthFactor(self, args, ship, pStats):			return 3.0

SolidMass('SolidMass')

class HullElement(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	# def HullStrengthFactor(self, args, ship, pStats):				return 4000.0
	def SetPrimary(self, args, ship, pStats):					return '0'
	def SetRepairComplexity(self, args, ship, pStats):			return 3.0 * ship.RepairIndex()
	# def SetDisabledPercentage(self, args, ship, pStats):		return '0.0'


class Bridge(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 3.0
	def SetCritical(self, args, ship, pStats):					return 1
	def SetTargetable(self, args, ship, pStats):				return 1
	# def SetPrimary(self, args, ship, pStats):					return '0'
	def SetRepairComplexity(self, args, ship, pStats):			return 4.0 * ship.RepairIndex()
	# def SetDisabledPercentage(self, args, ship, pStats):		return '0.0'


class Engine(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def SetPrimary(self, args, ship, pStats):					return 1
	def HullStrengthFactor(self, args, ship, pStats):			return 1.0
	def SetRepairComplexity(self, args, ship, pStats):			return 3.0 * ship.RepairIndex()
	# def SetDisabledPercentage(self, args, ship, pStats):		return '0.0'


class CloakingDevice(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def SetPrimary(self, args, ship, pStats):					return 1
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.5
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return self.BasePower(ship) / 1.5
	def SetCloakStrength(self, args, ship, pStats):				return 90.0

class ShipType(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	# def SetGenus(self, args, ship, pStats):					return 1
	# def SetSpecies(self, args, ship, pStats):					return 101
	# def SetMass(self, args, ship, pStats):					return 120.0
	def SetMass(self, args, ship, pStats):
		# print 'ship', ship, args, ship.Mass()
		return ship.Mass()
	# def SetRotationalInertia(self, args, ship, pStats):		return 15000.0
	def SetRotationalInertia(self, args, ship, pStats):			return ship.RotationalInertia()
	# def SetShipName(self, args, ship, pStats):				return "Dauntless"
	# def SetModelFilename(self, args, ship, pStats):			return ""
	# def SetDamageResolution(self, args, ship, pStats):		return 10.0
	# def SetAffiliation(self, args, ship, pStats):				return '0'
	# def SetStationary(self, args, ship, pStats):				return '0'
	# def SetAIString(self, args, ship, pStats):				return "FedAttack"
	# def SetDeathExplosionSound(self, args, ship, pStats):		return "g_lsDeathExplosions"


class Sensor(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def SetTargetable(self, args, ship, pStats):				return '0'
	def HullStrengthFactor(self, args, ship, pStats):			return 2.0
	def SetRepairComplexity(self, args, ship, pStats):			return 0.5 * ship.RepairIndex()
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.400000
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return ship.SensorPower()
	def SetBaseSensorRange(self, args, ship, pStats):
		d = 3000.0 * ship.SensorIndex()
		statLog.Average(ship, 'Sensor Range', d)
		return d

	# def SetMaxProbes(self, args, ship, pStats):					return 10


class Power(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 2.0
	def SetCritical(self, args, ship, pStats):					return 1
	def SetTargetable(self, args, ship, pStats):				return 1
	# def SetPrimary(self, args, ship, pStats):					return 1
	def SetRepairComplexity(self, args, ship, pStats):			return 2.0 * ship.RepairIndex()
	# def SetDisabledPercentage(self, args, ship, pStats):		return 0.500000

	def BasePower(self, ship):
		level = ship.powerPercent[0]
		pct = ship.powerPercent[1]
		retval = float(int(ship.powerRequired[level] * pct / 100) * 100.0)
		return retval

	def SetMainBatteryLimit(self, args, ship, pStats):			return ship.battery * self.BasePower(ship)
	def SetBackupBatteryLimit(self, args, ship, pStats):		return ship.bakBattery * self.BasePower(ship)
	def SetMainConduitCapacity(self, args, ship, pStats):		return ship.conduit * self.BasePower(ship)
	def SetBackupConduitCapacity(self, args, ship, pStats):		return ship.bakConduit * self.BasePower(ship)
	def SetPowerOutput(self, args, ship, pStats):
		# i = string.join((str(self.BasePower(ship)), str(ship.powerPercent)), ', ')
		# ShipRevisor.log(i)
		d = self.BasePower(ship)
		statLog.Average(ship, 'Power Output', d)
		return d



class ImpulseEngine(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	# def SetMaxCondition(self, args, ship, pStats):				return 10000.0
	def SetMaxCondition(self, args, ship, pStats):
		d = Component.SetMaxCondition(self, args, ship, pStats)
		statLog.Average(ship, self.name + ' HP', d)
		return d

	def SetCritical(self, args, ship, pStats):					return '0'
	def SetTargetable(self, args, ship, pStats):				return '0'
	def SetPrimary(self, args, ship, pStats):					return 1
	# def SetDisabledPercentage(self, args, ship, pStats):		return 0.500000
	# def SetRadius(self, args, ship, pStats):					return 0.250000
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return ship.EnginePower()

	def SetMaxAccel(self, args, ship, pStats):
		# d = 2.000000 * ship.AccelIndex()
		d = 3.000000 * ship.AccelIndex()
		statLog.Average(ship, 'Max Accel', d)
		return d

	def SetMaxAngularAccel(self, args, ship, pStats):
		# d = 0.08000 * ship.ManeuverAccelIndex()
		d = 0.10000 * ship.ManeuverAccelIndex()
		statLog.Average(ship, 'Max Angular Accel', d)
		return d

	def SetMaxAngularVelocity(self, args, ship, pStats):
		# d = 0.190000 * ship.ManeuverMaxIndex()
		d = 0.25000 * ship.ManeuverMaxIndex()
		statLog.Average(ship, 'Max Angular Velocity', d)
		return d

	# def SetMaxSpeed(self, args, ship, pStats):					return 6.300000 * ship.SpeedMaxIndex()
	def SetMaxSpeed(self, args, ship, pStats):
		# return 8.000000 * ship.SpeedMaxIndex()
		return 10.000000 * ship.SpeedMaxIndex()

	def SetEngineSound(self, args, ship, pStats):				return ship.EngineSound()


class WarpEngine(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	# def SetMaxCondition(self, args, ship, pStats):				return 10000.0
	def SetCritical(self, args, ship, pStats):					return '0'
	def SetTargetable(self, args, ship, pStats):				return '0'
	def SetPrimary(self, args, ship, pStats):					return 1
	# def SetDisabledPercentage(self, args, ship, pStats):		return 0.500000
	# def SetRadius(self, args, ship, pStats):					return 0.250000
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return ship.EnginePower()


shieldExp = re.compile(r'^\s*(\S+)\.(\S+)\_SHIELDS\s*\,\s*(\S*)')

class Shield(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 1.0
	def SetRepairComplexity(self, args, ship, pStats):			return 2.0 * ship.RepairIndex()
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.5
	# def SetRadius(self, args, ship, pStats):					return 0.5
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return ship.ShieldPower()
	# def SetMaxShields(self, args, ship, pStats):				return ShieldGenerator.FRONT_SHIELDS, 8000.0
	# def SetShieldChargePerSecond(self, args, ship, pStats):	return ShieldGenerator.FRONT_SHIELDS, 11.0
	def SetShieldGlowDecay(self, args, ship, pStats):			return 0.1

	# def SetNormalPowerPerSecond(self, args, ship, pStats):
	# 	chargeIndex = 0
	# 	for i in ship.shieldCharge.values():
	# 		chargeIndex = chargeIndex + i
	# 	chargeIndex = chargeIndex / 6.0
	# 	return (ship.stats['shieldIndex'] / 1000) * ((ship.SizeIndex() + 3) / 4) * chargeIndex * 400.0

	def SetMaxShields(self, args, ship, pStats):
		matching = shieldExp.match(args)
		if matching:
			dir = matching.group(2)
			num = ship.GetShields(dir)
			return matching.group(1) + '.%s_SHIELDS, %s' % (dir, num)
		else:
			raise 'bah'

	def SetShieldChargePerSecond(self, args, ship, pStats):
		matching = shieldExp.match(args)
		if matching:
			dir = matching.group(2)
			num = ship.GetShieldRecharge(dir)
			# print ship.name, dir, num
			return matching.group(1) + '.%s_SHIELDS, %s' % (dir, num)
		else:
			raise 'bah'


class RepairSystem(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 1.0
	def SetPrimary(self, args, ship, pStats):					return 1
	def SetRepairComplexity(self, args, ship, pStats):			return 2.0 * ship.RepairIndex()
	# def SetDisabledPercentage(self, args, ship, pStats):		return 0.1
	# def SetRadius(self, args, ship, pStats):					return 0.25
	def SetNormalPowerPerSecond(self, args, ship, pStats):		return 1.0
	def SetMaxRepairPoints(self, args, ship, pStats):
		return str(float(int(ship.RepairRate() * 100)) / 100.0)
	# def SetNumRepairTeams(self, args, ship, pStats):			return 3


class WarpEngine(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 1.0
	# def SetPrimary(self, args, ship, pStats):					return 1
	# def SetDisabledPercentage(self, args, ship, pStats):		return 0.5
	# def SetRadius(self, args, ship, pStats):					return 0.25
	# def SetNormalPowerPerSecond(self, args, ship, pStats):		return '0.0'


class WeaponSystem(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	# def SetMaxCondition(self, args, ship, pStats):					return 10000.0
	def SetPrimary(self, args, ship, pStats):						return 1

	def SetNormalPowerPerSecond(self, args, ship, pStats):
		d = ship.stats['terawatts'] / 15.0 / max(1, ship.numWeaponSystems)
		d = float(int(d * 10 + 5) / 10) + 100
		return d

	def CountsAsWeapon(self):
		print self.name, 'is a weapon system'
		return 1


class PhaserSystem(WeaponSystem):
	def __init__(self, name):
		WeaponSystem.__init__(self, name)

	def SetSingleFire(self, args, ship, pStats):				return 1


class MultiFirePhaserSystem(WeaponSystem):
	def __init__(self, name):
		WeaponSystem.__init__(self, name)

	def SetSingleFire(self, args, ship, pStats):				return '0'


class TorpedoSystem(WeaponSystem):
	def __init__(self, name):
		WeaponSystem.__init__(self, name)

	def RelyStaticLines(self):
		return 1

	def StaticLines(self, ship, name, linesOut):
		linesOut.append('%s.SetMaxCondition(%f)' % (name, 1000000.0))
		linesOut.append('%s.SetCritical(0)' % (name))
		linesOut.append('%s.SetTargetable(0)' % (name))
		linesOut.append('%s.SetPrimary(1)' % (name))
		linesOut.append('%s.SetPosition(0.000000, 0.000000, 0.000000)' % (name))
		linesOut.append('%s.SetPosition2D(64.0, 64.0)' % (name))
		linesOut.append('%s.SetRepairComplexity(0.1)' % (name))
		linesOut.append('%s.SetDisabledPercentage(0.0)' % (name))
		linesOut.append('%s.SetRadius(0.002)' % (name))
		linesOut.append('%s.SetNormalPowerPerSecond(50.000000)' % (name))
		linesOut.append('%s.SetWeaponSystemType(Torpedoes.WST_TORPEDO)' % (name))
		linesOut.append('%s.SetSingleFire(0)' % (name))
		linesOut.append('%s.SetAimedWeapon(1)' % (name))
		linesOut.append('kFiringChainString = App.TGString()')
		linesOut.append('kFiringChainString.SetString("%s")' % ship.sFiringString)
		linesOut.append('%s.SetFiringChainString(kFiringChainString)' % (name))

		for i in range(len(ship.lTorpTypes)):
			tup = ship.lTorpTypes[i]
			linesOut.append('%s.SetMaxTorpedoes(%d, %d)' % (name, i, tup[1]))
			linesOut.append('%s.SetTorpedoScript(%d, "ftb.Projectiles.%s")' % (name, i, tup[0]))

		linesOut.append('%s.SetNumAmmoTypes(%d)' % (name, len(ship.lTorpTypes)))



class TractorWeaponSystem(WeaponSystem):
	def __init__(self, name):
		WeaponSystem.__init__(self, name)

	def SetNormalPowerPerSecond(self, args, ship, pStats):
		return WeaponSystem.SetNormalPowerPerSecond(self, args, ship, pStats) * 0.8

	def CountsAsWeapon(self):
		return 0


class TractorBeam(Component):
	def __init__(self, name):
		Component.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):				return 1.0
	def SetCritical(self, args, ship, pStats):						return '0'
	def SetTargetable(self, args, ship, pStats):					return 1
	def SetDisabledPercentage(self, args, ship, pStats):			return 0.75
	def SetMaxDamageDistance(self, args, ship, pStats):				return 100.0
	def SetMaxDamage(self, args, ship, pStats):						return ship.TractorDamage()


Hull('Hull')
HullElement('HullElement')
Bridge('Bridge')
Hull('Hull')
ShipType('Ship')
Sensor('Sensor')
Power('Power')
ImpulseEngine('ImpulseEngine')
Engine('Engine')
Shield('Shield')
RepairSystem('RepairSystem')
WarpEngine('WarpEngine')
WeaponSystem('WeaponSystem')
PhaserSystem('PhaserSystem')
MultiFirePhaserSystem('MultiFirePhaserSystem')
TorpedoSystem('TorpedoSystem')
CloakingDevice('CloakingDevice')
TractorWeaponSystem('TractorWeaponSystem')
TractorBeam('TractorBeam')


class Weapon(TargettableComponent):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def SetMaxCondition(self, args, ship, pStats):
		d = Component.SetMaxCondition(self, args, ship, pStats)
		statLog.Average(ship, 'Weapon HP', d)
		return d

	def SetPrimary(self, args, ship, pStats):						return 1
	def SetDumbfire(self, args, ship, pStats):						return 1

	def SetRepairComplexity(self, args, ship, pStats):				return 4.0 * ship.RepairIndex()
	def SetDisabledPercentage(self, args, ship, pStats):			return 0.75

	def GetDamagePerSecond(self, args, ship, pStats):
		maxCharge = self.SetMaxCharge(args, ship, pStats)
		if maxCharge > 1.0:
			maxCharge = 1.0
		# print 'Weapon.maxCharge', maxCharge
		# retval = self.SetMaxDamage(args, ship, pStats) * maxCharge / 2.0
		retval = self.SetMaxDamage(args, ship, pStats) * maxCharge
		# print self, 'GetDamagePerSecond', retval
		return retval

	def BaseMaxCharge(self):										return 4.0
	def BaseMinFiringCharge(self):									return 2.5

	def SetMaxCharge(self, args, ship, pStats):
		retval = self.BaseMaxCharge()
		# print 'Weapon.SetMaxCharge', retval
		if pStats.has_key('maxCharge'):
			retval = retval * pStats['maxCharge']
		return retval
	def SetMinFiringCharge(self, args, ship, pStats):
		retval = self.BaseMinFiringCharge()
		if pStats.has_key('minFiringCharge'):
			retval = retval * pStats['minFiringCharge']
		elif pStats.has_key('maxCharge'):
			retval = retval * pStats['maxCharge']
		return retval

	def SetRechargeRate(self, args, ship, pStats):
		charge = 1.0
		if pStats.has_key('terawatts'):
			charge = pStats['terawatts']

		terawatts = ship.stats['terawatts'] * (charge / (ship.chargeCount + 0.0000001))

		# print self, ship.name, 'Terawatts', terawatts, 'charge', charge, 'count', ship.chargeCount
		dam = self.GetDamagePerSecond(args, ship, pStats)
		# print dam

		if dam:
			terawatts = terawatts / (dam * 30.0)
		else:
			terawatts = 0.0
		# print terawatts
		retval = (int(terawatts * 1000.0) + 1.0) / 1000.0
		# print retval
		return retval


class Blank(Weapon):
	def SetCritical(self, args, ship, pStats):					return '0'
	def SetTargetable(self, args, ship, pStats):				return '0'
	def SetPrimary(self, args, ship, pStats):					return '0'
	def SetMaxDamage(self, args, ship, pStats):						return 0.001
	def SetMaxCharge(self, args, ship, pStats):						return '0.0'
	def SetMinFiringCharge(self, args, ship, pStats):				return 1.0
	def SetMaxReady(self, args, ship, pStats):						return '0'
 	def SetPosition2D(self, args, ship, pStats):					return "0.0, 0.0"
 	def SetIconPositionX(self, args, ship, pStats):					return '0.0'
 	def SetIconPositionY(self, args, ship, pStats):					return '0.0'
 	def SetMaxReady(self, args, ship, pStats):						return '0'
 	def SetIconNum(self, args, ship, pStats):						return 374
 	def SetIndicatorIconNum(self, args, ship, pStats):				return 374
 	def SetIndicatorIconPositionX(self, args, ship, pStats):		return '0.0'
 	def SetIndicatorIconPositionY(self, args, ship, pStats):		return '0.0'

Blank('Blank')

class Phaser(Weapon):
	def __init__(self, name):
		Weapon.__init__(self, name)

	def SetDumbfire(self, args, ship, pStats):						return '0'
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetFireSound(self, args, ship, pStats):						return "'Galaxy Phaser'"
	def SetMaxDamage(self, args, ship, pStats):						return 100.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 30.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetPhaserTextureStart(self, args, ship, pStats):			return '0'
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 7
	def SetPhaserWidth(self, args, ship, pStats):					return 0.5
	def SetNumSides(self, args, ship, pStats):						return 6
	def SetMainRadius(self, args, ship, pStats):					return 0.075
	def SetTaperRadius(self, args, ship, pStats):					return 0.01
	def SetCoreScale(self, args, ship, pStats):						return 0.5
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetTaperMinLength(self, args, ship, pStats):				return 5.0
	def SetTaperMaxLength(self, args, ship, pStats):				return 30.0
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.01
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 2.5
	def SetTextureName(self, args, ship, pStats):					return "'data/phaser.tga'"

	def SetDamageRadiusFactor(self, args, ship, pStats):			return self.CoreScale(args, ship, pStats) / 5.0

	def BaseMaxCharge(self):										return 4.0
	def BaseMinFiringCharge(self):									return 2.5

	def StaticLines(self, ship, name, linesOut):
		linesOut.append('kColor = App.TGColorA()')
		linesOut.append('kColor.SetRGBA(%s)' % ( self.OuterShellColor() ))
		linesOut.append('%s.SetOuterShellColor(kColor)' % (name))
		linesOut.append('kColor.SetRGBA(%s)' % ( self.InnerShellColor() ))
		linesOut.append('%s.SetInnerShellColor(kColor)' % (name))
		linesOut.append('kColor.SetRGBA(%s)' % ( self.OuterCoreColor() ))
		linesOut.append('%s.SetOuterCoreColor(kColor)' % (name))
		linesOut.append('kColor.SetRGBA(%s)' % ( self.InnerCoreColor() ))
		linesOut.append('%s.SetInnerCoreColor(kColor)' % (name))

	def OuterShellColor(self):			return '0.639216, 0.000000, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.992157, 0.192157, 0.054902, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.592157, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '0.803922, 0.803922, 0.000000, 1.000000'

	def Exclude(self, lineIn):
		if string.find(lineIn, 'kColor') != -1:
			return 1


class PulseWeapon(Weapon):
	def __init__(self, name):
		Weapon.__init__(self, name)

	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDumbfire(self, args, ship, pStats):					return 1
	def SetDamageRadiusFactor(self, args, ship, pStats):		return (self.SetMaxDamage(args, ship, pStats) / 4000.0 + 0.1) / 2.0
	def SetFireSound(self, args, ship, pStats):					return "'FTB Klingon Pulse'"
	# def SetMaxCharge(self, args, ship, pStats):					return 3.0
	def SetMaxDamage(self, args, ship, pStats):					return 500.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 90.0
	# def SetMinFiringCharge(self, args, ship, pStats):			return 2.5
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 0.8
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk12PulseDisruptor'"

	def BaseMaxCharge(self):									return 6.0
	def BaseMinFiringCharge(self):								return 4.0

	def GetDamagePerSecond(self, args, ship, pStats):
		maxCharge = self.SetMaxCharge(args, ship, pStats)
		shots = maxCharge / self.SetNormalDischargeRate(args, ship, pStats)
		cooldown = self.SetCooldownTime(args, ship, pStats)
		# print 'shots', shots
		# print 'cooldown', cooldown
		firetime = cooldown * shots
		# print 'firetime', firetime
		damage = self.SetMaxDamage(args, ship, pStats)
		# print 'damage', damage
		if firetime > 1.0:
			damage = (damage * shots) / firetime
		else:
			damage = damage * shots
		return damage



class TorpedoTube(Weapon):
	def __init__(self, name):
		Weapon.__init__(self, name)

	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.17
	def SetImmediateDelay(self, args, ship, pStats):			return 0.25
	def SetReloadDelay(self, args, ship, pStats):				return 40.0
	def SetMaxReady(self, args, ship, pStats):					return 1



class TorpedoPulse(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'FTB Photon Torp'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBPhotonTorpedo'"
	def SetRechargeRate(self, args, ship, pStats):					return '0'
	def SetIconNum(self, args, ship, pStates):						return 370

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.13
	def SetMaxCharge(self, args, ship, pStats):						return 50.0
	def SetMaxDamage(self, args, ship, pStats):						return 1600.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 60.0
	def BaseMinFiringCharge(self):				return 1.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 2.0


#####################################################
# Federation weapons
class FedPhaser(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'Intrepid Phaser'"

	def SetMaxDamage(self, args, ship, pStats):						return 250.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 60.0
	def SetMainRadius(self, args, ship, pStats):					return 0.085
	def SetCoreScale(self, args, ship, pStats):						return 0.3
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.02
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0

	def BaseMaxCharge(self):										return 3.0
	def BaseMinFiringCharge(self):									return 2.0

	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/FedPhaser02.tga'"

	def OuterShellColor(self):			return '0.737255, 0.274510, 0.003922, 0.584314'
	def InnerShellColor(self):			return '0.992157, 0.439216, 0.019608, 1.000000'
	def OuterCoreColor(self):			return '0.992157, 0.458824, 0.137255, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 0.647059, 0.203922, 1.000000'


#####################################################
# TOSFederation weapons
class FedTOSPhaser(FedPhaser):
	def SetFireSound(self, args, ship, pStats):						return "'FTB TOS Phaser'"

	def SetMaxDamage(self, args, ship, pStats):						return 240.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0
	def SetCoreScale(self, args, ship, pStats):						return 0.25
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.01
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0

	def BaseMaxCharge(self):										return 2.0
	def BaseMinFiringCharge(self):									return 1.0

	def OuterShellColor(self):			return '0.000000, 0.000000, 0.639216, 1.000000'
	def InnerShellColor(self):			return '0.054902, 0.192157, 0.992157, 1.000000'
	def OuterCoreColor(self):			return '0.000000, 0.592157, 0.592157, 1.000000'
	def InnerCoreColor(self):			return '0.000000, 0.803922, 0.803922, 1.000000'
	

class PhaseCannon(FedTOSPhaser):
	def SetFireSound(self, args, ship, pStats):						return "'NX Phaser'"
	def SetMaxDamage(self, args, ship, pStats):						return 20.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 30.0



class FedTMPPhaser(FedPhaser):
	def SetFireSound(self, args, ship, pStats):						return "'FTB TMP Phaser'"

	def BaseMaxCharge(self):										return 1.5
	def BaseMinFiringCharge(self):									return 0.75

	def SetMaxDamage(self, args, ship, pStats):						return 300.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetPhaserTextureStart(self, args, ship, pStats):			return '0'
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 7
	def SetPhaserWidth(self, args, ship, pStats):					return 0.3
	def SetMainRadius(self, args, ship, pStats):					return 0.025
	def SetTaperRadius(self, args, ship, pStats):					return 0.010
	def SetCoreScale(self, args, ship, pStats):						return 0.075
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.1
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 5.5
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeam.tga'"

	def OuterShellColor(self):			return '1.000000, 0.164706, 0.003922, 1.000000'
	def InnerShellColor(self):			return '1.000000, 0.164706, 0.003922, 1.000000'
	def OuterCoreColor(self):			return '0.992157, 0.831373, 0.639216, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 0.901961, 0.858824, 1.000000'


class FedTMPVII(FedTMPPhaser):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetMaxDamage(self, args, ship, pStats):						return 300.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0

	def BaseMaxCharge(self):										return 2.5
	def BaseMinFiringCharge(self):									return 1.8


class FedTMPVIIa(FedTMPVII):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeamA.tga'"

	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetPhaserTextureStart(self, args, ship, pStats):			return '0'
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 3.5
	def SetTextureSpeed(self, args, ship, pStats):					return 5.5

class FedTMPVIIb(FedTMPVIIa):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeamB.tga'"



class FedTMPVIII(FedTMPVII):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetMaxDamage(self, args, ship, pStats):						return 400.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0


class FedTMPVIIIa(FedTMPVIII):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeamA.tga'"


class FedTMPVIIIb(FedTMPVIIIa):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeamB.tga'"


class FedTMPVIIIMega(FedTMPVIII):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetMaxDamage(self, args, ship, pStats):						return 1200.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 60.0

	def SetMainRadius(self, args, ship, pStats):					return 0.075
	def SetTaperRadius(self, args, ship, pStats):					return 0.03


class FedTypeDurandal(FedPhaser):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	def SetTextureName(self, args, ship, pStats):					return "'data/textures/tactical/Dur_phaser.tga'"
	def SetTextureSpeed(self, args, ship, pStats):					return 2.0

	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.05
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetCoreScale(self, args, ship, pStats):						return 0.3

	def OuterShellColor(self):			return '0.639216, 0.000000, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.992157, 0.192157, 0.054902, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.592157, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '0.803922, 0.803922, 0.000000, 1.000000'


class FedTypeDurandalR(FedPhaser):
	def __init__(self, name):
		FedPhaser.__init__(self, name)
	# def SetTextureName(self, args, ship, pStats):					return "'data/textures/tactical/Dur_phaser.tga'"
	def SetTextureSpeed(self, args, ship, pStats):					return 2.0

	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.01
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetPhaserWidth(self, args, ship, pStats):					return 0.02
	def SetCoreScale(self, args, ship, pStats):						return 0.7

	def OuterShellColor(self):			return '0.639216, 0.000000, 0.000000, 0.700000'
	def InnerShellColor(self):			return '0.992157, 0.192157, 0.054902, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.592157, 0.000000, 0.900000'
	def InnerCoreColor(self):			return '0.803922, 0.803922, 0.000000, 1.000000'


class FedTypeVII(FedTypeDurandalR):
	def __init__(self, name):
		FedTypeDurandalR.__init__(self, name)

	def SetMaxDamage(self, args, ship, pStats):						return 1000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0

	def BaseMaxCharge(self):										return 3.0
	def BaseMinFiringCharge(self):									return 2.0

	def OuterShellColor(self):			return '0.639216, 0.321569, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.992157, 0.572549, 0.058824, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.294118, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '0.800000, 0.400000, 0.000000, 1.000000'


class FedTypeVIII(FedTypeDurandalR):
	def __init__(self, name):
		FedTypeDurandalR.__init__(self, name)
	def SetMaxDamage(self, args, ship, pStats):						return 1350.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 45.0
	def SetMainRadius(self, args, ship, pStats):					return 0.06


class FedTypeVIIBank(FedTypeVII):
	def SetFireSound(self, args, ship, pStats):						return "'FTB Phaser Emitter'"


class FedTypeVIIIBank(FedTypeVIII):
	def SetFireSound(self, args, ship, pStats):						return "'FTB Phaser Emitter'"



class FedTypeIX(FedPhaser):
	def __init__(self, name):
		FedPhaser.__init__(self, name)

	def BaseMaxCharge(self):										return 3.2
	def BaseMinFiringCharge(self):									return 2.0

	def SetFireSound(self, args, ship, pStats):						return "'Ambassador Phaser'"
	def SetMaxDamage(self, args, ship, pStats):						return 1600.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 60.0

	def OuterShellColor(self):			return '0.639216, 0.000000, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.992157, 0.192157, 0.054902, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.592157, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '0.803922, 0.803922, 0.000000, 1.000000'


class FedTypeX(FedTypeIX):
	def __init__(self, name):
		FedTypeIX.__init__(self, name)

	def SetMainRadius(self, args, ship, pStats):					return 0.07
	def SetFireSound(self, args, ship, pStats):						return "'Galaxy Phaser'"
	def SetMaxDamage(self, args, ship, pStats):						return 2000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 80.0




class FedTypeXSmall(FedTypeX):
	def __init__(self, name):
		FedTypeX.__init__(self, name)
	def SetMainRadius(self, args, ship, pStats):					return 0.05


class FedTypeXII(FedTypeX):
	def __init__(self, name):
		FedTypeX.__init__(self, name)

	def BaseMaxCharge(self):										return 2.5
	def BaseMinFiringCharge(self):									return 1.0

	def SetFireSound(self, args, ship, pStats):						return "'Akira Phaser'"
	def SetMaxDamage(self, args, ship, pStats):						return 3000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 100.0

	def OuterShellColor(self):			return '1.000000, 0.501961, 0.000000, 1.000000'
	def InnerShellColor(self):			return '1.000000, 0.501961, 0.247059, 1.000000'
	def OuterCoreColor(self):			return '1.000000, 1.000000, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 0.501961, 1.000000'



class FedTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 4.0
	def SetReloadDelay(self, args, ship, pStats):				return 40.0
	def SetMaxReady(self, args, ship, pStats):					return 1


class Fed2ndTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 4.0
	def SetReloadDelay(self, args, ship, pStats):				return 40.0
	def SetMaxReady(self, args, ship, pStats):					return 2


class FedStdTorpedoTube(Fed2ndTorpedoTube):
	def __init__(self, name):
		Fed2ndTorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 2.0
	def SetReloadDelay(self, args, ship, pStats):				return 40.0
	def SetMaxReady(self, args, ship, pStats):					return 2


class FedType1BurstTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 2.85
	def SetReloadDelay(self, args, ship, pStats):				return 40
	def SetMaxReady(self, args, ship, pStats):					return 2


class FedType2BurstTorpedoTube(FedType1BurstTorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 2.5
	def SetReloadDelay(self, args, ship, pStats):				return 40
	def SetMaxReady(self, args, ship, pStats):					return 2


class FedType3BurstTorpedoTube(FedType2BurstTorpedoTube):
	def __init__(self, name):
		FedType2BurstTorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 0.5
	def SetReloadDelay(self, args, ship, pStats):				return 40
	def SetMaxReady(self, args, ship, pStats):					return 4


class FedType4BurstTorpedoTube(FedType3BurstTorpedoTube):
	def __init__(self, name):
		FedType3BurstTorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 0.42
	def SetReloadDelay(self, args, ship, pStats):				return 40
	def SetMaxReady(self, args, ship, pStats):					return 3


class FedPFTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 0.5
	def SetReloadDelay(self, args, ship, pStats):				return 30.0
	def SetMaxReady(self, args, ship, pStats):					return 2


class FedSingleTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 0.5
	def SetReloadDelay(self, args, ship, pStats):				return 40.0
	def SetMaxReady(self, args, ship, pStats):					return 1


class FedMk5TorpedoTurret(TorpedoPulse):
	def __init__(self, name):
		TorpedoPulse.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'FTB Photon Torp'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBMk5PhotonTorpedo'"

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.3
	def SetMaxCharge(self, args, ship, pStats):						return 15.0
	def SetMaxDamage(self, args, ship, pStats):						return 750.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 90.0
	def SetMinFiringCharge(self, args, ship, pStats):				return 1.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 45.0


class FedQuantumTorpedoTurret(TorpedoPulse):
	def __init__(self, name):
		TorpedoPulse.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'FTB Pulse Phaser'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBQuantumTorpedo'"

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.13
	def SetMaxCharge(self, args, ship, pStats):						return 10.0
	def SetMaxDamage(self, args, ship, pStats):						return 2400.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 90.0
	def SetMinFiringCharge(self, args, ship, pStats):				return 1.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 30.0


class FedPulsePhaser(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'FTB Pulse Phaser'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBPulsePhaser'"

	def BaseMaxCharge(self):										return 3.0
	def BaseMinFiringCharge(self):									return 2.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.08
	def SetMaxDamage(self, args, ship, pStats):						return 80.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 0.4


class CloakDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'FTB Cloak Disruptor'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBCloakDisruptor'"

	def BaseMaxCharge(self):										return 3.0
	def BaseMinFiringCharge(self):									return 2.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.08
	def SetMaxDamage(self, args, ship, pStats):						return 80.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 60.0


class FedC1PulsePhaser(FedPulsePhaser):
	def __init__(self, name):
		FedPulsePhaser.__init__(self, name)

	def SetTargetable(self, args, ship, pStats):				return '0'

	def SetFireSound(self, args, ship, pStats):						return "'FTB C1 Pulse Phaser'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBClass1PulsePhaser'"

	def BaseMaxCharge(self):										return 5.0
	def BaseMinFiringCharge(self):									return 4.0

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.14
	def SetMaxDamage(self, args, ship, pStats):						return 200.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 80.0
	def SetCooldownTime(self, args, ship, pStats):					return 0.15


class PulsePhaserBeam(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetDumbfire(self, args, ship, pStats):						return 1
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetFireSound(self, args, ship, pStats):						return "'FTB PulsePhaserBurst'"
	def SetMaxDamage(self, args, ship, pStats):						return 600.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetPhaserTextureStart(self, args, ship, pStats):			return '0'
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 7
	def SetPhaserWidth(self, args, ship, pStats):					return 0.5
	def SetNumSides(self, args, ship, pStats):						return 12
	def SetMainRadius(self, args, ship, pStats):					return 0.07
	def SetTaperRadius(self, args, ship, pStats):					return 0.01
	def SetCoreScale(self, args, ship, pStats):						return 0.5
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetTaperMinLength(self, args, ship, pStats):				return 5.0
	def SetTaperMaxLength(self, args, ship, pStats):				return 30.0
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.1
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 15.0
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Laurelin_PulseBeam.tga'"

	def BaseMaxCharge(self):										return 0.48
	def BaseMinFiringCharge(self):									return 0.48

	def OuterShellColor(self):			return '0.819608, 0.411765, 0.0, 1.0'
	def InnerShellColor(self):			return '1.0, 0.36863, 0.066667, 1.0'
	def OuterCoreColor(self):			return '1.0, 0.35686, 0.04706, 1.0'
	def InnerCoreColor(self):			return '1.0, 1.0, 1.0, 0.63092'


class FedAntimatter(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Klingon Pulse'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBAntimatter'"

	def BaseMaxCharge(self):									return 5.0
	def BaseMinFiringCharge(self):								return 6.0

	def SetIconNum(self, args, ship, pStats):					return 375
	def SetIndicatorIconNum(self, args, ship, pStats):			return 523

	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.12
	def SetMaxDamage(self, args, ship, pStats):					return 800.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 10.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 0.2




class FedParticleBeam(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'Ambassador Phaser'"
	def SetCoreScale(self, args, ship, pStats):						return 2.0

	def BaseMaxCharge(self):										return 10.0
	def BaseMinFiringCharge(self):									return 13.0

	# This thing is a special case
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetNormalPowerPerSecond(self, args, ship, pStats):			return '0.0'
	def GetDamagePerSecond(self, args, ship, pStats):				return '0.0'
	def SetRechargeRate(self, args, ship, pStats):					return '0.0'

	def SetMaxDamage(self, args, ship, pStats):						return 2000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 120.0
	def SetPhaserWidth(self, args, ship, pStats):					return 3.0
	def SetMainRadius(self, args, ship, pStats):					return 0.2
	def SetTaperRadius(self, args, ship, pStats):					return 0.04
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.01
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0

	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Laurelin_phaser27a.tga'"

	def OuterShellColor(self):			return '0.639216, 0.000000, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.992157, 0.192157, 0.054902, 1.000000'
	def OuterCoreColor(self):			return '0.592157, 0.592157, 0.000000, 1.000000'
	def InnerCoreColor(self):			return '0.803922, 0.803922, 0.000000, 1.000000'

class FedEngineering(RepairSystem):
	def __init__(self, name):
		RepairSystem.__init__(self, name)

	def SetMaxRepairPoints(self, args, ship, pStats):
		return str(float(int(ship.RepairRate() * 100)) / 80.0)
	def SetNumRepairTeams(self, args, ship, pStats):			return 5


FedTOSPhaser('FedTOSPhaser')
PhaseCannon('PhaseCannon')

FedTMPVII('FedTMPVII')
FedTMPVII('FedTMPVIIa')
FedTMPVII('FedTMPVIIb')
FedTMPVII('FedTMPVIII')
FedTMPVII('FedTMPVIIIa')
FedTMPVII('FedTMPVIIIb')
FedTMPVIIIMega('FedTMPVIIIMega')
FedTypeVII('FedTypeVII')
FedTypeVIII('FedTypeVIII')
FedTypeIX('FedTypeIX')
FedTypeX('FedTypeX')
FedTypeXSmall('FedTypeXSmall')
FedTypeXII('FedTypeXII')
FedPulsePhaser('FedPulsePhaser')
FedC1PulsePhaser('FedC1PulsePhaser')
PulsePhaserBeam('FedPulsePhaserBeam')
FedParticleBeam('FedParticleBeam')
FedAntimatter('FedAntimatter')
FedMk5TorpedoTurret('FedMk5TorpedoTurret')
FedQuantumTorpedoTurret('FedQuantumTorpedoTurret')
CloakDisruptor('CloakDisruptor')

FedTypeVIIBank('FedTypeVIIBank')
FedTypeVIIIBank('FedTypeVIIIBank')

FedTMPVII('FedTMPVII')
FedTMPVIII('FedTMPVIII')
FedTMPVIIb('FedTMPVIIb')
FedTMPVIIIb('FedTMPVIIIb')

FedEngineering('FedEngineering')


Fed2ndTorpedoTube('Fed2ndTorpedoTube')
FedStdTorpedoTube('FedStdTorpedoTube')
FedType1BurstTorpedoTube('FedType1BurstTorpedoTube')
FedType2BurstTorpedoTube('FedType2BurstTorpedoTube')
FedType3BurstTorpedoTube('FedType3BurstTorpedoTube')
FedType4BurstTorpedoTube('FedType4BurstTorpedoTube')
FedPFTorpedoTube('FedPFTorpedoTube')
FedSingleTorpedoTube('FedSingleTorpedoTube')


#####################################################
# Klingon weapons
class KliDisruptorBeam(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Disruptor Beam'"

	def BaseMaxCharge(self):									return 1.5
	def BaseMinFiringCharge(self):								return 0.8

	def SetMaxDamage(self, args, ship, pStats):					return 2800.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 60.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 0.255
	def SetPhaserTextureStart(self, args, ship, pStats):		return 16
	def SetPhaserTextureEnd(self, args, ship, pStats):			return 23
	def SetPhaserWidth(self, args, ship, pStats):				return 0.3
	def SetMainRadius(self, args, ship, pStats):				return 0.075
	def SetTaperRadius(self, args, ship, pStats):				return 0.03
	def SetCoreScale(self, args, ship, pStats):					return 0.175
	def SetTaperRatio(self, args, ship, pStats):				return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):	return 0.05
	def SetPerimeterTile(self, args, ship, pStats):				return 1.0
	def SetTextureSpeed(self, args, ship, pStats):				return 2.5
	def SetTextureName(self, args, ship, pStats):				return "'Custom/FTB/Textures/Tactical/Laurelin_poleron01.tga'"

	def OuterShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def InnerShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def OuterCoreColor(self):			return '0.513726, 1.000000, 0.501961, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class KliMk12DisruptorBeam(KliDisruptorBeam):
	def __init__(self, name):
		KliDisruptorBeam.__init__(self, name)

	def SetMainRadius(self, args, ship, pStats):				return 0.07
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.6


KliMk12DisruptorBeam('KliMk12DisruptorBeam')


class KliPulseDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Klingon Pulse'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk12PulseDisruptor'"

	def BaseMaxCharge(self):									return 5.0
	def BaseMinFiringCharge(self):								return 1.0

	def SetRepairComplexity(self, args, ship, pStats):			return PulseWeapon.SetRepairComplexity(self, args, ship, pStats) * 0.8
	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.12
	def SetMaxDamage(self, args, ship, pStats):					return 500.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 50.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 0.2


class KliDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Klingon Disruptor'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk10Disruptor'"

	def BaseMaxCharge(self):									return 2.5
	def BaseMinFiringCharge(self):								return 1.0

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.14
	def SetMaxDamage(self, args, ship, pStats):					return 1000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 50.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 1.0


class KliPlasma(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetMaxCharge(self, args, ship, pStats):					return 6.0
	def BaseMinFiringCharge(self):								return 6.0

	def SetFireSound(self, args, ship, pStats):					return "'Klingon Disruptor'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBKlingonPlasmaBurst'"

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.2
	def SetMaxDamage(self, args, ship, pStats):					return 2400.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 10.0


class KliFastPlasma(KliPlasma):
	def __init__(self, name):
		KliPlasma.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBKlingonFastPlasmaBurst'"
	def SetMaxDamageDistance(self, args, ship, pStats):			return 60.0


class KliMk6PulseDisruptor(KliPulseDisruptor):
	def __init__(self, name):
		KliPulseDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk6PulseDisruptor'"
	def SetMaxDamage(self, args, ship, pStats):					return 200.0


class KliMk10Disruptor(KliDisruptor):
	def __init__(self, name):
		KliDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk10Disruptor'"
	def SetMaxDamage(self, args, ship, pStats):					return 600.0



class KliMk12Disruptor(KliDisruptor):
	def __init__(self, name):
		KliDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk12Disruptor'"
	def SetMaxDamage(self, args, ship, pStats):					return 750.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 80.0


class KliMk12PulseDisruptor(KliPulseDisruptor):
	def __init__(self, name):
		KliPulseDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk12PulseDisruptor'"
	def SetMaxDamage(self, args, ship, pStats):					return 375.0


class KliMk18Disruptor(KliDisruptor):
	def __init__(self, name):
		KliDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk18Disruptor'"
	def SetMaxDamage(self, args, ship, pStats):					return 3000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 120.0
	def SetCooldownTime(self, args, ship, pStats):				return 6.0


class KliTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 2.0
	def SetReloadDelay(self, args, ship, pStats):				return 30.0
	def SetMaxReady(self, args, ship, pStats):					return 3


class KliSingleTorpedoTube(KliTorpedoTube):
	def __init__(self, name):
		KliTorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 25.0


class KliDoubleTorpedoTube(KliSingleTorpedoTube):
	def __init__(self, name):
		KliSingleTorpedoTube.__init__(self, name)

	def SetImmediateDelay(self, args, ship, pStats):			return 0.5
	def SetReloadDelay(self, args, ship, pStats):				return 25.0
	def SetMaxReady(self, args, ship, pStats):					return 2


class KliTripleTorpedoTube(KliDoubleTorpedoTube):
	def __init__(self, name):
		KliDoubleTorpedoTube.__init__(self, name)

	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.15
	def SetReloadDelay(self, args, ship, pStats):				return 25.0
	def SetMaxReady(self, args, ship, pStats):					return 3


KliMk6PulseDisruptor('KliMk6PulseDisruptor')
KliMk12PulseDisruptor('KliMk12PulseDisruptor')
KliMk10Disruptor('KliMk10Disruptor')
KliMk12Disruptor('KliMk12Disruptor')
KliMk18Disruptor('KliMk18Disruptor')
KliTorpedoTube('KliTorpedoTube')
KliSingleTorpedoTube('KliSingleTorpedoTube')
KliDoubleTorpedoTube('KliDoubleTorpedoTube')
KliTripleTorpedoTube('KliTripleTorpedoTube')
KliPlasma('KliPlasma')
KliFastPlasma('KliFastPlasma')


#####################################################
# Cardassian weapons
class CardPhaser(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def BaseMaxCharge(self):										return 4.5
	def BaseMinFiringCharge(self):									return 3.0

	def SetRepairComplexity(self, args, ship, pStats):				return Phaser.SetRepairComplexity(self, args, ship, pStats) * 0.6
	def SetFireSound(self, args, ship, pStats):						return "'Galor Phaser'"
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetMaxDamage(self, args, ship, pStats):						return 300.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	# def SetNumSides(self, args, ship, pStats):						return 8
	def SetPhaserTextureStart(self, args, ship, pStats):			return 1
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 15
	def SetPhaserWidth(self, args, ship, pStats):					return 0.5
	def SetMainRadius(self, args, ship, pStats):					return 0.06
	def SetTaperRadius(self, args, ship, pStats):					return 0.03
	def SetCoreScale(self, args, ship, pStats):						return 0.3
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.1
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 2.5
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga'"

	def OuterShellColor(self):			return '0.721569, 0.556863, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.721569, 0.556863, 0.000000, 1.000000'
	def OuterCoreColor(self):			return '0.984314, 0.756863, 0.058824, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class CardTypeVII(CardPhaser):
	def __init__(self, name):
		CardPhaser.__init__(self, name)
	def SetMaxDamage(self, args, ship, pStats):						return 1000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 30.0


class CardTypeVIISmall(CardTypeVII):
	def __init__(self, name):
		CardTypeVII.__init__(self, name)

	def BaseMaxCharge(self):										return 4.0
	def BaseMinFiringCharge(self):									return 2.0

	def SetMainRadius(self, args, ship, pStats):					return 0.037
	def SetTaperRadius(self, args, ship, pStats):					return 0.0075
	def SetMaxDamage(self, args, ship, pStats):						return 500.0


class CardTypeVIII(CardPhaser):
	def __init__(self, name):
		CardPhaser.__init__(self, name)

	def SetRepairComplexity(self, args, ship, pStats):				return Phaser.SetRepairComplexity(self, args, ship, pStats) * 0.8
	def SetTaperRadius(self, args, ship, pStats):					return 0.05
	def SetMaxDamage(self, args, ship, pStats):						return 1350.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 30.0

class CardTypeIX(CardPhaser):
	def __init__(self, name):
		CardPhaser.__init__(self, name)

	def SetMaxDamage(self, args, ship, pStats):						return 1750.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0


class CardTypeX(CardTypeIX):
	def __init__(self, name):
		CardTypeIX.__init__(self, name)

	def SetMaxDamage(self, args, ship, pStats):						return 2000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 45.0


class CardHiPower(CardTypeX):
	def __init__(self, name):
		CardTypeIX.__init__(self, name)

	def SetMainRadius(self, args, ship, pStats):					return 0.1
	def SetTaperRadius(self, args, ship, pStats):					return 0.02
	def SetCoreScale(self, args, ship, pStats):						return 0.6
	def SetTaperRatio(self, args, ship, pStats):					return 0.25

	def SetMaxDamage(self, args, ship, pStats):						return 3000.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0


class CardDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Disruptor'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBCardDisruptor'"

	def BaseMaxCharge(self):									return 2.0
	def BaseMinFiringCharge(self):								return 1.25

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.14
	def SetMaxDamage(self, args, ship, pStats):					return 600.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 90.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 1.0


class CardTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

class CardDoubleTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetMaxReady(self, args, ship, pStats):					return 2

CardTypeVII('CardTypeVII')
CardTypeVIISmall('CardTypeVIISmall')
CardTypeVIII('CardTypeVIII')
CardTypeIX('CardTypeIX')
CardTypeX('CardTypeX')
CardHiPower('CardHiPower')
CardDisruptor('CardDisruptor')

CardTorpedoTube('CardTorpedoTube')
CardDoubleTorpedoTube('CardDoubleTorpedoTube')



#####################################################
# Romulan weapons
class RomDisruptorBeam(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'Warbird Phaser'"

	def BaseMaxCharge(self):									return 2.5
	def BaseMinFiringCharge(self):								return 2.0

	def SetMaxDamage(self, args, ship, pStats):					return 1750.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 60.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 0.255
	def SetPhaserTextureStart(self, args, ship, pStats):		return 16
	def SetPhaserTextureEnd(self, args, ship, pStats):			return 23
	def SetPhaserWidth(self, args, ship, pStats):				return 0.3
	def SetMainRadius(self, args, ship, pStats):				return 0.075
	def SetTaperRadius(self, args, ship, pStats):				return 0.03
	def SetCoreScale(self, args, ship, pStats):					return 0.175
	def SetTaperRatio(self, args, ship, pStats):				return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):	return 0.05
	def SetPerimeterTile(self, args, ship, pStats):				return 1.0
	def SetTextureSpeed(self, args, ship, pStats):				return 2.5
	def SetTextureName(self, args, ship, pStats):				return "'Custom/FTB/Textures/Tactical/Laurelin_poleron01.tga'"

	def OuterShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def InnerShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def OuterCoreColor(self):			return '0.513726, 1.000000, 0.501961, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class RomDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Disruptor'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk6PulseDisruptor'"

	def BaseMaxCharge(self):									return 2.0
	def BaseMinFiringCharge(self):								return 1.25

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.14
	def SetMaxDamage(self, args, ship, pStats):					return 1000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 90.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 1.0


class RomEntDisruptor(RomDisruptor):
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.ENTRomDisruptor'"

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.1
	def SetMaxDamage(self, args, ship, pStats):					return 68.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 50.0


class RomPulseDisruptor(RomDisruptor):
	def __init__(self, name):
		RomDisruptor.__init__(self, name)

	def BaseMaxCharge(self):									return 2.5
	def BaseMinFiringCharge(self):								return 1.0
	def SetFireSound(self, args, ship, pStats):					return "'FTB Disruptor Pulse'"
	def SetCooldownTime(self, args, ship, pStats):				return 0.5


class RomMedPulseDisruptor(RomPulseDisruptor):
	def __init__(self, name):
		RomPulseDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBValdoreBlast'"
	def SetMaxDamage(self, args, ship, pStats):					return 500.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 80.0


class RomHeavyPulseDisruptor(RomPulseDisruptor):
	def __init__(self, name):
		RomPulseDisruptor.__init__(self, name)

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBValdoreHeavyBlast'"
	def SetMaxDamage(self, args, ship, pStats):					return 1000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 120.0
	def SetCooldownTime(self, args, ship, pStats):				return 3.0


class RomMk21Disruptor(RomDisruptor):
	def __init__(self, name):
		RomDisruptor.__init__(self, name)

	def BaseMaxCharge(self):									return 4.0
	def BaseMinFiringCharge(self):								return 1.0
	def SetFireSound(self, args, ship, pStats):					return "'FTB Romulan Disruptor'"

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBMk21Disruptor'"
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetMaxDamage(self, args, ship, pStats):					return 2200.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 120.0

	def SetCooldownTime(self, args, ship, pStats):				return 0.4


class RomTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 30


class RomS2TorpedoTube(RomTorpedoTube):
	def __init__(self, name):
		RomTorpedoTube.__init__(self, name)

	def SetMaxReady(self, args, ship, pStats):					return 2

class RomS3TorpedoTube(RomTorpedoTube):
	def __init__(self, name):
		RomTorpedoTube.__init__(self, name)

	def SetMaxReady(self, args, ship, pStats):					return 3


class RomCloakingDevice(CloakingDevice):
	def __init__(self, name):
		TargettableComponent.__init__(self, name)

	def SetNormalPowerPerSecond(self, args, ship, pStats):		return self.BasePower(ship) / 2.0
	def SetCloakStrength(self, args, ship, pStats):				return 100.0

RomDisruptorBeam('RomDisruptorBeam')
RomDisruptor('RomDisruptor')
RomMedPulseDisruptor('RomMedPulseDisruptor')
RomHeavyPulseDisruptor('RomHeavyPulseDisruptor')
RomMk21Disruptor('RomMk21Disruptor')
RomTorpedoTube('RomTorpedoTube')
RomS2TorpedoTube('RomS2TorpedoTube')
RomS3TorpedoTube('RomS3TorpedoTube')
RomCloakingDevice('RomCloakingDevice')
RomEntDisruptor('RomEntDisruptor')


#####################################################
# Dominion weapons
class DomPolaronBeam(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Polaron Beam'"

	def BaseMaxCharge(self):									return 1.5
	def BaseMinFiringCharge(self):								return 1.0

	def SetMaxDamage(self, args, ship, pStats):					return 3600.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 45.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 0.255
	def SetPhaserTextureStart(self, args, ship, pStats):		return 16
	def SetPhaserTextureEnd(self, args, ship, pStats):			return 23
	def SetPhaserWidth(self, args, ship, pStats):				return 0.3
	def SetMainRadius(self, args, ship, pStats):				return 0.075
	def SetTaperRadius(self, args, ship, pStats):				return 0.03
	def SetCoreScale(self, args, ship, pStats):					return 0.175
	def SetTaperRatio(self, args, ship, pStats):				return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):	return 0.05
	def SetPerimeterTile(self, args, ship, pStats):				return 1.0
	def SetTextureSpeed(self, args, ship, pStats):				return 2.5
	def SetTextureName(self, args, ship, pStats):				return "'Custom/FTB/textures/Tactical/Laurelin_poleron01.tga'"

	def OuterShellColor(self):			return '0.000000, 0.000000, 0.627451, 1.000000'
	def InnerShellColor(self):			return '0.003922, 0.619608, 0.992157, 0.803922'
	def OuterCoreColor(self):			return '0.231373, 0.254902, 0.513726, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class DomPulsePolaron(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Polaron Pulse'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBPulsePolaron'"

	def BaseMaxCharge(self):									return 2.0
	def BaseMinFiringCharge(self):								return 1.0

	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.12
	def SetMaxDamage(self, args, ship, pStats):					return 600.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 80.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 0.25


class DomPDPulsePolaron(DomPulsePolaron):
	def __init__(self, name):
		DomPulsePolaron.__init__(self, name)

	def BaseMaxCharge(self):									return 5.0
	def BaseMinFiringCharge(self):								return 1.0

	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBPDPulsePolaron'"
	def SetMaxDamage(self, args, ship, pStats):					return 300.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 45.0


class DomHeavyPulsePolaron(DomPulsePolaron):
	def __init__(self, name):
		DomPulsePolaron.__init__(self, name)

	def BaseMaxCharge(self):									return 2.2
	def BaseMinFiringCharge(self):								return 1.0

	def SetFireSound(self, args, ship, pStats):					return "'FTB Heavy Polaron'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBHeavyPulsePolaron'"
	def SetMaxDamage(self, args, ship, pStats):					return 3000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 135.0
	def SetCooldownTime(self, args, ship, pStats):				return 5.0


class DomTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

class DomPulseTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)
	def SetMaxReady(self, args, ship, pStats):					return 3


class DomMineLauncher(PulseWeapon):
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBDomMine'"

	def BaseMaxCharge(self):									return 4.0
	def BaseMinFiringCharge(self):								return 1.0
	def SetDumbfire(self, args, ship, pStats):					return '1'

	def SetDisabledPercentage(self, args, ship, pStats):		return 0.75
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.12
	def SetMaxDamage(self, args, ship, pStats):					return 5000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 200.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 4.0


DomPolaronBeam('DomPolaronBeam')
DomPulsePolaron('DomPulsePolaron')
DomPDPulsePolaron('DomPDPulsePolaron')
DomHeavyPulsePolaron('DomHeavyPulsePolaron')
DomTorpedoTube('DomTorpedoTube')
DomPulseTorpedoTube('DomPulseTorpedoTube')
DomMineLauncher('DomMineLauncher')


class BreenPhaser(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Breen Phaser'"

	def BaseMaxCharge(self):									return 1.5
	def BaseMinFiringCharge(self):								return 0.75

	def SetMaxDamage(self, args, ship, pStats):					return 2000.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 20.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetPhaserTextureStart(self, args, ship, pStats):		return '0'
	def SetPhaserTextureEnd(self, args, ship, pStats):			return 7
	def SetPhaserWidth(self, args, ship, pStats):				return 0.3
	def SetMainRadius(self, args, ship, pStats):				return 0.075
	def SetTaperRadius(self, args, ship, pStats):				return 0.03
	def SetCoreScale(self, args, ship, pStats):					return 0.2
	def SetTaperRatio(self, args, ship, pStats):				return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):	return 0.1
	def SetPerimeterTile(self, args, ship, pStats):				return 1.0
	def SetTextureSpeed(self, args, ship, pStats):				return 2.5
	def SetTextureName(self, args, ship, pStats):				return "'Custom/FTB/textures/Tactical/Firesaber_PulseBeam.tga'"

	def OuterShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def InnerShellColor(self):			return '0.000000, 0.721569, 0.039216, 1.000000'
	def OuterCoreColor(self):			return '0.513726, 1.000000, 0.501961, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class BreenDisruptor(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Breen Disruptor'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBFighterDisruptor'"

	def BaseMaxCharge(self):									return 3.0
	def BaseMinFiringCharge(self):								return 2.5

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.14
	def SetMaxDamage(self, args, ship, pStats):					return 200.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 80.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 0.8
	def SetCooldownTime(self, args, ship, pStats):				return 1.0


class BreenDamper(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):					return "'FTB Breen Damper'"
	def SetModuleName(self, args, ship, pStats):				return "'ftb.Projectiles.FTBBreenDamper'"

	def BaseMaxCharge(self):									return 8.0
	def BaseMinFiringCharge(self):								return 2.5

	def SetDisabledPercentage(self, args, ship, pStats):		return PulseWeapon.SetDisabledPercentage(self, args, ship, pStats) * 0.9
	def SetDamageRadiusFactor(self, args, ship, pStats):		return 0.14
	def SetMaxDamage(self, args, ship, pStats):					return 100.0
	def SetMaxDamageDistance(self, args, ship, pStats):			return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):		return 1.0
	def SetCooldownTime(self, args, ship, pStats):				return 60.0


class BreenTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 20.0

BreenPhaser('BreenPhaser')
BreenDisruptor('BreenDisruptor')
BreenDamper('BreenDamper')
BreenTorpedoTube('BreenTorpedoTube')




#####################################################
# Kessok weapons

class KessokPhaser(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def BaseMaxCharge(self):										return 7.0
	def BaseMinFiringCharge(self):									return 4.0

	def SetRepairComplexity(self, args, ship, pStats):				return Phaser.SetRepairComplexity(self, args, ship, pStats) * 0.6
	def SetFireSound(self, args, ship, pStats):						return "'Kessok Phaser'"
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetMaxDamage(self, args, ship, pStats):						return 400.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 120.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	# def SetNumSides(self, args, ship, pStats):						return 8
	def SetPhaserTextureStart(self, args, ship, pStats):			return 1
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 15
	def SetPhaserWidth(self, args, ship, pStats):					return 0.5
	def SetMainRadius(self, args, ship, pStats):					return 0.1
	def SetTaperRadius(self, args, ship, pStats):					return 0.02
	def SetCoreScale(self, args, ship, pStats):						return 0.3
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.1
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 2.5
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga'"

	def OuterShellColor(self):			return '0.000000, 0.501961, 0.749020, 1.000000'
	def InnerShellColor(self):			return '0.000000, 0.501961, 1.000000, 1.000000'
	def OuterCoreColor(self):			return '0.501961, 1.000000, 1.000000, 1.000000'
	def InnerCoreColor(self):			return '0.000000, 1.000000, 1.000000, 1.000000'


class KessokHeavyPhaser(KessokPhaser):
	def __init__(self, name):
		KessokPhaser.__init__(self, name)

	def SetMainRadius(self, args, ship, pStats):					return 0.15
	def SetTaperRadius(self, args, ship, pStats):					return 0.03
	def SetMaxDamage(self, args, ship, pStats):						return 800.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 200.0

class KessokLightPhaser(KessokPhaser):
	def __init__(self, name):
		KessokPhaser.__init__(self, name)

	def SetMainRadius(self, args, ship, pStats):					return 0.1
	def SetTaperRadius(self, args, ship, pStats):					return 0.03
	def SetMaxDamage(self, args, ship, pStats):						return 300.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 120.0

class KessokDoubleTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 50.0
	def SetMaxReady(self, args, ship, pStats):					return 2

class KessokTripleTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 50.0
	def SetMaxReady(self, args, ship, pStats):					return 3

class KessokRepairSystem(RepairSystem):
	def __init__(self, name):
		RepairSystem.__init__(self, name)

	def HullStrengthFactor(self, args, ship, pStats):			return 1.5
	def SetMaxRepairPoints(self, args, ship, pStats):
		return str(float(int(ship.RepairRate() * 100)) / 60.0)
	def SetNumRepairTeams(self, args, ship, pStats):			return 4

KessokPhaser('KessokPhaser')
KessokHeavyPhaser('KessokHeavyPhaser')
KessokLightPhaser('KessokLightPhaser')
KessokDoubleTorpedoTube('KessokDoubleTorpedoTube')
KessokTripleTorpedoTube('KessokTripleTorpedoTube')
KessokRepairSystem('KessokRepairSystem')


#####################################################
# Ferengi weapons

#####################################################
# Cardassian weapons
class FerengiPhaser(Phaser):
	def __init__(self, name):
		Phaser.__init__(self, name)

	def BaseMaxCharge(self):										return 4.5
	def BaseMinFiringCharge(self):									return 3.0

	def SetRepairComplexity(self, args, ship, pStats):				return Phaser.SetRepairComplexity(self, args, ship, pStats) * 0.6
	def SetFireSound(self, args, ship, pStats):						return "'Galor Phaser'"
	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.1
	def SetMaxDamage(self, args, ship, pStats):						return 900.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 40.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	# def SetNumSides(self, args, ship, pStats):						return 8
	def SetPhaserTextureStart(self, args, ship, pStats):			return 1
	def SetPhaserTextureEnd(self, args, ship, pStats):				return 15
	def SetPhaserWidth(self, args, ship, pStats):					return 0.5
	def SetMainRadius(self, args, ship, pStats):					return 0.06
	def SetTaperRadius(self, args, ship, pStats):					return 0.03
	def SetCoreScale(self, args, ship, pStats):						return 0.3
	def SetTaperRatio(self, args, ship, pStats):					return 0.25
	def SetLengthTextureTilePerUnit(self, args, ship, pStats):		return 0.1
	def SetPerimeterTile(self, args, ship, pStats):					return 1.0
	def SetTextureSpeed(self, args, ship, pStats):					return 2.5
	def SetTextureName(self, args, ship, pStats):					return "'Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga'"

	def OuterShellColor(self):			return '0.721569, 0.556863, 0.000000, 1.000000'
	def InnerShellColor(self):			return '0.721569, 0.556863, 0.000000, 1.000000'
	def OuterCoreColor(self):			return '0.984314, 0.756863, 0.058824, 1.000000'
	def InnerCoreColor(self):			return '1.000000, 1.000000, 1.000000, 1.000000'


class FerengiFusionBolt(PulseWeapon):
	def __init__(self, name):
		PulseWeapon.__init__(self, name)

	def SetFireSound(self, args, ship, pStats):						return "'Klingon Disruptor'"
	def SetModuleName(self, args, ship, pStats):					return "'ftb.Projectiles.FTBFusionBolt'"

	def BaseMaxCharge(self):										return 3.0
	def BaseMinFiringCharge(self):									return 2.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 50.0

	def SetDamageRadiusFactor(self, args, ship, pStats):			return 0.08
	def SetMaxDamage(self, args, ship, pStats):						return 600.0
	def SetMaxDamageDistance(self, args, ship, pStats):				return 80.0
	def SetNormalDischargeRate(self, args, ship, pStats):			return 1.0
	def SetCooldownTime(self, args, ship, pStats):					return 0.4

class FerengiTorpedoTube(TorpedoTube):
	def __init__(self, name):
		TorpedoTube.__init__(self, name)

	def SetReloadDelay(self, args, ship, pStats):				return 50.0
	def SetMaxReady(self, args, ship, pStats):					return 2

FerengiPhaser('FerengiPhaser')
FerengiFusionBolt('FerengiFusionBolt')
FerengiTorpedoTube('FerengiTorpedoTube')