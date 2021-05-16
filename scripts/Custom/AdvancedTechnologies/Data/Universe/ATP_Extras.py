import App

from ATP_Object import *
from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

class Extra(UniverseElement):
	def __init__(self,sName,Parent,V=NULL_VECTOR,bAttach=FALSE):
		## Super class
		UniverseElement.__init__(self)

		self.Attached =  bAttach
		self.sName = sName[:]
		self.Move(Parent)
		UniverseElement.SetPosition(self,V)		

	def save(self,first=TRUE):
		pass
		
	def post_save(self):
		pass

	def IsSaveable(self):
		return FALSE					
		
	def Attach(self,V = NULL_VECTOR):
		P = self.GetParent().GetPosition()
		P.Add(V)
		self.SetPosition(P)
		self.Attached = TRUE

	def SetPosition(self,V):
		if self.Attached:
			return
		UniverseElement.SetPosition(self,V)

		#debug(self.sName +" : "+printVector(V))

	def delete(self):
		## Remove wrapper related things
		for e,f in self.Timers.keys():
			self.RemoveClock(f,e)
		for e,s in self.Handlers.keys():
			self.RemoveHandler(e,s)
		
		## Base class delete
		TreeElement.delete(self)

	def Randomise(self):
		return		

	def Unrender(self):
		## Upperclass
		UniverseElement.Unrender(self)

		## Delete us aswell
		self.delete()


class Waypoint(Extra):
	def __init__(self,sName,Parent,V=NULL_VECTOR,bAttach=FALSE,NavPoint=FALSE):
		##Superclass
		Extra. __init__(self,sName,Parent,V,bAttach)

		## A navpoint?
		self.NavPoint = NavPoint
		
		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)
	

	def Render(self,pSet):
		## Base class
		# Extra.Render(self,pSet)
		debug('Rendering '+self.sName)

		if not self.NavPoint:
			self.Node = App.Waypoint_Create(self.sName+"_"+str(self.ID),pSet.GetName(),None)
		else:
			self.Node = App.Waypoint_Create(self.sName,pSet.GetName(),None)

		if self.Attached:
			ParentNode = self.GetParent().Node
			ParentNode.AttachObject(self.Node)
			self.Node.SetTranslate(self.GetPosition())
		
		self.Node.SetNavPoint(self.NavPoint)
		self.Node.SetSpeed(5.0)
		self.Node.SetStatic(FALSE)
		self.Node.SetTranslate(self.vPosition)
		kForward = App.TGPoint3()
		kForward.SetXYZ(0,1,0)
		kUp = App.TGPoint3()
		kUp.SetXYZ(0,0,1)		
		self.Node.AlignToVectors(kForward, kUp)
		self.Node.UpdateNodeOnly()

		## Node cache
		self.EnterNodeCache()

		debug('End Rendering '+self.sName)

	def Unrender(self): ## Cleared of suspicion
		debug("Urendering "+self.sName+ " BEGIN")
		if self.Node:
			pSet = self.Node.GetContainingSet()
			if pSet:
				pSet.RemoveObjectFromSet(self.Node.GetName())
				self.Node.Destroy()

		self.PurgeNodeCache(self.Node)
		self.Node = None

		Extra.Unrender(self)
		debug("Urendering END")

class Bulb(Extra):
	def __init__(self,pSun,sName="",iNum=16,cColour=None):
		## Some nodes
		self.Nodes = []

		## Upper class
		Extra.__init__(self,sName,pSun,pSun.GetPosition(),FALSE)

		## Our stuff
		self.Num = iNum
		
		if not sName:
			sName = pSun.sName+"_BULB"

		if not cColour:
			cColour = pSun.GetColour()
		self.cColour = copyColour(cColour)	

		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)		
		
	def Render(self,pSet):
		debug('Rendering '+self.sName)

		## Get the sun
		pSun = self.GetHolder()
		pSolar = pSun.GetSolar()
		assert pSun

		Ni = self.cColour
		kForward = App.TGPoint3()
		kForward.SetXYZ(0.0,1.0,0.0)
		kUp = App.TGPoint3()
		kUp.SetXYZ(0.0,0.0,1.0)
		M=App.TGMatrix3()
		M.MakeIdentity()

		V = self.GetPosition()

		f = 2.5/(pSolar.GetNumSuns()+1)/self.Num

		for i in range(0,self.Num):
			kForward.MultMatrixLeft(M)
			kForward.Unitize()

			Node = App.LightPlacement_Create("Directional Light"+"_"+str(pSun.ID)+"_"+str(self.ID)+"_"+str(i),pSolar.GetName(), None)
			Node.SetStatic(FALSE)
			Node.SetNavPoint(FALSE)
			Node.SetTranslate(V)
			Node.AlignToVectors(kForward, kUp)
			Node.ConfigDirectionalLight(Ni.r,Ni.g ,Ni.b,f)
			Node.Update(TRUE)
			Node.UpdateNodeOnly()				

			M.MakeZRotation(toRad(360.0/self.Num))
			self.Nodes.append(Node)

			## Node cache
			self.EnterNodeCache(Node)

		self.Node = self.Nodes.pop(0)

		debug('End Rendering '+self.sName)		
		
	def Unrender(self):
		debug("Urendering "+self.sName+ " BEGIN")
		pSet = self.Node.GetContainingSet()
		if pSet:
			for Node in self.Nodes + [ self.Node ]:
				pSet.RemoveObjectFromSet(Node.GetName())
				Node.Destroy()
				self.PurgeNodeCache(Node)							
					
		self.Node = None
		self.Nodes = []	

		Extra.Unrender(self)
		debug("Urendering END")

	def SetPosition(self,V):
		## Upper cllas
		Extra.SetPosition(self,V)
		
		## Children
		for Node in self.Nodes:
			Node.SetTranslate(V)
	

class Ambient(Extra):
	def __init__(self,pHolder,cColour):
		## Upper class
		Extra.__init__(self,pHolder.sName+"_AMBIENT",pHolder,pHolder.GetPosition(),FALSE)

		## Our stuff
		self.cColour = copyColour(cColour)
		
		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)		
		
	def Render(self,pSet):
		debug('Rendering '+self.sName)

		## Base class
		# Extra.Render(self,pSet)

		## Create our object
		self.Node = App.LightPlacement_Create(self.sName+"_"+str(self.ID),self.GetSolar().sName, None)
		self.Node.SetStatic(FALSE)
		self.Node.SetNavPoint(FALSE)
		self.Node.SetTranslate(self.GetPosition())
		kForward = App.TGPoint3()
		kForward.SetXYZ(0.000000, 1.000000, 0.000000)
		kUp = App.TGPoint3()
		kUp.SetXYZ(0.000000, 0.000000, 1.000000)
		self.Node.AlignToVectors(kForward, kUp)
		self.Node.ConfigAmbientLight(self.cColour.r, self.cColour.g, self.cColour.b, self.cColour.a)
		self.Node.Update(TRUE)
		self.Node.UpdateNodeOnly()

		## Node cache
		self.EnterNodeCache()

		debug('End Rendering '+self.sName)

	def Unrender(self):
		debug("Urendering "+self.sName+ " BEGIN")

		pSet = self.Node.GetContainingSet()
		if pSet:
			pSet.RemoveObjectFromSet(self.Node.GetName())
			self.Node.Destroy()
		

		self.PurgeNodeCache(self.Node)
		self.Node = None

		Extra.Unrender(self)
		debug("Urendering END")	


class Backdrop(Extra):
	def __init__(self,pSolar,sGfx,Forward,Up,HS = 0.3 ,VS = 0.3 ,H = 1.0,V = 1.0,R = 3.0e+2):
		## Upper class
		Extra.__init__(self,pSolar.sName+"_BACKDROP",pSolar,NULL_VECTOR,TRUE)

		## Our stuff
		self.sGfx = sGfx
		self.Forward    = copyVector(Forward)
		self.Up		= copyVector(Up)
		self.H		= H
		self.V		= V
		self.R		= R
		self.HS		= HS
		self.VS		= VS
		
		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)
	

	def Render(self,pSet):
		debug('Rendering '+self.sName)

		## Base class
		# Extra.Render(self,pSet)

		## Create the back drop
		self.Node = App.BackdropSphere_Create()
		self.EnterNodeCache()
		Node = self.Node
		Node.SetName("Backdrop_"+str(self.ID))
		Node.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
		Node.AlignToVectors(self.Forward, self.Up)
		Node.SetTextureFileName(self.sGfx)
		Node.SetTargetPolyCount(256)
		Node.SetHorizontalSpan(self.HS)
		Node.SetVerticalSpan(self.VS)
		Node.SetSphereRadius(self.R)
		Node.SetTextureHTile(self.H)
		Node.SetTextureVTile(self.V)
		Node.Rebuild()
		pSet.AddBackdropToSet(Node,self.Node.GetName())
		Node.Update(TRUE)
		Node.UpdateNodeOnly()

		## Node cache
		self.EnterNodeCache()

		debug('End Rendering '+self.sName)

	def SetPosition(self,V):
		return


class Stars(Extra):
	def __init__(self,pSolar,sGfx,Forward,Up,R = 3.0e+2):
		## Upper class
		Extra.__init__(self,pSolar.sName+"_STAR",pSolar,NULL_VECTOR,TRUE)

		## Our stuff
		self.sGfx = sGfx
		self.Forward    = copyVector(Forward)
		self.Up		= copyVector(Up)		
		self.R		= R	

		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)
	

	def Render(self,pSet):
		debug('Rendering '+self.sName)

		## Base class
		# Extra.Render(self,pSet)

		## Create the back drop
		self.Node = App.StarSphere_Create()
		self.EnterNodeCache()
		Node = self.Node
		Node.SetName("Backdrop stars")
		Node.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
		Node.AlignToVectors(self.Forward, self.Up)
		Node.SetTextureFileName(self.sGfx)
		Node.SetTargetPolyCount(256)#256
		Node.SetHorizontalSpan(1.0)
		Node.SetVerticalSpan(1.0)
		Node.SetSphereRadius(self.R)
		Node.SetTextureHTile(22.0)#22
		Node.SetTextureVTile(11.0)#11
		Node.Rebuild()
		pSet.AddBackdropToSet(Node,"Backdrop stars")
		Node.Update(TRUE)
		Node.UpdateNodeOnly()

		debug('End Rendering '+self.sName)
		
	def SetPosition(self,V):
		return


class SolarNebula(Extra):
	
	def __init__(	self,
			pNebula,
			pSolar,
			sInternalGfx='data/Backgrounds/nebulaoverlaygreen.tga',
			sExternalGfx='data/Backgrounds/nebulaexternalgreen.tga',
			cColour = Colour(0.125,0.75,0.125),
			fSensorModifier=0.5,
			fVisibility=150.0*km						):

		## Upper class
		Extra.__init__(self,pNebula.GetName(),pSolar,NULL_VECTOR,TRUE)

		## Attributes
		self.sInternalGfx	= sInternalGfx[:]
		self.sExternalGfx	= sExternalGfx[:]
		self.fSensorModifier	= fSensorModifier
		self.fVisibility	= fVisibility
		self.fSeize		= pSolar.GetRadius() * 2.0
		self.cColour		= copyColour(cColour)		

		## Render
		pSet = pSolar.Node
		self.Render(pSet)	


	################
	# Create the nebulae
	################
	
	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# scale factor for sensors in the nebula [0.0, 1.0] where 1.0 is normal range and 0.0 is no sensors
	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)

	# NOTE: There is currently a problem with MetaNebulae; if they are to certain colors,
	# the entire region will be filled with nebulous substance. Until this is fixed,
	# all MetaNebulae will be temporarily set to a color that we know works.
	# The lines with the correct colors are commented out for now.

	def Render(self,pSet):
		## Create the main holder
		self.Node = App.MetaNebula_Create(self.cColour.r,self.cColour.g,self.cColour.b,self.fVisibility,self.fSensorModifier,self.sInternalGfx,self.sExternalGfx)

		## Add a sphere
		self.Node.AddNebulaSphere(0.0, 0.0, 0.0, self.fSeize)

		## Puts the nebula in the set
		pSet.AddObjectToSet(self.Node,self.sName)

		## Caching
		self.EnterNodeCache()


class Comet(Extra):
	def __init__(self,pHolder,sName='',fScale=50.0,fMass=2.0e+6):
		## Upper class
		Extra.__init__(self,"Nothing",pHolder,NULL_VECTOR,FALSE)

		## Our stuff
		### Take a random Gfx	
		i = int(self.GetRandom(1,4))
		if self.GetRandomSign() == -1.0:
			self.sGfx = 'asteroid' + str(i)
		else:
			self.sGfx = 'asteroidh' + str(i)
				
		self.fScale = fScale
		self.fMass = fMass

		## Our name
		if not sName:
			self.sName = 'Comet CPX' + str(self.ID)
		else:	
			self.sName = sName + str(self.ID) 	

		## Render
		pSet = self.GetSolar().Node
		self.Render(pSet)	

	def Render(self,pSet):
		debug('Rendering '+self.sName)

		## Base class
		# Extra.Render(self,pSet)

		## Load the model
		if not App.g_kLODModelManager.Contains(self.sGfx):
			pLODModel = App.g_kLODModelManager.Create(self.sGfx, 10000)
			pLODModel.AddLOD("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Objects/Asteroids/"+self.sGfx+".NIF", 10, 1.0e+8, 4.50, 4.50, 499, 500, None, None, None)
			pLODModel.SetTextureSharePath("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Objects/Asteroids")
			pLODModel.Load()

		## Create the comet
		pAsteroid = App.DamageableObject_Create(self.sGfx)
		pAsteroid.SetMass (self.fMass)
		pAsteroid.SetNetType(0)
		pAsteroid.SetStatic(FALSE)
		pAsteroid.SetUsePhysics(TRUE)
		pAsteroid.SetScale(self.fScale)
		pAsteroid.Update(TRUE)
		SName = App.TGString ()
		SName.SetString (self.sName)
		pSet.AddObjectToSet(pAsteroid,self.sName)
		pAsteroid.SetDisplayName(SName)

		## Register the node
		self.Node = pAsteroid
		self.EnterNodeCache()
	
		## Position, Orientation and Speed
		V = self.GetHolder().FindSuitablePosition(pAsteroid.GetRadius(),1000.0*km)
		self.SetPosition(V)
		pAsteroid.RandomOrientation()
		# S = copyVector(eY)
		# S.Scale(-5000.0*km)
		# pAsteroid.SetVelocity(S)
		# R = copyVector(eY)
		# R.Scale(toRad(30.0))
		# pAsteroid.SetAngularVelocity(R,App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
		# pAsteroid.UpdateNodeOnly()
		
		## Attach a waypoint to ourself	
		Waypoint(self.sName+' ',self,e0,bAttach=TRUE,NavPoint=TRUE)

		## Node cache
		self.EnterNodeCache()

		debug('End Rendering '+self.sName)


class QueueModule(Extra):
	ACTIVE = 1
	PASSIVE = 2

	RED = 3
	GREEN = 4
	ORANGE = 1000

	LOCKED = 1
	UNLOCKED = 2
	

	def __init__(self,sName,pHolder):
		## Own data
		self.PreModules = []
		self.Queue = []
		self.PostModules = []
		self.Capacity = 0
		self.bRepairMode = FALSE

		self.EnterMode = QueueModule.ACTIVE
		self.ExitMode  = QueueModule.ACTIVE
		self.EnterLock = QueueModule.UNLOCKED
		self.ExitLock  = QueueModule.UNLOCKED

		self.ActionList = []
		

		self.ET_TRANSFER_DONE = GetNextEventType()

		## Upperclass
		Extra.__init__(self,sName,pHolder)

		## Aligned modules
		self.AlignedModules = []

	def Render(self,pSet):
		## Assign a handler
		self.AddHandler(self.ET_TRANSFER_DONE,"TransferDone")

	def Unrender(self):
		## Remove the handler
		self.RemoveHandler(self.ET_TRANSFER_DONE,"TransferDone")

	def Bind(self,iCapacity,lPreModules,iEnterMode,lPostModules,iExitMode,lActions):
		self.Capacity = iCapacity
		for pModule in lPreModules:
			self.PreModules.append(pModule.ID)
		for pModule in lPostModules:
			self.PostModules.append(pModule.ID)
		self.EnterMode = iEnterMode
		self.ExitMode  = iExitMode
		pModule = self.GetHolder()
		for oAction in lActions:
			self.ActionList.append(list(oAction))

	def GetTransferDone(self):
		return self.ET_TRANSFER_DONE			

	def SetRepairMode(self,bOn = TRUE):
		self.bRepairMode = bOn

	def GetPostModules(self):
		ret=[]
		for ID in self.PostModules:
			ret.append(GetByID(ID))
		return ret
	
	def GetPreModules(self):
		ret=[]
		for ID in self.PreModules:
			ret.append(GetByID(ID))
		return ret

	def GetAlignedModules(self):
		ret=[]
		for ID in self.AlignedModules:
			ret.append(GetByID(ID))
		return ret

	## Locks
	##################################
	def LockEntrance(self):
		self.EnterLock = QueueModule.LOCKED

	def LockExit(self):
		self.ExitLock = QueueModule.LOCKED

	def UnlockEntrance(self):
		if self.EnterLock == QueueModule.LOCKED:
			## Lock change
			self.EnterLock = QueueModule.UNLOCKED

			## Active pull
			self.EnterPull()

	def UnlockExit(self):
		if self.ExitLock == QueueModule.LOCKED:
			## Lock change
			self.ExitLock = QueueModule.UNLOCKED

			## debug
			debug('Module '+self.sName+': Unlocking...')

			## Active push
			self.ExitPush()
		
	## Push & pull
	############################################
	def EnterPush(self,pShip):
		## Someone is feeding us a ship
		assert pShip

		## debug
		debug('Enterpush of ship '+pShip.sName)

		## Locked?
		if self.EnterLock == QueueModule.LOCKED:
			return NAK

		## The ship is pushed in, if possible
		iState = self.EnterShip(pShip)

		## Return the response
		return iState

	def EnterPull(self):
		## debug
		debug('Enterpull')

		## We must be able accept the ship
		if self.GetLoad()+1  > self.GetCapacity():
			return NAK

		## Locked?
		if self.EnterLock == QueueModule.LOCKED:
			return NAK

		## Actively find a ship
		iState = NAK
		pModules = self.GetPreModules()
		if pModules:
			for pModule in pModules:
				pShip = pModule.ExitPull()
				if pShip:
					iState = self.EnterShip(pShip)
					assert iState == ACK
					break
		else:
			pShip = self.GetHolder().ExitPull()
			if pShip:
				iState = self.EnterShip(pShip)
				assert iState == ACK
						
		## Effect		
		return iState

	def ExitPull(self):
		## debug
		debug('Exitpull')

		## Locked?
		if self.ExitLock == QueueModule.LOCKED:
			return None

		## Provide a ship
		pShip = self.ExitShip()
		
		if pShip:
			## Remove it from the queue
			self.Queue.remove((pShip.ID,QueueModule.RED))

			## Remove the handler for shipdeath
			self.RemoveHandler(pShip.GetStateStartEvent(DEAD),"ShipDestroyed")

			## A new ship?
			self.EatNewShip()

		## Return the ship
		return pShip			

	def ExitPush(self):
		## debug
		debug('Exitpush')

		## Locked?
		if self.ExitLock == QueueModule.LOCKED:
			return

		## Provide a ship
		pShip = self.ExitShip()

		## Is there one?
		if not pShip:
			return

		## debug
		debug('Module '+self.sName+': Pushing '+pShip.sName+' out.')

		## Feed it to the other
		iState = NAK
		pModules = self.GetPostModules()
		if pModules:
			for pModule in pModules:
				iState = pModule.EnterPush(pShip)
				if iState == ACK:
					break
		else:
			## Push it in the holder
			iState = self.GetHolder().EnterPush(pShip)
		
		if iState == ACK:
			## Remove it from the queue
			self.Queue.remove((pShip.ID,QueueModule.RED))

			## Remove the handler for shipdeath
			self.RemoveHandler(pShip.GetStateStartEvent(DEAD),"ShipDestroyed")

			## A new ship?
			iState = self.EatNewShip()


	def EatNewShip(self):
		## debug
		debug('Eat')
		
		## A new ship?
		iState = ACK
		while(iState == ACK):
			## By default nothing
			iState = NAK

			## debug
			debug('EatCycle')
			
			for pModule in self.GetAlignedModules():
				if pModule.EnterMode == QueueModule.ACTIVE:
					iState = pModule.EnterPull()
					if iState == ACK:
						break
			if iState == NAK:
				if self.EnterMode == QueueModule.ACTIVE:
					iState = self.EnterPull()	

	def EnterShip(self,pShip):
		## debug
		debug('Entership of ship '+pShip.sName)

		## We must be able accept the ship
		if self.GetLoad(pShip)+1  > self.GetCapacity():
			## debug
			debug('Module '+self.sName+': Rejecting '+pShip.sName)

			## No...
			return NAK

		## debug
		debug('Module '+self.sName+': Accepting '+pShip.sName)

		## Register the ship
		assert pShip.IsTypeOf(SHIP)
		self.Queue.append((pShip.ID,QueueModule.ORANGE))
	
		## Add a handler for shipdeath
		self.AddHandler(pShip.GetStateStartEvent(DEAD),"ShipDestroyed")

		## Find the offset
		iState = self.GetState(pShip)
		i = ( iState - QueueModule.ORANGE )
		
		## Is the offset too large?
		if i >= len(self.ActionList):
			## Done
			self.SetState(pShip,QueueModule.RED)

			if self.bRepairMode:
				## Repair the ship
				self.Repair(pShip)
			else:
				## AI
				pShip.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],TRUE)

				## Push mode?
				if self.ExitMode == QueueModule.ACTIVE:
					self.ExitPush()
		else:
			## debug
			debug('Module '+self.sName+': Performing actions for '+pShip.sName)	

			## Assign a handler
			self.AddHandler(self.ET_TRANSFER_DONE,'TransferDone')
	
			## AI
			pShip.AssignAI(self.ActionList[i],TRUE)

		## Return succes
		return ACK

	def TransferDone(self,gEvent):
		## Decode
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return
		assert pShip.IsTypeOf(SHIP)

		## debug
		debug('Module '+self.sName+': Transfer done for '+pShip.sName)

		## ShipID
		SID = pShip.ID

		## Find the state
		iState = self.GetState(pShip)

		## Increase the state
		self.SetState(pShip,iState+1)		
		
		## Offset
		i = ( iState+1 - QueueModule.ORANGE )

		## Is the offset too large?
		if i >= len(self.ActionList):
			## Done
			self.SetState(pShip,QueueModule.RED)

			if self.bRepairMode:
				## Repair the ship
				self.Repair(pShip)

			else:
				## AI
				pShip.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],TRUE)
	
				## Push mode?
				if self.ExitMode == QueueModule.ACTIVE:
					self.ExitPush()
		else:
			## AI
			pShip.AssignAI(self.ActionList[i],TRUE)


	def ExitShip(self):
		## debug
		debug('Exitship')

		## Do we have a ship at red?
		for ID,iState in self.Queue:
			if iState == QueueModule.RED:
				## Found a ship
				pShip = GetByID(ID)
				
				## Return the ship
				return pShip

		## Nothing found, return None
		return None

	## Repair
	########################################
	def Repair(self,pShip):
		## debug
		debug(self.sName+' repairing '+pShip.sName)

		## Stay AI
		pShip.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],TRUE)

		## Repair it
		self.GetHolder().SwapForRepair(pShip,TRUE)

		## Self Lock
		self.LockExit()
	
			
	## Shipdeath
	########################################
	def ShipDestroyed(self,gEvent):
		## Decode
		pEvent = DecodeEvent(gEvent)
		if not pEvent:
			return
		pShip = pEvent.GetSource()
		if not pShip:
			return

		if self.HasShip(pShip):
			## Remove the ship
			self.SetState(pShip,QueueModule.RED)
			self.Queue.remove((pShip.ID,QueueModule.RED))	

			## Remove the handler for shipdeath
			self.RemoveHandler(pShip.GetStateStartEvent(DEAD),"ShipDestroyed")	

			## Push mode?
			if self.ExitMode == QueueModule.ACTIVE:
				## A new ship?
				self.EatNewShip()

		## Remove handler
		self.RemoveHandler(pShip.GetStateStartEvent(DEAD),"ShipDestroyed")

	## States
	##########################################
	def GetState(self,pShip):
		##ID
		SID = pShip.ID

		## Do we have a ship at red?
		for ID,iState in self.Queue:
			if ID == SID:
				## Found a ship
				return iState

		## not found
		raise RuntimeError

	def SetState(self,pShip,iState):
		assert pShip.IsTypeOf(SHIP)

		##ID
		SID = pShip.ID

		## Do we have a ship at red?
		i = 0
		for ID,Unused in self.Queue:
			if ID == SID:
				## Found a ship
				self.Queue[i]=ID,iState
				return
			i=i+1

		## not found
		raise RuntimeError
	

	## Alignment
	##########################################
	def Align(self,pModule):
		self.AlignedModules.append(pModule.ID)

	def Unalign(self,pModule):
		if self.AlignedModules.count(pModule.ID):
			self.AlignedModules.remove(pModule.ID)

	def GetCapacity(self):	
		iCap = self.Capacity
		for ModuleID in self.AlignedModules:
			pModule = GetByID(ModuleID)
			if pModule:
				iCap = min(iCap,pModule.Capacity)
		return iCap

	def GetLoad(self,pShip=None):
		iLoad = len(self.Queue)
		for ModuleID in self.AlignedModules:
			assert ModuleID != self.ID			
			pModule = GetByID(ModuleID)
			if pModule:
				iLoad = iLoad + len(pModule.Queue) - pModule.HasShip(pShip)
		iLoad = iLoad + len(self.Queue) - self.HasShip(pShip)
		
		## debug
		# debug('Load of '+self.sName+': '+str(iLoad))
		

		return iLoad

	def HasShip(self,pShip):
		if not pShip:
			return FALSE
		if 	((pShip.ID,QueueModule.RED)    in self.Queue or
			(pShip.ID,QueueModule.ORANGE) in self.Queue  or
			(pShip.ID,QueueModule.GREEN)  in self.Queue	):
			return TRUE
		return FALSE		

	def AlignModules(self,lModules):
		## This function aligns a list of modules
		for pModule in lModules:
			self.Align(pModule)
			pModule.Align(self)

def AlignModules(lModules):
	l = len(lModules)
	for i in range(l):
		lModules[i].AlignModules(lModules[:i])