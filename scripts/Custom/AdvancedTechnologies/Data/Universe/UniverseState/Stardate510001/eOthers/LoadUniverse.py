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
	pRace.SetName("Tzenkethi Coalition")

	### Vesselclasses, fully customizable
	pRace.SetVesselType('Shuttle',			'SH',	'Shuttle',	'Marauder',	50.0,		TRUE,	FALSE	)
	pRace.SetVesselType('ATP_Freighter',		'FR',	'Freighter $$',	'Marauder',	250.0,		FALSE,	FALSE	)
	#pRace.SetVesselType('TalarianWarship',		'CC',	'Cruiser $$',	'Warbird',	2500.0,		FALSE,	FALSE	)
	pRace.SetVesselType('Marauder',			'CC',	'Cruiser $$',	'Warbird',	2500.0,		FALSE,	FALSE	)
	pRace.SetVesselType('ATP_Shipyard',		'SY',	'$$ Dock',	'FedBase',	25000.0,	FALSE,	TRUE	)
	pRace.SetVesselType('FedOutpost',		'OP',	'$$ Station',	'FedBase',	75000.0,	FALSE,	TRUE	)

	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('STD_SYS_DEF',		'CC@6'				)
	pRace.AddFleetTemplate('HOME_SYS_DEF',		'CC@10'				)
	pRace.AddFleetTemplate('BASE_SYS_DEF',		'OP@1','OP@1;SY@1','OP@1;SY@2'	)
	pRace.AddFleetTemplate('HEAVY_COMMERCE_LINE',	'FR@6;CC@2'			)
	pRace.AddFleetTemplate('MEDIUM_COMMERCE_LINE',	'FR@4;CC@1'			)
	pRace.AddFleetTemplate('SMALL_COMMERCE_LINE',	'FR@2'				)

	### Colour
	pRace.SetColour(200.0/255.0,204.0/255.0,117.0/255.0,1.0)

	## Characters
	### Heads
	MAH = ('Human1','Human2','Human3','Human5','Human13','Human14','Human15','Human19','Human20','Human21','Human22','Romulan3','Romulan4','Romulan2')
	MPH = ('Human4', 'Human16','Human17','Human18','Human23' )
	FAH = ('Human6','Human7','Human10')
	FPH = ('Human11','Human12','Human8','Human9','Human24')
	
	### Bodies
	#### Male
	SAM = ('Male',)
	SOM = ('Male',)
	SSM = ('Male',)
	STM = ('Male',)
	M   = ('Male',)

	#### Female
	SAF = ('Female',)
	SOF = ('Female',)
	SSF = ('Female',)
	STF = ('Female',)
	F   = ('Female',)

	### Defs Male
	pRace.SetCharacters( 'Admiral',		'Admiral $$',		'M',	MAH,		SAM )
	pRace.SetCharacters( 'Captain',		'Captain $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Science',		'Lieutenant $$',	'M',	MAH+MPH,	SSM )
	pRace.SetCharacters( 'Helm',		'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Tactical',	'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Engineer',	'Lt. Commander $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Guest',		'$$',			'M',	MAH+MPH,	SAM+SOM+STM+SSM+M+F )
	pRace.SetCharacters( 'Extra',		'Ensign $$',		'M',	MAH+MPH,	SOM+STM+SSM )
	pRace.SetCharacters( 'Civilian',	'Mister $$',		'M',	MAH+MPH,	M )

	### Defs Female
	pRace.SetCharacters( 'Admiral',		'Admiral $$',		'F',	FAH,		SAF )
	pRace.SetCharacters( 'Captain',		'Captain $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Science',		'Lieutenant $$',	'F',	FAH+FPH,	SSF )
	pRace.SetCharacters( 'Helm',		'Lieutenant $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Tactical',	'Lieutenant $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Engineer',	'Lt. Commander $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Guest',		'$$',			'F',	FAH+FPH,	SAF+SOF+STF+SSF+F+F )
	pRace.SetCharacters( 'Extra',		'Ensign $$',		'F',	FAH+FPH,	SOF+STF+SSF )
	pRace.SetCharacters( 'Civilian',	'Miss $$',		'F',	FAH+FPH,	F )



	##################################
	#Create a new race
	##################################
	pRace=Race()

	### Name
	pRace.SetName("Nonaligned")

	### Vesselclasses, fully customizable
	pRace.SetVesselType('Shuttle',			'SH',	'Shuttle',	'Marauder',	50.0,		FALSE,	FALSE	)
	pRace.SetVesselType('ATP_Freighter',		'FR',	'Freighter $$',	'Marauder',	250.0,		FALSE,	FALSE	)
	pRace.SetVesselType('TalarianWarship',		'CC',	'Cruiser $$',	'Marauder',	2500.0,		FALSE,	FALSE	)
	
	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('STD_SYS_DEF',		'CC@6'	)
	pRace.AddFleetTemplate('HEAVY_COMMERCE_LINE',	'FR@6;CC@2'		)
	pRace.AddFleetTemplate('MEDIUM_COMMERCE_LINE',	'FR@4;CC@1'		)
	pRace.AddFleetTemplate('SMALL_COMMERCE_LINE',	'FR@2'			)
	
	### Colour
	pRace.SetColour(240.0/255,199/255.0,121.0/255.0,1.0)

	## Characters
	### Heads
	MAH = ('Human1','Human2','Human3','Human5','Human13','Human14','Human15','Human19','Human20','Human21','Human22','Romulan3','Romulan4','Romulan2')
	MPH = ('Human4', 'Human16','Human17','Human18','Human23' )
	FAH = ('Human6','Human7','Human10')
	FPH = ('Human11','Human12','Human8','Human9','Human24')
	
	### Bodies
	#### Male
	SAM = ('Male',)
	SOM = ('Male',)
	SSM = ('Male',)
	STM = ('Male',)
	M   = ('Male',)

	#### Female
	SAF = ('Female',)
	SOF = ('Female',)
	SSF = ('Female',)
	STF = ('Female',)
	F   = ('Female',)

	### Defs Male
	pRace.SetCharacters( 'Admiral',		'Admiral $$',		'M',	MAH,		SAM )
	pRace.SetCharacters( 'Captain',		'Captain $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Science',		'Lieutenant $$',	'M',	MAH+MPH,	SSM )
	pRace.SetCharacters( 'Helm',		'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Tactical',	'Lieutenant $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Engineer',	'Lt. Commander $$',	'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Guest',		'$$',			'M',	MAH+MPH,	SAM+SOM+STM+SSM+M+F )
	pRace.SetCharacters( 'Extra',		'Ensign $$',		'M',	MAH+MPH,	SOM+STM+SSM )
	pRace.SetCharacters( 'Civilian',	'Mister $$',		'M',	MAH+MPH,	M )

	### Defs Female
	pRace.SetCharacters( 'Admiral',		'Admiral $$',		'F',	FAH,		SAF )
	pRace.SetCharacters( 'Captain',		'Captain $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Science',		'Lieutenant $$',	'F',	FAH+FPH,	SSF )
	pRace.SetCharacters( 'Helm',		'Lieutenant $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Tactical',	'Lieutenant $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Engineer',	'Lt. Commander $$',	'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Guest',		'$$',			'F',	FAH+FPH,	SAF+SOF+STF+SSF+F+F )
	pRace.SetCharacters( 'Extra',		'Ensign $$',		'F',	FAH+FPH,	SOF+STF+SSF )
	pRace.SetCharacters( 'Civilian',	'Miss $$',		'F',	FAH+FPH,	F )

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