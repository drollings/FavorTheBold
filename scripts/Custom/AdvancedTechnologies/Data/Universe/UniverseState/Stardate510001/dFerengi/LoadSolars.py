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
	pRace = pUniverse.GetChildByName("Ferengi Alliance")

	## System Ferenginar
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Ferenginar",
			"M",
			"B;B;B;N;M@Ferenginar@78.2;L;F;E;O;J;J;H;P;C"		)
	pSolar.SetLocXYZ(-2.82,1.24,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## System Thalos
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Thalos",
			"M@Thalos I@+1;K@Thalos II@+5;G@Thalos III@+7",
			"B;B;B;N;F;F;L;M@Thalos@4.5;H@Colony@0.1;P;K;J;J;I;C"	)
	pSolar.SetLocXYZ(-2.74,1.56,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## System Balancar
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Balancar",
			"F@Balancar I@+1;F@Balancar II@+3",
			"B;N;A;M@Balancar@8.2;O@Second@5.6;K;K;L;L@Balancar Minor@0.15;J;I;J;P;C"	)
	pSolar.SetLocXYZ(-3.15,1.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)


	## System Clarus
	## Location of planet Archybite.  
	## Planetary group located near Ferenginar.
	## Nava took over the mining refineries in the Clarus System
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Clarus",
			"K@Clarus I@-1;M@Clarus II@+1;G@Clarus III@+3",
			"B;N;N;K;A;F;M@Archybite@5.2;H;K;P;J;J;J;J;J;P;C;C"	)
	pSolar.SetLocXYZ(-3.14,0.97,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar) 

	## System Irtok
	## Planetary group.  
	## Located near Ferenginar.
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Irtok",
			"G@Irtok Sun@+1",
			"N;N;K;H;M@Irtok@1.7;F;G;E;O;K;K;I;I;I",
			bCoreSystem=FALSE				)
	pSolar.SetLocXYZ(-3.62,1.04,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar) 