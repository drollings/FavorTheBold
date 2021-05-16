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

	pSolar=StarbaseSystem()
	pSolar.Bind(	pRace,
			"Starbase 10@Fortified Starbase near the Romulan Border and Bolarus",
			"{ATP_FedStarbase@1@Starbase 10;ATP_Shipyard@3@Shipyard}@Defense|ROM_NZ_SB+_DEF@Starbase 10 Guard")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(0.925,1.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(	pRace,
			"Starbase 23@Fortified Starbase near the Romulan Border",
			"{ATP_FedStarbase@1@Starbase 23;ATP_Shipyard@1@Shipyard}@Defense|ROM_NZ_SB+_DEF@Starbase 23 Guard")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(3.1,-0.95,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(	pRace,
			"Starbase 718@Starbase near the Romulan Border",
			"{ATP_FedStarbase@1@Starbase 718}@Base|ROM_NZ_SB_DEF@Starbase 718 Guard"		)
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(0.77,2.45,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(	pRace,
			"Starbase 514@Starbase in the Izar region",
			"{ATP_FedStarbase@1@Starbase 514}|STD_SB_DEF@Starbase 514 Guard"	)
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-2.58,3.58,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 39 - Sierra|Starbase 39S@Fortified Starbase near the Romulan Border and Kaleb","{ATP_FedStarbase@1@Starbase 39 - Sierra}@Base|ROM_NZ_SB+_DEF@Starbase 39 Guard")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(1.2,0.15,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Deep Space 4@Border station near the Typhon expanse","{FedOutpost@1@Deep Space 4}@Base")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.9,3.25,0.0)
	pSolar.SetNotInNebula()
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Deep Space 5","{FedOutpost@1@Deep Space 5}@Base")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.2,3.35,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Deep Space 3","{FedOutpost@1@Deep Space 3}@Base")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(-4.0,3.5,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Deep Space 6","{FedOutpost@1@Deep Space 6}@Base")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(5.4,3.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec I|I","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.85,-0.8,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec II|II","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.7,-0.7,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec III|III","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.55,-0.6,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec IV|IV","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.4,-0.5,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec V|V","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.25,-0.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Quebec VI|VI","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.1,-0.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
	
	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Romeo I|I","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.95,-0.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Romeo II|II","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.8,-0.1,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Romeo III|III","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.65,-0.0,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra I|I","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.5,+0.1,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra II|II","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.35,+0.2,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra III|III","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.2,+0.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra IV|IV","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.1,+0.35,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra V|V","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.075,+0.55,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra VI|VI","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.05,+0.70,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Sierra VII|VII","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.025,+0.85,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Science Station Tango Sierra|Science Station TS","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.00,+1.00,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Tango I|I","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.95,+1.1,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Tango II|II","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.9,+1.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Tango III|III","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.9,+1.55,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Tango IV|IV","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.875,+1.75,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 1|1","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.8,+1.875,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 2|2","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.9,+1.975,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 3|3","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(0.98,+2.15,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 4|4","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.0,+2.3,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 5|5","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.11,+2.45,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 6|6","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.23,+2.6,2.575)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 7|7","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.36,+2.7,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 8|8","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.5,+2.8,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 9|9","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.65,+2.85,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 10|10","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.80,+2.9,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 11|11","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(1.975,+2.93,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 12|12","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.15,+2.96,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 13|13","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.31,+2.9,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 14|14","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.475,+2.96,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 15|15","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.62,+2.9,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 16|16","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.75,+2.875,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 17|17","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.925,+2.85,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 18|18","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(3.05,+2.83,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 19|19","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(3.22,+2.75,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 21|21","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(3.30,+2.65,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 22|22","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(3.40,+2.55,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Earth Outpost 23|23","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(3.52,+2.475,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Science Station D5","{FedOutpost@1@Outpost}@Base|ROM_NZ_OUT_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.OUTPOST)
	pSolar.SetLocXYZ(2.975,+2.72,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 185","{ATP_FedStarbase@1@Starbase 185}@Base|STD_SB_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(5.28,4.33,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	#### CARDASSIAN BORDER
	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 375","{ATP_FedStarbase@1@Starbase 375}@Base|CARD_BD_SB_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-1.4,-1.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 621","{ATP_FedStarbase@1@Starbase 621}@Base|CARD_BD_SB_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-2.1,-0.75,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 310","{FedOutpost@1@Starbase 310}@Base|CARD_BD_SB+_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-1.8,-2.02,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 211","{ATP_FedStarbase@1@Starbase 211}@Base|CARD_BD_SB+_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-1.2,-2.4,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 47","{ATP_FedStarbase@1@Starbase 47}@Base|CARD_BD_SB+_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-1.2,-3.05,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar=StarbaseSystem()
	pSolar.Bind(pRace,"Starbase 129","{ATP_FedStarbase@1@Starbase 129}@Base|CARD_BD_SB+_DEF@Defense")
	pSolar.SetClass(StarbaseSystem.STARBASE)
	pSolar.SetLocXYZ(-2.65,-3.25,0.0)
	ATP_StarCharts.AddSolarSystem(pSolar)
