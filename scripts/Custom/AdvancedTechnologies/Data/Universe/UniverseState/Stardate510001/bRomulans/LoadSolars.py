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
	pRace = pUniverse.GetChildByName("Romulan Star Empire")

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Romulus",
			"K@Romulus Alpha@-3;M@Romulus Beta@-3",
			"B;B;N;Q@Remus@85.1;M@Romulus@9.65;K;K;A;J;C",
			"HOME_SYS_DEF@Romulan Imperial Fleet@Romulus|HOMEBASE_SYS_DEF@Romulus Stations@Romulus"	)
	pSolar.SetLocXYZ(1.5,2.0,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Rho Virginis",
			"B;B",
			"B;B;N;N;M@Rho Virginis@2.5;E;H;J;J;I;C;C;C;C",
			"STD_SYS_DEF@Defense@Rho Virginis")
	pSolar.SetLocXYZ(1.6,0.5,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Cheron",
			"F@Omicron Gruis@-1",
			"B;B;B;N;N;K;K;F;M@Cheron@4.5;L@Cheron Minor@1.2;F;F;J;J;C;C;C",
			"STD_SYS_DEF@Defense@Cheron|BASE_SYS_DEF@Cheron Station@Cheron")
	pSolar.SetLocXYZ(1.3,2.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Glinatara",
			"G@@+3",
			"N;L;O;O@Glinatara@6.1;K;K;K;F;H;H;H;I;C",
			"STD_SYS_DEF@Glinatara Defense@Glinatara|BASE_SYS_DEF@Glinatara Station@Glinatara")
	pSolar.SetLocXYZ(2.2,2.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Menkent",
			"K@Theta Centauri I@-1;K@Theta Centauri II@+1",
			"B;B;B;N;N;N;N;N;N;M@@7.5;M@@6.9;H;H;K;K;K;I;I;I;C",
			"STD_SYS_DEF@Menkent Defense@Menkent X")
	pSolar.SetLocXYZ(1.85,2.1,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Romii",
			"K",
			"B;B;N;N;N;N;F;E;L;O@Minor@0.4;M@Romii@2.5;K;K;K;P;H;K;I;I;J;C",
			"STD_SYS_DEF@Romii Defense@Romii|BASE_SYS_DEF@Romii Station@Romii")
	pSolar.SetLocXYZ(1.5,1.95,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Gacrux",
			"M@Gamma Crucis I@-5;F@Gamma Crucis II@+3",
			"B;B;B;B;B;B;N;N;H;E;H@Gacrux@0.5;K;K;I;I;I;I;J;J;J",
			"STD_SYS_DEF@Gacrux Defense@Gacrux")
	pSolar.SetLocXYZ(3.8,2.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Unroth",
			"F",
			"B;B;B;N;N;H;E;F;M@Unroth@1.5;K;F;E;K;I;I;C;C;C;C",
			"STD_SYS_DEF@Unroth Defense@Unroth|BASE_SYS_DEF@Unroth Station@Unroth")
	pSolar.SetLocXYZ(3.2,-0.75,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Rator",
			"K;K",
			"N;N;M@Rator@4.5;O@Rator Minor@0.9;K;L;C;H;P",
			"STD_SYS_DEF@Rator Defense@Rator Minor|BASE_SYS_DEF@Rator Station@Rator")
	pSolar.SetLocXYZ(3.2,0.0,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Terix",
			"A@+3",
			"B;B;B;N;K;G;H;G;M@Terix@2.1;J;J;Y;P;C;P;C;C",
			"STD_SYS_DEF@Terix Defense@Terix|BASE_SYS_DEF@Terix Station@Terix")
	pSolar.SetLocXYZ(1.8,1.65,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Vendor",
			"F;M",
			"B;N;L@Vendor@0.6;C",
			"STD_SYS_DEF@Vendor Defense@Vendor")
	pSolar.SetLocXYZ(2.3,0.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Belak",
			"G@@-3;K@@-1",
			"B;B;B;N;N;A;A;F;M@Belak@4.7;K;K;P;I;I;J;C;C;C",
			"STD_SYS_DEF@Belak Defense@Belak|BASE_SYS_DEF@Belak Station@Belak")
	pSolar.SetLocXYZ(2.6,2.07,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"T\'Met",
			"F",
			"B;B;F;H;E;O@T\'Met Minor@0.5;G;M@T\'Met@2.3;K;P;P;I;I;I;I",
			"STD_SYS_DEF@T\'Met Defense@T\'Met|BASE_SYS_DEF@T\'Met Station@T\'Met")
	pSolar.SetLocXYZ(2.29,2.77,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## Terminus of the wormhole from Delta Quadrant, 2351 location of Talvath
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Talvath",
			"K@@+3",
			"N;L;M@Talvath@2.5;K;O;D@Talvath Minor@0.4;P;J;J;I;P",
			"STD_SYS_DEF@Talvath Defense@Talvath|BASE_SYS_DEF@Talvath Station@Talvath")
	pSolar.SetLocXYZ(5.35,2.08,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## The Makar was lost in the Tal Shiar attack on the Founders' homeworld in 2371.
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Makar",
			"M@@+5;F",
			"B;B;N;Q;L;M@Makar@4.1;H;F;J;J;J;C;P;C",
			"STD_SYS_DEF@Makar Defense@Makar|BASE_SYS_DEF@Makar Station@Makar")
	pSolar.SetLocXYZ(7.16,2.15,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Zeta Volantis",
			"K@@+1;K",
			"Y;B;B;B;N;H;Q;H;H;J;I;I;J;P",
			"MIN_SYS_DEF@Defense@Zeta Volantis VII")
	pSolar.SetLocXYZ(6.02,1.60,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Xi Hydrae",
			"G@@+9;G",
			"B;B;N;M;G;E;E;K;J;J;J;J;J;P;P",
			"MIN_SYS_DEF@Defense@Xi Hydrae IV")
	pSolar.SetLocXYZ(5.55,1.42,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Alpha Volantis",
			"A@@+1;A",
			"Q;P;P;P;C",
			"MIN_SYS_DEF@Defense@Alpha Volantis I")
	pSolar.SetLocXYZ(5.90,1.36,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Rho Tucanae",
			"F@@+1;F",
			"B;B;B;N;N;L;P;H;K;F;J;J;I;I;I",
			"MIN_SYS_DEF@Defense@Rho Tucanae VI")
	pSolar.SetLocXYZ(3.40,2.34,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Gamma Tucanae",
			"F@@+1",
			"B;Q;B;N;N;H;L;H;K;F;I;J;P;P;P",
			"STD_SYS_DEF@Defense@Gamma Tucanae II")
	pSolar.SetLocXYZ(1.21,1.70,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Nu Octantis",
			"F@@-1",
			"N;N;F;F;H;L;L;P;P;J;J;C;C",
			"MIN_SYS_DEF@Defense@Nu Octantis VI")
	pSolar.SetLocXYZ(2.02,1.96,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Algorab",
			"B@Delta Corvi A@+1;K@Delta Corvi B",
			"B;B;F;F;M@Algorab@25.2;O@Algorab Minor@7.9;K;K;L;J;J;I;C;P",
			"STD_SYS_DEF@Algorab Defense@Algorab|BASE_SYS_DEF@Algorab Station@Algorab|BASE_SYS_DEF@Algorab Minor Station@Algorab Minor")
	pSolar.SetLocXYZ(2.76,1.34,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Archernar",
			"B@Alpha Eridani A@+1;B@Alpha Eridani B",
			"B;N;L;K;M@Archenar@12.7;H;P;P;I;J;J;P",
			"STD_SYS_DEF@Archenar Defense@Archenar|BASE_SYS_DEF@Archenar Station@Archenar")
	pSolar.SetLocXYZ(3.48,1.35,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## Khazara
	## Imperial Romulan warbird, D'deridex-class warbird.  
	## This ship, captained by Commander Toreth, was seized by Subcommander N'Vek and Deanna Troi as part of a plot to enable Romulan Vice-Proconsul M'ret to defect to the Federation.
 	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Khazara",
			"G@@+7;M;K",
			"Y;Y;B;B;B;N;H;H;L;O@Khazara@8.2;F;I;I;J;H",
			"STD_SYS_DEF@Khazara Defense@Khazara|BASE_SYS_DEF@Khazara Station@Khazara")
	pSolar.SetLocXYZ(5.86,0.18,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Devoras",
			"M@@+1;M;K;F",
			"B;Q;E;M@Devoras@1.2;H;I",
			"STD_SYS_DEF@Devoras Defense@Devoras|BASE_SYS_DEF@Devoras Station@Devoras")
	pSolar.SetLocXYZ(4.18,-0.32,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	

	