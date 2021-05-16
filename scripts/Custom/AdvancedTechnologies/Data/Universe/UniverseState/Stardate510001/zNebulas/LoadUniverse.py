## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Wormholes import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_StarCharts import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *


## Load function
def LoadUniverse():
	
	## New race
	pRace = GetArchitect()

	pNebula = Nebula()
	pNebula.Bind(	'Briar Patch',
			Vector(0.9,-2.7,-0.1),
			0.32,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula001.tga',
			GalaxyIcon.SYSTEM_NEBULA_1,
			'Yellow'						)
	
	pNebula = Nebula()
	pNebula.Bind(	'Betreka Nebula',
			Vector(-0.25,-3.15,+0.2),
			0.15,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula007.tga',
			GalaxyIcon.SYSTEM_NEBULA_7,
			'Saphire'						)

	pNebula = Nebula()
	pNebula.Bind(	'Arachnid Nebula',
			Vector(-0.5,-1.8,+0.1),
			0.15,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula011.tga',
			GalaxyIcon.SYSTEM_NEBULA_2,
			'Green'						)

	pNebula = Nebula()
	pNebula.Bind(	'Tendaras Cluster',
			Vector(-0.75,-2.6,-0.15),
			0.075,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula003.tga',
			GalaxyIcon.SYSTEM_NEBULA_3,
			'Blue'						)

	pNebula = Nebula()
	pNebula.Bind(	'Argolis Cluster',
			Vector(-1.0,-2.15,+0.2),
			0.20,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula010.tga',
			GalaxyIcon.SYSTEM_NEBULA_4						)

	pNebula = Nebula()
	pNebula.Bind(	'Typhon Expanse',
			Vector(1.9,3.9,+0.2),
			0.6,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula004.tga',
			GalaxyIcon.SYSTEM_NEBULA_4,
			'Green'						)

	pNebula = Nebula()
	pNebula.Bind(	'Bassen Rift',
			Vector(0.8,1.05,+0.25),
			0.175,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula009.tga',
			GalaxyIcon.SYSTEM_NEBULA_9,
			'Yellow'								)

	pNebula = Nebula()
	pNebula.Bind(	'Mutara Nebula',
			Vector(-15.0,13.0,+0.25),
			1.5,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula008.tga',
			GalaxyIcon.SYSTEM_NEBULA_8,
			'Red'						)

	pNebula = Nebula()
	pNebula.Bind(	'Mc Allister C-5 Nebula',
			Vector(-1.8,-2.5,+0.25),
			0.2,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula006.tga',
			GalaxyIcon.SYSTEM_NEBULA_6,
			'Saphire'						)

	pNebula = Nebula()
	pNebula.Bind(	'Rolor Nebula',
			Vector(-3.72,-0.68,+0.125),
			0.225,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula013.tga',
			GalaxyIcon.SYSTEM_NEBULA_13,
			'Blue'						)

	pNebula = Nebula()
	pNebula.Bind(	'Amleth Nebula',
			Vector(-2.98,-2.12,+0.125),
			0.1,
			'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula014.tga',
			GalaxyIcon.SYSTEM_NEBULA_14,
			'Red'						)

	pBlackhole = BlackholeSystem()
	pBlackhole.Bind(pRace,'Cypheus Blackhole')
	pBlackhole.SetLocXYZ(1.5,4.8,0.0)
	AddSolarSystem(pBlackhole)
	
	

def PostLoadUniverse():
	## imports
	from Custom.AdvancedTechnologies.Data.Universe import ATP_Blackholes

	## Create somes wormholes
	pUniverse = GetUniverse()

	## Bajoran wormhole
	pWormhole = Wormhole()
	pSource1 = pUniverse.GetChildByName('Idran').GetChildByName('Idran')
	pSource2 = pUniverse.GetChildByName('Bajor').GetChildByName('Bajor')	
	pWormhole.Bind('Bajoran wormhole',pSource1,pSource2)
	##

	## Gemeni womrhole
	##

	## Create some blackholes	
	# pBlackhole = ATP_Blackholes.Blackhole()
	# pBlackhole.Bind( 'Gargantua Blackhole' , pUniverse.GetChildByName('Sol').GetChildByName('Moon') )


