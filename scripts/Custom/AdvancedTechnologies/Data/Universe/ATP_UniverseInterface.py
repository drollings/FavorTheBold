from ATP_Object import *

class MenuInterface:
	StaticMenus = { }

	def __init__(self,sName='',pParent=None,sDisplayName=''):
		## Our name
		if not sName:
			sName = 'MenuInterface ' + str(self.ID)
		if not sDisplayName:
			sDisplayName = sName		
		self.sName = sName
		self.sDisplayName = sDisplayName
	
		## Dictionary with all children
		self.dChildren = {}

		## Our new node
		self.Node = App.STMenu_Create(self.sDisplayName)
		self.Node.SetNotOpenable()

		## Our pParent
		if pParent:
			self.pParent = pParent
			pParent.AddChild(self)
		else:
			self.pParent = None			

	def GetNode(self):
		return self.Node

	def delete(self):
		## Delete the children
		for sKey in self.dChildren.keys():
			pChild = self.dChildren[sKey]
			pChild.delete()
		self.dChildren = {}

		## Remove the node
		if self.pParent and self.Node:
			if self.pParent.Node:
				self.pParent.Node.RemoveChild(self.Node)
		self.Node = None

		## Remove us from our pParent
		if self.pParent:
			self.pParent.RemoveChild(self)

	def DeleteAllChildren(self):
		## Delete the children
		for sKey in self.dChildren.keys():
			pChild = self.dChildren[sKey]
			pChild.delete()
		self.dChildren = {}		

	def AddChild(self,pChild):
		## Does it already exists ?
		if self.dChildren.has_key(pChild.sName):
			self.dChildren[pChild.sName].delete()

		## Add it to our dict
		self.dChildren[pChild.sName] = pChild

		## Allow to open it
		try:
			self.Node.SetOpenable()
		except AttributeError:
			pass

		## Add it in a game
		if self.Node and pChild.Node:
			self.Node.AddChild(pChild.Node)

		## Set us as pParent
		pChild.pParent = self

	def RemoveChild(self,pChild):
		## Remove it from the dict
		if self.dChildren.has_key(pChild.sName):
			del self.dChildren[pChild.sName]

		## Forget me, child...
		pChild.pParent = None

		## Children left ?
		if not self.dChildren:
			## Don't open it
			try:
				self.Node.SetNotOpenable()
			except AttributeError:
				pass
	def Close(self):
		## Ourself
		try:
			self.Node.Close()
			self.Node.ClearClickedOnce()
		except AttributeError:
			pass

	def FullClose(self):
		## Ourself
		try:
			self.Node.Close()
			self.Node.ClearClickedOnce()	
		except AttributeError:
			pass

		## Our children
		for sKey in self.dChildren.keys():
			self.dChildren[sKey].FullClose()

	def HasChildren(self):
		return len(self.dChildren.keys())		 			

	def GetInterface(self,sName):
		if self.dChildren.has_key(sName):
			return self.dChildren[sName]
		return None


class ButtonInterface:

	def __init__(self,sName='',iObjectID=0,pParent=None,oEventType=None,fWidth=0.0,fHeight=0.0,sDisplayName=''):
		## Our name
		if not sName:
			sName = 'ButtonInterface ' + str(self.ID)
		if not sDisplayName:
			sDisplayName = sName		
		self.sName = sName
		self.sDisplayName = sDisplayName

		## A eventtype
		if not oEventType:
			self.eClickEvent = GetNextEventType()
		else:
			self.eClickEvent = oEventType

		## Object ID to call with
		self.iObjectID = iObjectID

		## Linked event
		self.pClickEvent = App.TGIntEvent_Create()
    		self.pClickEvent.SetEventType(self.eClickEvent)
   		self.pClickEvent.SetInt(self.iObjectID)   		

		## Our new node
		if fWidth*fHeight == 0.0:
			self.Node = App.STButton_Create(self.sDisplayName,self.pClickEvent)
		else:
			self.Node = App.STRoundedButton_Create(self.sDisplayName,self.pClickEvent,fWidth,fHeight)

		## Our pParent
		if pParent:
			pParent.AddChild(self)
		else:
			self.pParent = None

	def SetHeight(self,f):
		self.Node.SetHeight(f)
	
	def SetWidth(self,f):
		self.Node.SetWidth(f)	

	def GetNode(self):
		return self.Node

	def GetClickEvent(self):
		return self.pClickEvent

	def GetClickEventInt(self):
		return self.pClickEvent
	
	def GetClickEventType(self):
		return self.eClickEvent

	def Close(self):
		self.Node.SetChosen(FALSE)

	def FullClose(self):
		self.Node.SetChosen(FALSE)

	def delete(self):
		## Remove the node
		if self.pParent and self.Node:
			if self.pParent.Node:
				self.pParent.Node.RemoveChild(self.Node)
		self.Node = None

		## Remove us from our pParent
		if self.pParent:
			self.pParent.RemoveChild(self)

def GetInterface(sMenu):
	if MenuInterface.StaticMenus.has_key(sMenu):
		return  MenuInterface.StaticMenus[sMenu]
	return None


def SynchroniseWithGame():
	## Game data
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if not pDatabase:
		return

	## Create a class for each character menu
	for sMenu in ('Helm','Tactical','Commander','Science','Engineering'):
		pMenu = MenuInterface(sMenu)
		pMenu.Node = pTactCtrlWindow.FindMenu(pDatabase.GetString(sMenu))
		MenuInterface.StaticMenus[sMenu] = pMenu

	## Remove some buttons
	for sDatabase,sMenu,oButtons in (	('data/TGL/Bridge Menus.tgl',
						 'Helm',
						 ('Intercept','Hail','Nav Points','Warp','Set Course','Orbit Planet','Dock','All Stop')),
			
						('data/TGL/QuickBattle/QuickBattle.tgl',
						 'Commander',
						 ('QuickBattle Configuration','Start Simulation','End Simulation'))
			
				
																):
		ppDatabase = App.g_kLocalizationManager.Load(sDatabase)
		pMenu = MenuInterface.StaticMenus[sMenu].Node

		for sButton in oButtons:
			pButton = pMenu.GetButtonW(ppDatabase.GetString(sButton))
			if pButton:
				pButton.SetNotVisible()
			else:
				pButton = pMenu.GetSubmenuW(ppDatabase.GetString(sButton))
				if pButton:
					pButton.SetNotVisible()

		App.g_kLocalizationManager.Unload(ppDatabase)


class InterstellarInterface(ATP_EventHandlerObject):

	def __init__(self,ID=0):
		## Superclass
		ATP_EventHandlerObject.__init__(self,INTERSTELLAR_INTERFACE_ID)

		## Attrs
		self.pTarget = None
		self.bMoveLock = FALSE
		self.SourceQueue = []
		self.iMaxQueue = 5
		self.lWormholes = []

		## Events
		self.ET_WORMHOLE = GetNextEventType()

		## Handlers
		self.AddHandler(self.ET_WORMHOLE ,  'EnterWormhole' )

		## Create the menus
		pStellarMenu = MenuInterface('Interstellar Interface', GetInterface('Helm'))

		## Create the open button for the Starcharts
		pButton = ButtonInterface( 'Interstellar Database' , 0 , pStellarMenu )
		GetStarCharts().AddHandler( pButton.GetClickEventType() , 'open' )

		## A select button
		pMenu = MenuInterface('Set Course',pStellarMenu)
		
		## Add the current system to the menu
		pPlayerSolar = GetPlayerFleet().GetSolar()
		self.AddSystem(None,pPlayerSolar)
	
		## Disable it
		pMenu.GetInterface(pPlayerSolar.sName).Node.SetDisabled()
				
		## A warpbutton
		#pButton = WarpButtonInterface('Warp',pStellarMenu)
		pButton = ButtonInterface('Warp',0,pStellarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler( pButton.GetClickEventType(),'Warp')

		## A dewarpbutton
		pButton = ButtonInterface('Drop to impulse',0,pStellarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler( pButton.GetClickEventType(),'Impulse')

		## Handlers
		pStarcharts = GetStarCharts()
		self.AddHandler( pStarcharts.GetAddToNavigationEvent() , 'AddSystem' )
		# self.AddHandler( GetPlayerFleet().GetStateStartEvent(NORMAL) , 'PlayerNormal' )
		self.AddHandler( GetPlayerFleet().GetStateDoneEvent(WARPING) , 'PlayerNormal' )
		self.AddHandler( GetPlayerFleet().GetStateDoneEvent(NORMAL) ,  'PlayerNotNormal' )

		## Forca player normal
		self.PlayerNormal(None)

	def AddSystem(self,gEvent,pSolar=None):
		if not pSolar:
			pEvent = DecodeEvent(gEvent)
			pSolar = pEvent.GetSource()
		
		## Menus
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
		pCourseMenu = pStellarMenu.GetInterface('Set Course')
		
		## List of current solars
		if self.SourceQueue.count(pSolar.ID):
			## Already here
			self.SourceQueue.remove(pSolar.ID)
			self.SourceQueue.append(pSolar.ID)
			
			## Reactivate the button
			pCourseMenu.GetInterface(pSolar.sName).Node.SetEnabled()			
		else:
			## New system

			## Too full ?
			iLen = len(self.SourceQueue)
			if  iLen >= self.iMaxQueue and iLen:
				## Remove one
				SolarID = self.SourceQueue.pop(0)
				pDropSolar = GetByID(SolarID)
				pButton = pCourseMenu.GetInterface(pDropSolar.sName)
				if pButton:
					self.RemoveHandler(pButton.GetClickEventType(),'SetCourse')
					pButton.delete()

			## New entry
			pButton = ButtonInterface(pSolar.sName,pSolar.ID,pCourseMenu)
			self.AddHandler(pButton.GetClickEventType(),'SetCourse')

			## Append
			self.SourceQueue.append(pSolar.ID)

		## Close the course button
		pCourseMenu.FullClose()

	def SetCourse(self,gEvent):
		## Linked object ?
		pSolar = GetByID(gEvent.GetInt())
		if not pSolar:
			return
		
		## Stellar menu
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')

		## Course menu
		pCourseMenu = pStellarMenu.GetInterface('Set Course')

		## Already course set to that location
		if pSolar == self.pTarget:
			## Close the menu
			pCourseMenu.FullClose()
			return

		## Remember
		self.pTarget = pSolar

		## May we allow warp ?
		if not self.bMoveLock:			
			pWarp = pStellarMenu.GetInterface('Warp')
			pWarp.Node.SetEnabled()			

		## Make Kiska speak
		lsLine = ( 'gh074' , 'KiskaPlottedCourse' , 'gh075' )
		sLine = self.GetRandomItem(lsLine)
		GetPlayerBridge().GetHelm().Speak(sLine)

		## Close the menu
		pCourseMenu.FullClose()
	
	def Warp(self,gEvent):
		## Destination
		pSolar = self.pTarget

		## Add the old system to the menu
		pPlayerSolar = GetPlayerFleet().GetSolar()
		self.AddSystem(None,pPlayerSolar)		
		
		## Stellar Menu
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
		
		## Disable the setcourse button
		pCourseMenu = pStellarMenu.GetInterface('Set Course')
		pCourseMenu.Node.SetDisabled()		

		## Disable the warp button
		pWarp = pStellarMenu.GetInterface('Warp')
		pWarp.Node.SetDisabled()

		## Allow the drop to impulse button
		pWarp = pStellarMenu.GetInterface('Drop to impulse')
		pWarp.Node.SetEnabled()

		## Full close
		pStellarMenu.FullClose()
	
		## Forget target
		self.pTarget = None	

		## Render the target system		
		pSolar.RenderAndRandomise()

		## Camera
		GetCameraManager().StartPlayerWarp()
		
		## Voyage...
		GetPlayerFleet().Voyage(pSolar)		

	# def Impulse(self,gEvent):
	#	import ATP_WarpSequence
	#
	#	## Get the warpsequence and abort it
	#	for pShip in GetPlayerFleet().GetShips():
	#		ATP_WarpSequence.DropToImpulse(pShip)
	#		
	#	## Full close
	#	pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
	#	pStellarMenu.FullClose()

	def PlayerNotNormal(self,gEvent):
		## Disable us
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
		pWarp = pStellarMenu.GetInterface('Warp')
		pWarp.Node.SetDisabled()

	def PlayerNormal(self,gEvent):
		## Stellar menu
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')

		## Reactivate the set course menu
		pCourseMenu = pStellarMenu.GetInterface('Set Course')
		pCourseMenu.Node.SetEnabled()
		
		## Disable the current system
		pSolar = GetPlayerFleet().GetSolar()
		pButton = pCourseMenu.GetInterface(pSolar.sName)
		if pButton:
			pButton.Node.SetDisabled()
		
		## Enable the warp button if there is a target
		if self.pTarget:
			pWarp = pStellarMenu.GetInterface('Warp')
			pWarp.Node.SetEnabled()

		## Disable drop to impulse
		pWarp = pStellarMenu.GetInterface('Drop to impulse')
		pWarp.Node.SetDisabled()

		## Remove the old wormholes
		for iWormhole in self.lWormholes:
			## Get the wormhole
			pWormhole = GetByID(iWormhole)
			if not pWormhole:
				continue

			## Get the button
			pButton = pStellarMenu.GetInterface('Enter ' + pWormhole.GetWormhole().GetName())
			if not pButton:
				continue
			
			## Delete it
			pButton.delete()
		self.lWormholes = []

		## Any wormholes ?
		lWormholes = pSolar.GetAllSolarWormholes()
		for pWormhole in lWormholes:
			## Add it
			self.lWormholes.append(pWormhole.ID)
			
			## Button
			pButton = ButtonInterface('Enter ' + pWormhole.GetWormhole().GetName(),pWormhole.ID,pStellarMenu,self.ET_WORMHOLE)

		## Unlock
		self.Unlock()
		pInterface = GetSolarInterface()
		if pInterface:
			pInterface.Unlock()

	def EnterWormhole(self,gEvent):
		## Data
		ID = gEvent.GetInt()

		## Wormhole
		pWormhole = GetByID(ID)
		if not pWormhole:
			return
		if not pWormhole.IsTypeOf(SUBWORMHOLE):
			return

		## Add the old system to the menu
		pPlayerSolar = GetPlayerFleet().GetSolar()
		self.AddSystem(None,pPlayerSolar)

		## Stellar menu
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')

		## Get the button
		pButton = pStellarMenu.GetInterface('Enter ' + pWormhole.GetWormhole().GetName())
	
		## Disable it
		pButton.Node.SetDisabled()

		## Target solar
		pSolar = pWormhole.GetOppositeSolar()
		pSolar.RenderAndRandomise()

		## Render the target system		
		pSolar.RenderAndRandomise()

		## The voyage function should select to take the wormhole
		GetPlayerFleet().Voyage( pSolar ,bInside = FALSE )

		## Lock the solar interface and ourself
		self.Lock()
		pInterface = GetSolarInterface()
		if pInterface:
			pInterface.Lock()		
		

	def Lock(self):
		## Lock...
		self.bMoveLock = TRUE

		## Disable us
		pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
		pWarp = pStellarMenu.GetInterface('Warp')
		pWarp.Node.SetDisabled()

	def Unlock(self):
		## Unlock
		self.bMoveLock = FALSE

		## Enable us
		if self.pTarget:
			pStellarMenu = GetInterface('Helm').GetInterface('Interstellar Interface')
			pWarp = pStellarMenu.GetInterface('Warp')
			pWarp.Node.SetEnabled()			
		

class SystemInterface(ATP_EventHandlerObject):
	
	NO_SERVICE 	= 0
	REPAIR 		= 1
	HEAVY_REPAIR 	= 2
	TRANSFER 	= 3
	
	def __init__(self,ID=0):
		## Superclass
		ATP_EventHandlerObject.__init__(self,SOLAR_INTERFACE_ID)

		## Attrs
		self.bMoveLock = FALSE
		self.iService = SystemInterface.NO_SERVICE

		## Event
		self.ET_SELECT = GetNextEventType()

		## Handlers for refresh
		pPlayer = GetPlayerShip()
		self.AddHandler(pPlayer.GetStateStartEvent(WARPING) , 'update_before_warp' )
		self.AddHandler(pPlayer.GetStateDoneEvent(WARPING)  , 'update_after_warp' )

		## Create a menu at Kiska
		pSolarMenu = MenuInterface('Solar Interface', GetInterface('Helm'))
			
		## Some submenus
		pIntercept = MenuInterface('Select', pSolarMenu)
		if pIntercept:
			for sMenu in ('Planets','Fleets','Stations','Suns','Phenomena','Comets'):
				pMenu = MenuInterface(sMenu, pIntercept)

		### Planet options
		pPlanets = pIntercept.GetInterface('Planets')
		pMenu = MenuInterface('Inhabited'   , pPlanets )
		pMenu = MenuInterface('Uninhabited' , pPlanets )

		## Various actions
		pButton = ButtonInterface('Contact',0,pSolarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType() ,'Contact')

		pButton = ButtonInterface('Intercept',0,pSolarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType() ,'Intercept')

		pButton = ButtonInterface('Orbit',0,pSolarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'Orbit')

		pButton = ButtonInterface('Dock',0,pSolarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'Dock')

		pButton = ButtonInterface('Undock',0,pSolarMenu)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'Undock')		

		pFacilities = MenuInterface('Services', pSolarMenu)
		pButton = ButtonInterface('Advanced Repair',SystemInterface.HEAVY_REPAIR,pFacilities)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'ServiceButtonPressed')
		pButton = ButtonInterface('Repair',SystemInterface.REPAIR,pFacilities)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'ServiceButtonPressed')
		pButton = ButtonInterface('Transfer Command',SystemInterface.TRANSFER,pFacilities)
		pButton.Node.SetDisabled()
		self.AddHandler(pButton.GetClickEventType(),'ServiceButtonPressed')
		pFacilities.Node.SetDisabled()		

		## Forced update
		self.update_after_warp(None)
		

	# def exit_game_delete(self):
	#	## Delete the menu	
	#	pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')
	#	pSolarMenu.delete()
		

	def update_before_warp(self,gEvent):
		## Disable the button
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')
		pSolarMenu.FullClose()
		pSolarMenu.Node.SetDisabled()

	def update_after_warp(self,gEvent):
		#debug('begin update_after_warp')

		## Remove the old handlers
		self.PurgeHandlers()		

		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		## Analyse the new system
		pSolar = GetPlayerShip().GetSolar()

		## Target menu
		pIntercept = pSolarMenu.GetInterface('Select')
		
		## Various targets
		pPlanets = pIntercept.GetInterface('Planets')
		pInh = pPlanets.GetInterface('Inhabited')
		pInh.DeleteAllChildren()
		pUnh = pPlanets.GetInterface('Uninhabited')
		pUnh.DeleteAllChildren()
		pFleets = pIntercept.GetInterface('Fleets')
		pFleets.DeleteAllChildren()	
		pSuns = pIntercept.GetInterface('Suns')
		pSuns.DeleteAllChildren()
		pFacs = pIntercept.GetInterface('Stations')
		pFacs.DeleteAllChildren()
		pComets = pIntercept.GetInterface('Comets')
		pComets.DeleteAllChildren()
		pPhenomena = pIntercept.GetInterface('Phenomena')
		pPhenomena.DeleteAllChildren()

		for pPlanet in pSolar.GetAllPlanets():
			if pPlanet.IsExactTypeOf(PLANET):
				if pPlanet.GetPop():
					pSubMenu = MenuInterface(pPlanet.sName,pInh)
				else:
					pSubMenu = MenuInterface(pPlanet.sName,pUnh)
				pButton = ButtonInterface(pPlanet.sName,pPlanet.ID,pSubMenu,self.ET_SELECT)
				#self.AddHandler(pButton.GetClickEventType() ,'Select' )
				for pMoon in pPlanet.GetMoons():
					pButton = ButtonInterface(pMoon.sName,pMoon.ID,pSubMenu,self.ET_SELECT)
					#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		for pFleet in pSolar.GetAllFleets():
			if pFleet.State == WARPING and pFleet.ID != PLAYER_FLEET_ID:
				continue
			
			pMenu = MenuInterface(pFleet.sName,pFleets)

			for pShip in pFleet.GetShips():
				if pShip.ID != PLAYER_SHIP_ID:
					pButton = ButtonInterface(pShip.sName,pShip.ID,pMenu,self.ET_SELECT)
					#self.AddHandler(pButton.GetClickEventType() ,'Select' )		

		for pSun in pSolar.GetAllSuns():
			pWay = pSun.GetDirectChildByName(pSun.sName)
			if pWay:
				pButton = ButtonInterface(pSun.sName,pWay.ID,pSuns,self.ET_SELECT)
				#self.AddHandler(pButton.GetClickEventType() ,'Select' )
			else:
				print 'Odd...'
				print str(pSun.Children)

		for pFac in pSolar.GetAllShips():
			if not pFac.IsStationary():
				continue
			pButton = ButtonInterface(pFac.sName,pFac.ID,pFacs,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType()	,'Select' )
					
		for pComet in pSolar.GetAllComets():
			pButton = ButtonInterface(pComet.sName,pComet.ID,pComets,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		for pHole in pSolar.GetAllSolarWormholes() + pSolar.GetAllBlackholes():
			pButton = ButtonInterface(pHole.sName,pHole.ID,pPhenomena,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		## Reenable the menu
		pSolarMenu.Node.SetEnabled()

		## No target
		self.pTarget = None
		
		## Handlers for refresh
		pPlayer = GetPlayerShip()
		self.AddHandler(pPlayer.GetStateStartEvent(WARPING)	,'update_before_warp' )
		self.AddHandler(pPlayer.GetStateDoneEvent(WARPING)	,'update_after_warp'  )

		self.AddHandler(pSolar.GetFleetWarpOutEvent()		,'fleet_warp_out'   )
		self.AddHandler(pSolar.GetFleetWarpInEvent()		,'fleet_warp_in'    )		
		self.AddHandler(pSolar.GetObjectDestroyedEvent()	,'object_destroyed' )
		self.AddHandler(pSolar.GetObjectCreationEvent()		,'object_creation'  )

		self.AddHandler(App.ET_TARGET_WAS_CHANGED		, 'SetTarget'	)
		self.AddHandler(self.ET_SELECT				, 'Select'	)

		#debug('end update_after_warp')

		## Player inside ?
		if GetPlayerFleet().State == INSIDE:
			self.StartDocked()

	def fleet_warp_out(self,gEvent):
		pEvent = DecodeEvent(gEvent)
		pFleet = pEvent.GetSource()
		if not pFleet:
			return
		if pFleet.ID == PLAYER_FLEET_ID:
			return
		
		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		## Fleetinvolved
		pFleetMenu = pSolarMenu.GetInterface('Select').GetInterface('Fleets').GetInterface(pFleet.sName)
		if pFleetMenu:
			pFleetMenu.delete()
		
	def fleet_warp_in(self,gEvent):
		pEvent = DecodeEvent(gEvent)
		pFleet = pEvent.GetSource()
		if not pFleet:
			return
		if pFleet.ID == PLAYER_FLEET_ID:
			return
		
		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')
		pFleetMenu = pSolarMenu.GetInterface('Select').GetInterface('Fleets')
		pMenu = MenuInterface(pFleet.sName,pFleetMenu)		

		for pShip in pFleet.GetShips():
			pButton = ButtonInterface(pShip.sName,pShip.ID,pMenu)
			self.AddHandler(pButton.GetClickEventType() ,'Select' )

	def object_destroyed(self,gEvent):
		pEvent = DecodeEvent(gEvent)
		pObj = pEvent.GetSource()
		if not pObj:
			return

		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		if pObj.IsTypeOf(SHIP):
			pFleet = pObj.GetFleet()
			pFleetMenu = pSolarMenu.GetInterface('Select').GetInterface('Fleets')
			pMenu = pFleetMenu.GetInterface(pFleet.sName)
			if pMenu:
				pMenu = pMenu.GetInterface(pObj.sName)
				if pMenu:
					pMenu.delete()
		
		if pObj.IsTypeOf(FLEET):
			pFleetMenu = pSolarMenu.GetInterface('Select').GetInterface('Fleets')
			pMenu = pFleetMenu.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()

		if pObj.IsTypeOf(STARBASE) or pObj.IsTypeOf(SHIPYARD):
			pFacMenu = pSolarMenu.GetInterface('Select').GetInterface('Stations')
			pMenu = pFacMenu.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()

		if pObj.IsExactTypeOf(PLANET):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Planets')
			if not pObj.GetPop():
				pPlanets = pPlanets.GetInterface('Uninhabited')
			else:
				pPlanets = pPlanets.GetInterface('Inhabited')

			pMenu = pPlanets.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()

		if pObj.IsExactTypeOf(MOON):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Planets')
			pPlanet = pObj.GetHolder()
			if not pPlanet.GetPop():
				pPlanets = pPlanets.GetInterface('Uninhabited')
			else:
				pPlanets = pPlanets.GetInterface('Inhabited')

			pMenu = pPlanets.GetInterface(pObj.GetHolder().sName)
			if pMenu:
				pMenu = pMenu.GetInterface(pObj.sName)
				if pMenu:
					pMenu.delete()

		if pObj.IsTypeOf(COMET):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Comets')
			pMenu = pPlanets.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()

		if pObj.IsTypeOf(WAYPOINT):
			pSuns = pSolarMenu.GetInterface('Select').GetInterface('Suns')
			pMenu = pSuns.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()

		if pObj.IsTypeOf(BLACKHOLE) or pObj.IsTypeOf(SUBWORMHOLE):
			pSuns = pSolarMenu.GetInterface('Select').GetInterface('Phenomena')
			pMenu = pSuns.GetInterface(pObj.sName)
			if pMenu:
				pMenu.delete()	

	def object_creation(self,gEvent):
		pEvent = DecodeEvent(gEvent)
		pObj = pEvent.GetSource()
		if not pObj:
			return

		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		if pObj.IsTypeOf(SHIP):
			pFleet = pObj.GetFleet()
			pFleetMenu = pSolarMenu.GetInterface('Select').GetInterface('Fleets')
			pMenu = MenuInterface(pFleet.sName,pFleetMenu)
			pButton = ButtonInterface(pObj.sName,pObj.ID,pMenu,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsTypeOf(STARBASE) or pObj.IsTypeOf(SHIPYARD):
			pFacMenu = pSolarMenu.GetInterface('Select').GetInterface('Stations')
			pButton = ButtonInterface(pObj.sName,pObj.ID,pFacMenu,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsExactTypeOf(PLANET):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Planets')
			if not pObj.GetPop():
				pPlanets = pPlanets.GetInterface('Uninhabited')
			else:
				pPlanets = pPlanets.GetInterface('Inhabited')

			pButton = ButtonInterface(pObj.sName,pObj.ID,pPlanets,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsExactTypeOf(MOON):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Planets')
			pPlanet = pObj.GetHolder()
			if not pPlanet.GetPop():
				pPlanets = pPlanets.GetInterface('Uninhabited')
			else:
				pPlanets = pPlanets.GetInterface('Inhabited')

			pMenu = pPlanets.GetInterface(pObj.GetHolder().sName)
			if pMenu:
				pButton = ButtonInterface(pObj.sName,pObj.ID,pMenu,self.ET_SELECT)
				#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsTypeOf(COMET):
			pPlanets = pSolarMenu.GetInterface('Select').GetInterface('Comets')
			pButton = ButtonInterface(pObj.sName,pObj.ID,pPlanets,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsTypeOf(WAYPOINT):
			pSuns = pSolarMenu.GetInterface('Select').GetInterface('Suns')
			pButton = ButtonInterface(pObj.sName,pObj.ID,pSuns,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )

		if pObj.IsTypeOf(BLACKHOLE) or pObj.IsTypeOf(SUBWORMHOLE):
			pSuns = pSolarMenu.GetInterface('Select').GetInterface('Phenomena')
			pButton = ButtonInterface(pObj.sName,pObj.ID,pSuns,self.ET_SELECT)
			#self.AddHandler(pButton.GetClickEventType() ,'Select' )
		

	def Select(self,gEvent):
		## Linked object ?
		pObject = GetByID(gEvent.GetInt())
		if not pObject:
			return
		if not pObject.IsTypeOf(UNIVERSE_ELEMENT):
			return
		if not pObject.Node:
			return
		
		## Kiska ACK
		GetPlayerBridge().GetHelm().SayYes()

		## Close it
		GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Select').FullClose()

		## Set the target at the helm
		try:
			s = pObject.Node.GetName()
			if s:
				GetPlayerShip().Node.SetTarget(s)
		except:
			pass

	def SetTarget(self,gEvent,pObject=None):
		if not pObject:
			if gEvent:
				pShip = GetByNode(App.ShipClass_Cast(gEvent.GetDestination()))
				if not pShip:
					return
				if pShip.ID != PLAYER_SHIP_ID:
					return
				pTarget = GetPlayerShip().Node.GetTarget()
				pObject = GetByNode(pTarget)
				
		## Close it
		GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Select').FullClose()

		## Disable all
		self.DisableAllActionButtons()

		## Disable the services in normal mode
		if not self.bMoveLock:
			self.DisableServiceButtons()

		## An empty object disables all
		if not pObject:
			return

		## Depending on the type of object we enable a certain menu
		if pObject.IsTypeOf(PLANET):
			if not self.bMoveLock:
				self.EnableActionButton('Intercept')
				self.EnableActionButton('Orbit')

		if pObject.IsTypeOf(SUN) or pObject.IsTypeOf(WAYPOINT):
			if not self.bMoveLock:
				self.EnableActionButton('Intercept')

		if pObject.IsTypeOf(SHIP):
			self.EnableActionButton('Contact')
			if not self.bMoveLock:
				self.EnableActionButton('Intercept')
				self.EnableActionButton('Orbit')
			if pObject.IsDockable():
				if not self.bMoveLock:
					self.EnableActionButton('Dock')

		if pObject.IsTypeOf(STARBASE) or pObject.IsTypeOf(SHIPYARD):
			if not self.bMoveLock:
				self.EnableServiceButtons(pObject)

		if pObject.IsTypeOf(COMET):
			if not self.bMoveLock:
				self.EnableActionButton('Intercept')

		if pObject.IsTypeOf(BLACKHOLE):
			pass

		if pObject.IsTypeOf(SUBWORMHOLE):
			pass

		## Remember our target
		self.pTarget = pObject

	def Intercept(self,gEvent):
		## Our target
		GetPlayerFleet().Intercept(self.pTarget)

	def Contact(self,gEvent):
		## Our target
		pTarget = self.pTarget
	
		## Hail it
		pTarget.Contact()

	def Dock(self,gEvent=None):
		## Playerfleet
		pFleet = GetPlayerFleet()

		## Our target
		pTarget = self.pTarget

		## Error handling
		self.AddHandler(pFleet.GetStateStartEvent(VOYAGE_ERROR),'AbortDock')

		## Voyage to it
		iACK = GetPlayerFleet().Voyage(pTarget,bInside=TRUE)

		if iACK == ACK:
			## Lock movements
			self.Lock()

			## Handlers to unlock
			self.AddHandler(GetPlayerFleet().GetStateDoneEvent(ENTERING), 'EnterDone')
	
			## Recalculate the targetbuttons
			self.SetTarget(None,self.pTarget)

		## Disable the service button
		self.DisableServiceButtons()
			
		## Return result
		return iACK
	
	def StartDocked(self):
		## Lock movements
		self.Lock()

		## Recalculate the targetbuttons
		self.SetTarget(None,self.pTarget)
	
		## Enable service buttons
		self.EnableServiceButtons(GetPlayerFleet().GetHolder())

		## Enable undock
		pButton = GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Undock')
		self.AddHandler(pButton.GetClickEventType(),'Undock')
		pButton.Node.SetEnabled()

	def AbortDock(self,gEvent):
		pass

	def EnterDone(self,gEvent):
		## Remove the handler
		self.RemoveHandler(gEvent.GetEventType(),'EnterDone')

		## Enable undock
		pButton = GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Undock')
		self.AddHandler(pButton.GetClickEventType(),'Undock')	
		pButton.Node.SetEnabled()

		## Service present?
		self.Service()

	def ServiceButtonPressed(self,gEvent):
		## What service?
		self.iService = gEvent.GetInt()

		## Disable the service button
		self.DisableServiceButtons()

		## Close the menu
		GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Services').FullClose()

		## Playerfleet
		pFleet = GetPlayerFleet()

		## Where are we?
		if pFleet.State == INSIDE:
			## Already in...
			self.Service()

		else:
			## Dock
			self.Dock()

	def Service(self):
		## Playerfleet
		pFleet = GetPlayerFleet()

		## Base providing services
		pHolder = pFleet.GetHolder()

		## Actions
		if self.iService == SystemInterface.NO_SERVICE:
			self.EnableServiceButtons(pHolder)

		elif self.iService == SystemInterface.REPAIR:
			self.DisableServiceButtons()
			self.AddHandler(pFleet.GetStateDoneEvent(REPAIR),'ServiceDone')
			pHolder.Repair(pFleet)
			
		elif self.iService == SystemInterface.HEAVY_REPAIR:
			self.DisableServiceButtons()
			self.AddHandler(pFleet.GetStateDoneEvent(REPAIR),'ServiceDone')
			pHolder.HeavyRepair(pFleet)
			
		elif self.iService == SystemInterface.TRANSFER:
			## Activate the swap
			import ATP_Actions
			ATP_Actions.SwapPlayer()
			
			## Internal things
			self.EnableServiceButtons(pHolder)
			self.iService = SystemInterface.NO_SERVICE

			## Full Close
			GetInterface('Helm').GetInterface('Solar Interface').FullClose()
			GetInterface('Helm').GetInterface('Interstellar Interface').FullClose()

			## Rebuild a menu part
			self.RebuildPlayerFleetMenu()

	def ServiceDone(self,gEvent=None):
		## Remove handler
		self.RemoveHandler(GetPlayerFleet().GetStateDoneEvent(REPAIR),'ServiceDone')

		## Clear the service
		self.iService = SystemInterface.NO_SERVICE

		## Base providing services
		pHolder = GetPlayerFleet().GetHolder()

		# Reactive the servicebuttons
		self.EnableServiceButtons(pHolder)

	def Undock(self,gEvent):
		pFleet = GetPlayerFleet()

		## If there is a service abort it
		if self.iService != SystemInterface.NO_SERVICE:
			## Send an abort signal
			pFleet.GetHolder().AbortService(pFleet)	

		## Handlers to unlock
		self.AddHandler(GetPlayerFleet().GetStateDoneEvent(EXITING), 'ExitDone')

		if pFleet.Voyage(pFleet.GetHolder(),bInside=FALSE) == ACK:
			## Enable undock
			pButton = GetInterface('Helm').GetInterface('Solar Interface').GetInterface('Undock')	
			pButton.Node.SetDisabled()
			
			## Disable the service buttons
			self.DisableServiceButtons()	

			## Recalculate the targetbuttons
			self.SetTarget(None,self.pTarget)				

	def ExitDone(self,gEvent):
		## Remove the handler
		self.RemoveHandler(gEvent.GetEventType(),'ExitDone')

		## Release the lock
		self.Unlock()		

	def DisableAllActionButtons(self):
		## Our menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		for sMenu in ('Contact','Intercept','Orbit','Dock'):
			pSolarMenu.GetInterface(sMenu).Node.SetDisabled()

	def EnableActionButton(self,sMenu):
		## Our menu
		pButton = GetInterface('Helm').GetInterface('Solar Interface').GetInterface(sMenu)
		pButton.Node.SetEnabled()		
		self.AddHandler(pButton.GetClickEventType(),sMenu)

	def DisableServiceButtons(self):
		## Our main menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		## Get Service Menu
		pServices = pSolarMenu.GetInterface('Services')

		## Close the menu
		pServices.FullClose()

		## Get Service Menu
		pServices.Node.SetDisabled()

		## Disable the buttons
		for sButton in ('Advanced Repair','Repair','Transfer Command'):
			pButton = pServices.GetInterface(sButton)
			pButton.Node.SetDisabled()			

	def EnableServiceButtons(self,pBase):
		## Our main menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		## Get Service Menu
		pServices = pSolarMenu.GetInterface('Services')

		## What services does the base give ?
		sActivate = ()
		if pBase.IsTypeOf(STARBASE):
			sActivate = ('Repair','Transfer Command')
		elif pBase.IsTypeOf(SHIPYARD):
			if pBase.IsRepairYard():
				sActivate = ('Advanced Repair',)		
		
		## Activate some buttons
		for sButton in sActivate:
			pButton = pServices.GetInterface(sButton)
			pButton.Node.SetEnabled()
			self.AddHandler(pButton.GetClickEventType(),'ServiceButtonPressed')
		
		## Enable the menu
		if sActivate:
			pServices.Node.SetEnabled()
		else:
			pServices.Node.SetDisabled()
	
	def Lock(self):
		## Lock movements
		self.bMoveLock = TRUE

		## Lock services
		self.DisableServiceButtons()
		
		## Recalculate the targetbuttons
		self.SetTarget(None,self.pTarget)

		## Lock the Interstellar interface aswell
		GetInterstellarInterface().Lock()

	def Unlock(self):
		## Lock movements
		self.bMoveLock = FALSE

		## Recalculate the targetbuttons
		self.SetTarget(None,self.pTarget)

		## Lock the Interstellar interface aswell
		GetInterstellarInterface().Unlock()

	def RebuildPlayerFleetMenu(self):
		## The playerfleet
		pFleet = GetPlayerFleet()

		## Our main menu
		pSolarMenu = GetInterface('Helm').GetInterface('Solar Interface')

		## Fleetmenu
		pFleets = pSolarMenu.GetInterface('Select').GetInterface('Fleets')
	
		## Get the playerfleet menu
		pPlayerFleetMenu = pFleets.GetInterface(pFleet.sName)

		## Remove it
		if pPlayerFleetMenu:
			pPlayerFleetMenu.delete()

		## Make a new one
		pPlayerFleetMenu = MenuInterface(pFleet.sName,pFleets)

		## Add the children
		for pShip in pFleet.GetShips():
			if pShip.ID != PLAYER_SHIP_ID:
				pButton = ButtonInterface(pShip.sName,pShip.ID,pPlayerFleetMenu)
				self.AddHandler(pButton.GetClickEventType() ,'Select' )
			
			

		

		
	
				
			
					

		
		