## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

sPath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/UniverseState/Stardate510001/bRomulans/'


## Load function
def LoadUniverse():

	##################################
	#Create a new race
	##################################
	pRace=Race()

	### Name
	pRace.SetName('Romulan Star Empire')

	### Vesselclasses, fully customizable
	pRace.SetVesselType('FTB_Dderidex',	'DN',	'RIS $$',	'Warbird',	10000.0,	TRUE,	FALSE	)
	pRace.SetVesselType('FTB_Valdore',	'DN',	'RIS $$',	'Warbird',	12500.0,	FALSE,	FALSE	)
	pRace.SetVesselType('FedOutpost',	'OUT',	'RIS $$',	'Warbird',	22500.0,	FALSE,	TRUE	)
	pRace.SetVesselType('ATP_FedStarbase',	'SB',	'Station $$',	'Warbird',	200000.0,	FALSE,	TRUE	)
	pRace.SetVesselType('ATP_Shipyard',	'SY',	'$$ Facility',	'Warbird',	30000.0,	FALSE,	TRUE	)
	
	## Fleetcomposition, fully customizable
	pRace.AddFleetTemplate('MIN_SYS_DEF',		'DN@1','DN@2'				)
	pRace.AddFleetTemplate('STD_SYS_DEF',		'DN@3','DN@4','DN@5'			)
	pRace.AddFleetTemplate('HOME_SYS_DEF',		'DN@10'					)
	pRace.AddFleetTemplate('BASE_SYS_DEF',		'OUT@1','OUT@1;SY@1' ,'OUT@1;SY@2'	)
	pRace.AddFleetTemplate('HOMEBASE_SYS_DEF',	'SB@1;OUT@2;SY@4'			)
	pRace.AddFleetTemplate('STD_OUT_DEF',		'DN@4'					)
	pRace.AddFleetTemplate('STD_SB_DEF',		'DN@6'					)
	pRace.AddFleetTemplate('STD_SB+_DEF',		'DN@8'					)
	
	### Colour
	pRace.SetColour(0.1,1.0,0.2,1.0)

	## Characters
	### Heads
	MAH = ('Romulan2','Romulan3','Romulan4' )
	MPH = ()
	FAH = ('Romulan1','Tpol')
	FPH = ('Romulan5',)
	
	### Bodies
	#### Male
	SAM = ('RomulanMale',)
	SOM = ('RomulanMale',)
	SSM = ('RomulanMale',)
	STM = ('RomulanMale',)
	M   = ('Male',)

	#### Female
	SAF = ('RomulanFemale',)
	SOF = ('RomulanFemale',)
	SSF = ('RomulanFemale',)
	STF = ('RomulanFemale',)
	F   = ('Female',)

	### Defs Male
	pRace.SetCharacters( 'Admiral',		'Tribune $$',		'M',	MAH,		SAM )
	pRace.SetCharacters( 'Captain',		'Commander $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'M',	MAH,		SOM )
	pRace.SetCharacters( 'Science',		'Centurion $$',		'M',	MAH+MPH,	SSM )
	pRace.SetCharacters( 'Helm',		'Centurion $$',		'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Tactical',	'Centurion $$',		'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Engineer',	'Centurion $$',		'M',	MAH+MPH,	STM )
	pRace.SetCharacters( 'Guest',		'$$',			'M',	MAH+MPH,	SAM+SOM+STM+SSM+M )
	pRace.SetCharacters( 'Extra',		'Soldier $$',		'M',	MAH+MPH,	SOM+STM+SSM )
	pRace.SetCharacters( 'Civilian',	'Mister $$',		'M',	MAH+MPH,	M )

	### Defs Female
	pRace.SetCharacters( 'Admiral',		'Tribune $$',		'F',	FAH,		SAF )
	pRace.SetCharacters( 'Captain',		'Commander $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Commander',	'Commander $$',		'F',	FAH,		SOF )
	pRace.SetCharacters( 'Science',		'Centurion $$',		'F',	FAH+FPH,	SSF )
	pRace.SetCharacters( 'Helm',		'Centurion $$',		'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Tactical',	'Centurion $$',		'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Engineer',	'Centurion $$',		'F',	FAH+FPH,	STF )
	pRace.SetCharacters( 'Guest',		'$$',			'F',	FAH+FPH,	SAF+SOF+STF+SSF+F )
	pRace.SetCharacters( 'Extra',		'Soldier $$',		'F',	FAH+FPH,	SOF+STF+SSF )
	pRace.SetCharacters( 'Civilian',	'Miss $$',		'F',	FAH+FPH,	F )

	## Shipnames
	pRace.SetShipnameFile(sPath + 'Shipnames.dat')
	
	## Shipnames
	pRace.SetCharacternameFile(sPath + 'Characternames.dat')

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