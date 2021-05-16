from ATP_Object import *

def SwapPlayer(pShip = None):
	## The player data
	pPlayer = GetPlayerShip()
	pFleet  = GetPlayerFleet()

	## What ship to swap?
	if not pShip:
		pHolder = pFleet.GetHolder()
		pFleets = pHolder.GetFleets()
		for ppFleet in pFleets:
			if ppFleet.ID != pFleet.ID:
				continue
			if ppFleet.State == INSIDE:
				pShip = pPlayer
				while(pShip.ID == pPlayer.ID):
					pShip = pPlayer.GetRandomItem(ppFleet.GetShips())
				break

	## Some assertions
	assert pPlayer.State == INSIDE
	assert pShip.State == INSIDE
	assert pPlayer.GetFleet().State == INSIDE
	assert pShip.GetFleet().State == INSIDE
	assert pShip.ID != pPlayer.ID
	assert pShip.Node and pPlayer.Node

	## Remember names
	sPlayerName = pPlayer.sName[:]
	pPlayer.sName,pShip.sName = pShip.sName[:],pPlayer.sName[:]
	sPlayerBridge = GetPlayerBridge().sBridgeType[:]
	sShipBridge   = pShip.GetBridge().sBridgeType[:]

	## Remember the shiptype
	sBridgeType = pShip.GetBridge().sBridgeType[:]
	
	## Swap the nodes
	pShip.Node , pPlayer.Node = pPlayer.Node , pShip.Node

	## Inform the game of player change
	GetGame().Node.SetPlayer(pPlayer.Node)

	## Modify the node cache
	# SID = pShip.Node.GetObjID()
	# PID = pPlayer.Node.GetObjID()
	# NodeCache = UniverseElement.NodeCache
	# NodeCache[SID],NodeCache[PID] = pPlayer,pShip
	pPlayer.PurgeNodeCache()

	## Change sGfx, hull, etc...
	pShip.sGfx , pPlayer.sGfx = pPlayer.sGfx , pShip.sGfx
	pShip.Hull , pPlayer.Hull = pPlayer.Hull , pShip.Hull
	pShip.Class , pPlayer.Class = pPlayer.Class , pShip.Class
	pShip.BuildPoints , pPlayer.BuildPoints = pPlayer.BuildPoints , pShip.BuildPoints
	pShip.BuildPercentage , pPlayer.BuildPercentage = pPlayer.BuildPercentage , pShip.BuildPercentage
	pShip.HullPercentage , pPlayer.HullPercentage = pPlayer.HullPercentage , pShip.HullPercentage

	## Change names
	pString=String('player')
	pPlayer.Node.SetName('player')
	pPlayer.Node.SetDisplayName(pString)
	pString=String(pShip.sName)
	pShip.Node.SetName(pShip.sName)
	pShip.Node.SetDisplayName(pString)

	## Reconfirm affiliation
	pFriendlies = GetGame().GetMission().GetFriendlyGroup()
	pFriendlies.AddName(pShip.sName)

	## Another thing to swap... Dock Slots at the Starbase
	pHolder = pPlayer.GetHolder()
	if pHolder.IsTypeOf(STARBASE):
		pHolder.SwapSlots(pPlayer,pShip)	
	
	## Change the bridge type of the ship	
	pShip.GetBridge().sBridgeType = sPlayerBridge
	
	## Make the new bridge
	import LoadBridge	
	LoadBridge.Load(sBridgeType + 'Bridge')

	## Resynchronise
	import ATP_Bridge
	ATP_Bridge.SynchroniseWithGame(sShipBridge)

	import ATP_Characters
	ATP_Characters.SynchroniseWithGame()

	## Enter that bridge
	GetCameraManager().EnterBridge()
