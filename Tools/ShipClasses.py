import BCShipRecords

shipList = BCShipRecords.shipList


def Initialize(Race, Ship, raceList, propertyList):

	Race('Bioship')
	Race('Federation')
	Race('Klingon')
	Race('Romulan')
	Race('Ferengi')
	Race('Cardassian')
	Race('Breen')
	Race('Imperial')
	Race('Bajoran')
	Race('Borg')
	Race('ImperialCap')
	Race('Dominion')
	Race('Hirogen')
	Race('Kazon')
	Race('Sona')
	Race('Kessok')

	class FedShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Federation']
			self.SetProperty('Phaser', '.*', propertyList['FedTypeX'])
			self.SetProperty('PulseWeapon', '.*', propertyList['FedC1PulsePhaser'])
			self.SetProperty('TorpedoTube', '.*', propertyList['FedPFTorpedoTube'])
			self.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
			self.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 100], ['FTBMk6PhotonTorpedo', 0], ['FTBQuantumTorpedo', 0], ['FTBTricobalt', 0] ]
			self.SetProperty('RepairSubsystem', '.*', propertyList['FedEngineering'])
			self.SetProperty('Phaser', 'Deflector.*', propertyList['Blank'], { 'terawatts': 0.0 })


	class SmallFedShip(FedShip):
		def __init__(self, name):
			FedShip.__init__(self, name)
			self.SetProperty('PulseWeapon', '.', propertyList['FedPulsePhaser'])
			self.lTorpTypes = [ ['FTBMicroPhotonTorpedo', 5] ]

	class TMPFedShip(FedShip):
		def __init__(self, name):
			FedShip.__init__(self, name)
			self.SetProperty('Phaser', '.*', propertyList['FedTypeVIII'])
			self.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])
			self.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
			self.SetProperty('RepairSubsystem', '.*', propertyList['FedEngineering'])

	class KlingonShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Klingon']
			self.SetProperty('Phaser', '.', propertyList['KliMk12DisruptorBeam'])
			self.SetProperty('PulseWeapon', '.*', propertyList['KliMk6PulseDisruptor'])
			self.SetProperty('PulseWeapon', '.*Mk12.*', propertyList['KliMk12Disruptor'])
			self.SetProperty('PulseWeapon', '.*Mk12.*Pulse.*', propertyList['KliMk12PulseDisruptor'])
			self.SetProperty('PulseWeapon', '.*Mk18.*', propertyList['KliMk18Disruptor'])
			self.SetProperty('TorpedoTube', '.*', propertyList['KliDoubleTorpedoTube'])
			self.SetProperty('CloakingSubsystem', '.*', propertyList['CloakingDevice'])
			self.lTorpTypes = [ ['FTBKlingonTorpedo', 100], ['FTBFastKlingonTorpedo', 100] ]
			self.powerPercent = ('red', 0.6)

		def EngineSound(self):
			return "'Klingon Engines'"

	class RomulanShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Romulan']
			self.SetProperty('Phaser', '.', propertyList['RomDisruptorBeam'])
			self.SetProperty('PulseWeapon', '.', propertyList['RomDisruptor'])
			self.SetProperty('PulseWeapon', '.*Mk21.*', propertyList['RomMk21Disruptor'])
			self.SetProperty('TorpedoTube', '.', propertyList['RomTorpedoTube'])
			self.SetProperty('CloakingSubsystem', '.*', propertyList['RomCloakingDevice'])
			self.lTorpTypes = [ ['FTBRomTorpedo', 100], ['FTBRomPlasmaBurst', 10] ]

		def EngineSound(self):
			return "'Romulan Engines'"

	class FerengiShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Ferengi']
			self.SetProperty('Phaser', '.', propertyList['FerengiPhaser'])
			self.SetProperty('PulseWeapon', '.', propertyList['FerengiFusionBolt'])
			self.SetProperty('TorpedoTube', '.', propertyList['FerengiTorpedoTube'])
		def EngineSound(self):
			return "'Ferengi Engines'"


	class BaseCardassianShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Cardassian']
			self.SetProperty('Phaser', '.*', propertyList['CardTypeVII'])
			self.SetProperty('Phaser', '.*TypeVIII.*', propertyList['CardTypeVIII'])
			self.SetProperty('Phaser', '.*TypeIX.*', propertyList['CardTypeIX'])
			self.SetProperty('Phaser', '.*TypeX.*', propertyList['CardTypeX'])
			self.SetProperty('Phaser', '.*Small.*', propertyList['CardTypeVIISmall'])
			self.SetProperty('Phaser', '.*Spiral.*', propertyList['CardHiPower'], { 'terawatts': 4.0 })
			self.SetProperty('PulseWeapon', '.', propertyList['CardDisruptor'])
			self.SetProperty('TorpedoTube', '.', propertyList['CardTorpedoTube'])
			self.SetProperty('CloakingSubsystem', '.*', propertyList['CloakingDevice'])
			self.SetProperty('WeaponSystem', '.*Compress.*', propertyList['PhaserSystem'])
			self.lTorpTypes = [ ['FTBCardTorpedo', 0], ['FTBCardPlasmaBurst', 0] ]

		def EngineSound(self):
			return "'Cardassian Engines'"


	class CardassianShip(BaseCardassianShip):
		def __init__(self, name):
			BaseCardassianShip.__init__(self, name)
			self.SetProperty('Phaser', '.*', propertyList['CardTypeVII'])
			self.SetProperty('Phaser', '.*TypeVIII.*', propertyList['CardTypeVIII'])
			self.SetProperty('Phaser', '.*TypeIX.*', propertyList['CardTypeIX'])
			self.SetProperty('Phaser', '.*TypeX.*', propertyList['CardTypeX'])
			self.SetProperty('Phaser', '.*Small.*', propertyList['CardTypeVIISmall'])
			self.SetProperty('Phaser', '.*Spiral.*', propertyList['CardHiPower'], { 'terawatts': 4.0 })
			self.SetProperty('TorpedoTube', '.', propertyList['CardTorpedoTube'])
			self.SetProperty('CloakingSubsystem', '.*', propertyList['CloakingDevice'])
			self.SetProperty('WeaponSystem', '.*Compress.*', propertyList['PhaserSystem'])

	class SmallCardassianShip(BaseCardassianShip):
		def __init__(self, name):
			BaseCardassianShip.__init__(self, name)
			self.SetProperty('Phaser', '.*', propertyList['CardTypeVIISmall'])
			self.lTorpTypes = [ ['FTBMicroCardTorpedo', 0] ]

	class CardassianBase(BaseCardassianShip):
		def __init__(self, name):
			BaseCardassianBase.__init__(self, name)
			self.SetProperty('Phaser', '.*', propertyList['CardTypeX'])
			self.SetProperty('Phaser', '.*TypeVIII.*', propertyList['CardTypeVIII'])
			self.SetProperty('Phaser', '.*TypeIX.*', propertyList['CardTypeIX'])
			self.SetProperty('Phaser', '.*TypeX.*', propertyList['CardTypeX'])
			self.SetProperty('Phaser', '.*Small.*', propertyList['CardTypeVIISmall'])
			self.SetProperty('Phaser', '.*Spiral.*', propertyList['CardHiPower'], { 'terawatts': 4.0 })
			self.SetProperty('TorpedoTube', '.', propertyList['CardTorpedoTube'])
			self.SetProperty('CloakingSubsystem', '.*', propertyList['CloakingDevice'])
			self.SetProperty('WeaponSystem', '.*Compress.*', propertyList['MultiFirePhaserSystem'])

	class BreenShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Breen']
			self.SetProperty('Phaser', '.', propertyList['BreenPhaser'] )
			self.SetProperty('PulseWeapon', '.', propertyList['BreenDisruptor'] )
			self.SetProperty('TorpedoTube', '.', propertyList['BreenTorpedoTube'])
			self.lTorpTypes = [ ['FTBBreenTorpedo', 50], ['FTBBreenDamper', 1] ]

	class ImperialShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Imperial']

	class BajoranShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Bajoran']

	class BorgShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Borg']

	class ImperialCapShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['ImperialCap']

	class DominionShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Dominion']
			self.SetProperty('Phaser', '.', propertyList['DomPolaronBeam'])
			self.SetProperty('PulseWeapon', '.', propertyList['DomPulsePolaron'])
			self.SetProperty('PulseWeapon', '.*PD.*', propertyList['DomPDPulsePolaron'])
			self.SetProperty('PulseWeapon', '.*Heavy.*', propertyList['DomHeavyPulsePolaron'])
			self.SetProperty('TorpedoTube', '.', propertyList['DomTorpedoTube'])
			self.lTorpTypes = [ ['FTBPolaronTorpedo', 100], ['FTBMicroPolaronTorpedo', 100] ]

	class HirogenShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Hirogen']

	class KazonShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Kazon']

	class SonaShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Sona']

	class KessokShip(Ship):
		def __init__(self, name):
			Ship.__init__(self, name)
			self.stats['race'] = raceList['Kessok']
			self.powerPercent = ('red', 0.8)
			self.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
			self.SetProperty('Phaser', '.*', propertyList['KessokPhaser'])
			self.SetProperty('PulseWeapon', '.*', propertyList['DomPulsePolaron'])
			self.SetProperty('TorpedoTube', '.*', propertyList['KessokDoubleTorpedoTube'])
			self.SetProperty('RepairSubsystem', '.*', propertyList['KessokRepairSystem'])

	s8472bioship = Ship('8472bioship')
	s8472bioship.stats['cost'] = 1560
	s8472bioship.stats['crew'] = 50
	s8472bioship.stats['hullIndex'] = 2400
	s8472bioship.stats['length'] = 200
	s8472bioship.stats['width'] = 20
	s8472bioship.stats['height'] = 40
	s8472bioship.stats['maneuverIndex'] = 10000
	s8472bioship.stats['maneuverThrustIndex'] = 10000
	s8472bioship.stats['mass'] = 120000
	s8472bioship.stats['maxVelocity'] = 900
	s8472bioship.stats['rangeIndex'] = 2315
	s8472bioship.stats['sensorIndex'] = 1000
	s8472bioship.stats['shieldIndex'] = 2580
	s8472bioship.stats['terawatts'] = 400000
	s8472bioship.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	s8472bioship.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	asteroid = FedShip('asteroid')
	asteroid.stats['cost'] = 1250
	asteroid.stats['crew'] = 500
	asteroid.stats['hullIndex'] = 200
	asteroid.stats['length'] = 464.43
	asteroid.stats['width'] = 316.67
	asteroid.stats['height'] = 87.43
	asteroid.stats['maneuverIndex'] = 4500
	asteroid.stats['maneuverThrustIndex'] = 4500
	asteroid.stats['mass'] = 3055000
	asteroid.stats['maxVelocity'] = 575
	asteroid.stats['rangeIndex'] = 640
	asteroid.stats['sensorIndex'] = 800
	asteroid.stats['shieldIndex'] = 695
	asteroid.stats['terawatts'] = 17500
	asteroid.SetShields( {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 } )
	asteroid.SetShieldCharge( {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 } )
	asteroid.SetProperty('Hull', '.*', propertyList['SolidMass'])
	asteroid.powerPercent = ('red', 0.52)
	shipList.Register(asteroid, 'asteroid1')
	shipList.Register(asteroid, 'asteroid2')
	shipList.Register(asteroid, 'asteroid3')
	shipList.Register(asteroid, 'amagon')

	asteroidh = FedShip('asteroidh')
	asteroidh.stats['cost'] = 1250
	asteroidh.stats['crew'] = 500
	asteroidh.stats['hullIndex'] = 40000
	asteroidh.stats['length'] = 464.43
	asteroidh.stats['width'] = 316.67
	asteroidh.stats['height'] = 87.43
	asteroidh.stats['maneuverIndex'] = 4500
	asteroidh.stats['maneuverThrustIndex'] = 4500
	asteroidh.stats['mass'] = 3055000
	asteroidh.stats['maxVelocity'] = 575
	asteroidh.stats['rangeIndex'] = 640
	asteroidh.stats['sensorIndex'] = 800
	asteroidh.stats['shieldIndex'] = 695
	asteroidh.stats['terawatts'] = 17500
	asteroidh.SetShields( {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 } )
	asteroidh.SetShieldCharge( {'front': 0, 'rear': 0, 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 } )
	asteroidh.SetProperty('Hull', '.*', propertyList['SolidMass'])
	asteroidh.powerPercent = ('red', 0.52)
	shipList.Register(asteroidh, 'asteroidh1')
	shipList.Register(asteroidh, 'asteroidh2')
	shipList.Register(asteroidh, 'asteroidh3')

	akira = FedShip('akira')
	akira.stats['cost'] = 1250
	akira.stats['crew'] = 500
	akira.stats['hullIndex'] = 640
	akira.stats['length'] = 464.43
	akira.stats['width'] = 316.67
	akira.stats['height'] = 87.43
	akira.stats['maneuverIndex'] = 4500
	akira.stats['maneuverThrustIndex'] = 4500
	akira.stats['mass'] = 3055000
	akira.stats['maxVelocity'] = 575
	akira.stats['rangeIndex'] = 640
	akira.stats['sensorIndex'] = 800
	akira.stats['shieldIndex'] = 695
	akira.stats['terawatts'] = 17500
	akira.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	akira.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	akira.SetProperty('Phaser', '.*Phaser.*', propertyList['FedTypeX'])
	akira.SetProperty('TorpedoTube', '.*', propertyList['FedSingleTorpedoTube'])
	akira.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	akira.powerPercent = ('red', 0.52)
	akira.battery = 200
	akira.bakBattery = 150
	akira.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 150], ['FTBMk6PhotonTorpedo', 150] ]
	shipList.Register(akira, 'akirageronimo')

	ambassador = FedShip('ambassador')
	ambassador.stats['cost'] = 720
	ambassador.stats['crew'] = 550
	ambassador.stats['hullIndex'] = 800
	ambassador.stats['length'] = 526
	ambassador.stats['width'] = 320
	ambassador.stats['height'] = 125
	ambassador.stats['maneuverIndex'] = 1500
	ambassador.stats['maneuverThrustIndex'] = 1500
	ambassador.stats['mass'] = 2350000
	ambassador.stats['maxVelocity'] = 550
	ambassador.stats['rangeIndex'] = 880
	ambassador.stats['sensorIndex'] = 850
	ambassador.stats['shieldIndex'] = 750
	ambassador.stats['terawatts'] = 30000
	ambassador.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ambassador.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ambassador.SetProperty('Phaser', '.*Phaser.*', propertyList['FedTypeIX'])
	ambassador.SetProperty('TorpedoTube', '.*', propertyList['FedType2BurstTorpedoTube'])
	ambassador.battery = 375
	ambassador.lTorpTypes = [ ['FTBMk4PhotonTorpedo', 150], ['FTBMk4PhotonTorpedoS', 10], ['FTBMk4PhotonTorpedoM', 5] ]
	ambassador.bakBattery = 180

	assaultgunboat = ImperialShip('assaultgunboat')
	assaultgunboat.stats['cost'] = 60
	assaultgunboat.stats['crew'] = 1
	assaultgunboat.stats['maneuverIndex'] = 6000
	assaultgunboat.stats['maneuverThrustIndex'] = 6000
	assaultgunboat.stats['mass'] = 40
	assaultgunboat.stats['maxVelocity'] = 540
	assaultgunboat.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	assaultgunboat.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	assaulttransport = ImperialShip('assaulttransport')
	assaulttransport.stats['cost'] = 125
	assaulttransport.stats['crew'] = 4
	assaulttransport.stats['maneuverIndex'] = 2000
	assaulttransport.stats['maneuverThrustIndex'] = 2000
	assaulttransport.stats['mass'] = 40
	assaulttransport.stats['maxVelocity'] = 400
	assaulttransport.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	assaulttransport.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	bailey = FedShip('bailey')
	bailey.stats['cost'] = 1050
	bailey.stats['crew'] = 700
	bailey.stats['hullIndex'] = 600
	bailey.stats['length'] = 600
	bailey.stats['width'] = 600
	bailey.stats['height'] = 600
	bailey.stats['maneuverIndex'] = 25
	bailey.stats['maneuverThrustIndex'] = 25
	bailey.stats['mass'] = 2500000
	bailey.stats['maxVelocity'] = 350
	bailey.stats['rangeIndex'] = 1260
	bailey.stats['sensorIndex'] = 500
	bailey.stats['shieldIndex'] = 2700
	bailey.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	bailey.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	bailey.stats['terawatts'] = 36000
	bailey.SetProperty('Phaser', '.*Phaser.*', propertyList['FedTypeX'])

	bajoranassaultcraft = BajoranShip('bajoranassaultcraft')
	bajoranassaultcraft.stats['cost'] = 25
	bajoranassaultcraft.stats['crew'] = 1
	bajoranassaultcraft.stats['hullIndex'] = 10
	bajoranassaultcraft.stats['length'] = 140.72
	bajoranassaultcraft.stats['width'] =  221.76 
	bajoranassaultcraft.stats['height'] = 51.76
	bajoranassaultcraft.stats['maneuverIndex'] = 9000
	bajoranassaultcraft.stats['maneuverThrustIndex'] = 9000
	bajoranassaultcraft.stats['mass'] = 35
	bajoranassaultcraft.stats['maxVelocity'] = 800
	bajoranassaultcraft.stats['rangeIndex'] = 20
	bajoranassaultcraft.stats['sensorIndex'] = 400
	bajoranassaultcraft.stats['shieldIndex'] = 4
	bajoranassaultcraft.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	bajoranassaultcraft.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	bajoranassaultcraft.stats['terawatts'] = 1000

	bakrus = CardassianShip('bakrus')
	bakrus.stats['cost'] = 550
	bakrus.stats['crew'] = 680
	bakrus.stats['hullIndex'] = 900
	bakrus.stats['length'] = 300
	bakrus.stats['width'] = 300
	bakrus.stats['height'] = 66
	bakrus.stats['maneuverIndex'] = 4000
	bakrus.stats['maneuverThrustIndex'] = 1000
	bakrus.stats['mass'] = 1450000
	bakrus.stats['maxVelocity'] = 500
	bakrus.stats['rangeIndex'] = 500
	bakrus.stats['sensorIndex'] = 600
	bakrus.stats['shieldIndex'] = 870
	bakrus.SetShields( {'front': 1.75, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 0.75, 'right': 0.75 } )
	bakrus.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	bakrus.stats['terawatts'] = 20750
	bakrus.powerPercent = ('red', 0.66)
	bakrus.battery = 120
	bakrus.bakBattery = 60
	bakrus.SetProperty('Phaser', '.*Spiral.*', propertyList['CardHiPower'], { 'maxCharge': 0.4, 'terawatts': 4.0 })
	bakrus.lTorpTypes = [ ['FTBCardPlasmaBurst', 50] ]

	boreth = KlingonShip('boreth')
	boreth.stats['cost'] = 830
	boreth.stats['crew'] = 150
	boreth.stats['hullIndex'] = 480
	boreth.stats['length'] = 480
	boreth.stats['width'] = 300
	boreth.stats['height'] = 80
	boreth.stats['maneuverIndex'] = 10000
	boreth.stats['maneuverThrustIndex'] = 10000
	boreth.stats['mass'] = 120000
	boreth.stats['maxVelocity'] = 800
	boreth.stats['rangeIndex'] = 415
	boreth.stats['sensorIndex'] = 700
	boreth.stats['shieldIndex'] = 550
	boreth.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	boreth.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	boreth.stats['terawatts'] = 17000
	boreth.SetProperty('TorpedoTube', '.*', propertyList['KliTripleTorpedoTube'])
	boreth.SetProperty('WeaponSystem', '.*', propertyList['PhaserSystem'])

	borgcube = BorgShip('borgcube')
	borgcube.stats['blastradiusdamage'] = 1000
	borgcube.stats['blastradiusshockwave'] = 1
	borgcube.stats['cost'] = 80000
	borgcube.stats['crew'] = 5000
	borgcube.stats['hullIndex'] = 10000
	borgcube.stats['length'] = 3036
	borgcube.stats['width'] = 3036
	borgcube.stats['height'] = 3036
	borgcube.stats['maneuverIndex'] = 10000
	borgcube.stats['maneuverThrustIndex'] = 10000
	borgcube.stats['mass'] = 90000000
	borgcube.stats['maxVelocity'] = 700
	borgcube.stats['rangeIndex'] = 2675
	borgcube.stats['sensorIndex'] = 3000
	borgcube.stats['shieldIndex'] = 10670
	borgcube.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgcube.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgcube.stats['terawatts'] = 750000

	borgdiamond = BorgShip('borgdiamond')
	borgdiamond.stats['cost'] = 800
	borgdiamond.stats['crew'] = 20
	borgdiamond.stats['hullIndex'] = 4700
	borgdiamond.stats['length'] = 2000
	borgdiamond.stats['width'] = 2000
	borgdiamond.stats['height'] = 2000
	borgdiamond.stats['maneuverIndex'] = 10000
	borgdiamond.stats['maneuverThrustIndex'] = 10000
	borgdiamond.stats['mass'] = 2800000
	borgdiamond.stats['maxVelocity'] = 600
	borgdiamond.stats['rangeIndex'] = 1075
	borgdiamond.stats['sensorIndex'] = 3000
	borgdiamond.stats['shieldIndex'] = 870
	borgdiamond.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgdiamond.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgdiamond.stats['terawatts'] = 20000

	borgprobe = BorgShip('borgprobe')
	borgprobe.stats['cost'] = 30
	borgprobe.stats['crew'] = 0
	borgprobe.stats['hullIndex'] = 15
	borgprobe.stats['length'] = 360
	borgprobe.stats['width'] = 100
	borgprobe.stats['height'] = 60
	borgprobe.stats['maneuverIndex'] = 12500
	borgprobe.stats['maneuverThrustIndex'] = 12500
	borgprobe.stats['mass'] = 500
	borgprobe.stats['maxVelocity'] = 750
	borgprobe.stats['rangeIndex'] = 475
	borgprobe.stats['sensorIndex'] = 3000
	borgprobe.stats['shieldIndex'] = 10
	borgprobe.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgprobe.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgprobe.stats['terawatts'] = 2000

	borgscout = BorgShip('borgscout')
	borgscout.stats['cost'] = 800
	borgscout.stats['crew'] = 5
	borgscout.stats['hullIndex'] = 160
	borgscout.stats['length'] = 160
	borgscout.stats['width'] = 160
	borgscout.stats['height'] = 160
	borgscout.stats['maneuverIndex'] = 5500
	borgscout.stats['maneuverThrustIndex'] = 5500
	borgscout.stats['mass'] = 5000
	borgscout.stats['maxVelocity'] = 675
	borgscout.stats['rangeIndex'] = 875
	borgscout.stats['sensorIndex'] = 3000
	borgscout.stats['shieldIndex'] = 90
	borgscout.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgscout.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgscout.stats['terawatts'] = 40000

	borgsphere = BorgShip('borgsphere')
	borgsphere.stats['cost'] = 1500
	borgsphere.stats['crew'] = 50
	borgsphere.stats['hullIndex'] = 5440
	borgsphere.stats['length'] = 600
	borgsphere.stats['width'] = 600
	borgsphere.stats['height'] = 600
	borgsphere.stats['maneuverIndex'] = 10000
	borgsphere.stats['maneuverThrustIndex'] = 10000
	borgsphere.stats['mass'] = 4200000
	borgsphere.stats['maxVelocity'] = 700
	borgsphere.stats['rangeIndex'] = 830
	borgsphere.stats['sensorIndex'] = 3000
	borgsphere.stats['shieldIndex'] = 500
	borgsphere.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgsphere.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgsphere.stats['terawatts'] = 50000

	borgtaccube = BorgShip('taccube')
	borgtaccube.stats['cost'] = 80000
	borgtaccube.stats['crew'] = 5000
	borgtaccube.stats['hullIndex'] = 10000
	borgtaccube.stats['length'] = 3036
	borgtaccube.stats['width'] = 3036
	borgtaccube.stats['height'] = 3036
	borgtaccube.stats['maneuverIndex'] = 20000
	borgtaccube.stats['maneuverThrustIndex'] = 20000
	borgtaccube.stats['mass'] = 900000000
	borgtaccube.stats['maxVelocity'] = 700
	borgtaccube.stats['rangeIndex'] = 2675
	borgtaccube.stats['sensorIndex'] = 3000
	borgtaccube.stats['shieldIndex'] = 10670
	borgtaccube.SetShields( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgtaccube.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	borgtaccube.stats['terawatts'] = 5000000
	borgtaccube.SetProperty('Phaser', '.', propertyList['KliMk12DisruptorBeam'] )
	borgtaccube.SetProperty('PulseWeapon', '.', propertyList['KliMk12PulseDisruptor'] )
	borgtaccube.SetProperty('TorpedoTube', '.', propertyList['KliTripleTorpedoTube'])

	breenfrigate = BreenShip('breenfrigate')
	breenfrigate.stats['cost'] = 280
	breenfrigate.stats['crew'] = 40
	breenfrigate.stats['hullIndex'] = 175
	breenfrigate.stats['length'] = 300
	breenfrigate.stats['width'] = 245
	breenfrigate.stats['height'] = 40
	breenfrigate.stats['maneuverIndex'] = 10000
	breenfrigate.stats['maneuverThrustIndex'] = 10000
	breenfrigate.stats['mass'] = 50000
	breenfrigate.stats['maxVelocity'] = 750
	breenfrigate.stats['rangeIndex'] = 450
	breenfrigate.stats['sensorIndex'] = 500
	breenfrigate.stats['shieldIndex'] = 250
	breenfrigate.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenfrigate.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenfrigate.stats['terawatts'] = 5000
	breenfrigate.powerPercent = ('red', 0.6)
	breenfrigate.battery = 200
	breenfrigate.bakBattery = 60
	breenfrigate.SetProperty('PulseWeapon', 'Cannon 1', propertyList['BreenDamper'])

	breenfighter = BreenShip('breenfighter')
	breenfighter.stats['cost'] = 60
	breenfighter.stats['crew'] = 1
	breenfighter.stats['hullIndex'] = 160
	breenfighter.stats['length'] = 300 * 0.2
	breenfighter.stats['width'] = 245 * 0.2
	breenfighter.stats['height'] = 40 * 0.2
	breenfighter.stats['maneuverIndex'] = 30000
	breenfighter.stats['maneuverThrustIndex'] = 10000
	breenfighter.stats['mass'] = 80
	breenfighter.stats['maxVelocity'] = 800
	breenfighter.stats['rangeIndex'] = 20
	breenfighter.stats['sensorIndex'] = 400
	breenfighter.stats['shieldIndex'] = 40
	breenfighter.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenfighter.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenfighter.powerPercent = ('red', 0.7)
	breenfighter.stats['terawatts'] = 3000

	breenmpwg = BreenShip('breenmpwg')
	breenmpwg.stats['cost'] = 550
	breenmpwg.stats['crew'] = 40
	breenmpwg.stats['hullIndex'] = 750
	breenmpwg.stats['length'] = 300 * 1.2
	breenmpwg.stats['width'] = 245 * 1.2
	breenmpwg.stats['height'] = 40 * 1.2
	breenmpwg.stats['maneuverIndex'] = 5000
	breenmpwg.stats['maneuverThrustIndex'] = 5000
	breenmpwg.stats['mass'] = 120000
	breenmpwg.stats['maxVelocity'] = 675
	breenmpwg.stats['rangeIndex'] = 250
	breenmpwg.stats['sensorIndex'] = 500
	breenmpwg.stats['shieldIndex'] = 750
	breenmpwg.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenmpwg.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	breenmpwg.stats['terawatts'] = 6000

	kvort = KlingonShip('kvort')
	kvort.stats['cost'] = 385
	kvort.stats['crew'] = 390
	kvort.stats['hullIndex'] = 700 * 1.2
	kvort.stats['length'] = 327
	kvort.stats['width'] = 276
	kvort.stats['height'] = 60
	kvort.stats['maneuverIndex'] = 2800
	kvort.stats['maneuverThrustIndex'] = 2800
	kvort.stats['mass'] = 800000
	kvort.stats['maxVelocity'] = 575
	kvort.stats['rangeIndex'] = 370
	kvort.stats['sensorIndex'] = 500
	kvort.stats['shieldIndex'] = 325 + 150
	kvort.stats['terawatts'] = 14250
	kvort.SetShields( {'front': 1.5, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	kvort.SetShieldCharge( {'front': 1.25, 'rear': 0.75, 'top': 1.25, 'bottom': 1.25, 'left': 0.75, 'right': 0.75 } )
	kvort.SetProperty('PulseWeapon', '.*Cannon', propertyList['Blank'], { 'terawatts': 0.0 })
	kvort.SetProperty('PulseWeapon', '.*', propertyList['KliMk6PulseDisruptor'], { 'terawatts': 0.2 })
	kvort.SetProperty('PulseWeapon', '.*Mk12.*', propertyList['KliMk12PulseDisruptor'])
	kvort.SetProperty('TorpedoTube', '.*', propertyList['KliTripleTorpedoTube'])
	kvort.battery = 200
	kvort.bakBattery = 90
	kvort.SetProperty('WeaponSystem', '.*', propertyList['MultiFirePhaserSystem'])
	kvort.lTorpTypes[0][1] = 85
	kvort.lTorpTypes[1][1] = 150
	shipList.Register(kvort, 'rankuf')

	brel = KlingonShip('brel')
	brel.stats['cost'] = 260
	brel.stats['crew'] = 25
	brel.stats['hullIndex'] = 500
	brel.stats['length'] = 109
	brel.stats['width'] = 92
	brel.stats['height'] = 20
	brel.stats['maneuverIndex'] = 11650 + 5000
	brel.stats['maneuverThrustIndex'] = 18000
	brel.stats['mass'] = 30000
	brel.stats['maxVelocity'] = 725
	brel.stats['rangeIndex'] = 200
	brel.stats['sensorIndex'] = 400
	brel.stats['shieldIndex'] = 120 + 100
	brel.SetShields( {'front': 1.5, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	brel.SetShieldCharge( {'front': 1.25, 'rear': 0.75, 'top': 1.25, 'bottom': 1.25, 'left': 0.75, 'right': 0.75 } )
	brel.stats['terawatts'] = 10000
	brel.SetProperty('PulseWeapon', '.', propertyList['KliMk6PulseDisruptor'])
	brel.SetProperty('TorpedoTube', '.*', propertyList['KliSingleTorpedoTube'])
	brel.SetProperty('WeaponSystem', '.*', propertyList['MultiFirePhaserSystem'])
	brel.powerPercent = ('red', 0.7)
	brel.battery = 140
	brel.bakBattery = 50
	brel.lTorpTypes = [ ['FTBFastKlingonTorpedo', 35] ]
	shipList.Register(brel, 'brel')

	birdofprey = KlingonShip('birdofprey')
	birdofprey.stats['cost'] = 260
	birdofprey.stats['crew'] = 25
	birdofprey.stats['hullIndex'] = 200
	birdofprey.stats['length'] = 109
	birdofprey.stats['width'] = 92
	birdofprey.stats['height'] = 20
	birdofprey.stats['maneuverIndex'] = 18000
	birdofprey.stats['maneuverThrustIndex'] = 18000
	birdofprey.stats['mass'] = 30000
	birdofprey.stats['maxVelocity'] = 725
	birdofprey.stats['rangeIndex'] = 200
	birdofprey.stats['sensorIndex'] = 300
	birdofprey.stats['shieldIndex'] = 235
	birdofprey.SetShields( {'front': 1.5, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	birdofprey.SetShieldCharge( {'front': 3.5, 'rear': 1.25, 'top': 3.5, 'bottom': 3.5, 'left': 1.75, 'right': 1.75 } )
	birdofprey.stats['terawatts'] = 10250
	birdofprey.SetProperty('PulseWeapon', '.', propertyList['KliMk6PulseDisruptor'])
	birdofprey.SetProperty('TorpedoTube', '.*', propertyList['KliSingleTorpedoTube'])
	birdofprey.powerPercent = ('red', 0.62)
	birdofprey.battery = 250
	birdofprey.bakBattery = 50
	birdofprey.lTorpTypes = [ ['FTBFastKlingonTorpedo', 35] ]
	shipList.Register(birdofprey, 'birdofprey')


	cardassianrepairfacility = CardassianShip('cardassianrepairfacility')
	cardassianrepairfacility.stats['cost'] = 1500
	cardassianrepairfacility.stats['crew'] = 5500
	cardassianrepairfacility.stats['hullIndex'] = 5000
	cardassianrepairfacility.stats['length'] = 5000
	cardassianrepairfacility.stats['width'] = 5000
	cardassianrepairfacility.stats['height'] = 5000
	cardassianrepairfacility.stats['immobile'] = 'TRUE'
	cardassianrepairfacility.stats['maneuverIndex'] = 0
	cardassianrepairfacility.stats['maneuverThrustIndex'] = 0
	cardassianrepairfacility.stats['mass'] = 81600000
	cardassianrepairfacility.stats['maxVelocity'] = 50
	cardassianrepairfacility.stats['rangeIndex'] = 1100
	cardassianrepairfacility.stats['sensorIndex'] = 1200
	cardassianrepairfacility.stats['shieldIndex'] = 7000
	cardassianrepairfacility.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cardassianrepairfacility.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cardassianrepairfacility.stats['terawatts'] = 80000

	cardhybrid = CardassianShip('cardhybrid')
	cardhybrid.stats['cost'] = 550 * 2.0
	cardhybrid.stats['crew'] = 680
	cardhybrid.stats['hullIndex'] = 1154
	cardhybrid.stats['length'] = 300
	cardhybrid.stats['width'] = 300
	cardhybrid.stats['height'] = 66
	cardhybrid.stats['maneuverIndex'] = 1600
	cardhybrid.stats['maneuverThrustIndex'] = 1200
	cardhybrid.stats['mass'] = 1550000
	cardhybrid.stats['maxVelocity'] = 500 * 0.75
	cardhybrid.stats['rangeIndex'] = 1200
	cardhybrid.stats['sensorIndex'] = 867
	cardhybrid.stats['shieldIndex'] = 870 * 2.0
	cardhybrid.SetShields( {'front': 1.5, 'rear': 0.5, 'top': 1.5, 'bottom': 1.5, 'left': 0.75, 'right': 0.75 } )
	cardhybrid.SetShieldCharge( {'front': 4, 'rear': 3, 'top': 4, 'bottom': 3, 'left': 3, 'right': 3 } )
	cardhybrid.stats['terawatts'] = 20750 * 2.5
	cardhybrid.powerPercent = ('red', 0.7)
	cardhybrid.battery = 120
	cardhybrid.bakBattery = 60
	cardhybrid.SetProperty('Phaser', '^Forward Beam.*', propertyList['KessokHeavyPhaser'], { 'terawatts': 2.0 })
	cardhybrid.SetProperty('Phaser', '.*Beam.*', propertyList['KessokPhaser'], { 'terawatts': 1.0 })
	cardhybrid.SetProperty('Phaser', '.*Spiral.*', propertyList['CardHiPower'], { 'maxCharge': 0.4, 'terawatts': 4.0 })
	cardhybrid.SetProperty('WeaponSystem', 'Beams', propertyList['MultiFirePhaserSystem'])
	cardhybrid.lTorpTypes = [ ['FTBAntimatterTorpedo', 50] ]

	cargoferry = ImperialShip('cargoferry')
	cargoferry.stats['cost'] = 650
	cargoferry.stats['crew'] = 2
	cargoferry.stats['maneuverIndex'] = 15000
	cargoferry.stats['maneuverThrustIndex'] = 15000
	cargoferry.stats['mass'] = 364500
	cargoferry.stats['maxVelocity'] = 475
	cargoferry.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cargoferry.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	carrack = ImperialCapShip('carrack')
	carrack.stats['cost'] = 500
	carrack.stats['crew'] = 4000
	carrack.stats['maneuverIndex'] = 210
	carrack.stats['maneuverThrustIndex'] = 210
	carrack.stats['mass'] = 214375
	carrack.stats['maxVelocity'] = 480
	carrack.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	carrack.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	cerberus = DominionShip('cerberus')
	cerberus.stats['cost'] = 650
	cerberus.stats['crew'] = 102
	cerberus.stats['hullIndex'] = 800
	cerberus.stats['length'] = 300
	cerberus.stats['width'] = 200
	cerberus.stats['height'] = 80
	cerberus.stats['maneuverIndex'] = 3925
	cerberus.stats['maneuverThrustIndex'] = 5000
	cerberus.stats['mass'] = 170000
	cerberus.stats['maxVelocity'] = 500
	cerberus.stats['rangeIndex'] = 175
	cerberus.stats['sensorIndex'] = 900
	cerberus.stats['shieldIndex'] = 740
	cerberus.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cerberus.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cerberus.stats['terawatts'] = 28000
	cerberus.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])

	churchill = TMPFedShip('churchill')
	churchill.stats['cost'] = 295
	churchill.stats['crew'] = 405
	churchill.stats['hullIndex'] = 130
	churchill.stats['length'] =  312 ## Length
	churchill.stats['width'] = 156 ## Beam
	churchill.stats['height'] = 68 ## Draft
	churchill.stats['maneuverIndex'] = 900
	churchill.stats['maneuverThrustIndex'] = 4500
	churchill.stats['mass'] = 1470000
	churchill.stats['maxVelocity'] = 625
	churchill.stats['rangeIndex'] = 405
	churchill.stats['sensorIndex'] = 500
	churchill.stats['shieldIndex'] = 450
	churchill.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	churchill.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	churchill.stats['terawatts'] = 17500
	churchill.SetProperty('TorpedoTube', '.*', propertyList['FedStdTorpedoTube'])
	churchill.SetProperty('Phaser', '.*', propertyList['FedTMPVIIa'])
	churchill.SetProperty('Phaser', '.*b', propertyList['FedTMPVIIb'])
	churchill.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
	churchill.powerPercent = ('red', 0.5)
	churchill.battery = 120
	churchill.bakBattery = 90
	churchill.lTorpTypes[0][1] = 300

	constellation = FedShip('constellation')
	constellation.stats['cost'] = 230
	constellation.stats['crew'] = 280
	constellation.stats['hullIndex'] = 150
	constellation.stats['length'] = 231
	constellation.stats['width'] = 135
	constellation.stats['height'] = 65
	constellation.stats['maneuverIndex'] = 6000
	constellation.stats['maneuverThrustIndex'] = 6000
	constellation.stats['mass'] = 230000
	constellation.stats['maxVelocity'] = 750
	constellation.stats['rangeIndex'] = 255
	constellation.stats['sensorIndex'] = 600
	constellation.stats['shieldIndex'] = 440
	constellation.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constellation.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constellation.stats['terawatts'] = 8000
	constellation.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])
	constellation.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	constellation.SetProperty('Phaser', '.*', propertyList['FedTypeVIIIBank'], { 'maxCharge': 0.3 })
	constellation.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 200] ]
	shipList.Register(constellation, 'constellationtng')

	constellationtmp = FedShip('constellationtmp')
	constellationtmp.stats['cost'] = 230
	constellationtmp.stats['crew'] = 280
	constellationtmp.stats['hullIndex'] = 150
	constellationtmp.stats['length'] = 231
	constellationtmp.stats['width'] = 135
	constellationtmp.stats['height'] = 65
	constellationtmp.stats['maneuverIndex'] = 2000
	constellationtmp.stats['maneuverThrustIndex'] = 2000
	constellationtmp.stats['mass'] = 230000
	constellationtmp.stats['maxVelocity'] = 550
	constellationtmp.stats['rangeIndex'] = 255
	constellationtmp.stats['sensorIndex'] = 300
	constellationtmp.stats['shieldIndex'] = 220
	constellationtmp.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constellationtmp.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constellationtmp.stats['terawatts'] = 8000
	constellationtmp.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])
	constellationtmp.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
	constellationtmp.SetProperty('Phaser', '.*', propertyList['FedTMPVIIIa'])
	constellationtmp.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIIb'])
	constellationtmp.lTorpTypes = [ ['FTBMk1PhotonTorpedo', 200] ]
	shipList.Register(constellationtmp, 'constellation')


	constitution = TMPFedShip('constitutionncc1701')
	constitution.stats['cost'] = 300
	constitution.stats['crew'] = 450
	constitution.stats['hullIndex'] = 10 * 10.0
	constitution.stats['length'] = 289
	constitution.stats['width'] = 130
	constitution.stats['height'] = 67
	constitution.stats['maneuverIndex'] = 4740 / 2.0
	constitution.stats['maneuverThrustIndex'] = 4740 / 2.0
	constitution.stats['mass'] = 600000
	constitution.stats['maxVelocity'] = 600
	constitution.stats['rangeIndex'] = 300
	constitution.stats['sensorIndex'] = 100
	constitution.stats['shieldIndex'] = 220
	constitution.SetShields( {'front': 1.25, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitution.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitution.stats['terawatts'] = 4000
	constitution.SetProperty('Phaser', '.*', propertyList['FedTOSPhaser'])
	constitution.SetProperty('TorpedoTube', '.*', propertyList['FedSingleTorpedoTube'])
	constitution.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
	constitution.lTorpTypes = [ ['FTBTOSPhotonTorpedo', 120] ]
	shipList.Register(constitution, 'tosconstitution')

	constitutionmk2 = TMPFedShip('constitutionmk2ncc1701')
	constitutionmk2.stats['cost'] = 300
	constitutionmk2.stats['crew'] = 450
	constitutionmk2.stats['hullIndex'] = 10 * 10.0
	constitutionmk2.stats['length'] = 305
	constitutionmk2.stats['width'] = 140
	constitutionmk2.stats['height'] = 75
	constitutionmk2.stats['maneuverIndex'] = 5340 / 4.0
	constitutionmk2.stats['maneuverThrustIndex'] = 5340 / 3.0
	constitutionmk2.stats['mass'] = 620000
	constitutionmk2.stats['maxVelocity'] = 600
	constitutionmk2.stats['rangeIndex'] = 300
	constitutionmk2.stats['sensorIndex'] = 100
	constitutionmk2.stats['shieldIndex'] = 260
	constitutionmk2.SetShields( {'front': 1.25, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitutionmk2.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitutionmk2.stats['terawatts'] = 6000
	constitutionmk2.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])
	constitutionmk2.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
	constitutionmk2.lTorpTypes[0][1] = 120
	constitutionmk2.SetProperty('Phaser', '.*', propertyList['FedTMPVIIa'])
	constitutionmk2.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIb'])
	constitutionmk2.lTorpTypes = [ ['FTBMk1PhotonTorpedo', 120] ]
	shipList.Register(constitutionmk2, 'constitutionmk2')

	constitutionmk2r = FedShip('constitutionmk2rncc1701')
	constitutionmk2r.stats['cost'] = 300
	constitutionmk2r.stats['crew'] = 450
	constitutionmk2r.stats['hullIndex'] = 10 * 10.0
	constitutionmk2r.stats['length'] = 305
	constitutionmk2r.stats['width'] = 140
	constitutionmk2r.stats['height'] = 75
	constitutionmk2r.stats['maneuverIndex'] = 5340 / 2.0
	constitutionmk2r.stats['maneuverThrustIndex'] = 5340 / 2.0
	constitutionmk2r.stats['mass'] = 620000
	constitutionmk2r.stats['maxVelocity'] = 600
	constitutionmk2r.stats['rangeIndex'] = 300 * 3.0
	constitutionmk2r.stats['sensorIndex'] = 100 * 5.0
	constitutionmk2r.stats['shieldIndex'] = 260 * 2.0
	constitutionmk2r.SetShields( {'front': 1.25, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitutionmk2r.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	constitutionmk2r.stats['terawatts'] = 6000
	constitutionmk2r.powerPercent = ('red', 0.42)  # This is not an easy ship to fly!
	constitutionmk2r.SetProperty('TorpedoTube', '.*', propertyList['FedStdTorpedoTube'])
	constitutionmk2r.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['MultiFirePhaserSystem'])
	constitutionmk2r.SetProperty('Phaser', '.*', propertyList['FedTypeVIIBank'], { 'maxCharge': 0.75 })
	constitutionmk2r.SetProperty('Phaser', '.*Hull.*', propertyList['FedTypeVIIBank'], { 'maxCharge': 0.25 })
	constitutionmk2r.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 30] ]
	shipList.Register(constitutionmk2r, 'constitutionmk2r')

	corelliancorvette = ImperialShip('corelliancorvette')
	corelliancorvette.stats['cost'] = 360
	corelliancorvette.stats['crew'] = 46
	corelliancorvette.stats['maneuverIndex'] = 500
	corelliancorvette.stats['maneuverThrustIndex'] = 500
	corelliancorvette.stats['mass'] = 16875
	corelliancorvette.stats['maxVelocity'] = 360
	corelliancorvette.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	corelliancorvette.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	cudgel = DominionShip('cudgel')
	cudgel.stats['cost'] = 275
	cudgel.stats['crew'] = 80
	cudgel.stats['hullIndex'] = 330
	cudgel.stats['length'] = 330
	cudgel.stats['width'] = 330
	cudgel.stats['height'] = 330
	cudgel.stats['maneuverIndex'] = 6000
	cudgel.stats['maneuverThrustIndex'] = 6000
	cudgel.stats['mass'] = 250000
	cudgel.stats['maxVelocity'] = 550
	cudgel.stats['rangeIndex'] = 700
	cudgel.stats['sensorIndex'] = 700
	cudgel.stats['shieldIndex'] = 425
	cudgel.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cudgel.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	cudgel.stats['terawatts'] = 17000
	cudgel.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	cudgel.lTorpTypes[0][1] = 20

	d7 = KlingonShip('d7')
	d7.stats['cost'] = 280
	d7.stats['crew'] = 510
	d7.stats['hullIndex'] = 440
	d7.stats['length'] = 228
	d7.stats['width'] = 160
	d7.stats['height'] = 60
	d7.stats['maneuverIndex'] = 3000
	d7.stats['maneuverThrustIndex'] = 2000
	d7.stats['mass'] = 490000
	d7.stats['maxVelocity'] = 625
	d7.stats['rangeIndex'] = 360
	d7.stats['sensorIndex'] = 300
	d7.stats['shieldIndex'] = 380
	d7.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	d7.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	d7.stats['terawatts'] = 13500
	d7.SetProperty('PulseWeapon', '.', propertyList['KliMk10Disruptor'])
	d7.SetProperty('TorpedoTube', '.', propertyList['KliTorpedoTube'])
	d7.powerPercent = ('red', 0.71)
	d7.battery = 100
	d7.bakBattery = 60
	d7.SetProperty('WeaponSystem', '.*', propertyList['MultiFirePhaserSystem'])
	d7.lTorpTypes[0][1] = 130
	d7.lTorpTypes[1][1] = 0
	shipList.Register(d7, 'tosd7')

	danube = SmallFedShip('danube')
	danube.stats['cost'] = 180
	danube.stats['crew'] = 2
	danube.stats['hullIndex'] = 100
	danube.stats['length'] = 23.1
	danube.stats['width'] = 13.7
	danube.stats['height'] = 5.4
	danube.stats['maneuverIndex'] = 10000
	danube.stats['maneuverThrustIndex'] = 10000
	danube.stats['mass'] = 159
	danube.stats['maxVelocity'] = 600
	danube.stats['rangeIndex'] = 25
	danube.stats['sensorIndex'] = 500
	danube.stats['shieldIndex'] = 21
	danube.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	danube.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	danube.stats['terawatts'] = 650
	danube.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])
	danube.lTorpTypes[0][1] = 10

	dauntless = FedShip('dauntless')
	dauntless.stats['cost'] = 720
	dauntless.stats['crew'] = 120
	dauntless.stats['hullIndex'] = 60
	dauntless.stats['length'] = 60
	dauntless.stats['width'] = 60
	dauntless.stats['height'] = 60
	dauntless.stats['maneuverIndex'] = 7500
	dauntless.stats['maneuverThrustIndex'] = 7500
	dauntless.stats['mass'] = 450000
	dauntless.stats['maxVelocity'] = 550
	dauntless.stats['rangeIndex'] = 515
	dauntless.stats['sensorIndex'] = 1000
	dauntless.stats['shieldIndex'] = 240
	dauntless.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dauntless.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dauntless.stats['terawatts'] = 12000

	dderidex = RomulanShip('dderidex')
	dderidex.stats['cost'] = 980
	dderidex.stats['crew'] = 1650
	dderidex.stats['hullIndex'] = 1200
	dderidex.stats['length'] = 1041.65
	dderidex.stats['width'] = 772.43
	dderidex.stats['height'] = 285.47
	dderidex.stats['maneuverIndex'] = 1080
	dderidex.stats['maneuverThrustIndex'] = 1680
	dderidex.stats['mass'] = 4320000
	dderidex.stats['maxVelocity'] = 450
	dderidex.stats['rangeIndex'] = 1660
	dderidex.stats['sensorIndex'] = 1000
	dderidex.stats['shieldIndex'] = 850
	dderidex.SetShields( {'front': 2.0, 'rear': 1, 'top': 2.0, 'bottom': 2.0, 'left': 1, 'right': 1 } )
	dderidex.SetShieldCharge( {'front': 2, 'rear': 2, 'top': 2, 'bottom': 2, 'left': 2, 'right': 2 } )
	dderidex.stats['terawatts'] = 65000
	dderidex.SetProperty('Phaser', '.', propertyList['RomDisruptorBeam'], { 'terawatts': 0.4, 'maxCharge': 0.6 } )
	dderidex.SetProperty('Phaser', 'Disruptor', propertyList['Blank'], { 'terawatts': 0.0 } )
	dderidex.SetProperty('Phaser', 'Aft.*', propertyList['RomDisruptorBeam'], { 'terawatts': 0.2, 'maxCharge': 0.6 } )
	dderidex.SetProperty('TorpedoTube', '.', propertyList['RomTorpedoTube'])
	dderidex.SetProperty('PulseWeapon', '.', propertyList['RomMk21Disruptor'], { 'terawatts': 3.0 } )
	dderidex.powerPercent = ('red', 0.7)
	dderidex.battery = 400
	dderidex.bakBattery = 160
	dderidex.lTorpTypes = [ ['FTBRomPlasmaBurst', 20], ['FTBRomTorpedo', 200] ]
	shipList.Register(dderidex, 'warbird')
	shipList.Register(dderidex, 'e2m0warbird')

	defensedrone = RomulanShip('defensedrone')
	defensedrone.stats['cost'] = 40
	defensedrone.stats['crew'] = 90
	defensedrone.stats['hullIndex'] = 10
	defensedrone.stats['length'] = 10
	defensedrone.stats['width'] = 10
	defensedrone.stats['height'] = 10
	defensedrone.stats['maneuverIndex'] = 6000
	defensedrone.stats['maneuverThrustIndex'] = 6000
	defensedrone.stats['mass'] = 500
	defensedrone.stats['maxVelocity'] = 1500
	defensedrone.stats['rangeIndex'] = 100
	defensedrone.stats['sensorIndex'] = 100000
	defensedrone.stats['shieldIndex'] = 8
	defensedrone.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	defensedrone.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	defensedrone.stats['terawatts'] = 1500

	defiant = FedShip('defiant')
	defiant.stats['cost'] = 1400
	defiant.stats['crew'] = 50
	defiant.stats['hullIndex'] = 3400 - 2000.0 # Much of this is due to ablative armor.
	defiant.stats['length'] =  170.68
	defiant.stats['width'] = 134.11
	defiant.stats['height'] = 30.1
	defiant.stats['maneuverIndex'] = 8660 * 3.0
	defiant.stats['maneuverThrustIndex'] = 8660 * 3.0
	defiant.stats['mass'] = 120000
	defiant.stats['maxVelocity'] = 850
	defiant.stats['rangeIndex'] = 815
	defiant.stats['sensorIndex'] = 850
	defiant.stats['shieldIndex'] = 880
	defiant.stats['terawatts'] = 70000
	defiant.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	defiant.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	defiant.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.15, 'maxCharge': 0.5 })
	defiant.SetProperty('PulseWeapon', '.', propertyList['FedC1PulsePhaser'], { 'terawatts': 5.0, 'maxCharge': 1.0 })
	defiant.SetProperty('TorpedoTube', '.*', propertyList['FedPFTorpedoTube'])
	defiant.powerPercent = ('red', 0.62)
	defiant.battery = 250
	defiant.bakBattery = 90
	defiant.lTorpTypes = [ ['FTBQuantumTorpedo', 100] ]

	deltadx9transport = ImperialShip('deltadx9transport')
	deltadx9transport.stats['cost'] = 125
	deltadx9transport.stats['crew'] = 4
	deltadx9transport.stats['maneuverIndex'] = 2000
	deltadx9transport.stats['maneuverThrustIndex'] = 2000
	deltadx9transport.stats['mass'] = 40
	deltadx9transport.stats['maxVelocity'] = 400

	ddreadnaught = DominionShip('ddreadnaught')
	ddreadnaught.stats['cost'] = 25962
	ddreadnaught.stats['crew'] = 1200 / 3.0
	ddreadnaught.stats['hullIndex'] = 10440 / 8.0
	ddreadnaught.stats['length'] = 4800
	ddreadnaught.stats['width'] = 3235
	ddreadnaught.stats['height'] = 1393
	ddreadnaught.stats['maneuverIndex'] = 250
	ddreadnaught.stats['maneuverThrustIndex'] = 400
	ddreadnaught.stats['mass'] = 18200000 * 8.0
	ddreadnaught.stats['maxVelocity'] = 325 / 3.74415
	ddreadnaught.stats['rangeIndex'] = 1460
	ddreadnaught.stats['sensorIndex'] = 1500
	ddreadnaught.stats['shieldIndex'] = 18700
	ddreadnaught.SetShields( {'front': 1.5, 'rear': 1.5, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ddreadnaught.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 2, 'bottom': 2, 'left': 1, 'right': 1 } )
	ddreadnaught.stats['terawatts'] = 3000000
	ddreadnaught.SetProperty('Phaser', '.*', propertyList['DomPolaronBeam'], { 'terawatts': 1.25 })
	ddreadnaught.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	ddreadnaught.SetProperty('TorpedoTube', '.*', propertyList['DomPulseTorpedoTube'])
	ddreadnaught.SetProperty('PulseWeapon', '.*', propertyList['DomPulsePolaron'], { 'maxCharge': 2.0 } )
	ddreadnaught.SetProperty('PulseWeapon', '^Main.*', propertyList['DomHeavyPulsePolaron'], { 'terawatts': 1.5 } )
	ddreadnaught.powerPercent = ('red', 0.65)
	ddreadnaught.battery = 400
	ddreadnaught.bakBattery = 150
	ddreadnaught.lTorpTypes[0][1] = 1000
	ddreadnaught.lTorpTypes[1][1] = 1000

	devastator = DominionShip('devastator')
	devastator.stats['cost'] = 1050
	devastator.stats['crew'] = 490
	devastator.stats['hullIndex'] = 1550
	devastator.stats['length'] = 639.75
	devastator.stats['width'] = 568.44
	devastator.stats['height'] = 204.97
	devastator.stats['maneuverIndex'] = 2000
	devastator.stats['maneuverThrustIndex'] = 2000
	devastator.stats['mass'] = 7500000
	devastator.stats['maxVelocity'] = 425
	devastator.stats['rangeIndex'] = 1400
	devastator.stats['sensorIndex'] = 950
	devastator.stats['shieldIndex'] = 950
	devastator.SetShields( {'front': 1.25, 'rear': 1, 'top': 1.25, 'bottom': 1.0, 'left': 0.75, 'right': 0.75 } )
	devastator.SetShieldCharge( {'front': 3.0, 'rear': 3.0, 'top': 4.0, 'bottom': 4.0, 'left': 2.0, 'right': 2.0 } )
	devastator.stats['terawatts'] = 75000
	devastator.SetProperty('Phaser', '.*', propertyList['DomPolaronBeam'])
	devastator.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	devastator.SetProperty('PulseWeapon', '.*', propertyList['DomPulsePolaron'], { 'terawatts': 2.0 } )
	devastator.SetProperty('PulseWeapon', '^Main Cannon$', propertyList['DomHeavyPulsePolaron'], { 'terawatts': 1.5 } )
	devastator.powerPercent = ('red', 0.75)
	devastator.battery = 150
	devastator.bakBattery = 100
	devastator.lTorpTypes[0][1] = 200
	devastator.lTorpTypes[1][1] = 200

	dominator = DominionShip('dominator')
	dominator.stats['blastradiusdamage'] = 2500
	dominator.stats['blastradiusshockwave'] = '0.95'
	dominator.stats['cost'] = 250
	dominator.stats['crew'] = 30
	dominator.stats['hullIndex'] = 320
	dominator.stats['length'] = 68.32
	dominator.stats['width'] = 70.02
	dominator.stats['height'] = 18.32
	dominator.stats['maneuverIndex'] = 25000
	dominator.stats['maneuverThrustIndex'] = 22000
	dominator.stats['mass'] = 75000
	dominator.stats['maxVelocity'] = 750 / 0.5
	dominator.stats['rangeIndex'] = 200
	dominator.stats['sensorIndex'] = 400
	dominator.stats['shieldIndex'] = 160
	dominator.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dominator.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dominator.stats['terawatts'] = 16250
	dominator.SetProperty('Phaser', '.*', propertyList['DomPolaronBeam'])
	dominator.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	dominator.powerPercent = ('red', 0.85)
	dominator.battery = 60
	dominator.bakBattery = 45
	dominator.lTorpTypes = [ ['FTBMicroPolaronTorpedo', 5] ]
	shipList.Register(dominator, 'bugship')

	entdragon = RomulanShip('entdragon')
	entdragon.stats['cost'] = 650
	entdragon.stats['crew'] = 850
	entdragon.stats['hullIndex'] = 700
	entdragon.stats['length'] = 1041.65 * 0.6
	entdragon.stats['width'] = 772.43 * 0.5
	entdragon.stats['height'] = 285.47 * 0.6
	entdragon.stats['maneuverIndex'] = 1200
	entdragon.stats['maneuverThrustIndex'] = 1200
	entdragon.stats['mass'] = 1500000
	entdragon.stats['maxVelocity'] = 300
	entdragon.stats['rangeIndex'] = 1000
	entdragon.stats['sensorIndex'] = 500
	entdragon.stats['shieldIndex'] = 675
	entdragon.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	entdragon.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	entdragon.stats['terawatts'] = 16500
	entdragon.SetProperty('PulseWeapon', '.', propertyList['RomEntDisruptor'])
	entdragon.lTorpTypes = [ ['FTBRomPlasmaBurst', 0] ]
	entdragon.powerPercent = ('red', 0.7)
	entdragon.battery = 400
	entdragon.bakBattery = 200

	dreadnought = CardassianShip('dreadnought')
	dreadnought.stats['blastradiusdamage'] = 12000
	dreadnought.stats['blastradiusshockwave'] = '20.0'
	dreadnought.stats['cost'] = 420
	dreadnought.stats['crew'] = 80
	dreadnought.stats['hullIndex'] = 100
	dreadnought.stats['length'] = 300
	dreadnought.stats['width'] = 45
	dreadnought.stats['height'] = 18
	dreadnought.stats['maneuverIndex'] = 2500
	dreadnought.stats['maneuverThrustIndex'] = 2500
	dreadnought.stats['mass'] = 100000
	dreadnought.stats['maxVelocity'] = 550
	dreadnought.stats['rangeIndex'] = 750
	dreadnought.stats['sensorIndex'] = 600
	dreadnought.stats['shieldIndex'] = 440
	dreadnought.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dreadnought.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dreadnought.lTorpTypes = [ ['FTBQuantumTorpedo', 20] ]
	dreadnought.stats['terawatts'] = 6000

	droiddefense = ImperialShip('droiddefense')
	droiddefense.stats['cost'] = 115
	droiddefense.stats['crew'] = 0
	droiddefense.stats['maneuverIndex'] = 7000
	droiddefense.stats['maneuverThrustIndex'] = 7000
	droiddefense.stats['mass'] = 5
	droiddefense.stats['maxVelocity'] = 480
	droiddefense.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	droiddefense.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	droidscout = ImperialShip('droidscout')
	droidscout.stats['cost'] = 50
	droidscout.stats['crew'] = 0
	droidscout.stats['maneuverIndex'] = 9000
	droidscout.stats['maneuverThrustIndex'] = 9000
	droidscout.stats['mass'] = 1000
	droidscout.stats['maxVelocity'] = 690
	droidscout.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	droidscout.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	ds9 = FedShip('ds9')
	ds9.stats['cost'] = 1500
	ds9.stats['crew'] = 500
	ds9.stats['hullIndex'] = 400
	ds9.stats['length'] = 1451.82
	ds9.stats['width'] = 368.8
	ds9.stats['height'] = 969.26
	ds9.stats['immobile'] = 'TRUE'
	ds9.stats['maneuverIndex'] = 1
	ds9.stats['maneuverThrustIndex'] = 1
	ds9.stats['mass'] = 4500000
	ds9.stats['maxVelocity'] = 50
	ds9.stats['rangeIndex'] = 1210
	ds9.stats['sensorIndex'] = 1000
	ds9.stats['shieldIndex'] = 12000
	ds9.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ds9.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ds9.stats['terawatts'] = 150000
	ds9.SetProperty('Phaser', '.*', propertyList['CardTypeX'], {'maxCharge': 1.2})
	ds9.lTorpTypes[0][1] = 5000
	shipList.Register(ds9, 'cardstarbase')

	

	dtarsis = RomulanShip('dtarsis')
	dtarsis.stats['cost'] = 650
	dtarsis.stats['crew'] = 780
	dtarsis.stats['hullIndex'] = 400
	dtarsis.stats['length'] = 1041.65 * 0.5
	dtarsis.stats['width'] = 772.43 * 0.5
	dtarsis.stats['height'] = 285.47 * 0.5
	dtarsis.stats['maneuverIndex'] = 2000
	dtarsis.stats['maneuverThrustIndex'] = 2000
	dtarsis.stats['mass'] = 2200000
	dtarsis.stats['maxVelocity'] = 550
	dtarsis.stats['rangeIndex'] = 1000
	dtarsis.stats['sensorIndex'] = 500
	dtarsis.stats['shieldIndex'] = 675
	dtarsis.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dtarsis.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dtarsis.stats['terawatts'] = 13500
	dtarsis.powerPercent = ('red', 0.7)
	dtarsis.battery = 300
	dtarsis.bakBattery = 160

	dverix = RomulanShip('dverix')
	dverix.stats['cost'] = 650
	dverix.stats['crew'] = 850
	dverix.stats['hullIndex'] = 700
	dverix.stats['length'] = 1041.65 * 0.6
	dverix.stats['width'] = 772.43 * 0.5
	dverix.stats['height'] = 285.47 * 0.6
	dverix.stats['maneuverIndex'] = 1200
	dverix.stats['maneuverThrustIndex'] = 1200
	dverix.stats['mass'] = 1500000
	dverix.stats['maxVelocity'] = 300
	dverix.stats['rangeIndex'] = 1000
	dverix.stats['sensorIndex'] = 500
	dverix.stats['shieldIndex'] = 675
	dverix.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dverix.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	dverix.stats['terawatts'] = 16500
	dverix.powerPercent = ('red', 0.7)
	dverix.battery = 400
	dverix.bakBattery = 200

	enslaver = DominionShip('enslaver')
	enslaver.stats['cost'] = 2500
	enslaver.stats['crew'] = 1200 / 3.0
	enslaver.stats['hullIndex'] = 1740
	enslaver.stats['length'] = 1282
	enslaver.stats['width'] = 864
	enslaver.stats['height'] = 372
	enslaver.stats['maneuverIndex'] = 400
	enslaver.stats['maneuverThrustIndex'] = 800
	enslaver.stats['mass'] = 18200000
	enslaver.stats['maxVelocity'] = 325 / 1.2
	enslaver.stats['rangeIndex'] = 1460
	enslaver.stats['sensorIndex'] = 800
	enslaver.stats['shieldIndex'] = 1720
	enslaver.SetShields( {'front': 1.5, 'rear': 1.5, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	enslaver.SetShieldCharge( {'front': 4.0, 'rear': 4.0, 'top': 6.0, 'bottom': 6.0, 'left': 4.0, 'right': 4.0 } )
	enslaver.stats['terawatts'] = 235000
	enslaver.SetProperty('Phaser', '.*', propertyList['DomPolaronBeam'])
	enslaver.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	enslaver.SetProperty('TorpedoTube', '.*', propertyList['DomPulseTorpedoTube'])
	enslaver.SetProperty('PulseWeapon', '.*', propertyList['DomPulsePolaron'], { 'maxCharge': 3.0 } )
	enslaver.SetProperty('PulseWeapon', '^Main.*', propertyList['DomHeavyPulsePolaron'], { 'terawatts': 1.5 } )
	enslaver.SetProperty('WeaponSystem', '.*Cannon.*', propertyList['MultiFirePhaserSystem'])
	enslaver.powerPercent = ('red', 0.68)
	enslaver.battery = 400
	enslaver.bakBattery = 150
	enslaver.lTorpTypes[0][1] = 300
	enslaver.lTorpTypes[1][1] = 300

	escortcarrier = ImperialCapShip('escortcarrier')
	escortcarrier.stats['cost'] = 600
	escortcarrier.stats['crew'] = 1000
	escortcarrier.stats['maneuverIndex'] = 100
	escortcarrier.stats['maneuverThrustIndex'] = 100
	escortcarrier.stats['mass'] = 625000
	escortcarrier.stats['maxVelocity'] = 240
	escortcarrier.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	escortcarrier.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	escorttransport = ImperialShip('escorttransport')
	escorttransport.stats['cost'] = 200
	escorttransport.stats['crew'] = 4000
	escorttransport.stats['maneuverIndex'] = 800
	escorttransport.stats['maneuverThrustIndex'] = 800
	escorttransport.stats['mass'] = 17
	escorttransport.stats['maxVelocity'] = 500
	escorttransport.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	escorttransport.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )


	eximius = FedShip('eximius')
	eximius.stats['cost'] = 1800
	eximius.stats['crew'] = 50
	eximius.stats['hullIndex'] = 2800
	eximius.stats['length'] = 400
	eximius.stats['width'] = 220
	eximius.stats['height'] = 80
	eximius.stats['maneuverIndex'] = 15000
	eximius.stats['maneuverThrustIndex'] = 15000
	eximius.stats['mass'] = 280000
	eximius.stats['maxVelocity'] = 700
	eximius.stats['rangeIndex'] = 815
	eximius.stats['sensorIndex'] = 1850
	eximius.stats['shieldIndex'] = 1280
	eximius.stats['terawatts'] = 55000
	eximius.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	eximius.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	eximius.SetProperty('Phaser', '.*', propertyList['FedTypeXII'])
	eximius.SetProperty('PulseWeapon', '.', propertyList['FedC1PulsePhaser'])
	eximius.SetProperty('TorpedoTube', '.*', propertyList['FedPFTorpedoTube'])
	eximius.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	eximius.powerPercent = ('red', 0.62)
	eximius.battery = 250
	eximius.bakBattery = 120


	excelsior = FedShip('excelsior')
	excelsior.stats['cost'] = 360
	excelsior.stats['crew'] = 565
	excelsior.stats['hullIndex'] = 520
	excelsior.stats['length'] = 467
	excelsior.stats['width'] = 185
	excelsior.stats['height'] = 100
	excelsior.stats['maneuverIndex'] = 800
	excelsior.stats['maneuverThrustIndex'] = 3000
	excelsior.stats['mass'] = 1870000
	excelsior.stats['maxVelocity'] = 525
	excelsior.stats['rangeIndex'] = 645
	excelsior.stats['sensorIndex'] = 600
	excelsior.stats['shieldIndex'] = 620
	excelsior.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsior.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsior.stats['terawatts'] = 20500
	excelsior.powerPercent = ('red', 0.6)
	excelsior.battery = 140
	excelsior.bakBattery = 80
	excelsior.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	excelsior.SetProperty('WeaponSystem', 'Phaser.*', propertyList['PhaserSystem'])
	excelsior.SetProperty('Phaser', '.*', propertyList['FedTypeVIIIBank'], { 'maxCharge': 0.5 })
	excelsior.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 150] ]
	shipList.Register(excelsior, 'excelsiortng')
	shipList.Register(excelsior, 'excelsiorp81')

	excelsiormk2 = FedShip('excelsiormk2')
	excelsiormk2.stats['cost'] = 360
	excelsiormk2.stats['crew'] = 565
	excelsiormk2.stats['hullIndex'] = 520
	excelsiormk2.stats['length'] = 467
	excelsiormk2.stats['width'] = 185
	excelsiormk2.stats['height'] = 100
	excelsiormk2.stats['maneuverIndex'] = 800
	excelsiormk2.stats['maneuverThrustIndex'] = 1500
	excelsiormk2.stats['mass'] = 1870000
	excelsiormk2.stats['maxVelocity'] = 525
	excelsiormk2.stats['rangeIndex'] = 325
	excelsiormk2.stats['sensorIndex'] = 300
	excelsiormk2.stats['shieldIndex'] = 310
	excelsiormk2.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiormk2.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiormk2.stats['terawatts'] = 20500
	excelsiormk2.powerPercent = ('red', 0.6)
	excelsiormk2.battery = 140
	excelsiormk2.bakBattery = 80
	excelsiormk2.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	excelsiormk2.SetProperty('WeaponSystem', 'Phaser.*', propertyList['MultiFirePhaserSystem'])
	excelsiormk2.SetProperty('Phaser', '.*', propertyList['FedTMPVIIIa'])
	excelsiormk2.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIIb'])
	excelsiormk2.SetProperty('Phaser', '.*4', propertyList['FedTMPVIIIb'])
	excelsiormk2.lTorpTypes = [ ['FTBMk1PhotonTorpedo', 150] ]
	shipList.Register(excelsiormk2, 'enterpriseb')

	excelsiormk2tng = FedShip('excelsiormk2tng')
	excelsiormk2tng.stats['cost'] = 360
	excelsiormk2tng.stats['crew'] = 565
	excelsiormk2tng.stats['hullIndex'] = 520
	excelsiormk2tng.stats['length'] = 467
	excelsiormk2tng.stats['width'] = 185
	excelsiormk2tng.stats['height'] = 100
	excelsiormk2tng.stats['maneuverIndex'] = 800
	excelsiormk2tng.stats['maneuverThrustIndex'] = 1500
	excelsiormk2tng.stats['mass'] = 1870000
	excelsiormk2tng.stats['maxVelocity'] = 525
	excelsiormk2tng.stats['rangeIndex'] = 325
	excelsiormk2tng.stats['sensorIndex'] = 300
	excelsiormk2tng.stats['shieldIndex'] = 310
	excelsiormk2tng.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiormk2tng.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiormk2tng.stats['terawatts'] = 20500
	excelsiormk2tng.powerPercent = ('red', 0.6)
	excelsiormk2tng.battery = 140
	excelsiormk2tng.bakBattery = 80
	excelsiormk2tng.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	excelsiormk2tng.SetProperty('WeaponSystem', 'Phaser.*', propertyList['PhaserSystem'])
	excelsiormk2tng.SetProperty('Phaser', '.*', propertyList['FedTypeVIIIBank'], { 'maxCharge': 0.5 })
	excelsiormk2tng.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 150] ]

	excelsiortmp = FedShip('excelsiortmp')
	excelsiortmp.stats['cost'] = 360
	excelsiortmp.stats['crew'] = 565
	excelsiortmp.stats['hullIndex'] = 520
	excelsiortmp.stats['length'] = 467
	excelsiortmp.stats['width'] = 185
	excelsiortmp.stats['height'] = 100
	excelsiortmp.stats['maneuverIndex'] = 800
	excelsiortmp.stats['maneuverThrustIndex'] = 1500
	excelsiortmp.stats['mass'] = 1870000
	excelsiortmp.stats['maxVelocity'] = 525
	excelsiortmp.stats['rangeIndex'] = 325
	excelsiortmp.stats['sensorIndex'] = 300
	excelsiortmp.stats['shieldIndex'] = 310
	excelsiortmp.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiortmp.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	excelsiortmp.stats['terawatts'] = 18750
	excelsiortmp.powerPercent = ('red', 0.6)
	excelsiortmp.battery = 140
	excelsiortmp.bakBattery = 80
	excelsiortmp.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	excelsiortmp.SetProperty('WeaponSystem', 'Phaser.*', propertyList['MultiFirePhaserSystem'])
	excelsiortmp.SetProperty('Phaser', '.*', propertyList['FedTMPVIIIa'])
	excelsiortmp.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIIb'])
	excelsiortmp.SetProperty('Phaser', '.*4', propertyList['FedTMPVIIIb'])
	excelsiortmp.lTorpTypes = [ ['FTBMk1PhotonTorpedo', 150] ]
	shipList.Register(excelsiortmp, 'excelsior')

	fedstation = FedShip('fedstation')
	fedstation.stats['cost'] = 1500
	fedstation.stats['crew'] = 500
	fedstation.stats['hullIndex'] = 400
	fedstation.stats['length'] = 1451.82
	fedstation.stats['width'] = 368.8
	fedstation.stats['height'] = 969.26
	fedstation.stats['immobile'] = 'TRUE'
	fedstation.stats['maneuverIndex'] = 1
	fedstation.stats['maneuverThrustIndex'] = 1
	fedstation.stats['mass'] = 4500000
	fedstation.stats['maxVelocity'] = 50
	fedstation.stats['rangeIndex'] = 1210
	fedstation.stats['sensorIndex'] = 1000
	fedstation.stats['shieldIndex'] = 12000
	fedstation.SetShields( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	fedstation.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	fedstation.stats['terawatts'] = 150000
	fedstation.SetProperty('Phaser', '.*', propertyList['FedTypeXII'], {'maxCharge': 2.0})
	fedstation.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 15000] ]
	shipList.Register(fedstation, 'biranustation')
	shipList.Register(fedstation, 'drydock')
	shipList.Register(fedstation, 'commarray')
	shipList.Register(fedstation, 'commlight')

	firehawk = RomulanShip('firehawk')
	firehawk.stats['cost'] = 385
	firehawk.stats['crew'] = 390
	firehawk.stats['hullIndex'] = 700
	firehawk.stats['length'] = 700 ##
	firehawk.stats['width'] = 700 ## 
	firehawk.stats['height'] = 700 ##
	firehawk.stats['maneuverIndex'] = 2800
	firehawk.stats['maneuverThrustIndex'] = 2800
	firehawk.stats['mass'] = 800000
	firehawk.stats['maxVelocity'] = 575
	firehawk.stats['rangeIndex'] = 370
	firehawk.stats['sensorIndex'] = 500
	firehawk.stats['shieldIndex'] = 325
	firehawk.stats['terawatts'] = 14250
	firehawk.SetShields( {'front': 1.5, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	firehawk.SetShieldCharge( {'front': 1.25, 'rear': 0.75, 'top': 1.25, 'bottom': 1.25, 'left': 0.75, 'right': 0.75 } )
	firehawk.SetProperty('PulseWeapon', '.*', propertyList['KliMk6PulseDisruptor'], { 'terawatts': 0.2 })
	firehawk.SetProperty('PulseWeapon', '.*Mk12.*', propertyList['KliMk12PulseDisruptor'])
	firehawk.SetProperty('TorpedoTube', '.*', propertyList['KliDoubleTorpedoTube'])
	firehawk.battery = 200
	firehawk.bakBattery = 90
	firehawk.SetProperty('WeaponSystem', '.*', propertyList['MultiFirePhaserSystem'])
	firehawk.lTorpTypes[0][1] = 50
	firehawk.lTorpTypes[1][1] = 80


	lakota = FedShip('lakota')
	lakota.stats['cost'] = 1301
	lakota.stats['crew'] = 790
	lakota.stats['hullIndex'] = 310
	lakota.stats['length'] = 467
	lakota.stats['width'] = 185
	lakota.stats['height'] = 100
	lakota.stats['maneuverIndex'] = 3000 / 2.0
	lakota.stats['maneuverThrustIndex'] = 3000
	lakota.stats['mass'] = 2495000
	lakota.stats['maxVelocity'] = 500
	lakota.stats['rangeIndex'] = 700
	lakota.stats['sensorIndex'] = 700
	lakota.stats['shieldIndex'] = 875
	lakota.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	lakota.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	lakota.stats['terawatts'] = 40000
	lakota.SetProperty('TorpedoTube', '.*', propertyList['FedPFTorpedoTube'])
	lakota.SetProperty('Phaser', '.*', propertyList['FedTypeIX'], { 'maxCharge': 0.4 })
	lakota.SetProperty('PulseWeapon', '.', propertyList['FedC1PulsePhaser'])
	lakota.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	lakota.powerPercent = ('red', 0.65)
	lakota.battery = 200
	lakota.bakBattery = 80
	lakota.lTorpTypes = [ ['FTBQuantumTorpedo', 150] ]


	galaxy = FedShip('galaxy')
	galaxy.stats['cost'] = 1000
	galaxy.stats['crew'] = 1000
	galaxy.stats['hullIndex'] = 1000
	galaxy.stats['length'] = 641
	galaxy.stats['width'] = 470
	galaxy.stats['height'] = 145
	galaxy.stats['maneuverIndex'] = 1000
	galaxy.stats['maneuverThrustIndex'] = 1000
	galaxy.stats['mass'] = 5125000
	galaxy.stats['maxVelocity'] = 400
	galaxy.stats['rangeIndex'] = 1000
	galaxy.stats['sensorIndex'] = 1000
	galaxy.stats['shieldIndex'] = 1000
	galaxy.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxy.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxy.stats['terawatts'] = 50000
	galaxy.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.1, 'maxCharge': 0.3 })
	# galaxy.SetProperty('Phaser', '^Particle.*', propertyList['FedParticleBeam'], { 'terawatts': 0.0 })
	galaxy.SetProperty('Phaser', '^Ventral Phaser [1-4]', propertyList['FedTypeX'])
	galaxy.SetProperty('Phaser', '^Dorsal Phaser [1-4]', propertyList['FedTypeX'])
	# galaxy.SetProperty('Phaser', 'Main Array$', propertyList['FedTypeX'])
	galaxy.SetProperty('TorpedoTube', '.*', propertyList['Blank'])
	galaxy.SetProperty('TorpedoTube', 'Forward Torpedo 1', propertyList['FedType3BurstTorpedoTube'])
	galaxy.SetProperty('TorpedoTube', 'Aft Torpedo 1', propertyList['FedType3BurstTorpedoTube'])
	galaxy.SetProperty('PulseWeapon', '.*Antimatter.*', propertyList['FedAntimatter'], { 'terawatts': 0.0 })
	galaxy.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	galaxy.powerPercent = ('red', 0.7)
	galaxy.battery = 375
	galaxy.bakBattery = 80
	galaxy.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 175], ['FTBMk5PhotonTorpedoS', 5], ['FTBMk5PhotonTorpedoM', 5], ['FTBMk5PhotonTorpedoB', 5] ]
	shipList.Register(galaxy, 'galaxydauntless')
	shipList.Register(galaxy, 'venture')
	shipList.Register(galaxy, 'mvamgalaxy')


	galaxysaucer = FedShip('galaxysaucer')
	galaxysaucer.stats['cost'] = 300
	galaxysaucer.stats['crew'] = 700
	galaxysaucer.stats['hullIndex'] = 1000
	galaxysaucer.stats['length'] = 357
	galaxysaucer.stats['width'] = 470
	galaxysaucer.stats['height'] = 63
	galaxysaucer.stats['maneuverIndex'] = 400
	galaxysaucer.stats['maneuverThrustIndex'] = 400
	galaxysaucer.stats['mass'] = 3125000
	galaxysaucer.stats['maxVelocity'] = 400
	galaxysaucer.stats['rangeIndex'] = 1000
	galaxysaucer.stats['sensorIndex'] = 1000
	galaxysaucer.stats['shieldIndex'] = 1000
	galaxysaucer.SetShields( {'front': 0.75, 'rear': 0.75, 'top': 1.5, 'bottom': 1.5, 'left': 0.75, 'right': 0.75 } )
	galaxysaucer.SetShieldCharge( {'front': 0.5, 'rear': 0.5, 'top': 0.5, 'bottom': 0.5, 'left': 1, 'right': 1 } )
	galaxysaucer.stats['terawatts'] = 50000
	galaxysaucer.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.1, 'maxCharge': 0.6 })
	galaxysaucer.SetProperty('Phaser', '^Ventral Phaser [1-4]', propertyList['FedTypeX'])
	galaxysaucer.SetProperty('Phaser', '^Dorsal Phaser [1-4]', propertyList['FedTypeX'])
	# galaxysaucer.SetProperty('Phaser', 'Main Array$', propertyList['FedTypeX'])
	galaxysaucer.SetProperty('TorpedoTube', '.*', propertyList['FedType3BurstTorpedoTube'])
	galaxysaucer.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	galaxysaucer.battery = 80
	galaxysaucer.bakBattery = 20
	galaxysaucer.powerPercent = ('red', 0.6)
	galaxysaucer.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 20 ] ]
	shipList.Register(galaxysaucer, 'mvamgalaxysaucer')


	galaxydrive = FedShip('galaxydrive')
	galaxydrive.stats['cost'] = 700
	galaxydrive.stats['crew'] = 300
	galaxydrive.stats['hullIndex'] = 1000
	galaxydrive.stats['length'] = 391
	galaxydrive.stats['width'] = 210
	galaxydrive.stats['height'] = 122
	galaxydrive.stats['maneuverIndex'] = 2000
	galaxydrive.stats['maneuverThrustIndex'] = 2000
	galaxydrive.stats['mass'] = 2000000
	galaxydrive.stats['maxVelocity'] = 400
	galaxydrive.stats['rangeIndex'] = 1000
	galaxydrive.stats['sensorIndex'] = 1000
	galaxydrive.stats['shieldIndex'] = 1000
	galaxydrive.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxydrive.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxydrive.stats['terawatts'] = 50000
	# galaxydrive.SetProperty('Phaser', '^Ventral Phaser [1-4]', propertyList['FedTypeX'])
	# galaxydrive.SetProperty('Phaser', '^Dorsal Phaser [1-4]', propertyList['FedTypeX'])
	# galaxydrive.SetProperty('Phaser', 'Main Array$', propertyList['FedTypeX'])
	galaxydrive.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.1, 'maxCharge': 0.6 })
	galaxydrive.SetProperty('TorpedoTube', '.*', propertyList['FedType3BurstTorpedoTube'])
	galaxydrive.SetProperty('TorpedoTube', '.*[2-4]', propertyList['Blank'])
	galaxydrive.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	galaxydrive.battery = 170
	galaxydrive.bakBattery = 60
	galaxydrive.powerPercent = ('red', 0.75)
	galaxydrive.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 175], ['FTBMk5PhotonTorpedoS', 5], ['FTBMk5PhotonTorpedoM', 5], ['FTBMk5PhotonTorpedoB', 5] ]
	shipList.Register(galaxydrive, 'mvamgalaxystardrive')




	galaxyx = FedShip('galaxyx')
	galaxyx.stats['cost'] = 1500
	galaxyx.stats['crew'] = 1000
	galaxyx.stats['hullIndex'] = 1000
	galaxyx.stats['length'] = 641
	galaxyx.stats['width'] = 470
	galaxyx.stats['height'] = 145
	galaxyx.stats['maneuverIndex'] = 1400
	galaxyx.stats['maneuverThrustIndex'] = 1400
	galaxyx.stats['mass'] = 5600000
	galaxyx.stats['maxVelocity'] = 425
	galaxyx.stats['rangeIndex'] = 1200
	galaxyx.stats['sensorIndex'] = 1000
	galaxyx.stats['shieldIndex'] = 1300
	galaxyx.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxyx.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galaxyx.stats['terawatts'] = 80000
	galaxyx.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	galaxyx.SetProperty('Phaser', '^Ventral Phaser [1-4]', propertyList['FedTypeX'])
	galaxyx.SetProperty('Phaser', '^Dorsal Phaser [1-4]', propertyList['FedTypeX'])
	galaxyx.SetProperty('TorpedoTube', '.*', propertyList['FedType3BurstTorpedoTube'])
	galaxyx.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	galaxyx.lTorpTypes[0][1] = 150
	galaxyx.lTorpTypes[1][1] = 100

	galor = CardassianShip('galor')
	galor.stats['cantargetmultipletargets'] = 'false'
	galor.stats['cost'] = 340
	galor.stats['crew'] = 600
	galor.stats['hullIndex'] = 620
	galor.stats['length'] = 371.88
	galor.stats['width'] = 192.23
	galor.stats['height'] = 59
	galor.stats['maneuverIndex'] = 780
	galor.stats['maneuverThrustIndex'] = 2000
	galor.stats['mass'] = 900000
	galor.stats['maxVelocity'] = 525
	galor.stats['rangeIndex'] = 940
	galor.stats['sensorIndex'] = 500
	galor.stats['rotatetoretaliate'] = 'false'
	galor.stats['shieldIndex'] = 550
	galor.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	galor.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	galor.stats['terawatts'] = 13000+6500	# I don't think DITL stats reflect a design that stands a chance against a Galaxy even outnumbering it three to one.
	galor.SetProperty('Phaser', '^Dorsal.*', propertyList['CardTypeVII'],  { 'terawatts': 0.2, 'maxCharge': 0.6 } )
	galor.SetProperty('Phaser', '^Ventral.*', propertyList['CardTypeVII'], { 'terawatts': 0.2, 'maxCharge': 0.6 } )
	galor.SetProperty('Phaser', '^Aft.*', propertyList['CardTypeVII'], { 'terawatts': 0.8, 'maxCharge': 0.6 })
	galor.SetProperty('TorpedoTube', '.*', propertyList['CardDoubleTorpedoTube'])
	galor.lTorpTypes = [ ['FTBCardTorpedo', 60], ['FTBCardPlasmaBurst', 0] ]
	galor.powerPercent = ('red', 0.62)
	galor.battery = 80
	galor.lTorpTypes[0][1] = 60

	groumal = CardassianShip('groumal')
	groumal.stats['cost'] = 380
	groumal.stats['crew'] = 8
	groumal.stats['hullIndex'] = 90
	groumal.stats['length'] = 255.65
	groumal.stats['width'] = 55.13
	groumal.stats['height'] = 63.21
	groumal.stats['maneuverIndex'] = 2300
	groumal.stats['maneuverThrustIndex'] = 2300
	groumal.stats['mass'] = 150000
	groumal.stats['maxVelocity'] = 425
	groumal.stats['rangeIndex'] = 5
	groumal.stats['sensorIndex'] = 300
	groumal.stats['shieldIndex'] = 500
	groumal.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	groumal.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	groumal.stats['terawatts'] = 50
	shipList.Register(groumal, 'cardfreighter')
	shipList.Register(groumal, 'bombfreighter')

	hideki = SmallCardassianShip('hideki')
	hideki.stats['cost'] = 150
	hideki.stats['crew'] = 40
	hideki.stats['hullIndex'] = 260
	hideki.stats['length'] = 85.78
	hideki.stats['width'] = 60.14
	hideki.stats['height'] = 12.43
	hideki.stats['maneuverIndex'] = 10000
	hideki.stats['maneuverThrustIndex'] = 10000
	hideki.stats['mass'] = 100000
	hideki.stats['maxVelocity'] = 625
	hideki.stats['rangeIndex'] = 55
	hideki.stats['sensorIndex'] = 500
	hideki.stats['shieldIndex'] = 120
	hideki.SetShields( {'front': 1, 'rear': 1, 'top': 0.5, 'bottom': 1.5, 'left': 0.5, 'right': 0.5 } )
	hideki.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 0.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	hideki.stats['terawatts'] = 12000
	hideki.powerPercent = ('red', 0.68)
	hideki.battery = 60
	hideki.bakBattery = 20
	hideki.lTorpTypes[0][1] = 0

	hirogen = HirogenShip('hirogen')
	hirogen.stats['cost'] = 200
	hirogen.stats['crew'] = 80
	hirogen.stats['hullIndex'] = 500
	hirogen.stats['length'] = 65
	hirogen.stats['width'] = 39
	hirogen.stats['height'] = 17
	hirogen.stats['maneuverIndex'] = 8000
	hirogen.stats['maneuverThrustIndex'] = 8000
	hirogen.stats['mass'] = 140000
	hirogen.stats['maxVelocity'] = 700
	hirogen.stats['rangeIndex'] = 950
	hirogen.stats['sensorIndex'] = 1000
	hirogen.stats['shieldIndex'] = 720
	hirogen.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	hirogen.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	hirogen.stats['terawatts'] = 12000

	horda = DominionShip('horda')
	horda.stats['cost'] = 70
	horda.stats['crew'] = 1
	horda.stats['hullIndex'] = 16
	horda.stats['length'] = 40
	horda.stats['width'] = 40
	horda.stats['height'] = 16
	horda.stats['maneuverIndex'] = 16000
	horda.stats['maneuverThrustIndex'] = 16000
	horda.stats['mass'] = 150
	horda.stats['maxVelocity'] = 800
	horda.stats['rangeIndex'] = 20
	horda.stats['sensorIndex'] = 200
	horda.stats['shieldIndex'] = 9
	horda.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	horda.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	horda.stats['terawatts'] = 2800
	horda.lTorpTypes[0][1] = 2

	imperialrepairdock = ImperialCapShip('imperialrepairdock')
	imperialrepairdock.stats['cost'] = 8000
	imperialrepairdock.stats['crew'] = 150000
	imperialrepairdock.stats['maneuverIndex'] = 1
	imperialrepairdock.stats['maneuverThrustIndex'] = 1
	imperialrepairdock.stats['mass'] = 245000000
	imperialrepairdock.stats['maxVelocity'] = 0

	insidious = DominionShip('insidious')
	insidious.stats['cost'] = 90
	insidious.stats['crew'] = 2
	insidious.stats['hullIndex'] = 180
	insidious.stats['length'] = 120
	insidious.stats['width'] = 180
	insidious.stats['height'] = 40
	insidious.stats['maneuverIndex'] = 4200
	insidious.stats['maneuverThrustIndex'] = 5000
	insidious.stats['mass'] = 1800
	insidious.stats['maxVelocity'] = 800
	insidious.stats['rangeIndex'] = 25
	insidious.stats['sensorIndex'] = 200
	insidious.stats['shieldIndex'] = 20
	insidious.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	insidious.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	insidious.stats['terawatts'] = 10000
	insidious.SetProperty('TorpedoTube', '.*', propertyList['DomTorpedoTube'])
	insidious.battery = 30
	insidious.bakBattery = 50

	interdictorcruiser = ImperialCapShip('interdictorcruiser')
	interdictorcruiser.stats['cost'] = 900
	interdictorcruiser.stats['crew'] = 8000
	interdictorcruiser.stats['maneuverIndex'] = 150
	interdictorcruiser.stats['maneuverThrustIndex'] = 150
	interdictorcruiser.stats['mass'] = 1080000
	interdictorcruiser.stats['maxVelocity'] = 360
	interdictorcruiser.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	interdictorcruiser.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	intrepid = FedShip('intrepid')
	intrepid.stats['cost'] = 550
	intrepid.stats['crew'] = 141
	intrepid.stats['hullIndex'] = 500
	intrepid.stats['length'] = 343
	intrepid.stats['width'] = 133
	intrepid.stats['height'] = 66
	intrepid.stats['maneuverIndex'] = 9100 / 2.0
	intrepid.stats['maneuverThrustIndex'] = 9100
	intrepid.stats['mass'] = 700000
	intrepid.stats['maxVelocity'] = 700
	intrepid.stats['rangeIndex'] = 415
	intrepid.stats['sensorIndex'] = 1200
	intrepid.stats['shieldIndex'] = 270 * 2.0
	intrepid.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	intrepid.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	intrepid.stats['terawatts'] = 15000
	intrepid.SetProperty('Phaser', '.*Phaser.*', propertyList['FedTypeVIII'])
	intrepid.SetProperty('TorpedoTube', '.*', propertyList['FedStdTorpedoTube'])
	intrepid.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	intrepid.powerPercent = ('red', 0.60)
	intrepid.battery = 140
	intrepid.bakBattery = 80
	intrepid.lTorpTypes = [ ['FTBMk6PhotonTorpedo', 50], ['FTBTricobalt', 4] ]

	jeroth = CardassianShip('jeroth')
	jeroth.stats['cost'] = 125
	jeroth.stats['crew'] = 30
	jeroth.stats['hullIndex'] = 80
	jeroth.stats['length'] = 80 ##
	jeroth.stats['width'] = 80
	jeroth.stats['height'] = 80
	jeroth.stats['maneuverIndex'] = 6000
	jeroth.stats['maneuverThrustIndex'] = 6000
	jeroth.stats['mass'] = 400
	jeroth.stats['maxVelocity'] = 600
	jeroth.stats['rangeIndex'] = 70
	jeroth.stats['sensorIndex'] = 1000
	jeroth.stats['shieldIndex'] = 35
	jeroth.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	jeroth.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	jeroth.stats['terawatts'] = 1000

	karemman = DominionShip('karemman')
	karemman.stats['cost'] = 350
	karemman.stats['crew'] = 80
	karemman.stats['hullIndex'] = 200
	karemman.stats['length'] = 388
	karemman.stats['width'] = 120
	karemman.stats['height'] = 83
	karemman.stats['maneuverIndex'] = 1000
	karemman.stats['maneuverThrustIndex'] = 1000
	karemman.stats['mass'] = 500000
	karemman.stats['maxVelocity'] = 450
	karemman.stats['rangeIndex'] = 0
	karemman.stats['sensorIndex'] = 700
	karemman.stats['shieldIndex'] = 800
	karemman.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	karemman.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	karemman.stats['terawatts'] = 0

	kazon = KazonShip('kazon')
	kazon.stats['cost'] = 115
	kazon.stats['crew'] = 430
	kazon.stats['hullIndex'] = 10
	kazon.stats['length'] = 165 
	kazon.stats['width'] = 40
	kazon.stats['height'] = 70
	kazon.stats['maneuverIndex'] = 1000
	kazon.stats['maneuverThrustIndex'] = 1000
	kazon.stats['mass'] = 200000
	kazon.stats['maxVelocity'] = 650
	kazon.stats['rangeIndex'] = 100
	kazon.stats['sensorIndex'] = 200
	kazon.stats['shieldIndex'] = 70
	kazon.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	kazon.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	kazon.stats['terawatts'] = 8500

	keldon = CardassianShip('keldon')
	keldon.stats['cost'] = 480
	keldon.stats['crew'] = 800
	keldon.stats['hullIndex'] = 720
	keldon.stats['length'] = 371.88
	keldon.stats['width'] = 192.23
	keldon.stats['height'] = 70.13
	keldon.stats['maneuverIndex'] = 800
	keldon.stats['maneuverThrustIndex'] = 2400
	keldon.stats['mass'] = 1400000
	keldon.stats['maxVelocity'] = 500
	keldon.stats['rangeIndex'] = 940
	keldon.stats['sensorIndex'] = 600
	keldon.stats['shieldIndex'] = 650
	keldon.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	keldon.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	keldon.stats['terawatts'] = 24500+12250
	keldon.SetProperty('Phaser', '^Dorsal.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	keldon.SetProperty('Phaser', '^Ventral.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	keldon.SetProperty('Phaser', '^Aft.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	keldon.SetProperty('TorpedoTube', '.*', propertyList['CardDoubleTorpedoTube'])
	keldon.battery = 140
	keldon.bakBattery = 60
	keldon.lTorpTypes = [ ['FTBCardTorpedo', 80], ['FTBCardPlasmaBurst', 0] ]

	matankeldon = CardassianShip('matankeldon')
	matankeldon.stats['cost'] = 480
	matankeldon.stats['crew'] = 800
	matankeldon.stats['hullIndex'] = 720
	matankeldon.stats['length'] = 371.88
	matankeldon.stats['width'] = 192.23
	matankeldon.stats['height'] = 70.13
	matankeldon.stats['maneuverIndex'] = 800
	matankeldon.stats['maneuverThrustIndex'] = 2400
	matankeldon.stats['mass'] = 1400000
	matankeldon.stats['maxVelocity'] = 500
	matankeldon.stats['rangeIndex'] = 940
	matankeldon.stats['sensorIndex'] = 600
	matankeldon.stats['shieldIndex'] = 900
	matankeldon.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	matankeldon.SetShieldCharge( {'front': 3, 'rear': 3, 'top': 3, 'bottom': 3, 'left': 3, 'right': 3 } )
	matankeldon.stats['terawatts'] = 24500+12250
	matankeldon.SetProperty('Phaser', '^Dorsal.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	matankeldon.SetProperty('Phaser', '^Ventral.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	matankeldon.SetProperty('Phaser', '^Aft.*', propertyList['CardTypeVIII'], { 'terawatts': 0.25, 'maxCharge': 0.6 })
	matankeldon.SetProperty('TorpedoTube', '.*', propertyList['CardDoubleTorpedoTube'])
	matankeldon.battery = 140
	matankeldon.bakBattery = 60
	matankeldon.lTorpTypes = [ ['FTBCardTorpedo', 80], ['FTBCardPlasmaBurst', 0] ]

	kessokheavy = KessokShip('kessokheavy')
	kessokheavy.stats['cost'] = 3000
	kessokheavy.stats['crew'] = 800 * 3.0
	kessokheavy.stats['hullIndex'] = 2000
	kessokheavy.stats['length'] = 800.0 
	kessokheavy.stats['width'] = 800.0
	kessokheavy.stats['height'] = 120.0
	kessokheavy.stats['maneuverIndex'] = 1100
	kessokheavy.stats['maneuverThrustIndex'] = 880
	kessokheavy.stats['mass'] = 8125000
	kessokheavy.stats['maxVelocity'] = 200
	kessokheavy.stats['rangeIndex'] = 2000
	kessokheavy.stats['sensorIndex'] = 1167
	kessokheavy.stats['shieldIndex'] = 800
	kessokheavy.SetShields( {'front': 1.7, 'rear': 1, 'top': 4.0, 'bottom': 0.5, 'left': 1, 'right': 1 } )
	kessokheavy.SetShieldCharge( {'front': 3.4, 'rear': 2.0, 'top': 8.0, 'bottom': 1, 'left': 1, 'right': 1 } )
	kessokheavy.stats['terawatts'] = 60000
	kessokheavy.battery = 300
	kessokheavy.bakBattery = 200
	kessokheavy.SetProperty('Phaser', '^Forward.*', propertyList['KessokHeavyPhaser'], { 'terawatts': 1.5 })
	kessokheavy.SetProperty('TorpedoTube', '.*', propertyList['CardDoubleTorpedoTube'])
	kessokheavy.lTorpTypes = [ ['FTBKessokTorpedo', 260], ['FTBKessokPlasmaBurst', 0] ]

	kessoklight = KessokShip('kessoklight')
	kessoklight.stats['cost'] = 3000
	kessoklight.stats['crew'] = 800 * 3.0
	kessoklight.stats['hullIndex'] = 2000
	kessoklight.stats['length'] = 800.0 
	kessoklight.stats['width'] = 800.0
	kessoklight.stats['height'] = 120.0
	kessoklight.stats['maneuverIndex'] = 1500
	kessoklight.stats['maneuverThrustIndex'] = 1120
	kessoklight.stats['mass'] = 14321357
	kessoklight.stats['maxVelocity'] = 225
	kessoklight.stats['rangeIndex'] = 1940
	kessoklight.stats['sensorIndex'] = 1600
	kessoklight.stats['shieldIndex'] = 500
	kessoklight.SetShields( {'front': 1.7, 'rear': 1, 'top': 4.0, 'bottom': 0.5, 'left': 1, 'right': 1 } )
	kessoklight.SetShieldCharge( {'front': 3.4, 'rear': 2.0, 'top': 8.0, 'bottom': 1, 'left': 1, 'right': 1 } )
	kessoklight.stats['terawatts'] = 30000
	kessoklight.battery = 200
	kessoklight.bakBattery = 180
	kessoklight.SetProperty('Phaser', '^Port.*2', propertyList['KessokLightPhaser'], { 'terawatts': 0.8 })
	kessoklight.SetProperty('Phaser', '^Star.*2', propertyList['KessokLightPhaser'], { 'terawatts': 0.8 })
	kessoklight.SetProperty('TorpedoTube', '.*', propertyList['CardDoubleTorpedoTube'])
	kessoklight.lTorpTypes = [ ['FTBKessokTorpedo', 150], ['FTBKessokPlasmaBurst', 0] ]

	kessokmine = KessokShip('kessokmine')
	kessokmine.stats['cost'] = 3000
	kessokmine.stats['crew'] = 800 * 3.0
	kessokmine.stats['hullIndex'] = 2000
	kessokmine.stats['length'] = 800.0 
	kessokmine.stats['width'] = 800.0
	kessokmine.stats['height'] = 120.0
	kessokmine.stats['maneuverIndex'] = 4000
	kessokmine.stats['maneuverThrustIndex'] = 2000
	kessokmine.stats['mass'] = 3068862
	kessokmine.stats['maxVelocity'] = 10
	kessokmine.stats['rangeIndex'] = 1940
	kessokmine.stats['sensorIndex'] = 1600
	kessokmine.stats['shieldIndex'] = 0
	kessokmine.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	kessokmine.SetShieldCharge( {'front': 3, 'rear': 3, 'top': 3, 'bottom': 3, 'left': 3, 'right': 3 } )
	kessokmine.stats['terawatts'] = 60000
	kessokmine.battery = 140
	kessokmine.bakBattery = 80
	kessokmine.lTorpTypes = [ ['FTBKessokTorpedo', 100], ['FTBKessokPlasmaBurst', 0] ]

	kimal = CardassianShip('kimal')
	kimal.stats['cost'] = 300
	kimal.stats['crew'] = 80
	kimal.stats['hullIndex'] = 150
	kimal.stats['length'] = 85.78 * 1.25
	kimal.stats['width'] = 60.14 * 1.25
	kimal.stats['height'] = 12.43 * 1.25
	kimal.stats['maneuverIndex'] = 8000
	kimal.stats['maneuverThrustIndex'] = 10000
	kimal.stats['mass'] = 140000
	kimal.stats['maxVelocity'] = 700
	kimal.stats['rangeIndex'] = 950
	kimal.stats['sensorIndex'] = 650
	kimal.stats['shieldIndex'] = 200
	kimal.SetShields( {'front': 1, 'rear': 1, 'top': 2, 'bottom': 2, 'left': 1, 'right': 1 } )
	kimal.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	kimal.stats['terawatts'] = 20000 # 4000

	ktinga = KlingonShip('ktinga')
	ktinga.stats['cost'] = 280
	ktinga.stats['crew'] = 510
	ktinga.stats['hullIndex'] = 340
	ktinga.stats['length'] = 246
	ktinga.stats['width'] = 160
	ktinga.stats['height'] = 68
	ktinga.stats['maneuverIndex'] = 3000
	ktinga.stats['maneuverThrustIndex'] = 2000
	ktinga.stats['mass'] = 490000
	ktinga.stats['maxVelocity'] = 625
	ktinga.stats['rangeIndex'] = 360
	ktinga.stats['sensorIndex'] = 450
	ktinga.stats['shieldIndex'] = 380
	ktinga.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ktinga.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	ktinga.stats['terawatts'] = 8500
	ktinga.powerPercent = ('red', 0.6)
	ktinga.lTorpTypes[0][1] = 115
	ktinga.lTorpTypes[1][1] = 0
	ktinga.SetProperty('PulseWeapon', '.', propertyList['KliMk10Disruptor'])
	ktinga.SetProperty('TorpedoTube', '.*', propertyList['KliSingleTorpedoTube'])

	lancer = ImperialCapShip('lancer')
	lancer.stats['cost'] = 475
	lancer.stats['crew'] = 4000
	lancer.stats['maneuverIndex'] = 320
	lancer.stats['maneuverThrustIndex'] = 320
	lancer.stats['mass'] = 78125
	lancer.stats['maxVelocity'] = 240
	lancer.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	lancer.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	leviathan = DominionShip('leviathan')
	leviathan.stats['cost'] = 1100
	leviathan.stats['crew'] = 4200
	leviathan.stats['hullIndex'] = 1400
	leviathan.stats['length'] = 1282 * 1.2
	leviathan.stats['width'] = 864 * 1.2
	leviathan.stats['height'] = 372 * 0.8
	leviathan.stats['maneuverIndex'] = 250
	leviathan.stats['maneuverThrustIndex'] = 250
	leviathan.stats['mass'] = 24500000
	leviathan.stats['maxVelocity'] = 250
	leviathan.stats['rangeIndex'] = 1500
	leviathan.stats['sensorIndex'] = 1000
	leviathan.stats['shieldIndex'] = 3000
	leviathan.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	leviathan.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	leviathan.stats['terawatts'] = 40000
	leviathan.lTorpTypes[0][1] = 200
	leviathan.lTorpTypes[1][1] = 200

	marauder = FerengiShip('marauder')
	marauder.stats['cost'] = 980
	marauder.stats['crew'] = 680
	marauder.stats['hullIndex'] = 100
	marauder.stats['length'] = 487
	marauder.stats['width'] = 440
	marauder.stats['height'] = 80
	marauder.stats['maneuverIndex'] = 1900
	marauder.stats['maneuverThrustIndex'] = 1900
	marauder.stats['mass'] = 3800000
	marauder.stats['maxVelocity'] = 700
	marauder.stats['rangeIndex'] = 640
	marauder.stats['sensorIndex'] = 900
	marauder.stats['shieldIndex'] = 500
	marauder.SetShields( {'front': 1.75, 'rear': 1.75, 'top': 1, 'bottom': 1, 'left': 0.75, 'right': 0.75 } )
	marauder.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	marauder.stats['terawatts'] = 20000
	marauder.powerPercent = ('red', 0.66)
	marauder.battery = 250
	marauder.bakBattery = 50

	mediterranean = FedShip('mediterranean')
	mediterranean.stats['cost'] = 360
	mediterranean.stats['crew'] = 565
	mediterranean.stats['hullIndex'] = 520
	mediterranean.stats['length'] = 381.87
	mediterranean.stats['width'] = 230
	mediterranean.stats['height'] = 58.54
	mediterranean.stats['maneuverIndex'] = 4410 / 2.0
	mediterranean.stats['maneuverThrustIndex'] = 4410
	mediterranean.stats['mass'] = 870000
	mediterranean.stats['maxVelocity'] = 525 * 1.25
	mediterranean.stats['rangeIndex'] = 645
	mediterranean.stats['sensorIndex'] = 600
	mediterranean.stats['shieldIndex'] = 100 * 2.5
	mediterranean.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	mediterranean.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	mediterranean.stats['terawatts'] = 2500 * 4.0		# DITL, this time you were full of it. ;)
	mediterranean.powerPercent = ('red', 0.65)
	mediterranean.battery = 100
	mediterranean.bakBattery = 80
	mediterranean.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	mediterranean.SetProperty('WeaponSystem', 'Phaser.*', propertyList['PhaserSystem'])
	mediterranean.SetProperty('Phaser', '.*', propertyList['FedTypeVIIIBank'], { 'maxCharge': 0.5 })
	mediterranean.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 50] ]
	shipList.Register(mediterranean, 'mediterranean')

	miranda = FedShip('miranda')
	miranda.stats['cost'] = 200
	miranda.stats['crew'] = 230
	miranda.stats['hullIndex'] = 120
	miranda.stats['length'] = 230
	miranda.stats['width'] = 127.1
	miranda.stats['height'] = 51
	miranda.stats['maneuverIndex'] = 5500
	miranda.stats['maneuverThrustIndex'] = 5500
	miranda.stats['mass'] = 230000
	miranda.stats['maxVelocity'] = 650
	miranda.stats['rangeIndex'] = 255
	miranda.stats['sensorIndex'] = 500
	miranda.stats['shieldIndex'] = 495
	miranda.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	miranda.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	miranda.stats['terawatts'] = 8000
	miranda.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	miranda.SetProperty('WeaponSystem', 'Phaser.*', propertyList['PhaserSystem'])
	miranda.SetProperty('Phaser', '.*', propertyList['FedTypeVIIBank'], { 'terawatts': 0.3, 'maxCharge': 0.3 })
	miranda.SetProperty('Phaser', 'Mega.*', propertyList['FedTypeVII'])
	miranda.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 40] ]
	shipList.Register(miranda, 'miranda')

	mirandatmp = FedShip('mirandatmp')
	mirandatmp.stats['cost'] = 200
	mirandatmp.stats['crew'] = 230
	mirandatmp.stats['hullIndex'] = 120
	mirandatmp.stats['length'] = 230
	mirandatmp.stats['width'] = 127.1
	mirandatmp.stats['height'] = 51
	mirandatmp.stats['maneuverIndex'] = 1500
	mirandatmp.stats['maneuverThrustIndex'] = 2500
	mirandatmp.stats['mass'] = 230000
	mirandatmp.stats['maxVelocity'] = 450
	mirandatmp.stats['rangeIndex'] = 255
	mirandatmp.stats['sensorIndex'] = 250
	mirandatmp.stats['shieldIndex'] = 215
	mirandatmp.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	mirandatmp.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	mirandatmp.stats['terawatts'] = 4000
	mirandatmp.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	mirandatmp.SetProperty('WeaponSystem', 'Phaser.*', propertyList['MultiFirePhaserSystem'])
	mirandatmp.SetProperty('Phaser', '.*', propertyList['FedTMPVIIa'])
	mirandatmp.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIb'])
	mirandatmp.SetProperty('Phaser', 'Mega.*', propertyList['FedTMPVIIIMega'])
	mirandatmp.lTorpTypes = [ ['FTBMk1PhotonTorpedo', 40] ]
	shipList.Register(mirandatmp, 'mirandatmp')

	missileboat = ImperialShip('missileboat')
	missileboat.stats['cost'] = 90
	missileboat.stats['crew'] = 1
	missileboat.stats['maneuverIndex'] = 4000
	missileboat.stats['maneuverThrustIndex'] = 6000
	missileboat.stats['mass'] = 45
	missileboat.stats['maxVelocity'] = 900
	missileboat.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	missileboat.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	nebula = FedShip('nebula')
	nebula.stats['cost'] = 800
	nebula.stats['crew'] = 780
	nebula.stats['hullIndex'] = 1000
	nebula.stats['length'] = 442.23
	nebula.stats['width'] = 318.11
	nebula.stats['height'] = 130.43
	nebula.stats['maneuverIndex'] = 1250
	nebula.stats['maneuverThrustIndex'] = 1250
	nebula.stats['mass'] = 4500000
	nebula.stats['maxVelocity'] = 475
	nebula.stats['rangeIndex'] = 800
	nebula.stats['sensorIndex'] = 900
	nebula.stats['shieldIndex'] = 900
	nebula.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nebula.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nebula.stats['terawatts'] = 50000 * 0.825 # Not as much required as Galaxy, fewer arrays
	nebula.powerPercent = ('red', 0.6)
	nebula.SetProperty('Phaser', '.*', propertyList['FedTypeX'], { 'terawatts': 0.2, 'maxCharge': 0.3 })
	nebula.SetProperty('Phaser', '^Ventral Phaser [1-4]', propertyList['FedTypeX'])
	nebula.SetProperty('Phaser', '^Dorsal Phaser [1-4]', propertyList['FedTypeX'])
	nebula.SetProperty('TorpedoTube', '.*', propertyList['FedSingleTorpedoTube'])
	nebula.SetProperty('WeaponSystem', 'Phasers', propertyList['PhaserSystem'])
	nebula.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 220] ]
	shipList.Register(nebula, 'nebulaperegrine')
	shipList.Register(nebula, 'e3m2nebula')

	nebulonb = ImperialCapShip('nebulonb')
	nebulonb.stats['cost'] = 485
	nebulonb.stats['crew'] = 850
	nebulonb.stats['maneuverIndex'] = 160
	nebulonb.stats['maneuverThrustIndex'] = 160
	nebulonb.stats['mass'] = 1316874
	nebulonb.stats['maxVelocity'] = 240
	nebulonb.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nebulonb.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	neghvar = KlingonShip('neghvar')
	neghvar.stats['cost'] = 1900
	neghvar.stats['crew'] = 2780
	neghvar.stats['hullIndex'] = 2900
	neghvar.stats['length'] = 682.32
	neghvar.stats['width'] = 470.09
	neghvar.stats['height'] = 136.65
	neghvar.stats['maneuverIndex'] = 570
	neghvar.stats['maneuverThrustIndex'] = 770
	neghvar.stats['mass'] = 7000000
	neghvar.stats['maxVelocity'] = 400
	neghvar.stats['rangeIndex'] = 1280
	neghvar.stats['sensorIndex'] = 900
	neghvar.stats['shieldIndex'] = 1600
	neghvar.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	neghvar.SetShieldCharge( {'front': 1.5, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 0.75, 'right': 0.75 } )
	neghvar.stats['terawatts'] = 205000
	neghvar.SetProperty('Phaser', '.', propertyList['KliMk12DisruptorBeam'], { 'terawatts': 0.8 } )
	neghvar.SetProperty('PulseWeapon', '.*', propertyList['KliMk12PulseDisruptor'])
	neghvar.SetProperty('PulseWeapon', '.*Mk18.*', propertyList['KliMk18Disruptor'], { 'terawatts': 6.0 } )
	neghvar.SetProperty('TorpedoTube', '.*', propertyList['KliTripleTorpedoTube'])
	neghvar.SetProperty('WeaponSystem', '.*Beams$', propertyList['MultiFirePhaserSystem'])
	neghvar.SetProperty('WeaponSystem', '.*Cannon.*', propertyList['MultiFirePhaserSystem'])
	neghvar.powerPercent = ('red', 0.75)
	neghvar.battery = 300
	neghvar.bakBattery = 200
	neghvar.lTorpTypes = [ ['FTBKlingonTripleTorpedo', 200], ['FTBFastKlingonTorpedo', 500] ]
	shipList.Register(neghvar, 'mpneghvar')

	neworleans = FedShip('neworleans')
	neworleans.stats['cost'] = 330
	neworleans.stats['crew'] = 190
	neworleans.stats['hullIndex'] = 450
	neworleans.stats['length'] = 350
	neworleans.stats['width'] = 290
	neworleans.stats['height'] = 83
	neworleans.stats['maneuverIndex'] = 7000
	neworleans.stats['maneuverThrustIndex'] = 7000
	neworleans.stats['mass'] = 900000
	neworleans.stats['maxVelocity'] = 750
	neworleans.stats['rangeIndex'] = 145
	neworleans.stats['sensorIndex'] = 900
	neworleans.stats['shieldIndex'] = 355
	neworleans.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	neworleans.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	neworleans.stats['terawatts'] = 9500
	neworleans.SetProperty('Phaser', '.', propertyList['FedTypeVIII'])
	neworleans.SetProperty('TorpedoTube', '.', propertyList['FedStdTorpedoTube'])
	neworleans.powerPercent = ('red', 0.65)
	neworleans.battery = 30
	neworleans.bakBattery = 50
	neworleans.lTorpTypes[0][1] = 90

	norexan = RomulanShip('norexan')
	norexan.stats['cost'] = 1530
	norexan.stats['crew'] = 850
	norexan.stats['hullIndex'] = 400
	norexan.stats['length'] = 603.5
	norexan.stats['width'] = 911.4
	norexan.stats['height'] = 94
	norexan.stats['maneuverIndex'] = 2700
	norexan.stats['maneuverThrustIndex'] = 5000
	norexan.stats['mass'] = 1020000
	norexan.stats['maxVelocity'] = 725 / 0.8476
	norexan.stats['rangeIndex'] = 1660
	norexan.stats['sensorIndex'] = 1800
	norexan.stats['shieldIndex'] = 1200
	norexan.SetShields( {'front': 1.25, 'rear': 0.75, 'top': 1.25, 'bottom': 1.25, 'left': 0.75, 'right': 0.75 } )
	norexan.SetShieldCharge( {'front': 2, 'rear': 2, 'top': 2, 'bottom': 2, 'left': 2, 'right': 2 } )
	norexan.stats['terawatts'] = 30000
	norexan.SetProperty('TorpedoTube', '.', propertyList['RomTorpedoTube'])
	norexan.SetProperty('PulseWeapon', '.', propertyList['RomHeavyPulseDisruptor'])
	norexan.SetProperty('PulseWeapon', '^Star Cannon [1-2]', propertyList['RomMedPulseDisruptor'])
	norexan.SetProperty('PulseWeapon', '^Port Cannon [1-2]', propertyList['RomMedPulseDisruptor'])
	norexan.powerPercent = ('red', 0.42)
	norexan.lTorpTypes[0][1] = 40
	norexan.lTorpTypes[1][1] = 0
	norexan.battery = 400
	norexan.bakBattery = 160

	norway = FedShip('norway')
	norway.stats['cost'] = 305
	norway.stats['crew'] = 150
	norway.stats['hullIndex'] = 250
	norway.stats['length'] = 364.77
	norway.stats['width'] = 225.61
	norway.stats['height'] = 52.48
	norway.stats['maneuverIndex'] = 5000
	norway.stats['maneuverThrustIndex'] = 5000
	norway.stats['mass'] = 650000
	norway.stats['maxVelocity'] = 450
	norway.stats['rangeIndex'] = 200
	norway.stats['sensorIndex'] = 1100
	norway.stats['shieldIndex'] = 300
	norway.SetShields( {'front': 1.5, 'rear': 1.5, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	norway.SetShieldCharge( {'front': 1.5, 'rear': 1.5, 'top': 1, 'bottom': 1, 'left': 0.5, 'right': 0.5 } )
	norway.stats['terawatts'] = 9000
	norway.SetProperty('Phaser', '.*', propertyList['FedTypeVIII'])
	norway.SetProperty('TorpedoTube', '.*', propertyList['FedPFTorpedoTube'])
	norway.powerPercent = ('red', 0.62)
	norway.battery = 140
	norway.bakBattery = 60
	norway.lTorpTypes[0][1] = 50

	nova = FedShip('nova')
	nova.stats['cost'] = 320
	nova.stats['crew'] = 80
	nova.stats['hullIndex'] = 150
	nova.stats['length'] = 165
	nova.stats['width'] = 62
	nova.stats['height'] = 34
	nova.stats['maneuverIndex'] = 9200 / 1.5
	nova.stats['maneuverThrustIndex'] = 9200
	nova.stats['mass'] = 80000
	nova.stats['maxVelocity'] = 500
	nova.stats['rangeIndex'] = 400
	nova.stats['sensorIndex'] = 2000
	nova.stats['shieldIndex'] = 455
	nova.SetShields( {'front': 1.2, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	nova.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nova.stats['terawatts'] = 8000
	nova.SetProperty('Phaser', '.', propertyList['FedTypeVIII'])
	nova.SetProperty('TorpedoTube', '.', propertyList['FedStdTorpedoTube'])
	nova.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	nova.powerPercent = ('red', 0.55)
	nova.battery = 150
	nova.bakBattery = 60
	nova.lTorpTypes[0][1] = 25

	nx01 = FedShip('entnx01')
	nx01.stats['cost'] = 28
	nx01.stats['crew'] = 82
	nx01.stats['hullIndex'] = 126
	nx01.stats['length'] = 150
	nx01.stats['width'] = 116
	nx01.stats['height'] = 30
	nx01.stats['maneuverIndex'] = 2000 / 1.5
	nx01.stats['maneuverThrustIndex'] = 2000 * 3.0
	nx01.stats['mass'] = 280000
	nx01.stats['maxVelocity'] = 400
	nx01.stats['rangeIndex'] = 400
	nx01.stats['sensorIndex'] = 300
	nx01.stats['shieldIndex'] = 1
	nx01.SetShields( {'front': 1.2, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	nx01.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nx01.stats['terawatts'] = 12 * 5.0
	nx01.SetProperty('Phaser', '.', propertyList['PhaseCannon'])
	# nx01.SetProperty('PulseWeapon', '.', propertyList['RomHeavyPulseDisruptor'])
	nx01.SetProperty('TorpedoTube', '.', propertyList['FedSingleTorpedoTube'])
	nx01.SetProperty('WeaponSystem', '.*Phase.*', propertyList['PhaserSystem'])
	nx01.powerPercent = ('red', 0.65)
	nx01.battery = 60
	nx01.bakBattery = 30
	nx01.lTorpTypes = [ ['ENTNXTorp2', 30], ['ENTNXTorp', 10] ]
	shipList.Register(nx01, 'entnx01')

	nxintrepid = FedShip('entnxintrepid')
	nxintrepid.stats['cost'] = 23
	nxintrepid.stats['crew'] = 47
	nxintrepid.stats['hullIndex'] = 75
	nxintrepid.stats['length'] = 140
	nxintrepid.stats['width'] = 100
	nxintrepid.stats['height'] = 25
	nxintrepid.stats['maneuverIndex'] = 2000 / 1.5
	nxintrepid.stats['maneuverThrustIndex'] = 2000 * 4.0
	nxintrepid.stats['mass'] = 180000
	nxintrepid.stats['maxVelocity'] = 400
	nxintrepid.stats['rangeIndex'] = 400
	nxintrepid.stats['sensorIndex'] = 300
	nxintrepid.stats['shieldIndex'] = 1
	nxintrepid.SetShields( {'front': 1.2, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	nxintrepid.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	nxintrepid.stats['terawatts'] = 8 * 5.0
	nxintrepid.SetProperty('Phaser', '.', propertyList['PhaseCannon'])
	nxintrepid.SetProperty('TorpedoTube', '.', propertyList['FedSingleTorpedoTube'])
	nxintrepid.SetProperty('WeaponSystem', '.*Phase.*', propertyList['PhaserSystem'])
	nxintrepid.powerPercent = ('red', 0.72)
	nxintrepid.battery = 40
	nxintrepid.bakBattery = 30
	nxintrepid.lTorpTypes = [ ['ENTNXTorp2', 20] ]
	shipList.Register(nxintrepid, 'entneptune')

	oberth = FedShip('oberth')
	oberth.stats['cost'] = 116
	oberth.stats['crew'] = 80
	oberth.stats['hullIndex'] = 10
	oberth.stats['length'] = 150.81
	oberth.stats['width'] = 87
	oberth.stats['height'] = 41
	oberth.stats['maneuverIndex'] = 9500
	oberth.stats['maneuverThrustIndex'] = 4500
	oberth.stats['mass'] = 94000
	oberth.stats['maxVelocity'] = 500
	oberth.stats['rangeIndex'] = 95
	oberth.stats['sensorIndex'] = 600
	oberth.stats['shieldIndex'] = 90
	oberth.SetShields( {'front': 1.2, 'rear': 1, 'top': 1.2, 'bottom': 1.2, 'left': 1, 'right': 1 } )
	oberth.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	oberth.stats['terawatts'] = 3500
	oberth.SetProperty('Phaser', '.', propertyList['FedTypeVIIBank'])
	oberth.SetProperty('TorpedoTube', '.', propertyList['Fed2ndTorpedoTube'])
	oberth.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	oberth.powerPercent = ('red', 0.5)
	oberth.battery = 150
	oberth.bakBattery = 60
	oberth.lTorpTypes[0][1] = 25

	orbitaldefensedrone = CardassianShip('orbitaldefensedrone')
	orbitaldefensedrone.stats['cost'] = 480
	orbitaldefensedrone.stats['crew'] = 0
	orbitaldefensedrone.stats['hullIndex'] = 900
	orbitaldefensedrone.stats['length'] = 40
	orbitaldefensedrone.stats['width'] = 40
	orbitaldefensedrone.stats['height'] = 46
	orbitaldefensedrone.stats['maneuverIndex'] = 4000
	orbitaldefensedrone.stats['maneuverThrustIndex'] = 4000
	orbitaldefensedrone.stats['mass'] = 75000
	orbitaldefensedrone.stats['maxVelocity'] = 400
	orbitaldefensedrone.stats['rangeIndex'] = 900
	orbitaldefensedrone.stats['sensorIndex'] = 1000
	orbitaldefensedrone.stats['shieldIndex'] = 900
	orbitaldefensedrone.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	orbitaldefensedrone.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	orbitaldefensedrone.stats['terawatts'] = 20000

	orbitaldefenseplatform = CardassianShip('orbitaldefenseplatform')
	orbitaldefenseplatform.stats['cost'] = 600
	orbitaldefenseplatform.stats['crew'] = 0
	orbitaldefenseplatform.stats['hullIndex'] = 900
	orbitaldefenseplatform.stats['length'] = 40
	orbitaldefenseplatform.stats['width'] = 40
	orbitaldefenseplatform.stats['height'] = 46
	orbitaldefenseplatform.stats['maneuverIndex'] = 800
	orbitaldefenseplatform.stats['maneuverThrustIndex'] = 800
	orbitaldefenseplatform.stats['mass'] = 75000
	orbitaldefenseplatform.stats['maxVelocity'] = 120
	orbitaldefenseplatform.stats['rangeIndex'] = 900
	orbitaldefenseplatform.stats['sensorIndex'] = 1000
	orbitaldefenseplatform.stats['shieldIndex'] = 900
	orbitaldefenseplatform.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	orbitaldefenseplatform.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	orbitaldefenseplatform.stats['terawatts'] = 42000

	packrat = FedShip('packrat')
	packrat.stats['cost'] = 380
	packrat.stats['crew'] = 5
	packrat.stats['hullIndex'] = 90
	packrat.stats['length'] = 140
	packrat.stats['width'] = 90
	packrat.stats['height'] = 30
	packrat.stats['maneuverIndex'] = 4000
	packrat.stats['maneuverThrustIndex'] = 4000
	packrat.stats['mass'] = 130000
	packrat.stats['maxVelocity'] = 450
	packrat.stats['rangeIndex'] = 0
	packrat.stats['sensorIndex'] = 1000
	packrat.stats['shieldIndex'] = 400
	packrat.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	packrat.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	packrat.stats['terawatts'] = 0
	packrat.lTorpTypes[0][1] = 0

	peregrine = SmallFedShip('peregrine')
	peregrine.stats['cost'] = 54
	peregrine.stats['crew'] = 1
	peregrine.stats['hullIndex'] = 50
	peregrine.stats['length'] = 14
	peregrine.stats['width'] = 13.6
	peregrine.stats['height'] = 4.53
	peregrine.stats['maneuverIndex'] = 24000
	peregrine.stats['maneuverThrustIndex'] = 24000
	peregrine.stats['mass'] = 27
	peregrine.stats['maxVelocity'] = 850
	peregrine.stats['rangeIndex'] = 20
	peregrine.stats['sensorIndex'] = 300
	peregrine.stats['shieldIndex'] = 6
	peregrine.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	peregrine.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	peregrine.SetProperty('PulseWeapon', '.', propertyList['FedPulsePhaser'])
	peregrine.stats['terawatts'] = 2000
	peregrine.powerPercent = ('red', 0.72)
	peregrine.battery = 45
	peregrine.bakBattery = 30
	peregrine.lTorpTypes[0][1] = 2


	prometheus = FedShip('prometheus')
	prometheus.stats['cost'] = 1649
	prometheus.stats['crew'] = 175
	prometheus.stats['hullIndex'] = 3100
	prometheus.stats['length'] = 415
	prometheus.stats['width'] = 163
	prometheus.stats['height'] = 64
	prometheus.stats['maneuverIndex'] = 12500
	prometheus.stats['maneuverThrustIndex'] = 12500
	prometheus.stats['mass'] = 950000
	prometheus.stats['maxVelocity'] = 625
	prometheus.stats['rangeIndex'] = 1180
	prometheus.stats['sensorIndex'] = 1000
	prometheus.stats['shieldIndex'] = 1450
	prometheus.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	prometheus.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	prometheus.stats['terawatts'] = 60000
	prometheus.lTorpTypes[0][1] = 0
	prometheus.lTorpTypes[2][1] = 290


	prospector = FedShip('prospector')
	prospector.stats['cost'] = 380
	prospector.stats['crew'] = 50
	prospector.stats['hullIndex'] = 500
	prospector.stats['length'] = 500
	prospector.stats['width'] = 180
	prospector.stats['height'] = 90
	prospector.stats['maneuverIndex'] = 2100
	prospector.stats['maneuverThrustIndex'] = 2100
	prospector.stats['mass'] = 2000000
	prospector.stats['maxVelocity'] = 425
	prospector.stats['rangeIndex'] = 0
	prospector.stats['sensorIndex'] = 1000
	prospector.stats['shieldIndex'] = 800
	prospector.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	prospector.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	prospector.stats['terawatts'] = 1000
	prospector.SetProperty('TorpedoTube', '.*', propertyList['Fed2ndTorpedoTube'])

	raider = SmallFedShip('raider')
	raider.stats['cost'] = 100
	raider.stats['crew'] = 4
	raider.stats['hullIndex'] = 300
	raider.stats['length'] = 60
	raider.stats['width'] = 66
	raider.stats['height'] = 14.6
	raider.stats['maneuverIndex'] = 15000
	raider.stats['maneuverThrustIndex'] = 15000
	raider.stats['mass'] = 300
	raider.stats['maxVelocity'] = 700
	raider.stats['rangeIndex'] = 100
	raider.stats['sensorIndex'] = 1000
	raider.stats['shieldIndex'] = 110
	raider.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	raider.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	raider.stats['terawatts'] = 2250
	raider.lTorpTypes[0][1] = 30

	tpriex = RomulanShip('tpriex')
	tpriex.stats['cost'] = 940
	tpriex.stats['crew'] = 775
	tpriex.stats['hullIndex'] = 920
	tpriex.stats['length'] = 920 ##
	tpriex.stats['width'] = 920
	tpriex.stats['height'] = 920
	tpriex.stats['maneuverIndex'] = 200
	tpriex.stats['maneuverThrustIndex'] = 200
	tpriex.stats['mass'] = 3500000
	tpriex.stats['maxVelocity'] = 300
	tpriex.stats['rangeIndex'] = 880
	tpriex.stats['sensorIndex'] = 1000
	tpriex.stats['shieldIndex'] = 1000
	tpriex.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tpriex.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tpriex.powerPercent = ('red', 0.8)
	tpriex.stats['terawatts'] = 0

	rrderex = RomulanShip('rrderex')
	rrderex.stats['cost'] = 160
	rrderex.stats['crew'] = 1
	rrderex.stats['hullIndex'] = 425
	rrderex.stats['length'] = 98
	rrderex.stats['width'] = 94
	rrderex.stats['height'] = 15
	rrderex.stats['maneuverIndex'] = 17600
	rrderex.stats['maneuverThrustIndex'] = 17600
	rrderex.stats['mass'] = 3000
	rrderex.stats['maxVelocity'] = 750
	rrderex.stats['rangeIndex'] = 500
	rrderex.stats['sensorIndex'] = 600
	rrderex.stats['shieldIndex'] = 120
	rrderex.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	rrderex.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	rrderex.stats['terawatts'] = 6000
	rrderex.powerPercent = ('red', 0.8)
	rrderex.lTorpTypes[0][1] = 10
	rrderex.lTorpTypes[1][1] = 0
	rrderex.SetProperty('TorpedoTube', '.*', propertyList['RomTorpedoTube'])

	saber = FedShip('saber')
	saber.stats['cost'] = 330
	saber.stats['crew'] = 40
	saber.stats['hullIndex'] = 310
	saber.stats['length'] = 190
	saber.stats['width'] = 250
	saber.stats['height'] = 41
	saber.stats['maneuverIndex'] = 15000 / 1.25
	saber.stats['maneuverThrustIndex'] = 12000 / 1.25
	saber.stats['mass'] = 250000
	saber.stats['maxVelocity'] = 500
	saber.stats['rangeIndex'] = 175
	saber.stats['sensorIndex'] = 650
	saber.stats['shieldIndex'] = 370
	saber.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	saber.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	saber.stats['terawatts'] = 4000
	saber.SetProperty('Phaser', '.*', propertyList['FedTypeIX'])
	# saber.SetProperty('PulseWeapon', '.*', propertyList['FedC1PulsePhaser'], { 'maxCharge': 0.5, 'terawatts': 2.0 })
	saber.SetProperty('PulseWeapon', '.*', propertyList['FedMk5TorpedoTurret'])

	saber.SetProperty('TorpedoTube', '.', propertyList['FedPFTorpedoTube'])
	saber.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	saber.powerPercent = ('red', 0.6)
	saber.battery = 60
	saber.bakBattery = 60
	saber.lTorpTypes[0][1] = 30

	salvagetug = ImperialShip('salvagetug')
	salvagetug.stats['cost'] = 220
	salvagetug.stats['crew'] = 1
	salvagetug.stats['maneuverIndex'] = 10000
	salvagetug.stats['maneuverThrustIndex'] = 10000
	salvagetug.stats['mass'] = 42500
	salvagetug.stats['maxVelocity'] = 540
	salvagetug.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	salvagetug.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	scimitar = RomulanShip('scimitar')
	scimitar.stats['cost'] = 7745
	scimitar.stats['crew'] = 1650
	scimitar.stats['hullIndex'] = 1000
	scimitar.stats['length'] = 890
	scimitar.stats['width'] = 1350
	scimitar.stats['height'] = 245
	scimitar.stats['maneuverIndex'] = 3000
	scimitar.stats['maneuverThrustIndex'] = 1680
	scimitar.stats['mass'] = 14320000
	scimitar.stats['maxVelocity'] = 450
	scimitar.stats['rangeIndex'] = 1420
	scimitar.stats['sensorIndex'] = 1420
	scimitar.stats['shieldIndex'] = 800
	scimitar.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	scimitar.SetShieldCharge( {'front': 2, 'rear': 2, 'top': 2, 'bottom': 2, 'left': 2, 'right': 2 } )
	scimitar.stats['terawatts'] = 500000
	scimitar.powerPercent = ('red', 0.7)
	scimitar.battery = 400
	scimitar.bakBattery = 160
	scimitar.lTorpTypes[0][1] = 500
	scimitar.lTorpTypes[1][1] = 40
	scimitar.SetProperty('WeaponSystem', '.*', propertyList['MultiFirePhaserSystem'])
	shipList.Register(scimitar, 'scimitarjh')

	sds = KlingonShip('sds')
	sds.stats['cost'] = 850
	sds.stats['crew'] = 0
	sds.stats['hullIndex'] = 1300
	sds.stats['length'] = 1532
	sds.stats['width'] = 1532
	sds.stats['height'] = 1584
	sds.stats['maneuverIndex'] = 200
	sds.stats['maneuverThrustIndex'] = 200
	sds.stats['mass'] = 180000000
	sds.stats['maxVelocity'] = 100
	sds.stats['rangeIndex'] = 900
	sds.stats['sensorIndex'] = 1000
	sds.stats['shieldIndex'] = 1300
	sds.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sds.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sds.stats['terawatts'] = 50000
	sds.lTorpTypes[0][1] = 300
	sds.lTorpTypes[1][1] = 300
	sds.SetProperty('TorpedoTube', '.*', propertyList['KliTripleTorpedoTube'])

	shadowdroid = ImperialShip('shadowdroid')
	shadowdroid.stats['cost'] = 95
	shadowdroid.stats['crew'] = 0
	shadowdroid.stats['maneuverIndex'] = 4000
	shadowdroid.stats['maneuverThrustIndex'] = 4000
	shadowdroid.stats['mass'] = 5
	shadowdroid.stats['maxVelocity'] = 720
	shadowdroid.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	shadowdroid.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	shelley = FedShip('shelley')
	shelley.stats['cost'] = 300
	shelley.stats['crew'] = 200
	shelley.stats['hullIndex'] = 20
	shelley.stats['length'] = 261.5
	shelley.stats['width'] = 185
	shelley.stats['height'] = 100
	shelley.stats['maneuverIndex'] = 2100
	shelley.stats['maneuverThrustIndex'] = 2100
	shelley.stats['mass'] = 800000
	shelley.stats['maxVelocity'] = 525
	shelley.stats['rangeIndex'] = 0
	shelley.stats['sensorIndex'] = 1000
	shelley.stats['shieldIndex'] = 250
	shelley.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	shelley.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	shelley.stats['terawatts'] = 4000
	shelley.lTorpTypes[0][1] = 0
	shipList.Register(shelley, 'curryclass')
	shipList.Register(shelley, 'ragingqueen')

	shrike = RomulanShip('shrike')
	shrike.stats['cost'] = 262
	shrike.stats['crew'] = 30
	shrike.stats['hullIndex'] = 340
	shrike.stats['length'] = 40
	shrike.stats['width'] = 34
	shrike.stats['height'] = 15
	shrike.stats['maneuverIndex'] = 22000
	shrike.stats['maneuverThrustIndex'] = 22000
	shrike.stats['mass'] = 75000
	shrike.stats['maxVelocity'] = 750
	shrike.stats['rangeIndex'] = 200
	shrike.stats['sensorIndex'] = 1000
	shrike.stats['shieldIndex'] = 220
	shrike.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	shrike.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	shrike.lTorpTypes[0][1] = 2
	shrike.lTorpTypes[1][1] = 0
	shrike.stats['terawatts'] = 7750

	sonabattleship = SonaShip('sonabattleship')
	sonabattleship.stats['cost'] = 1835
	sonabattleship.stats['crew'] = 1400
	sonabattleship.stats['hullIndex'] = 600
	sonabattleship.stats['length'] = 855
	sonabattleship.stats['width'] = 1055
	sonabattleship.stats['height'] = 200
	sonabattleship.stats['maneuverIndex'] = 1600
	sonabattleship.stats['maneuverThrustIndex'] = 1600
	sonabattleship.stats['mass'] = 9000000
	sonabattleship.stats['maxVelocity'] = 425
	sonabattleship.stats['rangeIndex'] = 1410
	sonabattleship.stats['sensorIndex'] = 1000
	sonabattleship.stats['shieldIndex'] = 1500
	sonabattleship.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sonabattleship.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sonabattleship.stats['terawatts'] = 55000

	sovereign = FedShip('sovereign')
	sovereign.stats['cost'] = 2400
	sovereign.stats['crew'] = 700
	# sovereign.stats['hullIndex'] = 1900
	sovereign.stats['hullIndex'] = 1000
	sovereign.stats['length'] = 680
	sovereign.stats['width'] = 240
	sovereign.stats['height'] = 87
	sovereign.stats['maneuverIndex'] = 1800
	sovereign.stats['maneuverThrustIndex'] = 3500
	sovereign.stats['mass'] = 3500000
	sovereign.stats['maxVelocity'] = 500
	sovereign.stats['rangeIndex'] = 1260
	sovereign.stats['sensorIndex'] = 1290
	# sovereign.stats['shieldIndex'] = 1700
	sovereign.stats['shieldIndex'] = 1200
	sovereign.SetShields( {'front': 1.5, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sovereign.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sovereign.stats['terawatts'] = 85000
	sovereign.SetProperty('Phaser', '.*', propertyList['FedTypeXII'], { 'terawatts': 0.35, 'maxCharge': 0.75 })
	sovereign.SetProperty('Phaser', '^Dorsal Phaser [1-4].*', propertyList['FedTypeXII'])
	sovereign.SetProperty('Phaser', '^Ventral Phaser [1-4].*', propertyList['FedTypeXII'])
	sovereign.SetProperty('PulseWeapon', '^Torpedo Turret', propertyList['FedQuantumTorpedoTurret'])
	sovereign.SetProperty('TorpedoTube', '.*', propertyList['FedType4BurstTorpedoTube'])
	sovereign.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	# sovereign.powerPercent = ('red', 0.8523)
	sovereign.powerPercent = ('red', 0.525)
	sovereign.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 150], ['FTBMk5PhotonTorpedoS', 10], ['FTBMk5PhotonTorpedoM', 10], ['FTBMk5PhotonTorpedoB', 10] ]
	sovereign.battery = 300
	sovereign.bakBattery = 200

	sovereignmk2 = FedShip('sovereignmk2')
	sovereignmk2.stats['cost'] = 2400
	sovereignmk2.stats['crew'] = 700
	# sovereignmk2.stats['hullIndex'] = 1900
	sovereignmk2.stats['hullIndex'] = 1000
	sovereignmk2.stats['length'] = 680
	sovereignmk2.stats['width'] = 240
	sovereignmk2.stats['height'] = 87
	sovereignmk2.stats['maneuverIndex'] = 1800
	sovereignmk2.stats['maneuverThrustIndex'] = 3500
	sovereignmk2.stats['mass'] = 3500000
	sovereignmk2.stats['maxVelocity'] = 500
	sovereignmk2.stats['rangeIndex'] = 1260
	sovereignmk2.stats['sensorIndex'] = 1420
	# sovereignmk2.stats['shieldIndex'] = 1700
	sovereignmk2.stats['shieldIndex'] = 2125 - 500
	sovereignmk2.SetShields( {'front': 1.5, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sovereignmk2.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	sovereignmk2.stats['terawatts'] = 100000
	sovereignmk2.SetProperty('Phaser', '.*', propertyList['FedTypeXII'], { 'terawatts': 0.35, 'maxCharge': 0.75 })
	sovereignmk2.SetProperty('Phaser', '^Dorsal Phaser [1-4].*', propertyList['FedTypeXII'])
	sovereignmk2.SetProperty('Phaser', '^Ventral Phaser [1-4].*', propertyList['FedTypeXII'])
	sovereignmk2.SetProperty('PulseWeapon', '^Torpedo Turret', propertyList['FedQuantumTorpedoTurret'])
	sovereignmk2.SetProperty('TorpedoTube', '.*', propertyList['FedSingleTorpedoTube'])
	sovereignmk2.SetProperty('TorpedoTube', '^.*Torpedo [1-2]$', propertyList['FedType4BurstTorpedoTube'])
	sovereignmk2.SetProperty('WeaponSystem', '.*Phaser.*', propertyList['PhaserSystem'])
	# sovereignmk2.powerPercent = ('red', 0.8523)
	sovereignmk2.powerPercent = ('red', 0.5)
	sovereignmk2.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 190], ['FTBMk5PhotonTorpedoS', 16], ['FTBMk5PhotonTorpedoM', 16] ]
	sovereignmk2.battery = 300
	sovereignmk2.bakBattery = 200
	shipList.Register(sovereignmk2, 'sovereignenterprise')

	soyuz = FedShip('soyuz')
	soyuz.stats['cost'] = 200
	soyuz.stats['crew'] = 230
	soyuz.stats['hullIndex'] = 120
	soyuz.stats['length'] = 230
	soyuz.stats['width'] = 127.1
	soyuz.stats['height'] = 51
	soyuz.stats['maneuverIndex'] = 5500
	soyuz.stats['maneuverThrustIndex'] = 5500
	soyuz.stats['mass'] = 230000
	soyuz.stats['maxVelocity'] = 650
	soyuz.stats['rangeIndex'] = 255
	soyuz.stats['sensorIndex'] = 500
	soyuz.stats['shieldIndex'] = 495
	soyuz.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	soyuz.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	soyuz.stats['terawatts'] = 8000
	soyuz.SetProperty('TorpedoTube', '', propertyList['Fed2ndTorpedoTube'])
	soyuz.SetProperty('WeaponSystem', 'Phaser.*', propertyList['PhaserSystem'])
	soyuz.SetProperty('Phaser', '.*', propertyList['FedTMPVIIIa'])
	soyuz.SetProperty('Phaser', '.*2', propertyList['FedTMPVIIIb'])
	soyuz.SetProperty('PulseWeapon', '.*', propertyList['CloakDisruptor'])
	soyuz.lTorpTypes = [ ['FTBMk5PhotonTorpedo', 40] ]

	starbase375 = FedShip('starbase375')
	starbase375.stats['cost'] = 1500
	starbase375.stats['crew'] = 500
	starbase375.stats['hullIndex'] = 5500
	starbase375.stats['length'] = 5500
	starbase375.stats['width'] = 5500
	starbase375.stats['height'] = 5500
	starbase375.stats['immboile'] = 'TRUE'
	starbase375.stats['maneuverIndex'] = '0.1'
	starbase375.stats['maneuverThrustIndex'] = '0.1'
	starbase375.stats['mass'] = 12500000
	starbase375.stats['maxVelocity'] = 50
	starbase375.stats['rangeIndex'] = 1210
	starbase375.stats['sensorIndex'] = 1000
	starbase375.stats['shieldIndex'] = 5000
	starbase375.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	starbase375.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	starbase375.stats['terawatts'] = 200000

	stardestroyer = ImperialCapShip('stardestroyer')
	stardestroyer.stats['cost'] = 1500
	stardestroyer.stats['crew'] = 36810
	stardestroyer.stats['maneuverIndex'] = 100
	stardestroyer.stats['maneuverThrustIndex'] = 100
	stardestroyer.stats['mass'] = 20480000
	stardestroyer.stats['maxVelocity'] = 360
	stardestroyer.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	stardestroyer.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	stargalleon = ImperialCapShip('stargalleon')
	stargalleon.stats['cost'] = 800
	stargalleon.stats['crew'] = 1000
	stargalleon.stats['maneuverIndex'] = 300
	stargalleon.stats['maneuverThrustIndex'] = 300
	stargalleon.stats['mass'] = 135000
	stargalleon.stats['maxVelocity'] = 240
	stargalleon.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	stargalleon.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	starmobilebase = FedShip('starmobilebase')
	starmobilebase.stats['cost'] = 1500
	starmobilebase.stats['crew'] = 5500
	starmobilebase.stats['hullIndex'] = 5000
	starmobilebase.stats['length'] = 5000
	starmobilebase.stats['width'] = 5000
	starmobilebase.stats['height'] = 5000
	starmobilebase.stats['immobile'] = 'TRUE'
	starmobilebase.stats['maneuverIndex'] = 0
	starmobilebase.stats['maneuverThrustIndex'] = 0
	starmobilebase.stats['mass'] = 81600000
	starmobilebase.stats['maxVelocity'] = 50
	starmobilebase.stats['rangeIndex'] = 1100
	starmobilebase.stats['sensorIndex'] = 1000
	starmobilebase.stats['shieldIndex'] = 7000
	starmobilebase.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	starmobilebase.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	starmobilebase.stats['terawatts'] = 60000

	steamrunner = FedShip('steamrunner')
	steamrunner.stats['cost'] = 400
	steamrunner.stats['crew'] = 185
	steamrunner.stats['hullIndex'] = 680
	steamrunner.stats['length'] = 244
	steamrunner.stats['width'] = 160
	steamrunner.stats['height'] = 40
	steamrunner.stats['maneuverIndex'] = 1200
	steamrunner.stats['maneuverThrustIndex'] = 2000
	steamrunner.stats['mass'] = 1375000
	steamrunner.stats['maxVelocity'] = 625
	steamrunner.stats['rangeIndex'] = 965
	steamrunner.stats['sensorIndex'] = 750
	steamrunner.stats['shieldIndex'] = 500
	steamrunner.SetShields( {'front': 2, 'rear': 1, 'top': 2, 'bottom': 0.5, 'left': 0.75, 'right': 0.75 } )
	steamrunner.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1.5, 'bottom': 0.5, 'left': 1, 'right': 1 } )
	steamrunner.stats['terawatts'] = 13000
	steamrunner.SetProperty('Phaser', '.', propertyList['FedTypeVIII'])
	steamrunner.SetProperty('Phaser', 'Dorsal Phaser 2', propertyList['FedTypeIX'], { 'terawatts': 3.0 } )
	steamrunner.SetProperty('TorpedoTube', '.', propertyList['FedPFTorpedoTube'])
	steamrunner.powerPercent = ('red', 0.68)
	steamrunner.battery = 200
	steamrunner.bakBattery = 100
	steamrunner.lTorpTypes[0][1] = 100
	steamrunner.lTorpTypes[1][1] = 55
	steamrunner.lTorpTypes[3][1] = 6

	strikecruiser = ImperialCapShip('strikecruiser')
	strikecruiser.stats['cost'] = 760
	strikecruiser.stats['crew'] = 12000
	strikecruiser.stats['maneuverIndex'] = 180
	strikecruiser.stats['maneuverThrustIndex'] = 180
	strikecruiser.stats['mass'] = 455625
	strikecruiser.stats['maxVelocity'] = 360
	strikecruiser.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	strikecruiser.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	superxtransport = ImperialCapShip('superxtransport')
	superxtransport.stats['cost'] = 950
	superxtransport.stats['crew'] = 800
	superxtransport.stats['maneuverIndex'] = 500
	superxtransport.stats['maneuverThrustIndex'] = 500
	superxtransport.stats['mass'] = 340000
	superxtransport.stats['maxVelocity'] = 4338
	superxtransport.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	superxtransport.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	systempatrol = ImperialCapShip('systempatrol')
	systempatrol.stats['cost'] = 300
	systempatrol.stats['crew'] = 1
	systempatrol.stats['maneuverIndex'] = 200
	systempatrol.stats['maneuverThrustIndex'] = 200
	systempatrol.stats['mass'] = 86400
	systempatrol.stats['maxVelocity'] = 480
	systempatrol.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	systempatrol.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	teraknor = CardassianShip('teraknor')
	teraknor.stats['cost'] = 1500
	teraknor.stats['crew'] = 500
	teraknor.stats['hullIndex'] = 10
	teraknor.stats['length'] = 1451.82
	teraknor.stats['width'] = 368.8
	teraknor.stats['height'] = 969.26
	teraknor.stats['immobile'] = 'TRUE'
	teraknor.stats['maneuverIndex'] = 1
	teraknor.stats['maneuverThrustIndex'] = 1
	teraknor.stats['mass'] = 4500000
	teraknor.stats['maxVelocity'] = 50
	teraknor.stats['rangeIndex'] = 1210
	teraknor.stats['sensorIndex'] = 1000
	teraknor.stats['shieldIndex'] = 4000
	teraknor.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	teraknor.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	teraknor.stats['terawatts'] = 70000

	tieadvanced = ImperialShip('tieadvanced')
	tieadvanced.stats['cost'] = 60
	tieadvanced.stats['crew'] = 1
	tieadvanced.stats['maneuverIndex'] = 50000
	tieadvanced.stats['maneuverThrustIndex'] = 50000
	tieadvanced.stats['mass'] = 20
	tieadvanced.stats['maxVelocity'] = 1080
	tieadvanced.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tieadvanced.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	tiebomber = ImperialShip('tiebomber')
	tiebomber.stats['cost'] = 30
	tiebomber.stats['crew'] = 1
	tiebomber.stats['maneuverIndex'] = 5000
	tiebomber.stats['maneuverThrustIndex'] = 5000
	tiebomber.stats['mass'] = 30
	tiebomber.stats['maxVelocity'] = 480
	tiebomber.stats['shieldIndex'] = 0
	tiebomber.stats['hullIndex'] = 50
	tiebomber.stats['length'] = 50
	tiebomber.stats['width'] = 50
	tiebomber.stats['height'] = 50
	tiebomber.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tiebomber.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tiebomber.stats['terawatts'] = 500

	tiedefender = ImperialShip('tiedefender')
	tiedefender.stats['cost'] = 80
	tiedefender.stats['crew'] = 1
	tiedefender.stats['maneuverIndex'] = 15000
	tiedefender.stats['maneuverThrustIndex'] = 15000
	tiedefender.stats['mass'] = 15
	tiedefender.stats['maxVelocity'] = 975
	tiedefender.stats['shieldIndex'] = 225
	tiedefender.stats['hullIndex'] = 250
	tiedefender.stats['length'] = 250
	tiedefender.stats['width'] = 250
	tiedefender.stats['height'] = 250
	tiedefender.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tiedefender.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tiedefender.stats['terawatts'] = 2000

	tieexperimental = ImperialShip('tieexperimental')
	tieexperimental.stats['cost'] = 35
	tieexperimental.stats['crew'] = 1
	tieexperimental.stats['maneuverIndex'] = 10000
	tieexperimental.stats['maneuverThrustIndex'] = 10000
	tieexperimental.stats['mass'] = 15
	tieexperimental.stats['maxVelocity'] = 666
	tieexperimental.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tieexperimental.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	tiefighter = ImperialShip('tiefighter')
	tiefighter.stats['cost'] = 15
	tiefighter.stats['crew'] = 1
	tiefighter.stats['maneuverIndex'] = 20000
	tiefighter.stats['maneuverThrustIndex'] = 20000
	tiefighter.stats['mass'] = 15
	tiefighter.stats['maxVelocity'] = 600
	tiefighter.stats['shieldIndex'] = 0
	tiefighter.stats['hullIndex'] = 10
	tiefighter.stats['length'] = 10
	tiefighter.stats['width'] = 10
	tiefighter.stats['height'] = 10
	tiefighter.stats['terawatts'] = 500
	tiefighter.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tiefighter.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	tieinterceptor = ImperialShip('tieinterceptor')
	tieinterceptor.stats['cost'] = 25
	tieinterceptor.stats['crew'] = 1
	tieinterceptor.stats['maneuverIndex'] = 30000
	tieinterceptor.stats['maneuverThrustIndex'] = 30000
	tieinterceptor.stats['mass'] = 18
	tieinterceptor.stats['maxVelocity'] = 666
	tieinterceptor.stats['shieldIndex'] = 0
	tieinterceptor.stats['hullIndex'] = 15
	tieinterceptor.stats['length'] = 15
	tieinterceptor.stats['width'] = 15
	tieinterceptor.stats['height'] = 15
	tieinterceptor.stats['terawatts'] = 1000
	tieinterceptor.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	tieinterceptor.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	trammion = CardassianShip('trammion')
	trammion.stats['cost'] = 700
	trammion.stats['crew'] = 300
	trammion.stats['hullIndex'] = 700
	trammion.stats['length'] = 700
	trammion.stats['width'] = 700
	trammion.stats['height'] = 700
	trammion.stats['maneuverIndex'] = 400
	trammion.stats['maneuverThrustIndex'] = 400
	trammion.stats['mass'] = 4800000
	trammion.stats['maxVelocity'] = 400
	trammion.stats['rangeIndex'] = 600
	trammion.stats['sensorIndex'] = 1000
	trammion.stats['shieldIndex'] = 955
	trammion.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	trammion.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	trammion.stats['terawatts'] = 40000

	type9 = SmallFedShip('type9')
	type9.stats['cost'] = 54
	type9.stats['crew'] = 1
	type9.stats['hullIndex'] = 12
	type9.stats['length'] = 9.17
	type9.stats['width'] = 3.8
	type9.stats['height'] = 2.95
	type9.stats['maneuverIndex'] = 10000
	type9.stats['maneuverThrustIndex'] = 10000
	type9.stats['mass'] = 27
	type9.stats['maxVelocity'] = 850
	type9.stats['rangeIndex'] = 20
	type9.stats['sensorIndex'] = 300
	type9.stats['shieldIndex'] = 10
	type9.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	type9.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	type9.SetProperty('Phaser', '.*', propertyList['FedTypeVII'])
	type9.stats['terawatts'] = 1000
	type9.powerPercent = ('red', 0.4)
	type9.battery = 30
	type9.bakBattery = 15
	type9.lTorpTypes[0][1] = 0
	shipList.Register(type9, 'shuttle')

	v38 = ImperialShip('v38')
	v38.stats['cost'] = 50
	v38.stats['crew'] = 1
	v38.stats['maneuverIndex'] = 12000
	v38.stats['maneuverThrustIndex'] = 12000
	v38.stats['mass'] = 20
	v38.stats['maxVelocity'] = 600
	v38.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	v38.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	valdore = RomulanShip('valdore')
	valdore.stats['cost'] = 1930
	valdore.stats['crew'] = 850
	valdore.stats['hullIndex'] = 700
	valdore.stats['length'] = 603.5
	valdore.stats['width'] = 911.4
	valdore.stats['height'] = 94
	valdore.stats['maneuverIndex'] = 2000
	valdore.stats['maneuverThrustIndex'] = 3000
	valdore.stats['mass'] = 1320000
	valdore.stats['maxVelocity'] = 600 / 0.8476
	valdore.stats['rangeIndex'] = 1660
	valdore.stats['sensorIndex'] = 800
	valdore.stats['shieldIndex'] = 1200
	valdore.SetShields( {'front': 1.5, 'rear': 1, 'top': 1.5, 'bottom': 1.5, 'left': 1, 'right': 1 } )
	valdore.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	valdore.stats['terawatts'] = 30000
	valdore.SetProperty('TorpedoTube', '.', propertyList['RomTorpedoTube'])
	valdore.SetProperty('PulseWeapon', '.', propertyList['RomHeavyPulseDisruptor'])
	valdore.SetProperty('PulseWeapon', '^Star Cannon [1-2]', propertyList['RomMedPulseDisruptor'])
	valdore.SetProperty('PulseWeapon', '^Port Cannon [1-2]', propertyList['RomMedPulseDisruptor'])
	valdore.powerPercent = ('red', 0.45)
	valdore.lTorpTypes[0][1] = 40
	valdore.lTorpTypes[1][1] = 0
	valdore.battery = 400
	valdore.bakBattery = 180

	victorystardestroyer = ImperialCapShip('victorystardestroyer')
	victorystardestroyer.stats['cost'] = 915
	victorystardestroyer.stats['crew'] = 12000
	victorystardestroyer.stats['maneuverIndex'] = 150
	victorystardestroyer.stats['maneuverThrustIndex'] = 150
	victorystardestroyer.stats['mass'] = 3645000
	victorystardestroyer.stats['maxVelocity'] = 360
	victorystardestroyer.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	victorystardestroyer.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )

	virulent = DominionShip('virulent')
	virulent.stats['cost'] = 245
	virulent.stats['crew'] = 25
	virulent.stats['hullIndex'] = 300
	virulent.stats['length'] = 68.32 * 2.0
	virulent.stats['width'] = 70.02 * 1.8
	virulent.stats['height'] = 18.32 * 2.5
	virulent.stats['maneuverIndex'] = 9000
	virulent.stats['maneuverThrustIndex'] = 9000
	virulent.stats['mass'] = 85000
	virulent.stats['maxVelocity'] = 750
	virulent.stats['rangeIndex'] = 400
	virulent.stats['sensorIndex'] = 1000
	virulent.stats['shieldIndex'] = 170
	virulent.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	virulent.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	virulent.SetProperty('PulseWeapon', '.*', propertyList['DomMineLauncher'])
	virulent.stats['terawatts'] = 4000
	virulent.lTorpTypes = [ ['FTBDomMine', 8 ] ]

	vorcha = KlingonShip('vorcha')
	vorcha.stats['cost'] = 890
	vorcha.stats['crew'] = 780
	vorcha.stats['hullIndex'] = 1800
	vorcha.stats['length'] = 481.32
	vorcha.stats['width'] = 341.76
	vorcha.stats['height'] = 106.87
	vorcha.stats['maneuverIndex'] = 2590 / 2.75
	vorcha.stats['maneuverThrustIndex'] = 2590
	vorcha.stats['mass'] = 4900000
	vorcha.stats['maxVelocity'] = 500
	vorcha.stats['rangeIndex'] = 750
	vorcha.stats['sensorIndex'] = 1000
	vorcha.stats['shieldIndex'] = 775
	vorcha.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	vorcha.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	vorcha.stats['terawatts'] = 57500
	vorcha.SetProperty('Phaser', 'Disruptor', propertyList['Blank'], { 'terawatts': 0.0 } )
	vorcha.SetProperty('PulseWeapon', '.', propertyList['KliMk12PulseDisruptor'], { 'terawatts': 0.5 } )
	vorcha.SetProperty('PulseWeapon', '^Plasma', propertyList['KliFastPlasma'])
	vorcha.SetProperty('PulseWeapon', '^Star Cannon', propertyList['KliMk12PulseDisruptor'])
	vorcha.SetProperty('PulseWeapon', '^Port Cannon', propertyList['KliMk12PulseDisruptor'])
	vorcha.SetProperty('TorpedoTube', '.*', propertyList['KliTorpedoTube'])
	vorcha.SetProperty('WeaponSystem', '.*Beams$', propertyList['MultiFirePhaserSystem'])
	vorcha.SetProperty('WeaponSystem', '.*Cannon.*', propertyList['MultiFirePhaserSystem'])
	vorcha.lTorpTypes = [ ['FTBFastKlingonTorpedo', 150], ['FTBKlingonTripleTorpedo', 50] ]
	vorcha.battery = 300
	vorcha.bakBattery = 80

	wells = FedShip('wells')
	wells.stats['cost'] = 230
	wells.stats['crew'] = 280
	wells.stats['hullIndex'] = 4000
	wells.stats['length'] = 4000
	wells.stats['width'] = 4000
	wells.stats['height'] = 4000
	wells.stats['maneuverIndex'] = 6000
	wells.stats['maneuverThrustIndex'] = 6000
	wells.stats['mass'] = 230000
	wells.stats['maxVelocity'] = 950
	wells.stats['rangeIndex'] = 255
	wells.stats['sensorIndex'] = 1000
	wells.stats['shieldIndex'] = 24000
	wells.SetShields( {'front': 2, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	wells.SetShieldCharge( {'front': 1, 'rear': 1, 'top': 1, 'bottom': 1, 'left': 1, 'right': 1 } )
	wells.stats['terawatts'] = 800000
