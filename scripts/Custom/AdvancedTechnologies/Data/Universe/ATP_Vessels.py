import App
import math
import string
import loadspacehelper

from ATP_Object import *
from ATP_Extras import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

SOURCE = 1
DEST = 2

class Fleet(UniverseElement):
	INIT = 0
	DONE = 1000
	
	def __init__(self,ID=None):
		UniverseElement.__init__(self,ID)

		## Own data
		self.DestinationID = 0
		self.SourceID	   = 0
		
		self.fStay = 100.0
		self.lSpacelineDestinations = []		
		
		## Voyage control
		self.State  	 = NORMAL
		self.VoyageState = NORMAL
		self.bInside	 = FALSE

		## State changes
		self.StateToEventDict = {}

		## Cache
		self.Holder = None

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Fleet("+str(self.ID)+")")

		write_save_file("self.DestinationID	= "+str(self.DestinationID))
		write_save_file("self.SourceID		= "+str(self.SourceID))
		write_save_file("self.fStay		= "+str(self.fStay))
		
		## Upperclass
		UniverseElement.save(self,FALSE)

	## Caches
	###################################################
	def Move(self,newHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Move()')

		oldHolder = self.GetHolder()
		if oldHolder:
			oldHolder.RemoveChild(self)
		if newHolder:
			newHolder.AddChild(self)
			self.Holder = newHolder
			self.CachedSolar = newHolder.GetSolar()
		else:
			self.Holder = newHolder
			self.CachedSolar = 0
	
		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		

	def GetHolder(self):
		return self.Holder		

	## State control
	###################################################
	def GetStateDoneEvent(self,iState,internal = FALSE):
		iState = iState + Fleet.DONE
		if self.StateToEventDict.has_key(iState):
			return self.StateToEventDict[iState]
		elif not internal:
			e = GetNextEventType()
			self.StateToEventDict[iState] = e
			return e
		return 0

	def GetStateStartEvent(self,iState,internal = FALSE):
		iState = iState + Fleet.INIT
		if self.StateToEventDict.has_key(iState):
			return self.StateToEventDict[iState]
		elif not internal:
			e = GetNextEventType()
			self.StateToEventDict[iState] = e
			return e
		return 0

	def RaiseDoneEvent(self,iState):
		##debug("raising state done event "+str(iState)+" for fleet "+self.sName)
		e = self.GetStateDoneEvent(iState,TRUE)
		if e:
			self.Raise(e,self,self.GetHolder())

	def RaiseStartEvent(self,iState):
		##debug("raising state start event "+str(iState)+" for fleet "+self.sName)
		e = self.GetStateStartEvent(iState,TRUE)
		if e:
			self.Raise(e,self,self.GetHolder())		

	def SetState(self,newState):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Fleet_SetState(self,newState)')

		oldState = self.State
		self.State = newState
		if oldState == newState:
			return
		self.RaiseDoneEvent(oldState)		
		self.RaiseStartEvent(newState)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def SetVoyageState(self,newState):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Fleet_SetVoyageState(self,newState)')

		oldState = self.VoyageState
		self.VoyageState = newState
		if oldState == newState:
			return
		self.RaiseDoneEvent(oldState)		
		self.RaiseStartEvent(newState)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		
	## Overwrites
	########################################
	def GetOwnRadius(self,type=TREE_ELEMENT):
		return 0.0

	def GetRadius(self):
		f = 0.0
		for pShip in self.GetAllShips():
			f = f + 1.2 *pShip.GetRadius()
		return f
		
	## Binders
	########################################
	def Bind(self,pRace,pHolder,fleetName=None,lShips=None):
		## Bind it to the race and to the new system
		#assert pRace
		#assert pHolder
		self.Migrate(pRace)
		self.Move(pHolder)

		## sGfx 
		if not lShips:
			return

		if len(lShips):
			if not lShips[0]=='{':
				#A hybrid fleet string

				lParts=string.split(lShips,'@')
				lFleetTemplate=pRace.GetFleetTemplate(lParts[0])
				if not lFleetTemplate:
					raise RuntimeError , 'Fleettemplate '+lParts[0]+ ' isn\'t defined for race '+str(pRace)
				lsShips=string.split(lFleetTemplate,';')

				sNewTemplate = ''
				for lsShip in lsShips:
					lItems = Decode(lsShip,'@')
					sClass,Num = expand(lItems,2)

					if Num:
						Num = string.atoi(Num)
					else:
						Num = 1								
					
					for i in range(Num):
						sNewName = pRace.GetClassTemplate(sClass)
						if not sNewName:
							raise RuntimeError , 'Vesselclass '+sClass+ ' not defined for race '+pRace.sName
						sNewTemplate = sNewTemplate + sNewName + ';'																					
		
				lShips="{"+sNewTemplate[0:-1]+"}"
				#debug(str(lShips))				
											
			seq = Decode(lShips[1:-1],";@")
			iseq = len(seq)

			## Set the name
			if not fleetName:
				self.sName = "Fleet "+str(pRace.GetNumFleets()-1)
			else:
				self.sName = fleetName[:]
			
			for innerseq in seq:
				sGfx,Num,shipName = expand(innerseq,3)
				
				##Num in string format
				if Num:
					Num = string.atoi(Num)

				## Force items
				if not sGfx:
					sGfx = 'Akira'
				if not Num:
					Num = 1
		
				for k in range(0,Num):
					type=self.GetRace().GetVesselType(sGfx).sClass
						
					if type=="SY":
						import ATP_Shipyard2
						pShip=ATP_Shipyard2.Shipyard()						
					elif type=="SB" or  type=="SB+":
						import ATP_Starbase
						pShip=ATP_Starbase.Starbase()
					else:
						pShip=Ship()						

					if not shipName:
						sshipName = pRace.GetNextShipName(sGfx)
					else:
						if Num == 1:
							sshipName = shipName
						else:	
							sshipName = shipName + ' ' +str(k+1) 		
					
					#if fleetName:
					#	pShip.Bind(self,fleetName + ' - ' + sshipName,sGfx)
					#else:
					#	pShip.Bind(self,sshipName,sGfx)
					pShip.Bind(self,sshipName,sGfx)

		## A singular non named fleet bears the name of the ship
		if not fleetName and len(self.GetShips()) == 1:
			self.sName = self.GetShips()[0].sName
						

		## #debug
		# #debug("Finished creating the Fleet "+self.sName)

	## Warping
	##############################################################
	def ConWarpToSolar(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('ConWarpToSolar(self,pHolder)')

		## Change the state
		self.SetState(WARPING)

		## Alert our solar
		self.GetSolar().FleetWarpOut(self)

		## Conceptual move
		self.Move(pHolder)

		## Set the cached value
		self.CachedSolar = pHolder.GetSolar()

		## A delay
		self.AddDelay("ConWarpDone",self.Jitter(50.0))

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)


	def RealWarpToSolar(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Fleet_WarpToSolar')

		## Necesarry states
		#assert self.VoyageState == VOYAGING	## no warp without voyage
		#assert self.State == NORMAL		## valid state
		#assert pHolder.GetSolar().ID != self.GetSolar().ID 	## different solars required

		## Can we warp?
		if not self.CanWarp():
			## Stop local profiling
			App.TGProfilingInfo_StopTiming(idProfiling)
			return NAK		

		## Renderd
		bSelfRenderd	= self.IsRendered()
		bHolderRenderd = pHolder.IsRendered()

		## Handlers
		# Available through WarpIn(pShip)		
		
		if self.IsRendered() or pHolder.IsRendered():
			## Game warp
			#debug("fleet "+self.sName+" is game-warping to "+pHolder.sName+ " in the system "+pHolder.GetSolar().sName)
					
			## Prepare the placements & render if needed
			self.PrepareWarp(pHolder)

		else:
			## Conceptual warp
			#debug("fleet "+self.sName+" is conceptual-warping to "+pHolder.sName+ " in the system "+pHolder.GetSolar().sName)
			pass
		
		## Change the state
		self.SetState(WARPING)

		## Warp the ships out
		for pShip in self.GetShips():
			pShip.WarpToSolar(pHolder)

		## Conceptual move
		self.Move(pHolder)		

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		## Succes
		return ACK

	
	def PrepareWarp(self,pHolder): 
		## Any system active?
		pPlayerSolarID = GetPlayerShip().GetSolar().ID
		pOwnSolar = self.GetSolar()
		pDestSolar = pHolder.GetSolar()

		## Renderd
		bSelfRenderd	= self.IsRendered()
		bHolderRenderd = pHolder.IsRendered()

		if not bSelfRenderd:
			## Render&Randomise ourself
			pOwnSolar.Setup()
			self.Render(pOwnSolar.Node)
			self.Randomise()

		if not bHolderRenderd:
			## Setup the target system, nothing more
			pDestSolar.Setup()

		## Find an elaborate spot
		U = pHolder.FindSuitablePosition(self.GetRadius()*15.0)

		## Special for player
		if self.ID == PLAYER_FLEET_ID:
			i = 0
			fY = 0.0
			lSuns = pDestSolar.GetSuns()
			if lSuns:
				pSun = lSuns[0]					
				fX = pSun.GetPosition().GetX()
				fY = pSun.GetPosition().GetY() + pSun.GetOwnRadius()*3.0
				fZ = pSun.GetPosition().GetZ()	
				U.SetXYZ(fX,fY,fZ)
			else:
				U = pDestSolar.FindSuitablePosition(self.GetRadius()*10.0)
				debug(str(U.GetX()))			
	
		## Randomise of the fleet, concerning warp out spots
		fMinAngle, fMaxAngle = toRad(0.0) , toRad(360.0)
		radix = 5.0
		P=radix*self.GetOwnRadius()
		Z=App.TGPoint3()
		M=App.TGMatrix3()

		for pShip in self.GetShips():
			## Our relative position
			R=pShip.GetRadius()
			Z.SetXYZ(0.0,self.GetRandom(P+1.0*R,P+1.5*R),self.GetRandom(-R,R))
			P=P+2.0*radix*R

			M.MakeIdentity()
			M.MakeZRotation(self.GetRandom(fMinAngle,fMaxAngle)*self.GetRandomSign())
			Z.MultMatrixLeft(M)

			Z.Add(U)
						
			## Orient the waypoint towards the sun if possible
			pWay = pDestSolar.GetChildByName("__IN__"+str(pShip.ID))
			if not pWay:
				pWay = Waypoint("__IN__"+str(pShip.ID),pDestSolar,Z)
			else:
				pWay.SetPosition(Z)

			Suns = pHolder.GetSolar().GetSuns()
			if Suns:
				Sun = Suns[0]
				S = Sun.GetPosition()
				S.Subtract(Z)
				S.Unitize()
				Up=S.Cross(eX)
				pWay.GetNode().AlignToVectors(S,Up)
										
		## Adjust everything for the player
		if self.ID == PLAYER_FLEET_ID:
			pWay = pDestSolar.GetChildByName("__IN__"+str(GetPlayerShip().ID))
			V = pWay.GetPosition()
			pHolder.GetSolar().ShiftCenter(V)

	def CanWarp(self):
		for pShip in self.GetShips():
			if not pShip.GetNode():
				continue

			pWarp=pShip.GetNode().GetWarpEngineSubsystem()
			if not pWarp:
				return FALSE
			elif pWarp.IsDisabled():
				return FALSE
		return TRUE



	## Quick Warp
	###############################################################
	def MoveToSolar(self,pHolder):
		## Necesarry states
		#assert pHolder
		#assert self.VoyageState == VOYAGING		## no warp without voyage
		#assert self.State == NORMAL			## valid state
		#assert pHolder.GetSolar().ID != self.GetSolar().ID 	## different solars required

		## Rendered ?
		bSelfRendered	= self.IsRendered()
		bHolderRendered = pHolder.IsRendered()

		if bSelfRendered or bHolderRendered:

			if not bSelfRendered:
				## Render&Randomise ourself
				self.GetSolar().Setup()
				self.Render(self.GetSolar().Node)
				self.Randomise()

			if not bHolderRendered:
				## Setup the target system, nothing more
				pHolder.GetSolar().Setup()

		## Change the state
		self.SetState(WARPING)		

		## Move the children			
		for pShip in self.GetShips():	
			pShip.MoveToSolar(pHolder)

		## Conceptual Move
		self.Move(pHolder)

		## Succes
		return ACK


	## Intercept
	##################################
	def Intercept(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Fleet_Intercept')

		## #assertions
		#assert pHolder
		#assert self.VoyageState == VOYAGING		## no intercept without voyage
		#assert self.State == NORMAL			## valid state
		#assert pHolder.GetSolar().ID == self.GetSolar().ID 	## same solars required
		#assert pHolder.ID != self.GetHolder().ID		## different holders required

		## debug
		debug('I, fleet '+self.sName+' am intercepting '+pHolder.sName)

		## Change state 
		self.SetState(INTERCEPTING)

		## Intercept
		for pShip in self.GetShips():
			pShip.Intercept(pHolder)

		## Conceptual move
		self.Move(pHolder)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def URR_Intercept(self):
		## Just call the function on the children
		for pShip in self.GetShips():
			pShip.URR_Intercept()

	def RUR_Intercept(self):
		## Just call the function on the children
		for pShip in self.GetShips():
			pShip.RUR_Intercept()



	## Events
	#################################
	def WarpIn(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip  = pEvent.GetSource()
		pSolar = pEvent.GetDestination()
		if not pShip:
			return

		## #assertions
		#assert pShip and pSolar
		#assert self.HasChild(pShip)
		#assert self.VoyageState == VOYAGING	## Only warping while voyaging
		#assert self.State == WARPING		## Only when the fleet is warping too
		
		## #debug
		debug("My ship "+pShip.sName+" has warped in system "+pSolar.sName)	
		
		## All of them done warping?
		for pShip in self.GetShips():
			if pShip.GetState() != NORMAL:
				return

		## Special case that the system went up during conceptual warp
		if not self.IsRendered() and pSolar.IsRendered():
			assert 0
			## Correct this special case
			self.State = NORMAL ## forced and silent override
			pHolder = self.GetHolder()
			pMatrix = GetMatrix()
			self.Move(pMatrix)
			self.Render(pMatrix.Node)
			pMatrix.Randomise()			
			self.RealWarpToSolar(pHolder)
			return

		## A hack
		self.State = NORMAL

		## Special case that the system went down during real warp
		if self.IsRendered() and not pSolar.IsRendered():
			## Correct this special case
			self.Unrender()

		## A hack
		self.State = WARPING

		## All of them warped in, change our state
		self.SetState(NORMAL)

		## Alert our solar
		pSolar.FleetWarpIn(self)	
 
		## #debug
		debug("fleet "+self.sName+" has entirely warped in system "+pSolar.sName)

		

	def ConWarpDone(self,gEvent):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('ConWarpDone(self,gEvent)')				

		## Our holder
		pHolder = self.GetHolder()

		## Correct this special case
		if pHolder.IsRendered():			
			pHolder = self.GetHolder()
			self.URR_Warp(pHolder)

			## Stop local profiling
			App.TGProfilingInfo_StopTiming(idProfiling)

			return
		
		## Change the state
		if self.bInside:
			self.SetState(INSIDE)
		else:
			self.SetState(NORMAL)

		## We were voyaging
		self.SetVoyageState(IDLE)

		## Alert our solar
		self.GetSolar().FleetWarpIn(self)

		## Spaceline ?
		if self.lSpacelineDestinations:
			## A delay
			self.AddDelay("ConSwapSpaceline",self.fStay)
			
		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)	

	def WarpOut(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip  = pEvent.GetSource()
		pSolar = pEvent.GetDestination()
		if not pShip:
			return		
		
		## All of them done warping?
		for pShip in self.GetShips():
			if pShip.GetState() != WARPING:
				return

		## Alert our solar
		pSolar.FleetWarpOut(self)

	def InterceptDone(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip  = pEvent.GetSource()
		pHolder = pEvent.GetDestination()
		if not pShip:
			return

		## #assertions
		#assert pShip and pHolder
		#assert self.HasChild(pShip)
		#assert self.VoyageState == VOYAGING	## Only intercepting while voyaging
		#assert self.State == INTERCEPTING	## Only when the fleet is intercepting too

		## debug
		debug("ship "+pShip.sName+" has intercepted "+pHolder.sName)

		## All of them done intercepting?
		for pShip in self.GetShips():
			#assert pShip.State == INTERCEPTING or pShip.State == NORMAL
			if pShip.GetState() == INTERCEPTING:
				return
		
		## debug
		debug("fleet "+self.sName+" has intercepted "+pHolder.sName)

		## All of them are done, change our state
		self.SetState(NORMAL)	
 			
	
	def ShipDestroyed(self,pShip):
		#debug("ship "+pShip.sName+" was destroyed in me, "+self.sName)
		
		## Checks
		#assert self.HasChild(pShip)

		## Remove it		
		# pShip.Migrate(None)

		## Notify holder
		self.GetHolder().ShipDestroyed(pShip,self)
		self.GetRace().ShipDestroyed(pShip,self)	

		## Remove it
		pShip.Migrate(None)	

		## Children left?
		if not self.GetShips():
			self.SetState(DEAD)
			self.GetHolder().FleetDestroyed(self)
			self.GetRace().FleetDestroyed(self)

			## Delete ourself
			self.delete()
		else:
			## Regulise
			if self.State == NORMAL:
				pass

			elif self.State == INTERCEPTING:
				## All of them done intercepting?
				for pShip in self.GetShips():
					#assert pShip.State == INTERCEPTING or pShip.State == NORMAL
					if pShip.GetState() == INTERCEPTING:
						return
		
				## All of them are done, change our state
				self.SetState(NORMAL)

			elif self.State == WARPING:
				## All of them done intercepting?
				for pShip in self.GetShips():
					#assert pShip.State == WARPING or pShip.State == NORMAL
					if pShip.GetState() == WARPING:
						return
		
				## All of them are done, change our state
				self.SetState(NORMAL)
			else:
				pass
			

	def Kill(self):
		#debug("me, fleet "+self.sName+" was killed")
		for pShip in self.GetShips():
			pShip.Kill()

	def HolderDestroyed(self):
		## Data
		pHolder = self.GetHolder()
		pSuperHolder = pHolder.GetHolder()

		if self.State in (ENTERING,INSIDE,BUILDING,REPAIR,EXITING):
			## We cannot survive this
			self.Kill()

		elif self.State in(NORMAL,WARPING,INTERCEPTING):
			## We can survive this...
			
			## Move ourself
			self.Move(pSuperHolder)

			## Modify the rendered intercept course
			if self.State == INTERCEPTING and self.IsRendered():
				for pShip in self.GetShips():
					pShip.Intercept(pSuperHolder)
		else:
			raise RuntimeError

	## Rendering functions
	###############################
	def IsRendered(self):
		Ships = self.GetShips()
		if not Ships:
			return FALSE
		if Ships[0].Node:
			return TRUE
		return FALSE

	def Render(self,pSet):
		if not self.IsRendered():
			## Fleet state
			State = self.State
	
			## Reset ship states
			for pShip in self.GetShips():
				pShip.State = State

			if State in (NORMAL,INSIDE):
				## A spaceline ?
				if self.lSpacelineDestinations:
					self.RemoveClock("ConSwapSpaceline")
					self.AddDelay("SpacelineVoyage",self.Jitter(self.fStay*0.5))
			
			elif State in (WARPING,):
				return

			elif State in (BUILDING,):
				pass

			else:
				raise RuntimeError

		## Regular
		UniverseElement.Render(self,pSet)

	def Unrender(self):
		if not self.IsRendered():
			## Regular
			UniverseElement.Unrender(self)	
		else:
			State = self.State
			pHolder = self.GetHolder()
			
			if State in (NORMAL,INSIDE):
				## Regular
				UniverseElement.Unrender(self)

				## Spaceline
				if self.lSpacelineDestinations:
					self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*0.5))	

			elif State == REPAIR:
				## Regular
				UniverseElement.Unrender(self)

				## Force the repair to be done
				self.GetHolder().RUR_Repair(self)	

			elif State == ENTERING:
				## Regular
				UniverseElement.Unrender(self)
				
				## Voyage finish
				self.SetState(INSIDE)
				self.SetVoyageState(IDLE)
				
				## Spaceline ?
				if self.lSpacelineDestinations:
					self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*0.5))
	
			elif State == EXITING: 				
				## Regular
				UniverseElement.Unrender(self)
			
				## Destination
				pDestination = self.GetDestination()
				
				## Possibilities
				if pHolder == pDestination:

					self.SetState(NORMAL)
					self.SetVoyageState(IDLE)

					if self.lSpacelineDestinations:
						self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*1.5))
				
				elif pHolder.GetSolar() == pDestination.GetSolar():

					if self.bInside:
						self.SetState(INSIDE)
					else:	
						self.SetState(NORMAL)

					self.Move(pDestination)
					self.SetVoyageState(IDLE)

					if self.lSpacelineDestinations:
						self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*1.5))
				else:
					self.ConVoyage(pDestination)

			elif State == INTERCEPTING: 				
				## Regular
				UniverseElement.Unrender(self)

				## Inside or not?
				if self.bInside:
					self.SetState(INSIDE)
				else:	
					self.SetState(NORMAL)

				## Voyage finish
				self.SetVoyageState(IDLE)
				
				## Spaceline
				if self.lSpacelineDestinations:
					self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*1.5))

			elif State == WARPING:
				## Do nothing
				pass

			elif State == BUILDING:
				## Regular
				UniverseElement.Unrender(self)

			else:
				raise RuntimeError

	
	def URR_Warp(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('URR_Warp()')

		self.State = NORMAL ## forced and silent override
		for pShip in self.GetShips():
			pShip.State = NORMAL ## forced and silent override
			
		## Render us
		pMatrix = GetMatrix()
		pMatrix.Setup()
		self.Move(pMatrix)
		self.Render(pMatrix.Node)
		pMatrix.Randomise()

		## Activate the real cycle with this handler
		self.AddHandler(self.GetStateStartEvent(NORMAL),"EnterDestination")

		## Spaceline?
		if self.lSpacelineDestinations:
			## Add a handler
			self.AddHandler(self.GetStateDoneEvent(VOYAGING),"SpacelineVoyageStay")
			
		## This warp will be real
		self.RealWarpToSolar(pHolder)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)	
				

	def Randomise(self):
		UniverseElement.Randomise(self,SHIP,4.0)
		UniverseElement.Randomise(self,FLEET,8.0)

	def CheckedUnrender(self,gEvent):
		pPlayerSolar = GetByNode(GetPlayerShip().Node.GetContainingSet())
		if not pPlayerSolar:
			return

		for pShip in self.GetShips():
			if not pShip.Node:
				continue
			pSolar = GetByNode(pShip.Node.GetContainingSet())
			if not pSolar:
				continue		
			if pPlayerSolar.ID == pSolar.ID:
				return

		## Effective unrender
		self.Unrender()

	## Voyage functions
	######################################
	def GetSource(self):
		return GetByID(self.SourceID)

	def SetSource(self,Source):
		## Old source
		pOldSource = GetByID(self.SourceID)
		if pOldSource:
			if pOldSource.IsTypeOf(SHIP):
				self.RemoveHandler(pOldSource.GetStateStartEvent(DEAD),"SourceDestroyed")

		## New source
		if Source:
			## Register
			self.SourceID = Source.ID

			## Add hanlder for deaths
			if Source.IsTypeOf(SHIP):
				self.AddHandler(Source.GetStateStartEvent(DEAD),"SourceDestroyed")			
		else:
			self.SourceID = 0

	def GetDestination(self):
		return GetByID(self.DestinationID)

	def SetDestination(self,Destination):
		## Old Destination
		pOldDestination = GetByID(self.DestinationID)
		if pOldDestination:
			if pOldDestination.IsTypeOf(SHIP):
				self.RemoveHandler(pOldDestination.GetStateStartEvent(DEAD),"DestinationDestroyed")

		## New Destination
		if Destination:
			## Register
			self.DestinationID = Destination.ID

			## Add hanlder for deaths
			if Destination.IsTypeOf(SHIP):
				self.AddHandler(Destination.GetStateStartEvent(DEAD),"DestinationDestroyed")			
		else:
			self.DestinationID = 0

	def SourceDestroyed(self,gEvent):
		self.SetSource(self.GetSource().GetHolder())

	def DestinationDestroyed(self,gEvent):
		self.SetDestination(self.GetDestination().GetHolder())

	## Core Voyage function
	######################################
	def Voyage(self,pHolder,bInside = FALSE):
		## Check
		if self.VoyageState == VOYAGING:
			return NAK

		## Real or conceptual ?
		if self.IsRendered():
			return self.RealVoyage(pHolder,bInside)
		else:
			return self.ConVoyage(pHolder,bInside)

	def ConVoyage(self,pHolder,bInside = FALSE):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('ConVoyage()')

		## Inside?
		self.bInside = bInside

		## Change our state 
		self.SetVoyageState(VOYAGING)

		## Real voyage
		self.ConWarpToSolar(pHolder)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)


	def RealVoyage(self,pHolder,bInside = FALSE):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('RealVoyage()')		

		## Inside?
		self.bInside = bInside

		## Valid data
		#assert pHolder
		#assert pHolder.IsTypeOf(HOLDER)		
		
		## Change our state 
		self.SetVoyageState(VOYAGING)

		## Set the voyage begin and end	
		self.SetDestination(pHolder)
		self.SetSource(self.GetHolder())

		## #debug
		debug("fleet "+self.sName+" starts voyaging from "+self.GetSource().sName+" to "+self.GetDestination().sName)		

		## Change our state 
		self.SetVoyageState(VOYAGING)

		## Same holder and pos?
		if self.GetHolder().ID == pHolder.ID and  ( 	(self.State == INSIDE and self.bInside) or
								(self.State == NORMAL and not self.bInside)	):
			## Short trip...
			self.SetVoyageState(IDLE)			
		else:
			## Begin our voyage
			self.BeginVoyage()

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		## Status ok
		return ACK			

	def BeginVoyage(self):
		## debug
		debug("fleet "+self.sName+" is leaving "+self.GetSource().sName)

		## Catching
		if not self.GetDestination() or not self.GetSource():
			return

		## Let others handle the way of exit, just listen to the statedone event
		self.AddHandler(self.GetStateStartEvent(NORMAL),"MoveToDestination")
		
		## Exit...
		if self.State == INSIDE:

			if self.GetSource().ExitFleet(self) == NAK:

				## An error, abort the voyage
				self.RemoveHandler(self.GetStateStartEvent(NORMAL),"MoveToDestination")
				self.SetVoyageState(VOYAGE_ERROR)

		elif self.State == NORMAL:

			## Move Out
			self.MoveToDestination(None)

		else:
			raise RuntimeError

	def MoveToDestination(self,gEvent):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('MoveToDestination(self,gEvent)')

		## Catching
		if not self.GetDestination() or not self.GetSource():
			return

		## Remove the handler
		self.RemoveHandler(self.GetStateStartEvent(NORMAL),"MoveToDestination")

		## If the destination is in another system, warp
		S = self.GetHolder()
		D = self.GetDestination()
		
		# assert S
		# assert D

		pSolarA = S.GetSolar()
		pSolarB = D.GetSolar()

		if S.ID == D.ID:
			## Move immediate:
			self.EnterDestination(None)
			## Stop local profiling
			App.TGProfilingInfo_StopTiming(idProfiling)
			return

		## Handler
		self.AddHandler(self.GetStateStartEvent(NORMAL),"EnterDestination")

		bACK = NAK
		if pSolarA.ID != pSolarB.ID: 
			## Can we use a wormhole ?
			lWormholes = pSolarA.GetAllSolarWormholes()
			for pWormhole in lWormholes:
				if pWormhole.GetOppositeSolar().ID == pSolarB.ID:
					## Use the wormhole
					bACK = pWormhole.WormholeFleet(self)
					
					break
				
			## Warp to target			
			if bACK == NAK:
				debug("fleet "+self.sName+" is warping to "+D.GetSolar().sName)
				bACK = self.RealWarpToSolar(D)
			else:
				debug("fleet "+self.sName+" is wormholing to "+D.GetSolar().sName)	

		else:
			## Intercept the target
			debug("fleet "+self.sName+" is intercepting to "+D.sName)
			bACK = self.Intercept(D)

		## Error?
		if bACK == NAK:
			## An error, abort the voyage
			self.RemoveHandler(self.GetStateStartEvent(NORMAL),"MoveToDestination")
			self.SetVoyageState(VOYAGE_ERROR)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)


	def EnterDestination(self,gEvent):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('EnterDestination(self,gEvent)')

		## Catching
		if not self.GetDestination() or not self.GetSource():
			return

		## Remove the handler
		self.RemoveHandler(self.GetStateStartEvent(NORMAL),"EnterDestination")

		debug("fleet "+self.sName+" is entering "+self.GetDestination().sName)

		## Let the holder handle the way of exit, just listen to the statedone event
		self.AddHandler(self.GetStateStartEvent(INSIDE),"EndVoyage")
		
		## Enter... or not...
		if self.bInside:
			pHolder = self.GetHolder()
			if not pHolder.IsTypeOf(HOLDER):
				print 'Catch you object '+pHolder.sName+' with class '+str(pHolder.__class__)
				print 'for fleet '+self.sName
				return
			if pHolder.EnterFleet(self) == NAK:
				## An error, abort the voyage
				self.RemoveHandler(self.GetStateStartEvent(INSIDE),"EndVoyage")
				self.SetVoyageState(VOYAGE_ERROR)
		else:
			self.EndVoyage(None)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)
			
	def EndVoyage(self,gEvent):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('EndVoyage(self,gEvent)')

		## Catching
		if not self.GetDestination() or not self.GetSource():
			return

		## Remove the handler
		self.RemoveHandler(self.GetStateStartEvent(INSIDE),"EndVoyage")

		debug("fleet "+self.sName+" is arrived at "+self.GetDestination().sName)

		## Change our state
		self.SetVoyageState(IDLE)

		debug("fleet "+self.sName+" VOYAGE done")

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)		
	
	## Spaceline functions
	###############################
	def SetupSpaceline(self,lDestinations,fStay = 20.0):
		## Timestamps
		self.fStay = fStay
		
		## Destinations
		self.lSpacelineDestinations = lDestinations[:]
	
		if self.IsRendered():
			self.SpacelineVoyage(None)		
		else:
			self.ConSwapSpaceline(None)

	def ConSwapSpaceline(self,gEvent):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('ConSwapSpaceline()')

		## Swap spaceline destinations
		pDest = self.lSpacelineDestinations.pop(0)
		self.lSpacelineDestinations.append(pDest)
		
		## Decision ...
		if pDest.GetSolar() == self.GetSolar():
			self.SetState(INSIDE)
			self.Move(pDest)
			self.AddDelay("ConSwapSpaceline",self.Jitter(self.fStay*1.5))
		else:
			self.ConVoyage(pDest,TRUE)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def SpacelineVoyage(self,gEvent):
		## Add a handler
		self.AddHandler(self.GetStateDoneEvent(VOYAGING),"SpacelineVoyageStay")

		## Swap spaceline destinations
		pDestination = self.lSpacelineDestinations.pop(0)
		self.lSpacelineDestinations.append(pDestination)

		## Start the real voyage
		self.Voyage(pDestination,bInside = TRUE)		

	def SpacelineVoyageStay(self,gEvent):
		## Add a handler
		self.RemoveHandler(gEvent.GetEventType(),"SpacelineVoyageStay")

		## Stay a while...
		self.AddDelay("SpacelineVoyage",self.Jitter(self.fStay))
	

	## Enhancement
	###############################################
	def Enhance(self):
		if self.State == INTERCEPTING:
			## Position ourselfs somewhere
			V = self.GetSource().FindSuitablePosition(self.GetRadius()*3.0)
			self.SetPosition(V)						

			## Intercept on the ships
			self.URR_Intercept()
	
		elif self.State == ENTERING:
			## Synchronised enter
			self.GetHolder().URR_EnterFleet(self)
			
		elif self.State == EXITING:
			## Synchronised exit
			self.GetHolder().URR_ExitFleet(self)
			
		else:
			pass

		UniverseElement.Enhance(self)

	## Advanced Features
	######################################
	def RenderedRepair(self,pYard=None):
		## Find a shipyard ourselves if necessary
		if not pYard:
			
			lYards = self.GetSolar().GetAllShipyards()

			lPosYards = []
			for pYard in lYards:
				if pYard.IsRepairYard():
					lPosYards.append(pYard)
			if not lPosYards:
				return NAK

			V = self.GetPosition()
			Umin = 1.0e+20
			
			for ppYard in lPosYards:
				U = ppYard.GetPosition()
				U.Subtract(V)
				U.SqrLength()
				if U  < Umin:
					pYard = ppYard					

		## We have a yard now, voyage to it
		self.Voyage(pYard,bInside=TRUE)
				
		


## Merging functions
############################################
def MergeFleets(lFleets,sNewName=""):
	## Some assertions
	assert lFleets
	assert len(lFleets) > 1 ## minimum two fleets

	## Local copy
	lFleets = lFleets[:]

	## Some checks
	pFirstFleet = tFleets[0]
	HID = pFirstFleet.GetHolder().ID

	## Valid state
	assert pFirstFleet.VoyageState == NORMAL
	assert (pFirstFleet.State == NORMAL) or (pFirstFleet.State == INSIDE)

	## Some checks
	for pFleet in tFleets[1:]:
		assert pFleet.VoyageState == pFirstFleet.VoyageState
		assert pFleet.State 	  == pFirstFleet.State
		assert pFleet.GetHolder().ID == HID
		pass

	## Find the masterfleet (the one who remains)
	pMasterFleet = None

	## In a merge with a playerfleet, the playerfleet is the master
	for pFleet in lFleets:
		if pFleet.ID == PLAYER_FLEET_ID:
			pMasterFleet = pFleet
			lFleet.remove(pFleet)
			break

	## Are all ships singular fleets ?
	if not pMasterFleet:
		for pFleet in lFleets:
			if pFleet.IsExactTypeOf(FLEET):
				## A pure fleet
				pMasterFleet = pFleet
				lFleet.remove(pFleet)
				break
	
	## All non pure fleets, make a new one
	if not pMasterFleet:
		pMasterFleet = Fleet()
		pMasterFleet.Migrate(pFirstFleet.GetRace())
		pMasterFleet.Move(pFirstFleet.GetHolder())
		pMasterFleet.VoyageState = pFirstFleet.VoyageState
		pMasterFleet.State = pFirstFleet.State
		pMasterFleet.SetName(pFirstFleet.sName)
	
	## Merge, move the ships
	for pFleet in lFleets:
		## Move the children to the masterfleet
		for pShip in pFleet.GetShips():
			pShip.Migrate(pMasterFleet)

		## Delete that fleet
		pFleet.delete()
	
	## Change the name
	if sNewName:
		pMasterFleet.SetName(sNewName)

	## Return the new master
	return pMasterFleet



class SingularFleet(Fleet):
		
	def __init__(self,ID=None):
		Fleet.__init__(self,ID)

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = SingularFleet("+str(self.ID)+")")

		## Upperclass
		Fleet.save(self,FALSE)

	def Bind(self,pRace,pHolder,sGfx=None,sName=None):
		#assert pRace
		#assert pHolder
		self.Migrate(pRace)
		self.Move(pHolder)

		if not sGfx:
			sGfx = "Akira"
		if not sName:
			sName = sGfx+" "+str(pRace.GetNumFleets())
		self.sName = sName
		
		type=self.GetRace().GetVesselClass(sGfx)
		if type=="SY":
			import ATP_Shipyard2
			pShip=ATP_Shipyard2.Shipyard()
		elif type=="SB" or  type=="SB+":
			import ATP_Starbase
			pShip=ATP_Starbase.Starbase()
		else:
			pShip=Ship()

		## Bind the ship
		pShip.Bind(self,self.sName,sGfx)		

	def GetSingleShip(self):
		return self.GetShips()[0]
 

class PlayerFleet(Fleet):
	def __init__(self,ID=None):
		Fleet.__init__(self,ID)

		pPlayer=PlayerShip(PLAYER_SHIP_ID)
		pPlayer.Bind(self,PLAYER,"")

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = PlayerFleet("+str(self.ID)+")")

		## Upperclass
		Fleet.save(self,FALSE)

	def Bind(self,pRace,pHolder,sName=None,lShips=""):
		#Create the player ship
		Fleet.Bind(self,pRace,pHolder,sName,lShips)


class SingularFleet(Fleet):
		
	def __init__(self,ID=None):
		Fleet.__init__(self,ID)

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = SingularFleet("+str(self.ID)+")")

		## Upperclass
		Fleet.save(self,FALSE)

	def Bind(self,pRace,pHolder,sGfx=None,sName=None):
		#assert pRace
		#assert pHolder
		self.Migrate(pRace)
		self.Move(pHolder)

		if not sGfx:
			sGfx = "Akira"
		if not sName:
			sName = sGfx+" "+str(pRace.GetNumFleets())
		self.sName = sName
		
		type=self.GetRace().GetVesselClass(sGfx)
		if type=="SY":
			import ATP_Shipyard
			pShip=ATP_Shipyard.Shipyard()
		elif type=="SB" or  type=="SB+":
			import ATP_Starbase
			pShip=ATP_Starbase.Starbase()
		else:
			pShip=Ship()

		## Bind the ship
		pShip.Bind(self,self.sName,sGfx)		

	def GetShip(self):
		return self.GetShips()[0]

	
class Ship(Holder):
	PASSIVE		= 0
	COMBAT		= 1
	
	INIT	= 0
	DONE	= 100

	TYPE = __name__

	def __init__(self,ID=None):
		Holder.__init__(self,ID)

		self.sGfx="FTB_Akira"
		self.BuildPoints=1000.0
		self.BuildPercentage=1.0
		self.HullPercentage=1.0
		self.Hull=1000.0
		self.Class = "??"

		self.LocalHolderID = 0
	
		self.State  = NORMAL
		self.Status = Ship.PASSIVE
		self.StateToEventDict = {}
		
		self.INTERCEPT_DONE = 0

		self.Fleet = None

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Ship("+str(self.ID)+")")

		## Upperclass
		Holder.save(self,FALSE)

		## Our lines
		write_save_file("self.sGfx = \""+str(self.sGfx)+"\"")
		write_save_file("self.BuildPoints = "+str(self.BuildPoints))
		write_save_file("self.BuildPercentage = "+str(self.BuildPercentage))
		write_save_file("self.HullPercentage = "+str(self.HullPercentage))
		write_save_file("self.Hull = "+str(self.Hull))
		write_save_file("self.Status = "+str(self.Status))
		write_save_file("self.State = "+str(self.State))
		write_save_file("self.Class = \""+str(self.Class)+"\"")

	## Caches
	def Migrate(self,newParent):
		oldParent = self.GetFather()
		if oldParent:
			oldParent.RemoveChild(self)
		if newParent:
			newParent.AddChild(self)
			self.Fleet = newParent

	def GetHolder(self):
		return self.Fleet.Holder
	
	def GetSolar(self):
		return self.Fleet.GetSolar()

	## States
	###################################################
	def GetStateDoneEvent(self,iState,internal = FALSE):
		iState = iState + Ship.DONE
		if self.StateToEventDict.has_key(iState):
			return self.StateToEventDict[iState]
		elif not internal:
			e = GetNextEventType()
			self.StateToEventDict[iState] = e
			return e
		return 0

	def GetStateStartEvent(self,iState,internal = FALSE):
		iState = iState + Ship.INIT
		if self.StateToEventDict.has_key(iState):
			return self.StateToEventDict[iState]
		elif not internal:
			e = GetNextEventType()
			self.StateToEventDict[iState] = e
			return e
		return 0

	def RaiseDoneEvent(self,iState):
		##debug("raising state done event "+str(iState)+" for ship "+self.sName)
		e = self.GetStateDoneEvent(iState,TRUE)
		if e:
			self.Raise(e,self,self.GetHolder())

	def RaiseStartEvent(self,iState):
		##debug("raising state start event "+str(iState)+" for ship "+self.sName)
		e = self.GetStateStartEvent(iState,TRUE)
		if e:
			self.Raise(e,self,self.GetHolder())		

	def SetState(self,newState):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Ship_SetState(self,newState)')

		oldState = self.State
		self.State = newState
		if oldState == newState:
			return
		self.RaiseDoneEvent(oldState)		
		self.RaiseStartEvent(newState)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def GetState(self):
		return self.State	

	def GetClass(self):
		return self.Class

	def IsStationary(self):
		return self.GetRace().IsVesselStationary(self.sGfx)

	def IsDockable(self):
		return FALSE
	
	def GetGfx(self):
		return self.sGfx[:]

	def SetGfx(self,sGfx):
		self.sGfx=sGfx[:]

		try:
			pModule=__import__("Ships."+self.sGfx)
			self.BuildPoints=pModule.GetBuildPoints()			
		except ImportError:
			pass

	def SetBuildPoints(self,fVal):
		self.BuildPoints=fVal
			
	def GetBuildPoints(self):
		return self.BuildPoints

	def AddBuildPoints(self,fVal):
		f=self.BuildPercentage+fVal/self.BuildPoints
		self.SetBuildPercentage(f)
		
	def SetBuildPercentage(self,fVal):
		if fVal<0.0:
			fVal=0.0
		elif fVal>1.0:
			fVal=1.0
		self.BuildPercentage=fVal
				
	def GetBuildPercentage(self):
		return self.BuildPercentage		

	def SetHull(self,fVal):
		if fVal<0.0:
			fVal=0.0
		self.Hull=fVal
		if self.GetNode():
			if self.GetNode().GetHull():
				self.GetNode().GetHull().GetProperty().SetMaxCondition(fVal)				
	
	def GetHull(self):
		return self.Hull

	def DamageHull(self,fVal):
		f=self.HullPercentage-fVal/self.Hull
		self.SetHullPercentage(f)		

	def SetHullPercentage(self,fVal):
		if fVal<0.0:
			fVal=0.0
		elif fVal>1.0:
			fVal=1.0
		self.HullPercentage=fVal
		if self.GetNode():
			if self.GetNode().GetHull():
				self.GetNode().GetHull().SetConditionPercentage(fVal)			

	def GetHullPercentage(self):
		return self.HullPercentage

	def FullRepair(self):
		## Repair the hull
		self.SetHullPercentage(1.0)

	def IsHale(self):
		## Rendered
		if self.IsRendered():
			## Iterate over all systems
			pIterator = self.Node.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = self.Node.GetNextSubsystemMatch(pIterator)
			while (pSubsystem != None):
				if not pSubsystem.GetConditionPercentage() in (0.0,1.0):
					return FALSE					
				pSubsystem = self.Node.GetNextSubsystemMatch(pIterator)
			self.Node.EndGetSubsystemMatch(pIterator)

			## True
			return TRUE

		## Unrendered
		else:
			return ( self.HullPercentage == 1.0 )
	
	def Bind(self,pFleet,sName="",sGfx=""):
		#assert pFleet
		self.Migrate(pFleet)
		
		if not sName:
			sName = "Ship "+str(pFleet.GetNumShips()) 
		self.sName=sName[:]

		if not sGfx:
			sGfx = "Akira"
		self.sGfx=sGfx[:]

		self.Class = self.GetRace().GetVesselClass(sGfx)

		# #debug("Finished creating the ship "+self.sName)
	
	def Render(self,pSet):
		## Base class
		Holder.Render(self,pSet)
		
		## Own stuff
		debug('rendering '+self.sName+' with gfx: '+self.sGfx)
		if not self.IsRendered():			
			self.Node=loadspacehelper.CreateShip(self.sGfx,pSet,self.sName,'')
			if not self.Node:
				for i in range(25):
					self.Node=loadspacehelper.CreateShip(self.sGfx,pSet,self.sName + ' ' + NumToUpperAlpha[i],'')
					if self.Node:
						break
				if not self.Node:
					self.Node=loadspacehelper.CreateShip(self.sGfx, pSet,self.sName+" "+str(self.ID),'')
					if not self.Node:
						raise  RuntimeError , "ATP_Vessels: Ship "+self.sName+" cannot be created."
			
			## Add a clock for tactical events
			self.AddClock("RealEvents")

			## Extend sensorrange
			pSensors=self.Node.GetSensorSubsystem()
			if pSensors:
				pSensors.GetProperty().SetBaseSensorRange(SENSOR_MULTIPLYER*pSensors.GetBaseSensorRange())	

		debug('done rendering '+self.sName+' with gfx: '+self.sGfx)

		## Update the real things
		self.SetHullPercentage(self.GetHullPercentage())

		## Node cache
		self.EnterNodeCache()	
		
	def Unrender(self):
		## May we unrender?
		if self.State == WARPING:
			## Delay the unrender
			self.AddHandler(self.GetStateDoneEvent(WARPING),"DelayedUnrender")
			return

		## Remove things
		self.RemoveClock("RealEvents")
		
		## Base class
		Holder.Unrender(self)
	
	def DelayedUnrender(self,gEvent):
		## Delay the unrender
		self.RemoveHandler(self.GetStateDoneEvent(WARPING),"DelayedUnrender")
		self.Unrender()

	def CheckedUnrender(self,gEvent):
		## Remove the handler
		self.RemoveHandler(GetPlayerShip().GetStateDoneEvent(WARPING),"CheckedUnrender")
	
	def RealEvents(self,pEvent):
		if not self.Node:
			self.RemoveClock("RealEvents")
			return
		if self.Node.IsDead() or self.Node.IsDying():
			self.RemoveClock("RealEvents")
			return

		#Synchronise with the outside world
		self.SetHullPercentage(self.GetNode().GetHull().GetConditionPercentage())
		self.SetBuildPercentage(self.GetNode().GetHull().GetConditionPercentage())
		
		#Call next
		self.Wrapper.CallNextHandler(pEvent)

	def AssignAI(self,kArgs=None,force=FALSE):
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]
		
		if not self.Node:
			return

		#assert GetPlayerShip()

		pRace=self.GetRace()
		pPlayerRace=GetPlayerRace()
		pPlayerFleet=GetPlayerFleet()
		import MissionLib
		pMission=MissionLib.GetMission()
		
		if len(kArgs):
			pModuleName=kArgs.pop(0)
			kArgs.insert(0,self)
			##debug("Assigning "+pModuleName+" AI for "+self.sName)

		else:
			pModuleName=""
			# #debug("Assigning Standard AI for "+self.sName)

		
		#assert self.GetFleet()
		
		if pPlayerFleet:
			if pPlayerFleet.GetID()==self.GetFleet().GetID():
				if not pModuleName:
					from Custom.AdvancedTechnologies.Data.AI import ATP_GeneralFleetAI
					self.Node.SetAI(ATP_GeneralFleetAI.CreateAI(self.Node))
				else:
					pModule=__import__(pModuleName)
					self.Node.SetAI(pModule.CreateAI(kArgs))
				pFriendlies = pMission.GetFriendlyGroup()
				pFriendlies.AddName(self.Node.GetName())
				MissionLib.AddCommandableShip(self.Node.GetName())
				return
			
		if pPlayerRace.IsEnemy(pRace):
			if pModuleName:
				pModule=__import__(pModuleName)
				self.Node.SetAI(pModule.CreateAI(kArgs))
			else:
				if self.GetNode().GetShipProperty().IsStationary() or self.IsStationary():
					from Custom.AdvancedTechnologies.Data.AI import ATP_SBEnemyAI
					self.Node.SetAI(ATP_SBEnemyAI.CreateAI(self.Node))
				else:
					from Custom.AdvancedTechnologies.Data.AI import ATP_GeneralEnemyAI
					self.Node.SetAI(ATP_GeneralEnemyAI.CreateAI(self.Node))
			
			pEnemies = pMission.GetEnemyGroup()
			pEnemies.AddName(self.Node.GetName())

		elif pPlayerRace.IsAlly(pRace):
			if pModuleName:
				pModule=__import__(pModuleName)
				self.Node.SetAI(pModule.CreateAI(kArgs))
			else:
				if self.GetNode().GetShipProperty().IsStationary() or self.IsStationary() :
					from Custom.AdvancedTechnologies.Data.AI import ATP_SBAllyAI
					self.Node.SetAI(ATP_SBAllyAI.CreateAI(self.Node))
				else:
					from Custom.AdvancedTechnologies.Data.AI import ATP_GeneralAllyAI
					self.Node.SetAI(ATP_GeneralAllyAI.CreateAI(self.Node))
			
			pFriendlies = pMission.GetFriendlyGroup()
			pFriendlies.AddName(self.Node.GetName())

		elif pPlayerRace.IsNeutral(pRace):
			if pModuleName:
				pModule=__import__(pModuleName)
				self.Node.SetAI(pModule.CreateAI(kArgs))
			else:
				if self.GetNode().GetShipProperty().IsStationary() or self.IsStationary():
					from Custom.AdvancedTechnologies.Data.AI import ATP_SBNeutralAI
					self.Node.SetAI(ATP_SBNeutralAI.CreateAI(self.Node))
				else:
					from Custom.AdvancedTechnologies.Data.AI import ATP_GeneralNeutralAI
					self.Node.SetAI(ATP_GeneralNeutralAI.CreateAI(self.Node))

			pNeutrals = pMission.GetNeutralGroup()
			pNeutrals.AddName(self.Node.GetName())

		## Upperclass
		Holder.AssignAI(self,kArgs,force)

	## Warping
	#################
	def WarpToSolar(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Ship_WarpToSolar')

		## Some #assertions
		#assert pHolder
		#assert pHolder.GetSolar()
		#assert self.GetFleet().VoyageState == VOYAGING
		#assert self.GetFleet().State == WARPING
		#assert self.State == NORMAL

		## #debug 
		#debug("ship "+self.sName+" is warping to "+pHolder.GetSolar().sName)

		## Profiling
		idProfilingA = App.TGProfilingInfo_StartTiming('Ship_WarpToSolarSolars')

		## Destination solar
		pSolar = pHolder.GetSolar()
		pOwnSolar = self.GetSolar()

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfilingA)

		## Rendered?
		if self.IsRendered():
			## Profiling
			idProfilingA = App.TGProfilingInfo_StartTiming('Ship_WarpToSolarReal')


			## Game warp
			pWay = pSolar.GetChildByName("__IN__"+str(self.ID))
			#assert pWay
			#assert pWay.Node		

			## Assign the AI to warp out
			self.AssignAI([AI_PATH+".ATP_WarpToAI",pSolar,pWay],TRUE)

			## Set collisions off
			self.Node.SetCollisionsOn(FALSE)

			## Stop local profiling
			App.TGProfilingInfo_StopTiming(idProfilingA)


		## Not rendered
		else:
			## Profiling
			idProfilingA = App.TGProfilingInfo_StartTiming('Ship_WarpToSolarCon')

			## Fake the warp out
			gEvent, pEvent = self.FakeEvent(0,self,pOwnSolar)

			## Notify the ship & system
			self.WarpOut(gEvent)
			pOwnSolar.WarpOut(gEvent)

			## The conceptual warp end
			self.AddDelay("ConceptualWarpEnd",self.Jitter(60.0,25.0))

			## Garbage
			pEvent.delete()

			## Stop local profiling
			App.TGProfilingInfo_StopTiming(idProfilingA)


		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def ConceptualWarpEnd(self,pEvent):
		## #assert state
		#assert self.State == WARPING
		
		## Our own solar
		pSolar = self.GetSolar()

		## Fake the warp in
		gEvent, pEvent = self.FakeEvent(0,self,pSolar)

		## Notify the ship & system
		self.WarpIn(gEvent)
		pSolar.WarpIn(gEvent)

		## Garbage
		pEvent.delete()
		
	## Quick warp
	#########################
	def MoveToSolar(self,pHolder):
		## Some #assertions
		#assert pHolder
		#assert pHolder.GetSolar()
		#assert self.GetFleet().VoyageState == VOYAGING
		#assert self.GetFleet().State == WARPING
		#assert self.State == NORMAL

		## #debug
		#debug("ship "+self.sName+" is quickwarping to "+pHolder.GetSolar().sName)

		## Destination
		pSolar = pHolder.GetSolar()
		pOwnSolar = self.GetSolar()

		## Fake the warp out
		gEvent, pEvent = self.FakeEvent(0,self,pOwnSolar)

		## Notify the ship & system
		self.WarpOut(gEvent)
		pOwnSolar.WarpOut(gEvent)

		## Real move
		if self.IsRendered():			
			## Move the ship
			from Actions import ShipScriptActions
			ShipScriptActions.MoveBetweenSetsAction(None,self.Node.GetObjID(),pSolar.Node.GetName())

		## Garbage
		pEvent.delete()
		
		## Fake the warp in
		gEvent, pEvent = self.FakeEvent(0,self,pSolar)

		## Notify the ship & system
		self.WarpIn(gEvent)
		pSolar.WarpIn(gEvent)

		## Garbage
		pEvent.delete()


	## Warp events
	###############################
	def WarpOut(self,gEvent):
		## Data from the event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		pSolar = pEvent.GetDestination()

		## Me?
		#assert self.ID == pShip.ID
		#assert self.State == NORMAL
		
		## #debug
		#debug("ship "+self.sName+" has warped out")

		## Change the state
		self.SetState(WARPING)

		## Notify our fleet
		self.GetFleet().WarpOut(gEvent)

	def WarpIn(self,gEvent):
		## Data from the event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		pSolar = pEvent.GetDestination()

		## Me?
		#assert self.ID == pShip.ID

		## #debug
		debug("ship "+self.sName+" has warped in")

		## Correct state
		#assert self.State == WARPING		

		## Set the state
		self.SetState(NORMAL)
	
		## Notify our fleet
		self.GetFleet().WarpIn(gEvent)			
		
		## Reset collisions
		self.AddDelay("DelayedResetCollisions",4.0)

		## AI
		self.AssignAI()

		debug("end ship "+self.sName+" has warped in")
		
	
	def DelayedResetCollisions(self,pEvent):
		## Reset collisions
		if self.Node:
			self.Node.SetCollisionsOn(TRUE)
	
	

	## Intercepting
	#########################################
	def Intercept(self,pHolder):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Fleet_Intercept')

		## #assertions
		#assert pHolder
		#assert self.GetFleet().VoyageState == VOYAGING
		#assert self.GetFleet().State == INTERCEPTING
		#assert self.State == NORMAL

		## debug
		debug('I, ship '+self.sName+' am intercepting '+pHolder.sName)	
		
		## Action
		self.SetState(INTERCEPTING)

		## debug
		debug('I, ship '+self.sName+' am intercepting '+pHolder.sName)

		## Rendered?	
		if pHolder.IsRendered():
			## Ship must be rendered now
			#assert self.IsRendered()

			## Use AI to intercept
			if not self.INTERCEPT_DONE:
				self.INTERCEPT_DONE = GetNextEventType()

			self.AddHandler(self.INTERCEPT_DONE,"InterceptDone")
			self.AssignAI([AI_PATH+".ATP_Intercept",pHolder,self.INTERCEPT_DONE],TRUE)

			## debug
			debug('I, ship '+self.sName+' am intercepting WITH AI'+pHolder.sName)			
		else:	
			## Delay the intercept
			self.AddDelay("InterceptDone",self.Jitter(20.0),self,pHolder)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def URR_Intercept(self):
		#assert self.State == INTERCEPTING	## Must be already intercepting
		#assert self.IsRendered()		## must be rendered
		
		## Remove the clock
		self.RemoveClock("InterceptDone")
		self.AddHandler(self.INTERCEPT_DONE,"InterceptDone")	

		## Holder changed/update, replot course
		self.AssignAI([AI_PATH+".ATP_Intercept",self.GetHolder(),self.INTERCEPT_DONE],TRUE)

	def RUR_Intercept(self):
		#assert self.State == INTERCEPTING	## Must be already intercepting
		#assert not self.IsRendered()		## must not be rendered

		## Delay the intercept
		self.RemoveHandler(self.INTERCEPT_DONE,"InterceptDone")
		self.AddDelay("InterceptDone",20.0,self,self.GetHolder())

	def InterceptDone(self,gEvent):
		## #assertions
		#assert self.State == INTERCEPTING
		
		## debug
		debug('I, ship '+self.sName+' have done intercepting')

		## Assign normal AI
		if self.IsRendered():
			self.AssignAI()

		## Statechange
		self.SetState(NORMAL)

		## debug
		debug('I, ship '+self.sName+' have done intercepting')

		## Notify our fleet
		self.GetFleet().InterceptDone(gEvent)

		## Remove the handler
		self.RemoveHandler(self.INTERCEPT_DONE,"InterceptDone")
		self.RemoveClock("InterceptDone")


	## Bridge and Crew
	##################################
	def GetBridge(self):
		## Attr defined ?
		if hasattr(self,'pBridge'):
			if self.pBridge:
				return self.pBridge

		## Make a new bridge
		import ATP_Bridge
		self.pBridge = ATP_Bridge.Bridge()

		## Our data
		pVesselType = self.GetRace().GetVesselType(self.sGfx)
	
		## Bind it
		self.pBridge.Bind(self,pVesselType.sBridgeType)

		## Return
		return self.pBridge

	def Contact(self):
		## Pass it through
		self.GetBridge().Contact()
		

	## Destruction
	###########################################
	def SelfDestroyed(self,gEvent):
		#debug("me, ship "+self.sName+" was destroyed")		

		## Forget the wreck of our ship
		self.SetNode(None)
		
		## Avoid doubled events
		if self.State == DEAD:
			return			
		
		## Data from the event
		# pEvent = DecodeEvent(gEvent)
		# pShip = pEvent.GetSource()
		

		## Me?
		#assert self.ID == pShip.ID

		## We were killed, if we have children, do something about them
		for pFleet in self.GetFleets():
			pFleet.HolderDestroyed()

		## Notify our parent
		self.GetFleet().ShipDestroyed(self)

		## Change the state
		self.SetState(DEAD)
		
		## Delete ourself
		self.delete()	
	
	def Kill(self):
		#debug("me, ship "+self.sName+" was killed")

		## Avoid doubled events
		if self.State == DEAD:
			return

		## We were killed, if we have children, do something about them
		for pFleet in self.GetFleets():
			pFleet.HolderDestroyed()

		## Destroy our node
		if self.Node:
			if not self.Node.IsDying() and not self.Node.IsDead():
				self.Node.RunDeathScript()
		self.SetNode(None)

		## Notify our fleet
		self.GetFleet().ShipDestroyed(self)

		## Change the state
		self.SetState(DEAD)
		
		## Delete ourself
		self.delete()					

class PlayerShip(Ship):
	def __init__(self,ID=None):
		Ship.__init__(self,ID)
		
		self.OldSysID	  = None
		self.CurrentSysID = None
		self.t = 0.0
		

		## Create a listener for the warpbutton
		self.AddHandler(App.ET_WARP_BUTTON_PRESSED,"WarpButtonPressed")

		## Update the node, just be sure
		import MissionLib
		self.Node = MissionLib.GetPlayer()

	

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = PlayerShip("+str(self.ID)+")")

		## Upperclass
		Ship.save(self,FALSE)

		## Our lines
		write_save_file("self.OldSysID = "+str(self.OldSysID))
		write_save_file("self.CurrentSysID = "+str(self.CurrentSysID))

	def Bind(self,pFleet,sName="",sGfx=""):
		self.SetName(PLAYER)
		self.Migrate(pFleet)
		
		## Register the node
		import MissionLib
		self.Node=MissionLib.GetPlayer()
		self.Node.SetInvincible(TRUE)
				
		## Extend sensorrange
		pSensors=self.Node.GetSensorSubsystem()
		if pSensors:
			pSensors.GetProperty().SetBaseSensorRange(SENSOR_MULTIPLYER*pSensors.GetBaseSensorRange())
	
	def IsRendered(self):
		return TRUE

	def Render(self,pSet):
		#assert pSet
		
		## Update the node, just be sure
		import MissionLib
		self.Node=MissionLib.GetPlayer()

		## Update the currentsys
		self.CurrentSysID=GetByNode(self.Node.GetContainingSet()).ID

		## Nodecache
		self.EnterNodeCache()

		## Add a #debug clock
		# self.AddClock("BCPhysics",0.25)

	def Regulise(self):
		## Synchronise the player with the universe
		pSolar = self.GetSolar()
		pSolar.Setup()

		#pSet = self.Node.GetContainingSet()
		#self.Node = loadspacehelper.CreateShip('NubianCruiser',pSet,'player2','')
		#assert self.Node
		#pGame = App.Game_GetCurrentGame()
		#pGame.SetPlayer(self.Node)
			
		from Actions import ShipScriptActions
		ShipScriptActions.MoveBetweenSetsAction(None,self.Node.GetObjID(),pSolar.Node.GetName())		

	def BCPhysics(self,pEvent):
		A=self.Node.GetAccelerationTG()
		V=self.Node.GetVelocityTG()
		self.t=self.t+0.25
		#debug("["+str(self.t)+","+str(V.Length())+"],")

	def Unrender(self):
		pass

	def Kill(self):
		## Game is over
		GetGame().GameOver()

	def SelfDestroyed(self,gEvent):
		## Game is over
		GetGame().GameOver()

	def AssignAI(self,kArgs=None,force=FALSE):
		if not force:
			return	
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]		
		if not kArgs:
			self.Node.ClearAI()
			return

		## Arguments
		pModuleName=kArgs.pop(0)
		kArgs.insert(0,self)			
		
		## Use a MissionLib function
		import MissionLib
		pModule=__import__(pModuleName)
		MissionLib.SetPlayerAI("Helm",pModule.CreateAI(kArgs))

	def WarpIn(self,gEvent):
		pEvent = DecodeEvent(gEvent)

		debug('B warp in call player')

		## New system
		pSolar = pEvent.GetDestination()
		pShip  = pEvent.GetSource()		

		## Standard calls
		Ship.WarpIn(self,gEvent)

		## Update the Starcharts
		import ATP_StarCharts
		assert pSolar
		ATP_StarCharts.UpdateAfterWarp(pSolar)

		debug('E warp in call player')

		
	def WarpButtonPressed(self,pEvent):
		return

		## Player pressed warp button
		pWarpButton = App.SortedRegionMenu_GetWarpButton()
		pModule=__import__(pWarpButton.GetDestination())
		
		## Find the destination
		sModule = pWarpButton.GetDestination()
		sName = sModule[string.rfind(sModule,'.')+1:]
		
		pSolar = GetUniverse().GetChildByName(sName)
		pSolar.RenderAndRandomise()

		## #debug
		#debug(__name__+": Warp button pressed: "+str(pSolar)+" Wake up!!!")
	 
		## Send the entire fleet to system
		if pSolar.IsExactTypeOf(SOLAR):
			pHolder = self.GetRandomItem(pSolar.GetAllPlanets())
		elif pSolar.IsExactTypeOf(STARBASE_SYSTEM):
			pHolder = pSolar.GetBase()
		else:
			pHolder = pSolar
		pHolder = pSolar

		## Voyage...
		self.GetFleet().Voyage(pHolder)

	def IsConceptual(self,*lArgs):
		SID = self.Node.GetContainingSet().GetObjID()

		for pItem in lArgs:
			pSet = pItem.GetSolar().Node
			if pSet:
				if pSet.GetObjID() == SID:
					return FALSE	
		return TRUE
	
	

def IsWarping(pShip):
	if not pShip:
		return FALSE

	pWarp = pShip.GetWarpEngineSubsystem()
	if not pWarp:
		return FALSE

	if pWarp.GetWarpSequence():
		return TRUE

	return FALSE

def IsConceptualWarp(pGroup,pHolder):		 
	pOwnSolar  = pGroup.GetSolar()
	pDestSolar = pHolder.GetSolar()

	## Any system active?
	pPlayerSolarID	= GetPlayerShip().GetSolar().ID
	pOwnSolar 	= pGroup.GetSolar()
	pDestSolar	= pHolder.GetSolar()

	## Conceptual or real?
	return not (pOwnSolar.ID == pPlayerSolarID or pDestSolar.ID == pPlayerSolarID)

	


