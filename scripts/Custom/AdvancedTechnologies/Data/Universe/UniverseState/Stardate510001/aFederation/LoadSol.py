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

	############################################################
	#Create a new system
	############################################################
	#The Solar System
	#################
	pSolar=SolarSystem()
	pSol = pSolar
	pSolar.SetName("Sol")
	pSolar.Migrate(pRace)
	pSolar.Move(pUniverse)
	pSolar.SetLocXYZ(0.0,0.0,0.0)
	

	#The Stellar Elements
	#####################
	pSun=Sun()
	pSun.SetName("Sol Sun")
	pSun.SetClass("G")
	pSun.SetGfx(1.3e+6*km,1.3e+6*km, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSun.SetHolder(pSolar)

	pPlanet=Planet()
	pPlanet.SetName("Mercury")
	pPlanet.SetGfx(4.8e+3*km,GFX_PATH_PLANETS+"Mercury.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("B")
	pPlanet.SetHolder(pSun)
	
	pPlanet=Planet()
	pPlanet.SetName("Venus")
	pPlanet.SetGfx(12.1e+3*km,GFX_PATH_PLANETS+"Venus.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("N")
	pPlanet.SetHolder(pSun)

	pPlanet=Planet()
	pPlanet.SetName("Earth")
	pPlanet.SetGfx(12.7e+3*km,'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Planets/M-Class/Earth.nif')
	pPlanet.SetPopulation(4.2)
	pPlanet.SetClass("M")
	pPlanet.SetHolder(pSun)

	pMoon=Moon()
	pMoon.SetName("Moon")
	pMoon.SetGfx(3.4e+3*km,GFX_PATH_PLANETS+"moon.nif")
	pMoon.SetPopulation(1.1)
	pMoon.SetClass("D")
	pMoon.SetHolder(pPlanet)

	pPlanet=Planet()
	pPlanet.SetName("Mars")
	pPlanet.SetGfx(6.7e+3*km,GFX_PATH_PLANETS+"Mars.nif")
	pPlanet.SetPopulation(0.14)
	pPlanet.SetClass("K")
	pMars=pPlanet
	pPlanet.SetHolder(pSun)

	pPlanet=Planet()
	pPlanet.SetName("Jupiter")
	pPlanet.SetGfx(142.6e+3*km,GFX_PATH_PLANETS+"Jupiter.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("I")
	pPlanet.SetHolder(pSun)

	pPlanet=Planet()
	pPlanet.SetName("Saturn")
	pPlanet.SetGfx(120.0e+3*km,GFX_PATH_PLANETS+"Saturn.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("I")
	pPlanet.SetHolder(pSun)
	
	pPlanet=Planet()
	pPlanet.SetName("Uranus")
	pPlanet.SetGfx(51.0e+3*km,GFX_PATH_PLANETS+"Uranus.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("I")
	pPlanet.SetHolder(pSun)

	pPlanet=Planet()
	pPlanet.SetName("Neptune")
	pPlanet.SetGfx(49.0e+3*km,GFX_PATH_PLANETS+"Neptune.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("I")
	pPlanet.SetHolder(pSun)

	pPlanet=Planet()
	pPlanet.SetName("Pluto")
	pPlanet.SetGfx(2.3e+3*km,GFX_PATH_PLANETS+"Pluto.nif")
	pPlanet.SetPopulation(0.0)
	pPlanet.SetClass("C")
	pPlanet.SetHolder(pSun)
	
	ATP_StarCharts.AddSolarSystem(pSolar)

	pSolar.EvolveRandom(8)
		
	pFleet=Fleet()
	pFleet.Bind(pRace,pSolar.GetChildByName("Earth"),"","{ATP_FedStarbase@1@Spacedock}")
	
	pFleet=Fleet()
	pFleet.Bind(pRace,pSolar.GetChildByName("Mars"),"Utopia Planetia","{ATP_FedStarbase@1@Supply Starbase;FedOutpost@2@Orbital Office;ATP_Shipyard@1}")		
		
	pFleet=Fleet()
	pFleet.Bind(pRace,pSolar.GetChildByName("Earth"),"Taskforce 742","{FTB_Galaxy@3}")