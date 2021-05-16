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
	pRace = pUniverse.GetChildByName("Coalition")
	
	## Put your system declarations here
	pFleet = Fleet()

	pDominion = pUniverse.GetChildByName("Cardassian Union")
	pHolder   = pUniverse.GetChildByName("Bell").GetChildByName("Bell")
	pFleet.Bind(pDominion,pHolder,"Assaut Force 12","{FTB_Devastator@5;FTB_Dominator@20}")
	