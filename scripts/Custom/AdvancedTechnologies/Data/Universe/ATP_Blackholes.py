from ATP_Object import *

class Blackhole(Holder):

	EFFECTS_CYCLE = 0.2
	MASS = 6.0e+8
	MAX_RADIUS = 4000.0 * km
	MIN_RADIUS = 10.0 * km
	PHYSICS_FACTOR = 1.75

	# MAX_RADIUS >> ( EFFECTS_CYCLE * MASS ) ** (1/3)

	def __init__(self,ID=0):
		## Upper class
		Holder.__init__(self,ID)

		## Gfx
		self.sGfx = "Dummy"
		self.lGfx = 	(	("Wormhole_Cone",	 +05),
					("Wormhole_Helix1",	 +20),
					("Wormhole_Helix2",	 +20),
					("Wormhole_Outerring",	 -10)
				)
		self.fInitialScale = 40.0

		## Rotation
		self.phi = 0		

		## Data structs
		self.Nodes = []

	def Bind(self,sName,pHolder):
		## Binders
		self.SetName(sName)
		self.Move(pHolder)

	def Render(self,pSet):
		## imports
		import loadspacehelper

		## Already rendered?
		if self.Node:	
			return

		## Data
		pHolder = self.GetHolder()
		assert pHolder	
		fDish = 0.0

		## System
		pSolar = pHolder.GetSolar()
		pSet   = pSolar.Node
		if not pSet:
			pSolar.Setup()	
			pSet = pSolar.Node

		## Upperclass
		Holder.Render(self,pSet)	

		## Creation
		## The controller waypoint
		F = copyVector(eZ)
		F.Scale(+1.0)
		U = copyVector(eY)		
		V = self.GetHolder().FindSuitablePosition(40.0*km,250.0*km)
		pWay = WaypointDummy(pSet,"TEMPPOINT",V,F,U)
						
		## A main container object				
		self.Node = loadspacehelper.CreateShip(self.sGfx,pSet,self.sGfx+"_"+str(self.ID),pWay.GetName())
		self.Node.SetInvincible(TRUE)
		self.Node.AlignToVectors(F,U)
		App.DamageableObject_Cast(self.Node).SetCollisionsOn(FALSE)
		self.Node.SetScale(self.fInitialScale)
		self.Node.SetTargetable(FALSE)
		self.SetPosition(V)
				
		## Register
		self.EnterNodeCache(self.Node)
		
		## Load the models
		for sGfx,fSpeed in self.lGfx:
			## Create the dishes
			pBlackhole = loadspacehelper.CreateShip(sGfx,pSet,sGfx+"_"+str(self.ID),pWay.GetName())
			pBlackhole.AlignToVectors(F,U)
			pBlackhole.SetInvincible(TRUE)
			App.DamageableObject_Cast(pBlackhole).SetCollisionsOn(FALSE)
			pBlackhole.SetScale(self.fInitialScale)
			pBlackhole.SetTranslate(V)
					
			## Attach it to the holder
			# self.Node.AttachObject(pBlackhole)

			## Register
			self.Nodes.append(pBlackhole)
			self.EnterNodeCache(pBlackhole)
			fDish = max(pBlackhole.GetRadius(),fDish)

			## Orient and move
			Z = Vector(0.0,fSpeed,0.0)
			pBlackhole.SetAngularVelocity(Z,App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
			pBlackhole.UpdateNodeOnly()
			pBlackhole.SetTargetable(FALSE)

		## Rename the last
		pBlackhole.SetTargetable(TRUE)
		pBlackhole.SetName(self.sName)

		## Swap
		self.Node , self.Nodes[-1] = self.Nodes[-1] , self.Node

		## Disable collisions
		list = [self.Node] + self.Nodes
		for k in list:
			for l in list:
				k.EnableCollisionsWith(l,FALSE)
		
		## Lose the waypoint
		pWay.Destroy()

		## The clock to perform the blackhole effect
		self.AddGameClock('Effects',Blackhole.EFFECTS_CYCLE)

	def Enhance(self):
		## Upper class
		Holder.Enhance(self)

		## Holders position
		pHolder = self.GetHolder()
		HZ = pHolder.GetPosition().GetZ()
		Z = copyVector(eZ)
		Z.Scale(-1.05*pHolder.GetOwnRadius())
		LZ = Z.GetZ()
		NZ = HZ+LZ

		## Set our position
		V = self.GetPosition()
		V.SetZ(NZ)
		self.SetPosition(V)

		## Create some comets
		import ATP_Extras
		iComets = int(self.GetRandom(10,12))
		for i in range(iComets):
			ATP_Extras.Comet(self,sName='Comet BHX',fScale=10.0,fMass=2.0e+6)
	

	def Unrender(self):
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

		## Upperclass
		Holder.Unrender(self)

		## Clock
		self.RemoveClock('Effects')
	
	def SetPosition(self,V):
		## Upper
		Holder.SetPosition(self,V)
		
		## Subnodes
		for Node in self.Nodes:
			Node.SetTranslate(V)
			Node.UpdateNodeOnly()


	## The real stuff
	######################	
	def GetMass(self):
		return Blackhole.MASS

	def Effects(self,gEvent):
		## May we do actions ?
		pFleet = GetPlayerFleet()
		if pFleet.State == WARPING:
			return
		if pFleet.GetSolar().ID != self.GetSolar().ID:
			return

		## Do our stuff
		### Attract objects
		self.Attraction()

	def Attraction(self):
		from Custom.AdvancedTechnologies.Data.Actions import ATP_ActionDecoder

		## The set
		pSet = self.GetSolar().Node
		assert pSet

		## Point to be attracted to
		P = self.GetAttractionPoint()
		U = self.Node.GetWorldForwardTG()
		U.Unitize()

		## Set iterator
		pObject = pSet.GetFirstObject()
		if pObject:
			iFirstID = pObject.GetObjID()

		while (pObject):
			pFysObject = App.PhysicsObjectClass_Cast(pObject)	
			if not pFysObject:
				pass
			elif self.FixOwn(pObject):
				pass			
			elif ATP_ActionDecoder.IsActionShip(pObject):
				pass
			else:
				## Noone escapes
				pFysObject.SetStatic(FALSE)
			
				## Find the delta vector
				F = pObject.GetWorldLocation()				
				F.Subtract(P)
				F.Scale(-1.0)

				## Distance
				fReal = F.Length()
				fDist = max(Blackhole.MAX_RADIUS,fReal)

				## Current velocity
				V = pFysObject.GetVelocityTG()
				V.Unitize()
				F.Unitize()

				## Force (an incremental model v[n+1] = v[n] + dv = v[n] + a )
				fForce = self.GetMass() / math.pow(fDist,Blackhole.PHYSICS_FACTOR) * Blackhole.EFFECTS_CYCLE				

				## Current velocity
				V = pFysObject.GetVelocityTG()

				## F normalised
				F_normal = copyVector(F)

				## Phase vector
				R = U.Cross(F)
				R.Scale(fForce/2.0)

				## Force Vector							
				F.Scale(fForce)				

				## New velocity with phasing
				V.Add(F)
				V.Add(R)

				## With phasing
				# if fReal < Blackhole.MAX_RADIUS and fReal > Blackhole.MIN_RADIUS:
				if fReal > Blackhole.MIN_RADIUS:
					## Filter the fleeing attraction speed component
					fDot = F_normal.Dot(V)
					if fDot < 0.0:
						## Moving away, remove it
						F_normal.Scale(-fDot*1.25)
						V.Add(F_normal)

				elif fReal <= Blackhole.MIN_RADIUS:
					## Filter the homing attraction speed component
					fDot = F_normal.Dot(V)
					if fDot > 0.0:
						## Closing in, remove it
						F_normal.Scale(-fDot*1.01)
						V.Add(F_normal)					

				## Attract it
				pFysObject.SetVelocity(V)

				## Too close ?
				if fDist < 1.0:
					pShipObject = App.ShipClass_Cast(pObject)
					if pShipObject:
						pShipObject.RunDeathScript()	


			## Done ?
			pObject = pSet.GetNextObject(pObject.GetObjID())
			if (pObject.GetObjID() == iFirstID):
				pObject = None

	def GetAttractionPoint(self):
		V = self.GetPosition()
		U = self.Node.GetWorldForwardTG()
		U.Unitize()
		U.Scale(80.0*km)
		V.Add(U)
		return V

	def GetOwnRadius(self):
		return Blackhole.MIN_RADIUS	

	def FixOwn(self,pObject):
		OID = pObject.GetObjID()
		for pNode in self.Nodes + [self.Node]:
			PID = pNode.GetObjID()
			if PID == OID:
				return TRUE
		return FALSE
		
		
			
		