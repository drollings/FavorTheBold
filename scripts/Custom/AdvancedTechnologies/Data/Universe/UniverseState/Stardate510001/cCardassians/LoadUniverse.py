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
	pRace.SetName("Cardassian Union")

	### Vesselclasses, fully customizable
	pRace.SetVesselType('FTB_Galor',	'CC',	'CS $$',	'Galaxy', 7500.0,	FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Dominator',	'CC',	'CS $$',	'Galaxy', 10000.0,	FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Keldon',	'DN',	'CS $$',	'Galaxy', 10000.0,	FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Devastator',	'DN',	'CS $$',	'Galaxy', 10000.0,	FALSE,	FALSE	)
	
	
	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('STD_SYS_ASS',		'DN@4;CC@10'	)
	pRace.AddFleetTemplate('STD_SYS_DEF',		'DN@2;CC@3'	)
	pRace.AddFleetTemplate('STD_OUT_DEF',		'DN@2;CC@5'	)
	pRace.AddFleetTemplate('STD_SB_DEF',		'DN@4;CC@6'	)
	pRace.AddFleetTemplate('STD_SB+_DEF',		'DN@5;CC@8'	)

	## Characters
	### Heads
	MAH = ('Cardassian1','Cardassian3','Cardassian4','Cardassian5')
	MPH = ('Cardassian2', )
	
	### Bodies
	#### Male
	SAM = ('StarfleetAdmiralMale',)
	SOM = ('StarfleetOfficerMale',)
	SSM = ('StarfleetScienceMale',)
	STM = ('StarfleetTacticalMale',)
	M   = ('Male',)	

	### Defs Male
	pRace.SetCharacters( 'Admiral',		'Admiral $$',		'M',	MAH,		SAM )
	pRace.SetCharacters( 'Captain',		'Captain $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Science',		'Lieutenant $$',	'M',	MAH+MPH,	SSM )
	pRace.SetCharacters( 'Helm',		'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Tactical',	'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Engineer',	'Lt. Commander $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Guest',		'$$',			'M',	MAH+MPH,	SAM+SOM+STM+SSM+M )
	pRace.SetCharacters( 'Extra',		'Ensign $$',		'M',	MAH+MPH,	SOM+STM+SSM )
	pRace.SetCharacters( 'Civilian',	'Mister $$',		'M',	MAH+MPH,	M )
	
	### Colour
	pRace.SetColour(1.0,0.5,0.5,1.0)

	## Subsections
	import LoadSolars
	LoadSolars.LoadUniverse()

	import LoadBases
	LoadBases.LoadUniverse()

	

def PostLoadUniverse():

	## Create now the fleets
	import LoadFleets
	LoadFleets.LoadUniverse()

	## Diplomacy
	# ...	