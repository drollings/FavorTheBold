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
	pRace.SetName('Ferengi Alliance')

	## Vessels
	pRace.SetVesselType('Marauder',		'CC',	'FAS $$', 	'Marauder',	1500.0,	FALSE,	FALSE	)
	pRace.SetVesselType('ATP_Freighter',	'FR',	'FAS $$',	'Marauder',	250.0,	FALSE,	FALSE	)	

	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('HEAVY_COMMERCE_LINE'	,'FR@6;CC@2'		)
	pRace.AddFleetTemplate('MEDIUM_COMMERCE_LINE'	,'FR@4;CC@1'		)
	pRace.AddFleetTemplate('SMALL_COMMERCE_LINE'	,'FR@2'			)

	### Colour
	pRace.SetColour(115.0/255.0,158.0/255.0,125.0/255.0,1.0)
	
	## Characters
	### Heads
	MAH = ('Ferengi',)
	MPH = ( )
	
	### Bodies
	#### Male
	SM = ('Ferengi',)
	M  = ('Ferengi','Male')

	### Defs Male
	pRace.SetCharacters( 'Admiral',		'Nagus $$',	'M',	MAH,		SM )
	pRace.SetCharacters( 'Captain',		'$$',		'M',	MAH,		SM )
	pRace.SetCharacters( 'Commander',	'$$',		'M',	MAH,		SM )
	pRace.SetCharacters( 'Science',		'$$',		'M',	MAH+MPH,	SM )
	pRace.SetCharacters( 'Helm',		'$$',		'M',	MAH+MPH,	SM )
	pRace.SetCharacters( 'Tactical',	'$$',		'M',	MAH+MPH,	SM )
	pRace.SetCharacters( 'Engineer',	'$$',		'M',	MAH+MPH,	SM )
	pRace.SetCharacters( 'Guest',		'$$',		'M',	MAH+MPH,	SM+M )
	pRace.SetCharacters( 'Extra',		'$$',		'M',	MAH+MPH,	SM )
	pRace.SetCharacters( 'Civilian',	'$$',		'M',	MAH+MPH,	M )
	
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