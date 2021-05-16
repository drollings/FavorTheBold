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
	pRace = pUniverse.GetChildByName("Cardassian Union")

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Chin\'Toka",
			"G",
			"B;B;B;N;N;M@Chin\'Toka@1.6;K;G;F;P;I;I;J;C",
			"STD_SYS_DEF@Chin\'Toka Defense@Chin\'Toka")
	pSolar.SetLocXYZ(-1.5,-2.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	# A star system located in Cardassian space.  
	# The Cuellar system was the location of a Cardassian science station that was destroyed by the crew of the U.S.S. Phoenix in 2367.
 	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Cuellar",
			"G",
			"B;N;L;P;M@Cuellar@4.1;K;K;I;I;I;C;C;C",
			"STD_SYS_DEF@Cuellar Defense@Cuellar")
	pSolar.SetLocXYZ(-1.45,-2.6,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	#Kelrabi System
	#Planetary system located in Cardassian space.  
	#It was the destination of a Cardassian supply ship intercepted by the U.S.S. Phoenix and the Enterprise-D in 2367
 	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Kelrabi",
			"M@Kelrabi Sun@+5",
			"B;B;N;N;A;F;P;M@Kelrabi@2.1;K;G;K;I;I;J;C;C;C",
			"STD_SYS_DEF@Kelrabi Defense@Kelrabi")
	pSolar.SetLocXYZ(-1.65,-2.75,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Cardassia",
			"K@Cardassia Sun@-1",
			"B;B;M;M@Hutet@1.2;M@Cardassia Minor@2.7;M@Cardassia Prime@7.9;Q;I",
			"STD_SYS_DEF@Cardassia Defense")
	pSolar.SetLocXYZ(-3.15,-1.65,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	# Planet in the Demilitarized Zone near the Dorvan sector.  
	# Panora was a Cardassian colony world.
	# In 2373, the Maquis raided Panora, seriously damaging most of the defense systems there.
 	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Panora",
			"F",
			"B;B;B;N;O@Cardassian Colony@0.9;A;H;H;K;C;C;J",
			)
	pSolar.SetLocXYZ(-2.2,-2.175,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	# In the Demilitarised Zone. At least four moons; attacked by biogenic weapon
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Quatal",
			"A",
			"N;N;M@Quatal@1.8;D;D;D;D;A;K;I;I;I;C",
			)
	pSolar.SetLocXYZ(-1.9,-2.175,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	# Sisko finds himself trying to rescue Gul Dukat from the Maquis while trying to obey Starfleet's orders to stop the Maquis and bring peace back to the Volon colonies
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Volon@DMZ: Military movements forbidden",
			"M@Volon Sun@+5",
			"B;N;N;A;F;M@Federatian Colonies@0.2;K;I;I;J",
			)
	pSolar.SetLocXYZ(-1.2,-2.175,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)	

	#Salva II In the Demilitarised Zone. Cardassian colony in treaty signing.
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Salva@DMZ: Military movements forbidden",
			"F",
			"B;M@Cardassian Colony@1.1;G;F;K;I;I;J;K",
			)
	pSolar.SetLocXYZ(-1.35,-2.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)