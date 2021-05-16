## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *




## Load function
def LoadUniverse():

	##################################
	#Create a new race
	##################################
	pRace=Race()

	### Name
	pRace.SetName("Coalition")

	### Vesselclasses, fully customizable
	pRace.SetVesselType('NubianCruiser',	'DN',	'CS $$',	'Galaxy',	20000.0,	TRUE,	FALSE	)
	pRace.SetVesselType('NubianBattleship',	'DN',	'CS $$',	'Galaxy',	35000.0,	TRUE,	FALSE	)
	pRace.SetVesselType('CSD',		'BB',	'CSD $$',	'Galaxy',	350000.0,	FALSE,	FALSE	)
	#pRace.SetVesselType('CSB',		'BB',	'CSB $$',	'Galaxy',	500000.0,	FALSE,	FALSE	)
	#pRace.SetVesselType('CSS',		'BB',	'CSS $$',	'Galaxy',	15000000.0,	FALSE,	FALSE	)
	#pRace.SetVesselType('CSG',		'XL',	'CSG $$',	'Galaxy',	200000000.0,	FALSE,	FALSE	)	

	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('STD_SYS_ASS',		'BB@3'	)
	pRace.AddFleetTemplate('STD_SYS_DEF',		'DN@3'	)
	pRace.AddFleetTemplate('STD_OUT_DEF',		'DN@4'	)
	pRace.AddFleetTemplate('STD_SB_DEF',		'DN@6'	)
	pRace.AddFleetTemplate('STD_SB+_DEF',		'DN@8'	)
	
	### Colour
	pRace.SetColour(0.05,0.5,1.0,0.8)

	## Music
	pRace.SetEnterMusic('CoalitionAnthem')

	## Subsections
	import LoadSolars
	LoadSolars.LoadUniverse()

	import LoadBases
	LoadBases.LoadUniverse()

	

def PostLoadUniverse():

	## Create now the fleets
	import LoadFleets
	LoadFleets.LoadUniverse()