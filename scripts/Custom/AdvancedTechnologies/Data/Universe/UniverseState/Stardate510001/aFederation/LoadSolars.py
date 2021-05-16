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
	pRace = pUniverse.GetChildByName("United Federation of Planets")

	pSolar=SolarSystem()
	pSolar.Bind(pRace,"Andoria@Founding Member of the UFP",
                          "F@Procyon@-1;A@Alpha Canis Minoris",
                          "B;B;B;N;N;H;A;M@Andoria@38.2;K;K;Y;I;J;D;D;I;J",
                          "STD_SYS_DEF@Andoria Protector@Andoria|{FTB_Akira@1@USS Hope;FTB_Galaxy@1@USS Odeysee}@Heavy Taskforce 85")
	pSolar.SetLocXYZ(0.3,-0.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=SolarSystem()
	pSolar.Bind(pRace,"Betazed","G@Beta Zeta@+5","B;B;B;N;D;D;M@Betazed@1.3;D;D;J;J;J;C")
	pSolar.SetLocXYZ(-0.8,-2.5,0.0)
	pSolar.SetNotInNebula()
	ATP_StarCharts.AddSolarSystem(pSolar)
		
	pSolar=SolarSystem()
	pSolar.Bind(pRace,"Bolarus","B@Bolarsun Sun@-3","B;B;N;Q;H;O;M@Bolarus@54.5;D;D;K;P;I;D;D;J;D;D;D;J;I;C")
	pSolar.SetLocXYZ(0.45,1.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Vulcan@Founding Member of the UFP",
			"K@Omicron 2 Ceti@-1;A@Eridani B;M@Eridani C",
			"B;M@Vulcan@4.9;G@T\'Khut@0.2")
	pSolar.SetLocXYZ(0.2,-0.6,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Bajor",
			"G@B\'hava\'el@+3",
			"B;B;B;B;N;M;M@Bajor@3.2;D;D;D;D;D;P;K@Andros@0.9;D;D;I;I;J;C;C;C"	)
	pSolar.SetLocXYZ(-3.0,-1.9,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Rigel",
			"A@Beta Rigel@+3",
			"B;B;N;N;N;M@Rigel VI@0.2;M@Rigel VII@0.1;O;H;P@Rigel X@0.1;K;J;J;J;P;C")
	pSolar.SetLocXYZ(0.75,-1.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Capella",
			"G@Alpha Aurigae I@-3;G@Alpha Aurigae II;M@Alpha Aurigae III;M@Alpha Aurigae IV",
			"B;B;B;B;B;N;M@Capella@1.2;K;I;I;I;I",
			bCoreSystem = FALSE
				)
	pSolar.SetLocXYZ(-0.5,-2.0,0.0)
	pSolar.SetNotInNebula()
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Beta Renner",
			"G@Beta Renner Sun@-3","Y;Y;B;B;B;N;A;K;H;M@Selay@20.4;P;K;O@Selay Tertior@2.7;L;M@Antica@41.7;K;K;M@Selay Minor@2.0;I;J;J;J;I;I",
			bCoreSystem = FALSE)
	pSolar.SetLocXYZ(-25.0,-25.0,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.GetRandom()
	pSolar.Bind(	pRace,
			"Deneb",
			"G@Deneb Kaitos@-3",
			"B;M@Minor@1.0;O@Secundo@3.5;D;D;M@Tertior@3.3;D;M@Deneb@11.2;T@Proto Star",
			bCoreSystem = FALSE)
	pSolar.SetLocXYZ(-0.75,-0.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Benzar",
			"G@Delta Pavonis@+3",
			"B;M@Benzar@3.8;K;J;C")
	pSolar.SetLocXYZ(0.40,0.80,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Tellar@Founding Member of the UFP",
			"K@61 Cygni I@+3;K@62 Cygni II",
			"B;B;N;N;E;H;F;L;M@Tellar@5.2;O@Tellar Minor@2.6;A;P;P;K;K;K;J;J;C")
	pSolar.SetLocXYZ(-0.50,0.05,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Denobula Triaxa","G@Iota Bootis I@+5;G@Iota Bootis II",
			"B;B;N;N;F;E;K;M@Denobula@45.8;K;L;I;J;J;I;P;H",
			bCoreSystem = FALSE)
	pSolar.SetLocXYZ(-1.1,0.15,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Trill","G@Trillius I@+1;K@Trilius II",
			"B;B;N;A;G;F;H;K;P;P;M@Trill@0.65;L;K;A;C;P;H")
	pSolar.SetLocXYZ(-1.75,-1.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Regulus",
			"G@Alpha Leonis I@-5;K@Alpha Leonis II;M@Alpha Leonis III",
			"B;H;M@Regulus Minor@1.1;G;O@Regulus Prime@8.9;L;L;L;P;K;I;I;I;J;I;C;C",
			bCoreSystem = FALSE)
	pSolar.SetLocXYZ(+1.8,-1.8,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Delta","F@Delta Sun@+1",
			"B;B;N;F;M@Delta@3.8;D@Seyann@0.2;D@Cinera@0.6;H;P;J")
	pSolar.SetLocXYZ(-0.72,2.15,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(pRace,"Zakdorn",
                          "M@@-3;K@@-1",
                          "B;B;N;N;E;M@Zakdorn@5.2;F;G;L;M@Zakdorn Minor@1.2;K;P;P;J;I;J;C;C",
                          "STD_SYS_DEF@Zakdorn Protector@Zakdorn")
	pSolar.SetLocXYZ(5.65,3.72,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	## Caldos IV? Beverly with Ghost
	pSolar=SolarSystem()
	pSolar.Bind(pRace,	"Caldos",
                          	"A@Beta Octantis@+3",
                          	"B;B;N;M@Caldos@1.2;K;F;I;J;C;C;C;C",
                          	"STD_SYS_DEF@Caldos Protector@Caldos",
				bCoreSystem = FALSE)
	pSolar.SetLocXYZ(4.56,3.6,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(pRace,	"Epsilon Pavonis",
                          	"F",
                          	"B;B;N;N;H;K;F;P;P;P;I;I;J;C;C"
					                          	)
	pSolar.SetLocXYZ(2.8,3.6,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	# Class-M planet in the Gamma Hydra system.  
	# This was the location of an experimental colony where all six of its members, none of them over 30 years of age, died in 2267 of a radiation-induced hyperaccelerated-aging disease.
	# The disease later afflicted members of an Enterprise landing party that investigated the incident.
	# Analysis of a comet in the Gamma Hydra system showed that radiation on the extreme lower range of the scale might have caused the disease.
 	pSolar=SolarSystem()
	pSolar.Bind(pRace,	"Gamma Hydra",
                          	"G@Gamma Hydra Sun@-5",
                          	"B;B;N;M@Colony@0.2;H;K;K;I;I;I;C",
				bCoreSystem = FALSE
					                          	)
	pSolar.SetLocXYZ(3.85,3.38,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Rhaandar",
			"F@Alpha Indi@-3",
			"B;M@Rhaandar@2.3;L;M@Rhaandar Minor@0.8;H;P;P;I;I;I;C",
			bCoreSystem = FALSE						)
	pSolar.SetLocXYZ(0.53,4.0,0.0)
	pSolar.SetNotInNebula()
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Aaamazzara",
			"A@Alpha Serpentis",
			"B;B;N;N;K;M@Aaamazzara@4.3;L;A;P;P;I;J;I;C;C;C",
			bCoreSystem = FALSE						)
	pSolar.SetLocXYZ(-0.60,2.57,0.0)	
	ATP_StarCharts.AddSolarSystem(pSolar)


	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Goren",
			"F@Delta Geninorum I@-1;F@Delta Geninorum II@-1;K@Delta Geninorum III@+1",
			"B;B;N;A;F;O@Goren@2.3;K;K;P;J;J;J;C;C",
			bCoreSystem = FALSE						)
	pSolar.SetLocXYZ(0.8,-2.8,0.0)
	pSolar.SetNotInNebula()
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Ivor",
			"F@Eta Scorpii@-1",
			"B;B;N;N;N;G;H;N@Ivor Prime@1.2;L;P;P@Ivor Minor@0.2;J;J;C;C;C",
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(0.95,3.45,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)	

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Izar",
			"K@Epsilon Bootis@+5",
			"B;H;M@Izar@0.9;O;L;L;K;J;J;P",
			"STD_SYS_DEF@Izar Defense@Izar|BASE_SYS_DEF@Izar Station@Izar",
			bCoreSystem = TRUE			)
	pSolar.SetLocXYZ(-2.85,3.46,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Berengaria",
			"M@@+1;M",
			"B;Y;N;H;F;K;M@Berengaria@3.6;H;L;L;P;J;J;J;C;C",
			"STD_SYS_DEF@Berengaria Defense@Berengaria|BASE_SYS_DEF@Berengaria Station@Berengaria",
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(-3.25,3.76,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Tyberius",
			"K@Mu Aquilae@+5",
			"B;N;L;E;O@Tyberius Colony@0.3;K;P",			
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(-3.83,3.95,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Antos",
			"G@Kappa Delphini@-3",
			"B;N;N;M@Antos@4.3;H;H;P;J;I;I;H;C",
			"STD_SYS_DEF@Antos Defense@Antos|BASE_SYS_DEF@Antos Station@Antos",
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(-3.83,3.95,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=SolarSystem()
	pSolar.Bind(	pRace,
			"Ba\'Ku",
			"K@@+3",
			"Q;Q;M@Ba\'Ku",
			"",
			bCoreSystem = FALSE			)
	pSolar.SetLocXYZ(0.90,-2.58,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)




	0.9 -2.58