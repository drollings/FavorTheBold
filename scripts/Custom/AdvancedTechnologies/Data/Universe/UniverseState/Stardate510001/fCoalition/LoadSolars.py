## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Object import *
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

	pSolar=SolarSystem()
	pSolar.Bind(      pRace,
			  "Bell@Home system of the Coalition",
                          "A@Apollo@+1",
                          "B;N;L;L;M@Bell@17.9;D@Aderican@2.3;D@Benixius@0.4;D@Kristifious@1.5;O@Occania;L;P;K;J;J;P",
                          "{CSD@1@CSD Apollo;CSD@1@CSD Raxus;CSD@1@CSD Olloquilius;CSD@1@CSD Endavour}@Admiral Rombaut Fleet@Bell")	
	pSolar.SetLocXYZ(0.0,0.0,0.0,BELL_OFFSET)
	ATP_StarCharts.AddSolarSystem(pSolar)
	