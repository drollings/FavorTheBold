## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Object import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Extras import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Wormholes import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

## Load function
def LoadUniverse():
	## Load the player fleet
	LoadBasicUniverse()

	## Load the different submodules
	import Foundation
	sNamespaceFolder,sDirFolder = NamespaceToFolderNames(__name__)
	lsSubfolders = Foundation.GetFolderNames(sDirFolder)

	## Load the basic structure
	for sSubfolder in lsSubfolders:
		sFile = sSubfolder + "." + "LoadUniverse"
		pModule = __import__(sFile)
		#try:
		#	pModule = __import__(sFile)
		#except ImportError:
		#	raise ImportError,"Corrupted UniverseState folder: "+sFile+" not found."
		
		pModule.LoadUniverse()		

	## All systems should be created by now
	## Rasterise the systems in a map
	GetUniverse().Vectorise()

	## A second pass, especially good for fleets, when all systems have been created
	for sSubfolder in lsSubfolders:
		sFile = sSubfolder + "." + "LoadUniverse"
		pModule = __import__(sFile)
		#try:
		#	pModule = __import__(sFile)
		#except ImportError:
		#	raise ImportError,"Corrupted UniverseState folder: "+sFile+" not found."
		
		pModule.PostLoadUniverse()

	## Diplomacy
	Diplomacy()
	
	## Configure the player
	ConfigurePlayer()

	## Some action
	Action()

	## This sets off the race AI
	# Genisis()

def LoadBasicUniverse():
	## Load the player fleet
	pPlayerFleet=PlayerFleet(PLAYER_FLEET_ID)
	
def ConfigurePlayer():	
	## Choose a playerrace
	pRace = GetUniverse().GetChildByName("United Federation of Planets")	

	## Choose a system
	pSolar = GetUniverse().GetChildByName("Sol")
	
	## Choose a place
	pHolder = GetUniverse().GetChildByName("Bajor").GetChildByName("Bajor")
	pHolder = pSolar.GetChildByName("Earth").GetChildByName("Spacedock").GetChildByName("Spacedock")
	pHolder = pSolar.GetRandomItem(pSolar.GetChildByName("Mars").GetChildByName("Utopia Planetia").GetStarbases())
	
	## Reconfigure the playerfleet
	# GetPlayerFleet().Bind(pRace,pHolder,"Player Fleet","{FTB_Galaxy;FTB_Akira}")
	GetPlayerFleet().Bind(pRace,pHolder,"Player Fleet","{FTB_Sovereign}")
	# GetPlayerFleet().Bind(pRace,pHolder,"Player Fleet","")
	# GetPlayerFleet().Bind(pRace,pHolder,"Player Fleet","{FTB_Galaxy;FTB_Akira;FTB_Sovereign}")

	## Set the state correct
	GetPlayerFleet().SetState(NORMAL)
	for pShip in GetPlayerFleet().GetShips():
		pShip.State = NORMAL

	## Shipname of the player
	GetPlayerShip().sName = 'USS Dauntless'

def Action():
	pUniverse = GetUniverse()

	pEarth = GetUniverse().GetChildByName("Sol").GetChildByName('Earth')

	pFederation = pUniverse.GetChildByName("United Federation of Planets")
	pCoalition  = pUniverse.GetChildByName("Coalition")
	pCardassians = pUniverse.GetChildByName("Cardassian Union")
	pRomulans = pUniverse.GetChildByName("Romulan Star Empire")

	#pFleet = Fleet()
	#pFleet.Bind(pCardassians,GetMatrix(),'Assault Force 1','STD_SYS_ASS')
	#pFleet.Voyage(pEarth)
	#pFleet = Fleet()
	#pFleet.Bind(pCardassians,GetMatrix(),'Assault Force 2','STD_SYS_ASS')
	#pFleet.Voyage(pEarth)
	#pFleet = Fleet()
	#pFleet.Bind(pCoalition,GetMatrix(),'Admiral Rombaut','STD_SYS_ASS')
	#pFleet.Voyage(pEarth)
	
	
def Diplomacy():
	pUniverse = GetUniverse()

	pFederation = pUniverse.GetChildByName("United Federation of Planets")
	pCoalition  = pUniverse.GetChildByName("Coalition")
	pCardassians = pUniverse.GetChildByName("Cardassian Union")
	pRomulans = pUniverse.GetChildByName("Romulan Star Empire")

	pFederation.SetAlly(pCoalition)
	pFederation.SetEnemy(pCardassians)
	pFederation.SetEnemy(pRomulans)
	
	pCoalition.SetAlly(pFederation)
	pCoalition.SetEnemy(pCardassians)
	pCoalition.SetEnemy(pRomulans)

	pCardassians.SetEnemy(pFederation)
	pCardassians.SetEnemy(pCoalition)
	pCardassians.SetEnemy(pRomulans)

	pRomulans.SetEnemy(pFederation)
	pRomulans.SetEnemy(pCoalition)
	pRomulans.SetEnemy(pCardassians)