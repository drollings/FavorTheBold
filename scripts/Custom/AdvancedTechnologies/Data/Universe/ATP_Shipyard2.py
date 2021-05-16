import App

from ATP_Object   import *
from ATP_Vessels  import *

class Shipyard(Ship):
	IDLE   = 0
	BUILD  = 1
	REPAIR = 2

	CONCEPTUAL_CYCLE = 50.0
	RENDERED_CYCLE   = 1.0
	RECONFIRM_ORDERS = 25.0
	START_HULL_PERCENTAGE = 0.2
	SHIPYARD_BUILDSPEED = 0.25
	INITIAL_ORDERS = 2.0

	def __init__(self,ID=None):
		Ship.__init__(self,ID)
					
		self.BuildSpeed = Shipyard.SHIPYARD_BUILDSPEED
		self.iMode 	= Shipyard.BUILD
		self.iMode 	= Shipyard.REPAIR

		if self.iMode 	== Shipyard.BUILD:
			self.AddGameDelay('BuildNewShip',self.Jitter(Shipyard.INITIAL_ORDERS,75.0))

	def GetBuildFleet(self):
		for pFleet in self.GetFleets():
			if pFleet.State == BUILDING:
				return pFleet
		return None

	def GetBuildShip(self):
		pFleet = self.GetBuildFleet()
		if pFleet:
			for pShip in pFleet.GetShips():
				# if pShip.State == BUILDING:
				return pShip
		return None

	def IsRepairYard(self):
		return (self.iMode == Shipyard.REPAIR)

	def BuildNewShip(self,gEvent=None):
		## debug	
		# debug(self.sName+': BuildNewShip()')

		## Ask for a new ship to build
		pRace = self.GetRace()
		sGfx,sName = pRace.ShipyardAskForOrders(self)

		## A valid ship?
		if not sGfx:
			## No orders, ask again in a while
			self.AddGameDelay('BuildNewShip',self.Jitter(Shipyard.RECONFIRM_ORDERS))
			return

		## Start building the new ship
		pFleet = Fleet()
		pFleet.Bind(pRace,self,sName,'{'+sGfx+'}')

		## Set it building
		pFleet.SetState(BUILDING)

		## The build ship
		pShip = pFleet.GetShips()[0]

		## Rendered ?
		if self.IsRendered():
			## Start conditions
			pShip.SetBuildPercentage(0.0)
			pShip.SetHullPercentage(Shipyard.START_HULL_PERCENTAGE)

			## Construct it in a real way
			pFleet.Render(self.GetSolar().Node)

			## Assign AI
			pFleet.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],FALSE)

			## Position it
			pWay = self.GetChildByName('centre')
			vSpot = pWay.GetPosition()
			pFleet.SetPosition(vSpot)

			## Find the build ship
			pShip = self.GetBuildShip()
			assert pShip
			
			## Push it into the centre module
			M_centre = self.GetChildByName('module_centre')
			M_centre.EnterPush(pShip)

			## Create a real clock
			self.AddSpaceClock('RenderedBuild',Shipyard.RENDERED_CYCLE)

			## debug	
			# debug(self.sName+': BuildNewShip(): Rendered new fleet '+pFleet.sName)

		else:
			## Start conditions
			pShip.SetBuildPercentage(0.1)
			pShip.SetHullPercentage(Shipyard.START_HULL_PERCENTAGE)

			## Create a conclock
			self.AddSpaceClock('ConceptualBuild',self.Jitter(Shipyard.CONCEPTUAL_CYCLE,15.0))

			## debug	
			# debug(self.sName+': BuildNewShip(): Conceptual new fleet '+pFleet.sName)

		## Raise the creation event
		self.GetSolar().ObjectCreation(pShip)


	def RenderedBuild(self,gEvent):
		## For now our hull will indicate our build speed mod
		fAdd = self.BuildSpeed * self.HullPercentage
		
		## What ship do we build ?
		pShip = self.GetBuildShip()
		assert pShip

		## Add the build points
		pShip.AddBuildPoints(fAdd)

		## Visualise it with the hull
		pShip.DamageHull(-fAdd/pShip.GetBuildPoints()*pShip.GetHull()*(1-Shipyard.START_HULL_PERCENTAGE))

		## debug
		# debug(self.sName+' REAL Building ship '+pShip.sName+' with buildstatus '+str(pShip.GetBuildPercentage()))

		## Done ?
		if pShip.GetBuildPercentage()==1.0:
			self.RenderedBuildDone()

	def RenderedBuildDone(self):
		## Release the build fleet by changing its state
		pFleet = self.GetBuildFleet()
		pFleet.SetState(ENTERING)
		
		## Unlock the centre module
		M_centre = self.GetChildByName('module_centre')
		M_centre.UnlockExit()
		
		## And relock
		M_centre.LockExit()

		## Remove the build clock
		self.RemoveClock('RenderedBuild')

		## debug
		debug(self.sName+' Done Building ship.')		
				
	def ConceptualBuild(self,gEvent):
		## For now our hull will indicate our build speed mod
		fAdd = self.BuildSpeed * self.HullPercentage *  Shipyard.CONCEPTUAL_CYCLE
		
		## What ship do we build ?
		pShip = self.GetBuildShip()
		if not pShip:
			return			

		## Add the build points
		pShip.AddBuildPoints(fAdd)

		## debug
		# debug(self.sName+' CON Building ship '+pShip.sName+' with buildstatus '+str(pShip.GetBuildPercentage()))

		## Done ?
		if pShip.GetBuildPercentage()==1.0:
			self.ConceptualBuildDone()

	def ConceptualBuildDone(self):
		## Release the build fleet by changing its state
		pFleet = self.GetBuildFleet()
		pFleet.SetState(NORMAL)

		## debug
		# debug(self.sName+' Done Building ship '+pFleet.GetShips()[0].sName)

		## New ship		
		self.AddSpaceDelay('BuildNewShip',self.Jitter(Shipyard.RECONFIRM_ORDERS))

	def Render(self,pSet):
		## Upper class
		Ship.Render(self,pSet)	
		
		## Own part
		import ATP_Extras

		## Flags
		ACTIVE  = ATP_Extras.QueueModule.ACTIVE
		PASSIVE = ATP_Extras.QueueModule.PASSIVE		

		## Three Vectors & Waypoints
		import MissionLib
		pOldWaypoint = None
		pWays = ()
		for sWay in ( 'in1' , 'centre' , 'out1' , 'out2'):
			## Waypoint
			pWaypoint = Waypoint(sWay,self)
			
			## Position
			vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(self.Node,sWay)
			if not vPos:
				raise RuntimeError , 'Position Orienatation Property '+sWay+' not found in model '+self.sGfx				

			## Set
			PositionObjectFromInfo(pWaypoint.Node,self.Node,vPos,vFwd,vUp)

			## Link them
			if pOldWaypoint:
				pOldWaypoint.Node.InsertAfterObj(pWaypoint.Node)

			## Oldwaypoint
			pOldWaypoint = pWaypoint

			## Collect them
			pWays = pWays + ( pWaypoint , )

		## Waypoints
		pIn1,pCentre,pOut1,pOut2 = pWays

		## Four modules
		# Bind(iCapacity,lPreModules,iEnterMode,lPostModules,iExitMode,lActions)
		M_in_queue	= ATP_Extras.QueueModule('module_in_queue',	self )
		M_in		= ATP_Extras.QueueModule('module_in',		self )
		M_centre	= ATP_Extras.QueueModule('module_centre',	self )
		M_out		= ATP_Extras.QueueModule('module_out',		self )
		M_out_queue	= ATP_Extras.QueueModule('module_out_queue',	self )

		## AI
		sAI1 = ( AI_PATH+'.ATP_PositionByCirclingAI',	pIn1,		self, 	M_in.GetTransferDone(),		3.5	) 
		sAI2 = ( AI_PATH+'.ATP_DockExactAI',		pCentre,	self,	M_in.GetTransferDone(),		pCentre	)
		sAI3 = ( AI_PATH+'.ATP_DockAI', 		pOut1,		self,	M_out.GetTransferDone(),	pOut1	)
		sAI4 = ( AI_PATH+'.ATP_MoveAIWCA',		pOut2,		self,	M_out_queue.GetTransferDone(),	pOut2	)

		## Binding
		M_in_queue.Bind	(1000,	(),		PASSIVE,	(M_in,),	ACTIVE,	()		)
		M_in.Bind	(1,	(M_in_queue,),	ACTIVE,		(M_centre,),	ACTIVE,	(sAI1,sAI2)	)
		M_centre.Bind	(1,	(M_in,),	ACTIVE,		(M_out,),	ACTIVE,	()		)
		M_out.Bind	(1,	(M_centre,),	ACTIVE,		(M_out_queue,),	ACTIVE,	(sAI3,)		)
		M_out_queue.Bind(1000,	(M_out,),	ACTIVE,		(),		ACTIVE,	(sAI4,)		)

		## Sharing
		ATP_Extras.AlignModules( (M_in,M_out,M_centre) )

		## Repairmode ?
		if self.iMode == Shipyard.REPAIR:
			M_centre.SetRepairMode()

		elif self.iMode == Shipyard.BUILD:
			## Lock modules
			M_in_queue.LockEntrance()
			M_centre.LockExit()

			## What ship are we building?
			pShip = self.GetBuildShip()

			if pShip:
				## Set it in the centre module
				M_centre.EnterPush(pShip)

				## Switch the clocks

				### Remove the conceptual clock
				self.RemoveClock('ConceptualBuild')
				self.RemoveClock('RenderedBuild')

				### Add a clock for the rendered build
				self.AddSpaceClock('RenderedBuild',Shipyard.RENDERED_CYCLE)
				
				## Start hull
				pShip.SetHullPercentage(Shipyard.START_HULL_PERCENTAGE + (1-Shipyard.START_HULL_PERCENTAGE) * pShip.GetBuildPercentage() )
				
				#debug('shipyard2: switching to renderedclock in render()')

	def Randomise(self,type=UNIVERSE_ELEMENT,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		## Our children
		lObjects = self.GetChildren()

		## The build fleet
		pFleet = self.GetBuildFleet()
		if pFleet:
			lObjects.remove(pFleet)
		
		## Remove the modules and waypoints
		lObjectsBis=[]
		for pObject in lObjects:
			if not pObject.IsTypeOf(EXTRA):
				lObjectsBis.append(pObject)			

		## Randomise the remaining objects
		self.RandomiseFromList(lObjectsBis,radix,fMinAngle,fMaxAngle)

		## Center the other
		if pFleet:
			pWay = self.GetChildByName('centre')
			vSpot = pWay.GetPosition()
			pFleet.SetPosition(vSpot)

	def AssignAI(self,kArgs=None,force=FALSE):
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]

		#debug("Assigning AI for "+self.sName)
   
		## Own AI
		Ship.AssignAI(self,kArgs,force)

		## Children AI
		for pFleet in self.GetFleets():
			if pFleet.State == INSIDE:
				pFleet.AssignAI([AI_PATH+".ATP_HaltAI"],FALSE)
			elif pFleet.State == NORMAL:
				pFleet.AssignAI()
			elif pFleet.State == INTERCEPTING:
				pass
			elif pFleet.State == ENTERING:
				raise RuntimeError
			elif pFleet.State == EXITING:
				raise RuntimeError
			elif pFleet.State == WARPING:
				pass
			elif pFleet.State in (BUILDING,REPAIR):
				pFleet.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],FALSE)
			else:
				raise RuntimeError

	def Unrender(self):
		## Basic
		Ship.Unrender(self)

		## What ship are we building?
		pShip = self.GetBuildShip()

		if pShip:			
			if self.iMode == Shipyard.BUILD:
				## Switch the clocks

				### Remove the rendered clock
				self.RemoveClock('RenderedBuild')

				### Add a clock for the rendered build
				self.AddSpaceClock('ConceptualBuild',Shipyard.CONCEPTUAL_CYCLE)

	
	def RenderedEnterFleet(self,pFleet):
		## Enter module
		pModule = self.GetChildByName('module_in_queue')

		for pShip in pFleet.GetShips():
			## State change
			pShip.SetState(ENTERING)

			## No collisions
			pShip.Node.EnableCollisionsWith(self.Node,FALSE)
			self.Node.EnableCollisionsWith(pShip.Node,FALSE)

			## Push the ships in it
			pModule.EnterPush(pShip)	

	def EnterPush(self,pShip):
		## A ship was pushed out of the last module

		## debug	
		debug(self.sName+ ': Push out of '+pShip.sName)
		
		## Processing done
		self.EnterDone(pShip)
	
		if self.iMode == Shipyard.BUILD:
			## debug
			debug(self.sName+ ': Build complete.')

			## Organise a voyage
			pHolder = self.GetHolder()
			pShip.GetFleet().Voyage(self.GetHolder(),bInside=FALSE)		

			## New ship
			self.AddSpaceDelay('BuildNewShip',self.Jitter(Shipyard.RECONFIRM_ORDERS))

		elif self.iMode == Shipyard.REPAIR:
			## Normal AI
			pShip.AssignAI(force=TRUE)

		## Yes collisions
		pShip.Node.EnableCollisionsWith(self.Node,TRUE)
		self.Node.EnableCollisionsWith(pShip.Node,TRUE)

		## We accept
		return ACK

	def ExitPull(self):
		## Should not happen
		return None

	def EnterDone(self,pShip):
		## Upperclass
		Ship.EnterDone(self,pShip)

		## Concerned fleet
		pFleet = pShip.GetFleet()

		## Done ?	
		if pFleet.State == INSIDE:
			## Fake the repair
			self.HeavyRepair(pFleet)
			
			## Player?			
			if pFleet.ID == PLAYER_FLEET_ID:
				## Play repair complete sound
				GetPlayerBridge().GetEngineer().Speak('ge111') ## Repairs complete, sir

	def ShipDestroyed(self,pShip,pFleet):
		## Superclass
		Ship.ShipDestroyed(self,pShip,pFleet)

		## Own case
		if pShip.State == BUILDING:
			## Clear the clocks
			if self.IsRendered():
				self.RemoveClock('RenderedBuild')
			else:
				self.RemoveClock('ConceptualBuild')

			## Make a new ship
			self.AddSpaceDelay('BuildNewShip',self.Jitter(Shipyard.RECONFIRM_ORDERS))

	## Repair
	#################################################
	def HeavyRepair(self,pFleet):
		## Quickly done
		pFleet.SetState(REPAIR)
		pFleet.SetState(INSIDE)
	
	def SwapForRepair(self,pShip,bHeavy=FALSE):
		## Data dict
		if not hasattr(self,'dRepair'):
			## Create the dict
			self.dRepair = {}
			
			## Create the clock to cycle
			self.AddSpaceClock('RepairCycle',Holder.REPAIR_CYCLE)

		## The repair subsystem
		pRepair = pShip.Node.GetRepairSubsystem()
		if pRepair:
			## Property
			pRepairProp = pRepair.GetProperty()
			
			## Data
			iPoints = pRepairProp.GetMaxRepairPoints()
			iEng	= pRepairProp.GetNumRepairTeams()
			fDis	= pRepairProp.GetDisabledPercentage()

			## Save
			self.dRepair[pShip.ID] = (iPoints,iEng,fDis)

			## Turn the repair system on
			pRepairProp.SetDisabledPercentage(0.0)
			pRepair.SetConditionPercentage(max(0.25,pRepair.GetConditionPercentage()))

			## Increase the strength
			pRepairProp.SetMaxRepairPoints(max(750,iPoints*10))

			## Increase the number of teams
			pRepairProp.SetNumRepairTeams(max(10,iEng*4))

		## Repair all broken systems
		if bHeavy:
			## Iterate over all systems
			pIterator = pShip.Node.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.Node.GetNextSubsystemMatch(pIterator)
			while (pSubsystem != None):
				if pSubsystem.GetConditionPercentage() == 0.0:
					pSubsystem.SetConditionPercentage(0.01)					
				pSubsystem = pShip.Node.GetNextSubsystemMatch(pIterator)
			pShip.Node.EndGetSubsystemMatch(pIterator)
		

	def UnswapForRepair(self,pShip):
		## The repair subsystem
		pRepair = pShip.Node.GetRepairSubsystem()
		if pRepair and self.dRepair.has_key(pShip.ID):
			## Property
			pRepairProp = pRepair.GetProperty()
			
			## Saved data
			iPoints,iEng,fDis = self.dRepair[pShip.ID]

			## Reset data
			pRepairProp.SetDisabledPercentage(fDis)
			pRepairProp.SetMaxRepairPoints(iPoints)
			pRepairProp.SetNumRepairTeams(iEng)

			## Forget data
			del self.dRepair[pShip.ID]

		## Unlock and relock the centre
		M_centre = self.GetChildByName('module_centre')
		M_centre.UnlockExit()		

		## Ships left?
		if not self.dRepair:
			## Remove the clock
			self.RemoveClock('RepairCycle')

			## Remove the dict
			del self.dRepair
		
	def RepairCycle(self,gEvent):
		## Here we check if the ships are repaired		
		for SID in self.dRepair.keys():
			## The ship
			pShip = GetByID(SID)

			## Is the ship hale ?
			if pShip.IsHale():
				## Set it done
				self.UnswapForRepair(pShip)			


def PositionObjectFromInfo(pObject,pLocalInfoObject, vPos, vFwd, vUp,Z=0.0):
	M=App.TGMatrix3()
	M.MakeIdentity()
	M.MakeZRotation(toRad(Z))
	vWorldPos = pLocalInfoObject.GetWorldLocation()
	mWorldRot = pLocalInfoObject.GetWorldRotation()
	mWorldRot = M.MultMatrixLeft(mWorldRot)
	
	vPos.MultMatrixLeft( mWorldRot )
	vPos.Add(vWorldPos)
	vFwd.MultMatrixLeft( mWorldRot )
	vUp.MultMatrixLeft( mWorldRot )

	# Move the waypoint to this position/orientation.
	GetByNode(pObject).SetPosition(vPos)
	pObject.AlignToVectors(vFwd, vUp)
	pObject.UpdateNodeOnly()
