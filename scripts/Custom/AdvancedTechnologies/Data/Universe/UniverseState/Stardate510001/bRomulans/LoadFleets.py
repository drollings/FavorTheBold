## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.Universe  import ATP_StarCharts
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *


## Load function
def LoadUniverse():
	pUniverse = GetUniverse()
	pRace = pUniverse.GetChildByName("Romulan Star Empire")

	## Create a fleet
	# pFleet = Fleet()
	# pFleet.Bind(pRace,pDestA,"Merchant Fleet "+str(i),pRace.GetRandomFleetTemplate())
	# pFleet.SetupSpaceline(pDestB)