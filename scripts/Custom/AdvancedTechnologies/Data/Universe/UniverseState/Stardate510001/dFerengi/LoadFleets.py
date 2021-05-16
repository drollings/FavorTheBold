## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.Universe  import ATP_StarCharts
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *


## Load function
def LoadUniverse():
	## Race & Universe
	pUniverse = GetUniverse()
	pRace = pUniverse.GetChildByName('Ferengi Alliance')
	
	## Find some holders
	pFerenginar = pUniverse.GetChildByName('Ferenginar')
	X,Y = pUniverse.GetSectorCoords(pFerenginar)
	pSolars = pUniverse.GetSectorSolars(X,Y,3)

	pHolders = []	
	for pSolar in pSolars:
		pPlanets = pSolar.GetAllPlanets()
		if pPlanets:
			for i in range(pRace.GetRandomInt(1,5)):
				pHolders.append(pRace.GetRandomItem(pPlanets))

		pBases = pSolar.GetAllStarbases()
		if pBases:
			for i in range(pRace.GetRandomInt(1,3)):
				pHolders.append(pRace.GetRandomItem(pBases))


	## Type of fleets
	lsTypes = ( 'HEAVY_COMMERCE_LINE','MEDIUM_COMMERCE_LINE','MEDIUM_COMMERCE_LINE','SMALL_COMMERCE_LINE' )
	
	## Fleets
	for i in range(1,25):

		sType 		= pRace.GetRandomItem(lsTypes)
		iNumSpaces 	= pRace.GetRandomInt(1,6)
		lpDests 	= []
		pPrevDest 	= None

		for j in range(iNumSpaces):
			pDest = pRace.GetRandomItem(pHolders)
			while(pPrevDest == pDest):
				pDest = pRace.GetRandomItem(pHolders)
			pPrevDest = pDest				
			lpDests.append(pDest)			
		
		pFleet = Fleet()
		pFleet.Bind(pRace,lpDests[0],'Merchant Fleet '+str(i),sType)
		if len(lpDests) > 1:
			pFleet.SetupSpaceline(lpDests)
