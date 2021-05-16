import App
import loadspacehelper	

from ATP_Object import *
from ATP_Extras	import *
from ATP_Vessels import *
from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

class Wormhole(UniverseElement):
	def __init__(self,ID=0):
		## Upper class
		UniverseElement.__init__(self,ID)

		## The common horizon
		self.Horizon = 0

		## The two parts
		self.FirstWormhole  = SubWormhole()
		self.SecondWormhole = SubWormhole()

		## Expansion specs
		self.fMaxScale		= 17.5
		self.fGrowth		= 0.20
		self.fInitialScale	= 0.10
		self.fScale		= self.fInitialScale

		## Events
		self.ET_ENTER = 0

	def Bind(self,sName,pSource,pDestination):
		self.sName = sName[:]
		self.FirstWormhole.Bind(sName+"_FIRST",self,pSource)
		self.SecondWormhole.Bind(sName+"_SECOND",self,pDestination)

	def SetHorizon(self,pHorizon):
		if not pHorizon:
			self.Horizon = 0
		else:
			self.Horizon = pHorizon.ID

	def GetHorizon(self):
		return GetByID(self.Horizon)
	
	def OpenWormhole(self):
		## A high speed clock
		self.AddClock("AnimateOpen",0.05)

		## Initial scale for the object
		self.fScale = self.fInitialScale
		for Node in (self.FirstWormhole.Nodes+self.SecondWormhole.Nodes):	
			Node.SetScale(self.fScale)

	def AnimateOpen(self,gEvent):
		## Clocktick
		self.fScale = self.fScale + self.fGrowth

		## Scale the models
		for Node in (self.FirstWormhole.Nodes+self.SecondWormhole.Nodes):
			Node.SetScale(self.fScale)

		## Overscale, stop
		if self.fScale > self.fMaxScale:
			pEvent = DecodeEvent(gEvent)
			self.RemoveClock("AnimateOpen",pEvent.GetEventID())

	def CloseWormhole(self):
		## A high speed clock
		self.AddClock("AnimateClose",0.05)

		## Initial scale for the object
		self.fScale = self.fMaxScale
		for Node in (self.FirstWormhole.Nodes+self.SecondWormhole.Nodes):
			Node.SetScale(self.fScale)

	def AnimateClose(self,gEvent):
		## Clocktick
		self.fScale = self.fScale - self.fGrowth

		## Scale the models
		for Node in (self.FirstWormhole.Nodes+self.SecondWormhole.Nodes):
			Node.SetScale(self.fScale)

		## Overscale, stop
		if self.fScale <= self.fInitialScale * 1.05:
			pEvent = DecodeEvent(gEvent)
			self.RemoveClock("AnimateClose",pEvent.GetEventID())

	def Unrender(self):
		pA = self.FirstWormhole.GetHolder()
		pB = self.SecondWormhole.GetHolder()
		if GetPlayerShip().IsConceptual(pA,pB):
			self.FirstWormhole.EffectiveUnrender()
			self.SecondWormhole.EffectiveUnrender()

	

class SubWormhole(UniverseElement):
	def __init__(self,ID=0):
		## Upper class
		UniverseElement.__init__(self,ID)

		### Gfx
		self.sGfx = "Dummy"
		self.lGfx = 	(	("Wormhole_Cone",	 0.5),
					("Wormhole_Helix1",	 2.0),
					("Wormhole_Helix2",	 2.0),
					("Wormhole_Outerring",	 -1.0)
				)

		## Data structs
		self.Nodes = []
		self.Queue = []
		
		## Eventtypes
		self.ET_WARP		= 0
		self.ET_END_MOVE	= 0

	def GetBrother(self):
		list = self.GetWormhole().GetChildren()
		for item in list:
			if item.ID != self.ID:
				return item

	def GetOppositeSolar(self):
		return self.GetBrother().GetSolar()

	def SetHorizon(self,pHorizon):
		self.GetWormhole().Horizon = pHorizon.ID

	def GetHorizon(self):
		return GetByID(self.GetWormhole().Horizon)	

	def Bind(self,sName,pFather,pHolder):
		## Binders
		self.SetName(sName)
		self.Migrate(pFather)
		self.Move(pHolder)				
	
	def Render(self,pSet):
		## Already rendered?
		if self.Node:	
			return

		## Data
		pHolder = self.GetHolder()
		assert pHolder	
		fDish = 0.0

		## Upperclass
		UniverseElement.Render(self,pSet)

		## System
		pSolar = pHolder.GetSolar()
		pSet   = pSolar.Node
		if not pSet:
			pSolar.Setup()	
			pSet = pSolar.Node	

		## Our father
		pFather = self.GetWormhole()

		## Creation
		## The controller waypoint
		F = copyVector(eY)
		F.Scale(-1.0)
		U = copyVector(eZ)		
		V = self.GetHolder().FindSuitablePosition(40.0*km,250.0*km)
		pWay = WaypointDummy(pSet,"TEMPPOINT",V,F,U)
						
		## A main container object				
		self.Node = loadspacehelper.CreateShip(self.sGfx,pSet,self.sGfx+"_"+str(self.ID),pWay.GetName())
		self.Node.SetInvincible(TRUE)
		App.DamageableObject_Cast(self.Node).SetCollisionsOn(FALSE)
		self.Node.SetScale(pFather.fInitialScale)
		#self.Node.SetTargetable(FALSE)
		self.SetPosition(V)
				
		## Register
		self.EnterNodeCache(self.Node)
		
		## Load the models
		for sGfx,fSpeed in self.lGfx:
			## Create the dishes
			pWormhole = loadspacehelper.CreateShip(sGfx,pSet,sGfx+"_"+str(self.ID),pWay.GetName())
			pWormhole.AlignToVectors(F,U)
			pWormhole.SetInvincible(TRUE)
			App.DamageableObject_Cast(pWormhole).SetCollisionsOn(FALSE)
			pWormhole.SetScale(pFather.fInitialScale)
			pWormhole.SetTranslate(V)
					
			## Attach it to the holder
			# self.Node.AttachObject(pWormhole)

			## Register
			self.Nodes.append(pWormhole)
			self.EnterNodeCache(pWormhole)
			fDish = max(pWormhole.GetRadius(),fDish)

			## Orient and move
			Z = Vector(0.0,fSpeed,0.0)
			pWormhole.SetAngularVelocity(Z,App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
			pWormhole.UpdateNodeOnly()

		## Disable collisions
		list = [self.Node] + self.Nodes
		for k in list:
			for l in list:
				k.EnableCollisionsWith(l,FALSE)

		## Make the waypoints
		self.MakeWaypoints(V,F,U)

		## Some handlers
		if not self.ET_WARP:
			self.ET_WARP = GetNextEventType()
		self.AddHandler(self.ET_WARP,"WormholeWarp")		

		if not self.ET_END_MOVE:
			self.ET_END_MOVE = GetNextEventType()
		self.AddHandler(self.ET_END_MOVE,"EndMove")

		## Lose the waypoint
		pWay.Destroy()
	
	def SetPosition(self,V):
		UniverseElement.SetPosition(self,V)
		
		## Subnodes
		for Node in self.Nodes:
			Node.SetTranslate(V)
			Node.UpdateNodeOnly()	

	def Unrender(self):
		self.GetWormhole().Unrender()

	def CheckedUnrender(self,gEvent):
		self.GetWormhole().CheckedUnrender(gEvent)

	def EffectiveUnrender(self):
		## Unrender all ships in our queues
		lShips = self.Queue
		for SID in lShips:
			pShip = GetByID(SID)
			if pShip:
				pShip.GetFleet().Unrender()

		self.Queue = []
		
		## Remove our nodes
		if self.Node:
			pSet = self.Node.GetContainingSet()
			if pSet:
				for Node in self.Nodes:			
					if Node.IsTypeOf(App.CT_BASE_OBJECT):
						pSet.RemoveObjectFromSet(Node.GetName())
						Node.SetDeleteMe(TRUE)
					pSet.RemoveObjectFromSet(self.Node.GetName())
					self.Node.SetDeleteMe(TRUE)
		self.Node = None
		self.Nodes = []

		## Some handlers
		self.RemoveHandler( self.ET_WARP		,"WormholeWarp"		)
		self.RemoveHandler( self.ET_END_MOVE		,"EndMove"		)
			
		## Upperclass
		UniverseElement.Unrender(self)

	## Dynamical Holder Methods
	###############################

	def WormholeFleet(self,pFleet):
		pBrother = self.GetBrother()
		if not self.Node:
			pFleet.WarpToSolar(pBrother.GetHolder())
		else:
			## Set the state to warping
			pFleet.SetState(WARPING)

			## Move the ships
			for pShip in pFleet.GetShips():
				self.WormholeShip(pShip)

			## Conceptual move
			pFleet.Move(pBrother.GetHolder())

		return ACK		
	
	def WormholeShip(self,pShip):
		## Fake the warp out
		gEvent, pEvent = pShip.FakeEvent(0,pShip,self.GetSolar())

		## Notify the ship & system
		pShip.WarpOut(gEvent)
		self.GetSolar().WarpOut(gEvent)

		## Garbage
		pEvent.delete()

		## Individual ships can ONLY do this when rendered
		assert self.Node and pShip.Node

		if not self.GetHorizon():
			## Accept it
			self.SetHorizon(pShip)
			self.EnterShip(pShip)

			## Open the wormhole
			self.GetWormhole().OpenWormhole()
		else:
			## Put it on hold
			self.Queue.append(pShip.ID)		

	def EnterShip(self,pShip):
		## Send the ship to the enter lane
		PlaceObjectByName(pShip.Node,self.GetChildByName("Enter_01").Node)

		## Force a centercheck update
		if pShip.ID == PLAYER_SHIP_ID:
			self.GetSolar().CenterCheck(None)

		## Disable collisions
		pShip.Node.SetInvincible(TRUE)
		App.DamageableObject_Cast(pShip.Node).SetCollisionsOn(FALSE)
		
		## Use AI to move
		### Targetpoint
		pWay = self.GetChildByName("Enter_02")

		debug("Sending "+pShip.sName+ "to the horizon")
	
		### AI
		pShip.AssignAI([AI_PATH+".ATP_DockAI",pWay,self,self.ET_WARP],TRUE)		

	def WormholeWarp(self,gEvent):
		## the Ship
		pShip = self.GetHorizon()

		## My brother
		pBrother = self.GetBrother()

		## Possible cam glitch, try this hack
		pTopWindow = App.TopWindow_GetTopWindow()
		bOnBridge = pTopWindow.IsBridgeVisible()
		if not bOnBridge:
			pTopWindow.ForceBridgeVisible()

		## Move it the other
		from Actions import ShipScriptActions
		ShipScriptActions.MoveBetweenSetsAction(None,pShip.Node.GetObjID(),pBrother.GetSolar().Node.GetName())

		## Restore cam
		if not bOnBridge: 
			pTopWindow.ForceTacticalVisible()

		## Render my brother to be sure...
		self.GetBrother().Render(None)

		## Send the ship to the exit lane
		PlaceObjectByName(pShip.Node,pBrother.GetChildByName("Exit_01").Node)

		## Targetpoint
		pWay = pBrother.GetChildByName("Exit_02")
	
		## AI
		pShip.AssignAI([AI_PATH+".ATP_DockAI",pWay,pBrother,pBrother.ET_END_MOVE],TRUE)	

	def EndMove(self,gEvent):
		## Release the ship
		pShip = self.GetHorizon()
		pShip.AssignAI()		
		
		## Fake the warp in
		gEvent, pEvent = self.FakeEvent(0,pShip,self.GetSolar())

		## Notify the ship & system
		pShip.WarpIn(gEvent)
		self.GetSolar().WarpIn(gEvent)

		## Garbage
		pEvent.delete()		

		## Reenable collisions
		# pShip.Node.SetInvincible(FALSE)
		# App.DamageableObject_Cast(pShip.Node).SetCollisionsOn(TRUE)

		## My brother
		pBrother = self.GetBrother()
		## My father
		pFather = self.GetWormhole()

		## A new ship
		if self.Queue:
			pNewShip = GetByID(self.Queue.pop(0))
			
			## Accept it
			pFather.SetHorizon(pNewShip)
			self.EnterShip(pNewShip)

		elif pBrother.Queue:
			pNewShip = GetByID(pBrother.Queue.pop(0))
			
			## Accept it
			pFather.SetHorizon(pNewShip)
			pBrother.EnterShip(pNewShip)

		else:
			## Nobody left, close the wormhole
			pFather.SetHorizon(None)
			pFather.CloseWormhole()

	def Randomise(self,type=UNIVERSE_ELEMENT,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		pass

	def MakeWaypoints(self,V,F,U):
		## Vars
		Va = copyVector(V)
		Vb = copyVector(V)
		Vc = copyVector(V)
		FF = copyVector(F)
		FF.Scale(30.0*km)		
		Vc.Add(FF)
		Vd = copyVector(Vc)

		FI = copyVector(F)
		FO = copyVector(F)
		FI.Scale(-1.0)
					
		## Waypoints
		pWay = Waypoint("Exit_01" ,self,Va,bAttach=FALSE,NavPoint=FALSE)
		pWay.Node.SetTranslate(Va)
		pWay.Node.AlignToVectors(FO,U)

		pWay = Waypoint("Enter_02",self,Vb,bAttach=FALSE,NavPoint=FALSE)
		pWay.Node.SetTranslate(Vb)
		pWay.Node.AlignToVectors(FI,U)

		pWay = Waypoint("Enter_01",self,Vc,bAttach=FALSE,NavPoint=FALSE)
		pWay.Node.SetTranslate(Vc)
		pWay.Node.AlignToVectors(FI,U)
	
		pWay = Waypoint("Exit_02" ,self,Vd,bAttach=FALSE,NavPoint=FALSE)
		pWay.Node.SetTranslate(Vd)
		pWay.Node.AlignToVectors(FO,U)

def PlaceObjectByName(Node,pWay):
	Node.SetTranslate(pWay.GetWorldLocation())
	Node.AlignToVectors(pWay.GetWorldForwardTG(),pWay.GetWorldUpTG())
	Node.UpdateNodeOnly()


	