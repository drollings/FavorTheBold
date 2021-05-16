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
	pRace = pUniverse.GetChildByName("Tzenkethi Coalition")

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Tzenketh",
			"M@Tzenketh Sun@+9",
			"B;B;N;N;N;O@Tzenketh Minor@0.9;L;L;O@Tzenketh Tertior@2.4;G;M@Tzenketh Prime@9.8;L;O;M@Tzenketh Second@5.2;P;K;K;Q;K;J;J;J;J;C;P;C",
			"HOME_SYS_DEF@@Tzenketh Prime|BASE_SYS_DEF@@Tzenketh Prime")
	pSolar.SetLocXYZ(-2.45,-0.7,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	# M'kemas III
	# Planet located in Tzenkethi territory.  
	# In 2371, a Founder took control of the U.S.S. Defiant and planned to attack M'kemas III in hopes of starting a war between the Federation and the Tzenkethi.
 	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"M\'Kemas",
			"O@M\'Kemas Sun I@-2;B@M\'Kemas Sun II@+3",
			"B;N;M@M\'Kemas@5.2;K;K;P;G;H;H;J;J;I;C;C;C",
			"STD_SYS_DEF@@M\'Kemas|BASE_SYS_DEF@@M\'Kemas"
			)
	pSolar.SetLocXYZ(-2.85,-0.45,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Omega Piscium",
			"F@@+1;F;F",
			"B;B;N;O;P;H;H;K;J;J;J;J;J",
			"STD_SYS_DEF@@Omega Piscium IV"
			)
	pSolar.SetLocXYZ(-3.10,-0.58,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Lamemda",
			"F@@+5",
			"B;N;N;M@Lamemda@6.9;K;L;L;P;J;I;I;P;C",
			"STD_SYS_DEF@@Lamemda"
			)
	pSolar.SetLocXYZ(-3.03,-0.70,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)


	pUniverse = GetUniverse()
	pRace = pUniverse.GetChildByName("Nonaligned")


	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Cruses",
			"G@Zeta Gruis I@+1;K@Zeta Gruis II@+3",
			"B;B;B;N;L;M@Cruses@2.2;K;O;J;J;C;C",
			"STD_SYS_DEF@@Cruses",
			bCoreSystem=FALSE)
	pSolar.SetLocXYZ(1.35,2.72,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Garadius",
			"K@Delta Muscae I@-1;K@Delta Muscae I@+5",
			"B;B;B;M@Garadius@1.8;A;F;H;I;J;I;C;C",
			"STD_SYS_DEF@@Garadius",
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(0.53,4.0,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Idran",
			"F@@-5;O@@-1;O@@+3",
			"Q@Idran",
			bCoreSystem = FALSE	)
	pSolar.SetLocXYZ(0.0,0.0,0.0,IDRAN_OFFSET)
	ATP_StarCharts.AddSolarSystem(pSolar)
