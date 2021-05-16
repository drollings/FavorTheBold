## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

sPath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/UniverseState/Stardate510001/aFederation/'


## Load function
def LoadUniverse():

	##################################
	#Create a new race
	##################################
	pRace=Race()

	### Name
	pRace.SetName('United Federation of Planets')

	### Vesselclasses, fully customizable
	pRace.SetVesselType('Shuttle',		'SH',	'Shuttle',	'Marauder',	50.0,		FALSE,	FALSE	)
	pRace.SetVesselType('ATP_Freighter',	'FR',	'Freighter $$',	'Marauder',	250.0,		FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Intrepid',	'EX',	'USS $$',	'Galaxy',	5800.0,		FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Nova',		'EX',	'USS $$',	'Galaxy',	2500.0,		TRUE,	FALSE	)
	pRace.SetVesselType('FTB_Norway',	'FF',	'USS $$',	'Galaxy',	1500.0,		FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Steamrunner',	'CL',	'USS $$',	'Galaxy',	3500.0,		FALSE,	FALSE	)
	pRace.SetVesselType('FTB_Akira',	'CC',	'USS $$',	'Galaxy',	5500.0,		FALSE,	FALSE	)	
	pRace.SetVesselType('FTB_Nebula',	'CC',	'USS $$',	'Galaxy',	7500.0,		TRUE ,	FALSE	)
	pRace.SetVesselType('FTB_Ambassador',	'DN',	'USS $$',	'Galaxy',	15000.0,	TRUE ,	FALSE	)
	pRace.SetVesselType('FTB_Galaxy',	'DN',	'USS $$',	'Galaxy',	15000.0,	TRUE ,	FALSE	)
	pRace.SetVesselType('FTB_Sovereign',	'DN',	'USS $$',	'Sovereign',	21000.0,	FALSE,	FALSE	)	
	pRace.SetVesselType('ATP_FedStarbase',	'SB',	'$$ Station',	'Conference',	250000.0,	FALSE,	TRUE	)
	pRace.SetVesselType('FedOutpost',	'OP',	'$$ Outpost',	'FedBase',	40000.0,	FALSE,	TRUE	)
	pRace.SetVesselType('CardStarbase',	'OP',	'$$ Outpost',	'FedBase',	45000.0,	TRUE,	TRUE	)
	pRace.SetVesselType('ATP_Shipyard',	'SY',	'$$ Shipyard',	'FedBase',	18000.0,	FALSE,	TRUE	)

	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('BASE_SYS_DEF',		'OP@1' , 'OP@1;SY@1' , 'OP@1;SY@2'	)
	pRace.AddFleetTemplate('STD_SYS_DEF',		'DN@1;CC@1;CL@1;FF@1'			)
	pRace.AddFleetTemplate('STD_OUT_DEF',		'CC@1;CL@1;FF@1;EX@1'			)
	pRace.AddFleetTemplate('STD_SB_DEF',		'DN@2;CC@2;CL@2'			)
	pRace.AddFleetTemplate('STD_SB+_DEF',		'DN@3;CC@3;CL@3'			)	
	pRace.AddFleetTemplate('ROM_NZ_SYS_DEF',	'CL@1;FF@1'				)
	pRace.AddFleetTemplate('ROM_NZ_OUT_DEF',	'CL@1;FF@1;EX@1'			)
	pRace.AddFleetTemplate('ROM_NZ_SB_DEF',		'DN@1;CC@1;CL@2'			)
	pRace.AddFleetTemplate('ROM_NZ_SB+_DEF',	'DN@1;CC@2;CL@2'			)
	pRace.AddFleetTemplate('KL_NZ_SYS_DEF',		'DN@2;CC@2;CL@3;FF@3'			)
	pRace.AddFleetTemplate('KL_NZ_OUT_DEF',		'CC@3;CL@3;FF@3;EX@1'			)
	pRace.AddFleetTemplate('KL_NZ_SB_DEF',		'DN@4;CC@4;CL@4'			)
	pRace.AddFleetTemplate('KL_NZ_SB+_DEF',		'DN@5;CC@5;CL@5'			)
	pRace.AddFleetTemplate('CARD_BD_SYS_DEF',	'DN@2;CC@2;CL@2;FF@2'			)
	pRace.AddFleetTemplate('CARD_BD_OUT_DEF',	'DN@2;CC@3;CL@3;FF@2'			)
	pRace.AddFleetTemplate('CARD_BD_SB_DEF',	'DN@5;CC@5;CL@5'			)
	pRace.AddFleetTemplate('CARD_BD_SB+_DEF',	'DN@6;CC@6;CL@6'			)

	## Characters
	### Heads
	MAH = ('Andorian','Boolean','Human1','Human2','Human3','Human5','Human13','Human14','Human15','Human19','Human20','Human21','Human22','Romulan3','Romulan4','Romulan2')
	MPH = ('Human4', 'Human16','Human17','Human18','Human23' )
	FAH = ('Human6','Human7','Human10','Romulan1','Tpol')
	FPH = ('Human11','Human12','Human8','Human9','Human24','Romulan5')
	
	### Bodies
	#### Male
	SAM = ('StarfleetAdmiralMale',)
	SOM = ('StarfleetOfficerMale',)
	SSM = ('StarfleetScienceMale',)
	STM = ('StarfleetTacticalMale',)
	M   = ('Male',)

	#### Female
	SAF = ('StarfleetAdmiralFemale',)
	SOF = ('StarfleetOfficerFemale',)
	SSF = ('StarfleetScienceFemale',)
	STF = ('StarfleetTacticalFemale',)
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

	## Characternames
	pRace.SetCharacternameFile(sPath + 'Characternames.dat')

	## Shipnames
	pRace.SetShipnameFile(sPath + 'Shipnames.dat')

	### Colour
	pRace.SetColour(0.05,0.5,1.0,0.8)

	## Subsections
	import LoadSol
	LoadSol.LoadUniverse()

	import LoadSolars
	LoadSolars.LoadUniverse()

	import LoadBases
	LoadBases.LoadUniverse()

	

def PostLoadUniverse():

	## Create now the fleets
	import LoadFleets
	LoadFleets.LoadUniverse()	