import App
from math import *
import string
import loadspacehelper

from ATP_Object import *
from ATP_Extras	import *

SET_MIN_ANGLE = 15.0
SET_MAX_ANGLE = 70.0

sqrt2 = sqrt(2)


## offset
################################################################
IDRAN_OFFSET = Vector(-(8.0+1.5/2.5)*5000.0/20.0,(10.0-0.25/2.5)*5000.0/20.0,0.0)
BELL_OFFSET = Vector(-(8.0+1.5/2.5)*5000.0/20.0+20.0,(10.0-0.25/2.5)*5000.0/20.0-3,0.0)

class Universe(UniverseElement):
	def __init__(self,ID=None):
		UniverseElement.__init__(self,ID)
	
		self.sName = "__UNIVERSE__"
		self.SolarDict  = {}
		self.NebulaDict = {}

		## Add some handlers
		self.AddHandler(App.ET_EXITED_WARP,		"WarpIn")
		self.AddHandler(App.ET_START_WARP_NOTIFY ,	"WarpOut")		
		self.AddHandler(App.ET_OBJECT_EXPLODING,	"ShipDestroyed")

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Universe("+str(self.ID)+")")

		## Upperclass
		UniverseElement.save(self,FALSE)

	def Vectorise(self):
		self.SolarDict = {}
		for pSolar in self.GetSolars():
			V = pSolar.GetLoc()
			X = floor(V.GetX())
			Y = ceil(V.GetY())
			if not self.SolarDict.has_key(X,Y):
				self.SolarDict[X,Y]=[]
			self.SolarDict[X,Y].append(pSolar)

		self.NebulaDict = {}
		for pNebula in self.GetNebulas():
			V = pNebula.GetLoc()
			X = floor(V.GetX())
			Y = ceil(V.GetY())
			if not self.NebulaDict.has_key(X,Y):
				self.NebulaDict[X,Y]=[]
			self.NebulaDict[X,Y].append(pNebula)

	def GetSectorCoords(self,pInterStellarObject):
		assert pInterStellarObject
		V = pInterStellarObject.GetLoc()
		X = floor(V.GetX())
		Y = ceil(V.GetY())
		return X,Y

	def GetNearbySolars(self,pInterStellarObject,iRadius=0):
		X,Y = self.GetSectorCoords(pInterStellarObject)
		return self.GetSectorSolars(X,Y,iRadius)

	def GetNearbyNebulas(self,pInterStellarObject,iRadius=0):
		X,Y = self.GetSectorCoords(pInterStellarObject)
		return self.GetSectorNebulas(X,Y,iRadius)

	def GetSectorSolars(self,X,Y,iRadius=0):
		assert X is not None
		assert Y is not None
		assert iRadius is not None
		
		## Just be sure
		X = int(X)
		Y = int(Y)
		r = int(iRadius)
		l = []

		## Form the group
		for i in range(-r,r+1):
			XX = X + i
			for j in range(-r,r+1):
				YY = Y + j

				if self.SolarDict.has_key(XX,YY):
					l = l + self.SolarDict[XX,YY]
		return l

	def GetSectorRectangleSolars(self,Xa,Ya,Xb,Yb):
		## Return data
		lRet = []
		
		## Check
		if Xa > Xb or Ya > Yb:
			return lRet
		
		## Iterate over the rectangle
		for XX in range(Xa,Xb+1):
			for YY in range(Ya,Yb+1):
				if self.SolarDict.has_key(XX,YY):
					lRet = lRet + self.SolarDict[XX,YY]

		## Return
		return lRet

	def GetSectorNebulas(self,X,Y,iRadius=0):
		assert X is not None
		assert Y is not None
		assert iRadius is not None

		## just be sure
		X = int(X)
		Y = int(Y)
		r = int(iRadius)
		l = []

		## Form the group
		for i in range(-r,r+1):
			XX = X + i
			for j in range(-r,r+1):
				YY = Y + j

				if self.NebulaDict.has_key(XX,YY):
					l = l + self.NebulaDict[XX,YY]
		return l

	def GetSolarGroup(self,X,Y):
		l=[]
		## Form the group
		for x,y in ((X,Y),(X+1,Y),(X+1,Y+1),(X,Y+1),(X-1,Y+1),(X-1,Y),(X-1,Y-1),(X,Y-1),(X+1,Y-1)):
			if self.SolarDict.has_key(x,y):
				l = l + self.SolarDict[x,y]
		return l

	def GetExactSolarGroup(self,X,Y):
		l = []
		## Form the group
		if self.SolarDict.has_key(X,Y):
				l = self.SolarDict[X,Y][:]
		return l

	def FindWeightedNearest(self,l,X,Y):
		d = 1.25
		if not l:
			return None
		Res = None
		for pSolar in l:
			V = pSolar.GetLoc()
			DX = V.GetX() - X
			DY = V.GetY() - Y
			D  = (DX*DX+DY*DY)/pSolar.GetWeight()
			if D < d:
				d = D
				Res = pSolar
		return Res


	def AnalyseSector(self,X,Y,fGranulation):
		f = int(fGranulation)
		g = 2.0 * f 
		
		## Get nearby solars
		l = self.GetSolarGroup(X,Y)
		m = []
	
		## Iterate over each subsector
		for i in range(f+2):
			x = X + (-1.0+2.0*i)/g
			mx = []
			m.append(mx)
			for j in range(f+2):
				y = Y - (-1.0+2.0*j)/g
				pSolar = self.FindWeightedNearest(l,x,y)
				if pSolar:
					mx.append(pSolar.GetRace().ID)
				else:
					mx.append(0)

		return m

	def Borderise(self,X,Y,D,fGranulation):
		f = int(fGranulation)
	
		Matrix = {}
		BorderMatrix = {}

		## Construct a supermatrix
		for x in range(X,X+D):
			for y in range(Y-D+1,Y+1):
				Matrix[x,y] = self.AnalyseSector(x,y,f)

		for x in range(X,X+D):
			for y in range(Y-D+1,Y+1):
				cell = Matrix[x,y]
				m = []
				BorderMatrix[x,y] = m
				for i in range(1,f+1):
					mx = []
					m.append(mx)
					for j in range(1,f+1):

						CC = cell[i][j]
						SW = cell[i-1][j-1]
						SS = cell[i  ][j-1]
						SE = cell[i+1][j-1]
						EE = cell[i+1][j  ]
						NE = cell[i+1][j+1]
						NN = cell[i  ][j+1]
						NW = cell[i-1][j+1]
						WW = cell[i-1][j  ]

						CSW = 'B'
						CNW = 'B'
						CSE = 'B'
						CNE = 'B'
						RSW = 0
						RNW = 0
						RSE = 0
						RNE = 0						

						if CC == WW:
							CSW = 'Z'
							CNW = 'Z'
						if CC == NN:
							CNW = 'Z'
							CNE = 'Z'
						if CC == EE:
							CNE = 'Z'
							CSE = 'Z'
						if CC == SS:
							CSW = 'Z'
							CSE = 'Z'
						if CSW =='B':
							if CC == SW:
								## A choice
								CSW = 'Z'
							if CSW =='B':
								if SW == WW and SW == SS:
									RSW = SS
								elif WW == SS:
									RSW = WW																
						if CSE =='B':
							if CC == SE:
								## A choice
								if not EE == SS:
									CSE = 'Z'
								else:
									RSE = SS
							if CSE =='B':
								if SE == EE and SE == SS:
									RSE = SS
								elif SS == EE:
									RSE = EE
						if CNW =='B':
							if CC == NW:
								## A choice
								CNW = 'Z'
							if CNW =='B':
								if NW == WW and NW == NN:
									RNW = NN
								elif NN == WW:
									RNW = WW
						if CNE =='B':
							if CC == NE:
								## A choice
								if not NN == EE:
									CNE = 'Z'
								else:
									RNE = NN
							if CNE =='B':
								if NE == EE and NE == NN:
									RNE = NN
								elif NN == EE:
									RNE = EE

						mx.append((CSW,CSE,CNE,CNW,CC,RSW,RSE,RNE,RNW))
		return BorderMatrix

	def WarpIn(self,gEvent):
		pShip=App.ShipClass_Cast(gEvent.GetDestination())
		if not pShip:
			pShip=App.ShipClass_Cast(gEvent.GetSource())
			if not pShip:
				return
		pSet = pShip.GetContainingSet()
		if not pSet:
			return
		pShip = GetByNode(pShip)
		if not pShip:
			## SHIP CREATED OUT OF ATP KNOWLEDGE, FIX THIS
			return
		if not pShip.IsTypeOf(SHIP):
			return
		pSolar = GetByNode(pSet)
		if not pSolar:
			return

		## Create an event
		pEvent = ATP_Event(0,pShip,pSolar)
		gEvent = App.TGIntEvent_Create()
		gEvent.SetInt(pEvent.GetID())	
		
		## Notify the ship
		pShip.WarpIn(gEvent)
		pSolar.WarpIn(gEvent)

		## Event no longer needed
		pEvent.delete()	

	def WarpOut(self,gEvent):
		# debug("A ship is warping out")

		pShip=App.ShipClass_Cast(gEvent.GetDestination())
		if not pShip:
			pShip=App.ShipClass_Cast(gEvent.GetSource())
			if not pShip:
				return
		pSet = pShip.GetContainingSet()
		if not pSet:
			return
		pShip = GetByNode(pShip)
		if not pShip:
			## SHIP CREATED OUT OF ATP KNOWLEDGE, FIX THIS
			return
		if not pShip.IsTypeOf(SHIP):
			return
		pSolar = GetByNode(pSet)
		if not pSolar:
			return				 	
		
		## Create an event
		pEvent = ATP_Event(0,pShip,pSolar)
		gEvent = App.TGIntEvent_Create()
		gEvent.SetInt(pEvent.GetID())
		
		## Notify the ship, the fleet and the system
		pShip.WarpOut(gEvent)
		pSolar.WarpOut(gEvent)

		## Event no longer needed
		pEvent.delete()	
		
	def ShipDestroyed(self,gEvent):
		pShip=App.ShipClass_Cast(gEvent.GetDestination())
		if not pShip:
			pShip=App.ShipClass_Cast(gEvent.GetSource())
			if not pShip:
				return
		pSet = pShip.GetContainingSet()
		if not pSet:
			return
		pShip = GetByNode(pShip)
		if not pShip:
			## SHIP CREATED OUT OF ATP KNOWLEDGE, FIX THIS
			return
		# if not pShip.IsTypeOf(SHIP):
		#	return
		pSolar = GetByNode(pSet)
		if not pSolar:
			return	
	
		## Create an event
		pEvent = ATP_Event(0,pShip,pSolar)
		gEvent = App.TGIntEvent_Create()
		gEvent.SetInt(pEvent.GetID())
		
		## Notify the ship
		pShip.SelfDestroyed(gEvent)		

		## Event no longer needed
		pEvent.delete()	

class SolarSystem(Holder):
	## Class related functions
	def __init__(self,ID=None):
		Holder.__init__(self,ID)
		
		## A new attribute
		self.Loc	= App.TGPoint3()
		self.Loc.SetXYZ(0.0,0.0,0.0)
		self.NotInNebula = FALSE
		self.CoreSystem = TRUE
		self.Weight = 2.5
		self.Meta	= []
		self.bRendered = FALSE

		## Acquire some events
		self.ET_WARP_IN		= GetNextEventType()
		self.ET_WARP_OUT	= GetNextEventType()
		self.ET_FLEET_WARP_IN	= GetNextEventType()
		self.ET_FLEET_WARP_OUT	= GetNextEventType()
		self.ET_SHIP_DESTROYED	= GetNextEventType()
		self.ET_CREATION_SHIP   = GetNextEventType()
		
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = SolarSystem("+str(self.ID)+")")

		## Upperclass
		Holder.save(self,FALSE)

		## Our lines
		write_save_file("self.NotInNebula = "+str(self.NotInNebula))
		write_save_file("self.SetLocXYZ( "+str(self.Loc.GetX())+" , "+str(self.Loc.GetY())+" , "+str(self.Loc.GetZ())+" )")		
		write_save_file("self.CoreSystem = "+str(self.CoreSystem))
		write_save_file("self.bRendered		="+str(self.bRendered))
		write_save_file("self.Weight = "+str(self.Weight))		
		
	## Accessors and modifiers
	def GetWeight(self):
		return self.Weight

	def GetPop(self):
		f = 0.0
		for pPlanet in self.GetAllPlanets():
			f = f + pPlanet.GetPop()
		return f

	def IsCoreSystem(self):
		return self.CoreSystem

	def SetCoreSystem(self,bool):
		self.CoreSystem = bool

	def SetNotInNebula(self,bool = TRUE):
		self.NotInNebula = bool

	def GetWarpInEvent(self):
		return self.ET_WARP_IN

	def GetFleetWarpInEvent(self):
		return self.ET_FLEET_WARP_IN

	def GetWarpOutEvent(self):
		return self.ET_WARP_OUT

	def GetFleetWarpOutEvent(self):
		return self.ET_FLEET_WARP_OUT

	def GetObjectDestroyedEvent(self):
		return self.ET_SHIP_DESTROYED

	def GetObjectCreationEvent(self):
		return self.ET_CREATION_SHIP

	def SetLoc(self,V,O=e0):
		V = copyVector(V)
		V.Add(O)	
		self.Loc = V

	def SetLocXYZ(self,x,y,z,V=e0):
		x = x + V.GetX()
		y = y + V.GetY()
		z = z + V.GetZ()
		self.Loc.SetXYZ(x,y,z)

	def GetLoc(self):	
		return copyVector(self.Loc)
	
	def GetMeta(self):
		return self.Meta[:]

	def AddMeta(self,pChar):
		self.Meta.append(pChar)	

	def InsideNebula(self):
		Nebulas = GetUniverse().GetNebulas()
		S = self.GetLoc()
		for Nebula in Nebulas:
			N = Nebula.GetLoc()
			N.Subtract(S)
			D = N.Length()
		
			if Nebula.GetRadius() > D:
				return TRUE
		return FALSE

	## Overwrites
	def GetOwnRadius(self):
		return 0.0

	def SetPosition(self,V):
		for Child in self.GetChildren():
			U = Child.GetPosition()
			U.Add(V)
			Child.SetPosition(U)	
		
	def SetPositionXYZ(self,x,y,z):
		V = App.TGPoint3()
		V.SetXYZ(x,y,z)
		self.SetPosition(V)

	def GetPosition(self):
		V=App.TGPoint3()
		V.SetXYZ(0.0,0.0,0.0)
		return V

	def GetSolar(self):
		return self
	
	## Bind, Render,etc
	def Bind(self,pRace,sName="",lSuns="",lPlanets="",lShips="",bCoreSystem = TRUE):
		## This binds in a simple and short way the system parameters using formatted strings		
		## Set the Race
		self.Migrate(pRace)
		## Set it as part of the universe
		self.Move(GetUniverse())
		
		## Name
		if not sName:
			self.sName = pRace.GetName() + " System "+str(pRace.GetNumSolars())
		else:
			seq = Decode(sName,'@')
			for i in range(len(seq)):
				if i==0:
					names = Decode(seq[0],'|')
					self.sName,self.sShortName = expand(names,2)
					if not self.sShortName:
						self.sShortName = ""									
				else:
					self.AddMeta(seq[i])

		## Sun string eg "G@Sol@-3;K"
		sunseq 		= Decode(lSuns,";@")
	
		## Planet string eg "B;B;N;N@Oceania@5.0;D;D@Moon;D;L;M@Earth@10.2;L@Jungle;K"
		planetseq 	= Decode(lPlanets,";@")

		## Parameters
		k		= 0
		m		= 0
		numSuns		= len(sunseq)
		numPlanets	= len(planetseq)
				
		## Cache the random number
		cache=self.Random
				
		## Partition the system
		while(k<numSuns):
			l=int(self.GetRandom(k+1,numSuns+1))
			l=numSuns
			first = TRUE

			for i in range(k,l):
				Class,Name,Magnitude = expand(sunseq[i],3)
				
				pSun = Sun()
				if first:
					pSun.Bind(self,Class,Name,Magnitude)
					first = FALSE
					oldsun = pSun
				else:
					pSun.Bind(oldsun,Class,Name,Magnitude)
			k=l

			n=0
			if numPlanets and m<numPlanets:
				n=int(self.GetRandom(m,numPlanets+1))
				n=numPlanets
				if k>=numSuns:
					#Lead out
					n=numPlanets				

				for i in range(m,n):
					Class,Name,Pop	= expand(planetseq[i],3)

					##Pop in string format
					if Pop:
						Pop=string.atof(Pop)

					if planetseq[i][0]=="D":
						assert pPlanet
						pMoon 	= Moon()
						pMoon.Bind(pPlanet,Class,Name,Pop)				
					else:
						pPlanet 	= Planet()
						pPlanet.Bind(oldsun,Class,Name,Pop)	

			m=n+1

		# Add some extra moons
		pPlanets = self.GetAllPlanets()	
		for pPlanet in pPlanets:
			if pPlanet.IsTypeOf(MOON):
				continue
			if not pPlanet.GetMoons():
				## Some stats
				F,F,LM,UM,F = Planet.ClassToStats[pPlanet.Class]

				## Number or moons
				iMoons = int(pPlanet.GetRandom(LM,UM+1))

				## Add some moons
				for i in range(iMoons):
					pMoon = Moon()
					pMoon.Bind(pPlanet)

		#Fleet string eg "Defense1@Protector@Earth|{Akira@1@USS Hope;Galaxy@1@USS Odeysee}@Custom Fleet@Mars"
		seq = Decode(lShips,"|")
		for i in range(len(seq)):
			innerseq = seq[i]
			if innerseq[0]=="{":
				pos=string.rfind(innerseq,'}')
				if pos==-1:
					raise ValueError, "Invalid Fleet format: \"{\" opened but not closed."
				sGfx 			= innerseq[:pos+1]
				sFleet,sLocation	= expand(Decode(innerseq[pos+2:],"@"),2)
			else:
				sGfx,sFleet,sLocation	= expand(Decode(innerseq,"@"),3)

			import ATP_Vessels
			pFleet = ATP_Vessels.Fleet()
			if sLocation:
				pLocation = self.GetChildByName(sLocation)	
				if not pLocation:
					raise RuntimeError, 'Wrong fleet location: '+sLocation+' doesn\'t exist in '+self.sName
				pFleet.Bind(pRace,pLocation,sFleet,sGfx)
			else:
				pFleet.Bind(pRace,self,sFleet,sGfx)

		## Core system or not?
		self.CoreSystem = bCoreSystem		

		#debug("Finished creating a the system "+self.sName)

	def Setup(self):
		## Setup the system
		if self.Node:
			return

		## Create this needed file 
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		open_save_file(sfilename=self.sName+".py",sfilepath="scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\Dummy\\Systems")		
		write_save_file("import App")
		write_save_file("def GetSet():")
		write_save_file("return App.g_kSetManager.GetSet(\""+self.sName+"\")",1)
		close_save_file()

		# Create the set
		pSet = App.g_kSetManager.GetSet(self.sName)
		if not pSet:
			pSet = App.SetClass_Create()
			App.g_kSetManager.AddSet(pSet,self.sName)

		# Save the name of the region file that's creating the set.
		pSet.SetRegionModule("Custom.AdvancedTechnologies.Data.Universe.Dummy.Systems."+self.sName)

		# Activate the proximity manager for our set.
		pSet.SetProximityManagerActive(1)

		#Load and place the grid.
		pGrid = App.GridClass_Create()
		pSet.AddObjectToSet(pGrid, "grid")
		pGrid.SetHidden(1)

		## Register the node
		self.Node = pSet
	
		## Node cache
		self.EnterNodeCache()

		## Add an entry to the menu
		# import Systems.Utils
		# Systems.Utils.CreateSystemMenu(self.sName,"Custom.AdvancedTechnologies.Data.Universe.Dummy.Systems."+self.sName)

	def RenderAndRandomise(self,pSet=None):
		if not self.bRendered:
			self.Render(pSet)
			self.EnterNodeCache()
			self.Randomise()
			self.Enhance()
			self.AssignAI()

	def IsRendered(self):
		return self.bRendered

	def Render(self,pSet):
		if not self.Node:
			self.Setup()		

		## Render children
		Holder.Render(self,self.Node)
		
		## Add some extras
		if not self.IsRendered():
			## Add an ambient light
			if self.GetSuns():
				pAmbient = Ambient(self.GetSuns()[0],Colour(1.0,1.0,1.0,0.18))
			else:
				pAmbient = Ambient(self,Colour(1.0,1.0,1.0,0.18))
				pBulb = Bulb(self,self.sName+'_BULB',3,Colour(0.5,0.5,0.5,0.18))
			
			## Add the backdrops
			## The main star backdrop
			pDrop = Stars(self,GFX_PATH_STARS,eX,eZ)

			## Extra depending on nearby nebulas
			pUniverse = GetUniverse()
			iX,iY = pUniverse.GetSectorCoords(self) 
			lNebulas = pUniverse.GetSectorNebulas(iX,iY,2)
			S = self.GetLoc()

			for pNebula in lNebulas:
				N = pNebula.GetLoc()
				N.Subtract(S)
				w = 2.0*pNebula.GetRadius()
				N.Scale(-1.0)
				d = N.Length()
				d = d - w/2.0*sqrt2
				N.Unitize()

				tX = N.Cross(eZ)
				tZ = N.Cross(tX)

				if d <= 0.0 and not self.NotInNebula:
					## The entire system in the nebula
					debug("Creating a full nebula "+pNebula.sName+" for "+self.sName)
					pNebula.RenderNebulaInside(self)									

				else:
					## in sectors (20ly)
					import math
					if d < 0.001:
						d = 0.001 
					ratio = math.atan(w/d)/math.pi
					ratio = 2.0 * ratio**2	
			
					# debug("Adding the nebula "+pNebula.sName+" to the system "+self.sName)
					Backdrop(self,pNebula.GetGfx(),N,tZ,HS = ratio ,VS = ratio ,H = 1.0,V = 1.0)

		## Add a clock for high displacements
		self.AddClock("CenterCheck",2.5)

		## Add a clock to check for unrendering
		self.AddClock("PulsedUnrender",5.0)

		## Set rendered
		self.bRendered = TRUE
		
		## Node caching
		self.EnterNodeCache()

	def PulsedUnrender(self,gEvent):
		pShip = GetPlayerShip()

		## Player warping?	
		if GetPlayerFleet().State == WARPING:	
			return	
		## Where is the player or is going to ?
		if pShip.GetSolar().ID == self.ID:
			return
		pSolar = GetByNode(pShip.Node.GetContainingSet())
		if not pSolar:
			return
		if pSolar.ID == self.ID:
			return

		## Ok unrender ourself
		self.Unrender()

	def Unrender(self):
		if not self.Node:
			return

		print 'Unrendering '+self.sName
		debug ("Begin Unrendering Set "+self.sName)

		## Unrender children
		Holder.Unrender(self)

		## Caching
		self.PurgeNodeCache()

		## Mark unrendered
		self.bRendered = FALSE		

		## Remove clock
		self.RemoveClock("CenterCheck")
		self.RemoveClock("PulsedUnrender")

		debug ("End Unrendering Set")

	def Randomise(self):
		## Randomise children types		
		## Cache the random number
		cache = self.Random

		Holder.Randomise(self,BLACKHOLE,25.0,0.0,25.0)
		Holder.Randomise(self,SUN,1.05,0.0,25.0)
		Holder.Randomise(self,FLEET,5.0)
		Holder.Randomise(self,SUBWORMHOLE,2.0,0.0,25.0)
		
		
		## Do a centercheck
		self.CenterCheck(None)
		
		# Restore the random number
		self.Random=cache

	def Enhance(self):
		## Upcall
		Holder.Enhance(self)

		## Some static comets
		## Get our I,J,S,T planets
		lPlanets = self.GetAllPlanets()

		for pPlanet in lPlanets:
			sClass = pPlanet.Class
			if sClass == 'I' or sClass == 'J' or sClass == 'S' or sClass == 'T':
				iComets = int(self.GetRandom(3,10))
				for i in range(iComets):
					Comet(pPlanet,fScale=10.0,fMass=2.0e+6)
	
	def CenterCheck(self,pEvent):
		import MissionLib
		pPlayer=MissionLib.GetPlayer()
		if not pPlayer:
			return
		pSet=pPlayer.GetContainingSet()
		if not pSet:
			return

		if pSet.GetObjID() == self.Node.GetObjID():
			P=pPlayer.GetTranslate()
			if P.Length()>SHIFTING_THRESHOLD:
				debug(self.sName +" CenterCheck: Player prepos = "+printVector(pPlayer.GetTranslate()))
				self.ShiftCenter(P)
				debug(self.sName +" CenterCheck: Player aftpos = "+printVector(pPlayer.GetTranslate()))

	def ShiftCenter(self,V):
		from   Custom.AdvancedTechnologies.Data.Actions import ATP_ActionDecoder

		pSet=self.GetNode()
		assert pSet

		pObject = pSet.GetFirstObject()
		if pObject:
			iFirstID = pObject.GetObjID()

		while (pObject):
			if(	App.BaseObjectClass_Cast	(pObject)  	and
				not App.LightObjectClass_Cast	(pObject)	and
				not App.StarSphere_Cast		(pObject) 	and
				not App.Planet_Cast		(pObject)	and
				not App.ShipClass_Cast		(pObject)	and
				not App.BackdropSphere_Cast(pObject)			):				

				#Check if there is a conceptual version
				if GetByNode(pObject):
					pass
				elif ATP_ActionDecoder.IsActionShip(pObject):
					pass
				else:
					U = pObject.GetWorldLocation()
					U.Subtract(V)
					pObject.SetTranslate(U)
				
			pObject = pSet.GetNextObject(pObject.GetObjID())
			if (pObject.GetObjID() == iFirstID):
				pObject = None

		## Now move all conceptual things
		V.Scale(-1.0)
		self.SetPosition(V)		
	
	def Clear(self):
		pSet=self.GetNode()
		assert pSet

		pObject = pSet.GetFirstObject()
		if pObject:
			iFirstID = pObject.GetObjID()

		while (pObject):
			if(App.BaseObjectClass_Cast(pObject)):
				pObject.SetDeleteMe(TRUE)				
				
			pObject = pSet.GetNextObject(pObject.GetObjID())
			if (pObject.GetObjID() == iFirstID):
				pObject = None

	def WarpIn(self,gEvent):
		## Data from the event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()

		## Raise the trigger
		self.Raise(self.GetWarpInEvent(),pShip,self)

	def FleetWarpIn(self,pFleet):
		## Raise the trigger
		self.Raise(self.GetFleetWarpInEvent(),pFleet,self)

	def WarpOut(self,gEvent):
		## Data from the event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()

		## Raise the trigger
		self.Raise(self.GetWarpOutEvent(),pShip,self)

	def FleetWarpOut(self,pFleet):
		## Raise the trigger
		self.Raise(self.GetFleetWarpOutEvent(),pFleet,self)	

	def ObjectDestruction(self,pObj):
		## Raise the trigger
		self.Raise(self.GetObjectDestroyedEvent(),pObj,self)

	def ObjectCreation(self,pObj):
		## Raise the trigger
		self.Raise(self.GetObjectCreationEvent(),pObj,self)

	def GetDummyWaypoint(self):
		## Provide the dummy waypoint
		# pWay = self.GetDirectChildByName('__CENTER__')
		# if not pWay:
		#	## A new waypoint
		#	pWay = Waypoint("__CENTER__",self,V=e0,bAttach=FALSE,NavPoint=FALSE)
		#
		raise RuntimerError
		return pWay


	def GetInsideNebulas(self):
		## Return list
		lRet = []

		## Quickcheck
		if self.NotInNebula:
			return lRet
		
		## Nearby Nebulas
		pUniverse = GetUniverse()
		iX,iY = pUniverse.GetSectorCoords(self) 
		lNebulas = pUniverse.GetSectorNebulas(iX,iY,2)
		S = self.GetLoc()

		## Iterate over them
		for pNebula in lNebulas:
			N = pNebula.GetLoc()
			N.Subtract(S)
			w = 2.0*pNebula.GetRadius()
			N.Scale(-1.0)
			d = N.Length()
			d = d - w/2.0*sqrt2

			if d <= 0.0:
				lRet.append(pNebula)
		## Return it
		return lRet
		

class StarbaseSystem(SolarSystem):
	STARBASE = 0
	OUTPOST	 = 1
	COMM	 = 2

	## Class related functions
	def __init__(self,ID=None):
		SolarSystem.__init__(self,ID)

		## Class Type
		self.Class = StarbaseSystem.STARBASE
		self.Base  = 0

		## Overwrite
		self.Weight = 1.0

	def SetClass(self,iVal):
		self.Class = iVal

	def GetClass(self):
		return self.Class

	def SetBase(self,pBase):
		self.Base = pBase.ID

	def GetBase(self):
		return GetByID(self.Base)
	
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = StarbaseSystem("+str(self.ID)+")")

		## Upperclass
		SolarSystem.save(self,FALSE)

		## Our lines
		write_save_file("self.Base   = "+str(self.Base))		
		write_save_file("self.Class  = "+str(self.Class))	
		
	## Bind, Render,etc
	def Bind(self,pRace,sName="",lShips=""):
		## Upperclass
		SolarSystem.Bind(self,pRace,sName,'','',lShips,FALSE)

		## Set base
		for pShip in self.GetAllShips():
			if pShip.IsStationary():
				self.SetBase(pShip)
				break
		if not self.GetBase():
			raise RuntimeError, 'No base defined for Starbase system '+self.sName

		#debug("Finished creating a the system "+self.sName)	


class BlackholeSystem(SolarSystem):

	## Class related functions
	def __init__(self,ID=None):
		SolarSystem.__init__(self,ID)

		## the Blackhole
		self.iBlackhole = 0

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = BlackholeSystem("+str(self.ID)+")")

		## Upperclass
		SolarSystem.save(self,FALSE)
	
	def Bind(self,pRace,sName="",lSuns="",lPlanets="",lShips=""):
		## Upperclass
		SolarSystem.Bind(self,pRace,sName,lSuns,lPlanets,lShips,bCoreSystem = FALSE)

		## Add the blackhole somewhere
		import ATP_Blackholes
		pBlackhole = ATP_Blackholes.Blackhole()
		pBlackhole.Bind(self.GetName(),self)

		## the Blackhole
		self.iBlackhole = pBlackhole.ID

	def Enhance(self):
		## Upper class
		SolarSystem.Enhance(self)

		## Create some comets
		import ATP_Extras
		iComets = int(self.GetRandom(40,60))
		pBlackhole = GetByID(self.iBlackhole)
		for i in range(iComets):
			ATP_Extras.Comet(pBlackhole,sName='Comet BHX',fScale=10.0,fMass=2.0e+6)

	def GetOwnRadius(self):
		pBlackhole = GetByID(self.iBlackhole)
		return pBlackhole.GetOwnRadius()
		

class Nebula(UniverseElement):

	dsColourTosGfx = {	'Green' : (	'data/Backgrounds/nebulaoverlaygreen.tga' , 
						'data/Backgrounds/nebulaexternalgreen.tga',
						 Colour(0.125, 0.75, 0.125) 			),
			   	'Yellow': (	'data/Backgrounds/nebulaoverlayyellow.tga' , 
						'data/Backgrounds/nebulaexternalyellow.tga',
						 Colour(0.75, 0.75, 0.125)			) ,
				'Red' :   (	'data/Backgrounds/nebulaoverlayred.tga' , 
						'data/Backgrounds/nebulaexternalred.tga',
						 Colour(0.75, 0.125, 0.125)			) ,
			   	'Blue':   (	'data/Backgrounds/nebulaoverlayblue.tga' , 
						'data/Backgrounds/nebulaexternalblue.tga',
						 Colour(0.125, 0.125, 0.75)			) ,
				'Saphire': (	'data/Backgrounds/nebulaoverlaybz1.tga' , 
						'data/Backgrounds/nebulaexternalbz1.tga',
						 Colour(0.125, 0.75, 0.75)			) 
			 }	
	
	def __init__(self,ID=None):
		UniverseElement.__init__(self,ID)

		## Own attributes
		self.IconID = 0
		self.Radius = 1.0
		self.sGfx = ''
		self.sInternalGfx = ''
		self.sExternalGfx = ''
		self.cColour	  = None

		## Child of the universe
		self.Move(GetUniverse())

	def Bind(self,sName,vLocation,Radius,sGfx,IconID,sColour='Saphire'):
		self.sName = sName[:]
		self.SetLoc(vLocation)
		self.Radius = Radius
		self.IconID = IconID
		self.sGfx = sGfx[:]
		self.sInternalGfx,self.sExternalGfx,self.cColour = Nebula.dsColourTosGfx[sColour]


	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Nebula("+str(self.ID)+")")

		## Upperclass
		UniverseElement.save(self,FALSE)

		## Our lines
		write_save_file("self.Radius = "+str(self.Radius))
		write_save_file("self.IconID = "+str(self.IconID))
		write_save_file("self.sGfx = \""+str(self.sGfx)+"\"")

	def RenderNebulaOutside(self,pSolar,N,r):

		pSet = pSolar.Node
		pNebula = App.MetaNebula_Create(0.75, 0.75, 0.125, 20.0*km , 0.5,"data/Backgrounds/nebulaoverlayyellow.tga", "data/Backgrounds/nebulaexternalyellow.tga")

		T = copyVector(N)
		X = copyVector(T)
		X.Unitize()
		Y = eZ.Cross(X)
		Z = X.Cross(Y)
		
		tX = copyVector(X)
		tX.Scale(r/2.0)
		tY = copyVector(Y)
		tY.Scale(r/2.0)
		S0 = copyVector(T)
		S0.Add(tX)
		S0.Add(tY)
		S1 = copyVector(T)
		S1.Add(tX)
		S1.Subtract(tY)
		S2 = copyVector(T)
		S2.Subtract(tX)
		S2.Add(tY)
		S3 = copyVector(T)
		S3.Subtract(tX)
		S3.Subtract(tY)
	
		# Adds a fuzzy sphere at x, y, z (in world coord) of specified size
		f = sqrt(2.0)/2.0 * r
		pNebula.AddNebulaSphere(S0.GetX(), S0.GetY(), S0.GetZ(),f)
		pNebula.AddNebulaSphere(S1.GetX(), S1.GetY(), S1.GetZ(),f)
		pNebula.AddNebulaSphere(S2.GetX(), S2.GetY(), S2.GetZ(),f)
		pNebula.AddNebulaSphere(S3.GetX(), S3.GetY(), S3.GetZ(),f)
		
		## Put the nebula in the set
		pSet.AddObjectToSet(pNebula,self.sName)

		## Add navpoints
		S0 = copyVector(N)
		tX = copyVector(X)
		tX.Scale(-r*1.01)
		S0.Add(tX)
		S1 = copyVector(N)
		tX = copyVector(X)
		tX.Scale(-r*1.01)
		S1.Add(tX)

		Waypoint("Enter " + self.sName,pSolar,V=S1,bAttach=FALSE,NavPoint=TRUE)
		Waypoint("Exit "  + self.sName,pSolar,V=S0,bAttach=FALSE,NavPoint=TRUE)

		## Register
		self.Node = pNebula

		## Upperclass
		UniverseElement.Render(self,pSet)

	def RenderNebulaInside(self,pSolar):
		import ATP_Extras
		ATP_Extras.SolarNebula(self,pSolar,self.sInternalGfx,self.sExternalGfx,self.cColour)
	
	def GetGfx(self):
		return self.sGfx[:]
	
	def SetGfx(self,sGfx):
		self.sGfx = sGfx[:]
		
	def GetLoc(self):
		return self.GetPosition()
	
	def SetLoc(self,V):
		self.SetPosition(V)
	
	def SetLocXYZ(self,x,y,z):
		self.SetLoc(Vector(x,y,z))

	def GetIconID(self):
		return self.IconID

	def SetIconID(self,ID):
		self.IconID = ID
	
	def SetRadius(self,Width):
		self.Radius = Width

	def GetRadius(self):
		return self.Radius
	

class Sun(Holder):
	def __init__(self,ID=None):
		Holder.__init__(self,ID)
	
		self.Gfx=[5000.0, 5000, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRedOrange.tga"]
		self.Class="G"
		self.Magnitude=1
		
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Sun("+str(self.ID)+")")

		## Upperclass
		Holder.save(self,FALSE)

		## Our lines
		write_save_file("self.Gfx = "+str(self.Gfx))
		write_save_file("self.Class = \""+str(self.Class)+"\"")
		write_save_file("self.Magnitude = "+str(self.Magnitude))		

	def GetMagnitude(self):
		return self.Magnitude

	def SetMagnitude(self,fVal):
		self.Magnitude=fVal

	def GetClass(self):
		return self.Class

	def SetClass(self,Class):
		self.Class=Class

	def SetGfx(self,fRadius, fAtmosphereThickness, fDamagePerSec, sBaseTexture , sFlareTexture):
		self.Gfx=[fRadius*scale*sunscale, fAtmosphereThickness*scale*sunscale, fDamagePerSec, sBaseTexture , sFlareTexture]

	def GetColour(self):
		if self.Class=="O":
			k=App.NiColorA(128.0/255.0,0.0/255.0,255.0/255.0,1.0)
		elif self.Class=="B":
			k=App.NiColorA(0.0/255.0,128.0/255.0,255.0/255.0,1.0)
		elif self.Class=="A":
			k=App.NiColorA(176.0/255.0,216.0/255.0,225.0/255.0,1.0)
		elif self.Class=="F":
			k=App.NiColorA(145.0/255.0,225.0/255.0,255.0/255.0,1.0)
		elif self.Class=="G":
			k=App.NiColorA(255.0/255.0,213.0/255.0,40.0/255.0,1.0)
		elif self.Class=="K":
			k=App.NiColorA(255.0/255.0,128.0/255.0,64.0/255.0,1.0)
		elif self.Class=="M":
			k=App.NiColorA(254.0/255.0,102.0/255.0,1.0/255.0,1.0)
		else:
			k=App.NiColorA(128.0/255.0,128.0/255.0,128.0/255.0,1.0)
		return k		

	def Bind(self,pSolar,cClass="",sName="",sMagnitude="0"):
		##Bind it to the system
		self.Move(pSolar)
		self.Migrate(pSolar.GetFather())

		## Class specification
		if not cClass:
			r=int(Random(0,7))
			if r==0:
				cClass="O"
			elif r==1:
				cClass="B"
			elif r==2:
				cClass="A"
			elif r==3:
				cClass="F"
			elif r==4:
				cClass="G"
			elif r==5:
				cClass="K"
			elif r==6:
				cClass="M"
			else:
				cClass="G"

		if cClass=="O":
			fRadius=self.GetRandom(100000,400000)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.01,1.05)
			fDamagePerSec=self.GetRandom(5000.0,7500.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunO.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresBlue.tga"
		elif cClass=="B":
			fRadius=self.GetRandom(400000,800000)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.02,1.06)
			fDamagePerSec=self.GetRandom(4000.0,5000.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunB.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresBlue.tga"
		elif cClass=="A":
			fRadius=self.GetRandom(800000,1000000)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.03,1.04)
			fDamagePerSec=self.GetRandom(3000.0,5000.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunA.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresBlue.tga"
		elif cClass=="F":
			fRadius=self.GetRandom(1000000,1200000)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.04,1.05)
			fDamagePerSec=self.GetRandom(2000.0,3000.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunF.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresWhite.tga"
		elif cClass=="G":
			fRadius=self.GetRandom(1.2e+6,1.5e+6)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.05,1.06)
			fDamagePerSec=self.GetRandom(1000.0,2000.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunG.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresYellow.tga"
		elif cClass=="K":
			fRadius=self.GetRandom(1.5e+6,3.0e+6)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.1,1.12)
			fDamagePerSec=self.GetRandom(0.0,1000.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunK.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresOrange.tga"
		elif cClass=="M":
			fRadius=self.GetRandom(3.0e+6,20.0e+6)*km*scale
			fAtmosphereThickness=fRadius*self.GetRandom(1.15,1.2)
			fDamagePerSec=self.GetRandom(0.0,500.0)
			sBaseTexture="scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/SunM.tga"
			sFlareTexture="data/Textures/Effects/SunFlaresRed.tga"

		self.Class=cClass

		## Name
		if not sName:
			sName=pSolar.GetSolar().GetName()+" "+NumToUpperAlpha[pSolar.GetSolar().GetNumAllSuns()-1]
		self.sName = sName

		## Magnitude
		if not sMagnitude:
			sMagnitude	= "0"
		self.Magnitude	= string.atoi(sMagnitude)		
		
		## Gfx
		fRadius			= fRadius*sunscale
		fAtmosphereThickness	= fAtmosphereThickness*sunscale	
		self.Gfx		= [fRadius, fAtmosphereThickness, fDamagePerSec, sBaseTexture , sFlareTexture]
				
		#debug("Finished creating an "+self.Class+" Sun.")

	def Render(self,pSet):
		debug('rendering '+self.sName)

		## Render ourself
		if not self.IsRendered():
			self.Node = App.Sun_Create(self.Gfx[0],self.Gfx[1],self.Gfx[2],self.Gfx[3],self.Gfx[4])
			self.Node.SetAtmosphereRadius(0.0)
			pSet.AddObjectToSet(self.Node,"Sun_"+self.sName+"_"+str(self.ID))

		debug('end rendering '+self.sName)

		## Base class function
		Holder.Render(self,pSet)		
		
		## Node cache
		self.EnterNodeCache()	
					
	def Randomise(self):		
		## Randomise children
		Holder.Randomise(self,SUN,2.0,15.0,35.0)
		Holder.Randomise(self,FLEET,7.0,0.0,15.0)
		Holder.Randomise(self,PLANET,3.0,2.0,75.0)
		Holder.Randomise(self,SUBWORMHOLE,2.0,0.0,25.0)
		Holder.Randomise(self,BLACKHOLE,18.0,0.0,25.0)
	
		## Randomise ourself
		pass

	def Enhance(self):
		## Add the light
		if not self.GetDirectChildByName(self.sName+'_BULB'):
			pBulb = Bulb(self,self.sName+'_BULB',20)

		## Attach a waypoint to ourself	
		if not self.GetDirectChildByName(self.sName):
			Waypoint(self.sName,self,V=self.GetPosition(),NavPoint=TRUE)

		## Upperclass
		Holder.Enhance(self)


class Planet(Holder):

	ClassToStats = {	'A':(1.0e+3,1.0e+4,0.0,1.0,GFX_PATH_PLANETS+"TanGasPlanet.NIF"		),
				'B':(1.0e+3,1.0e+4,0.0,0.0,GFX_PATH_PLANETS+"Mercury.nif"		),
				'C':(1.0e+3,1.0e+4,0.0,0.0,GFX_PATH_PLANETS+"Pluto.nif"			),
				'E':(1.0e+4,1.0e+5,0.0,1.0,GFX_PATH_PLANETS+"RootBeerPlanet.NIF"	),
				'F':(1.0e+4,1.5e+4,0.0,1.0,GFX_PATH_PLANETS+"GreenPlanet.NIF"		),
				'G':(1.0e+4,1.5e+4,0.0,1.0,GFX_PATH_PLANETS+"SulfurPlanet.NIF"		),
				'H':(1.4e+4,1.5e+5,0.0,1.0,GFX_PATH_PLANETS+"dryplanet.NIF"		),
				'I':(1.5e+5,1.5e+6,2.0,4.0,GFX_PATH_PLANETS+"Jupiter.NIF"		),
				'J':(0.5e+5,1.5e+5,1.0,4.0,GFX_PATH_PLANETS+"Saturn.NIF"		),
				'K':(0.5e+3,1.0e+4,0.0,1.0,GFX_PATH_PLANETS+"Mars.NIF"			),
				'L':(1.0e+4,1.5e+4,0.0,1.0,GFX_PATH_PLANETS+"Mars.NIF"			),
				'M':(1.0e+4,1.5e+4,0.0,2.0,GFX_PATH_PLANETS+"Earth.NIF"			),
				'N':(1.0e+4,1.5e+4,0.0,0.0,GFX_PATH_PLANETS+"Venus.NIF"			),
				'O':(1.0e+4,1.5e+4,0.0,1.0,GFX_PATH_PLANETS+"AquaPlanet.NIF"		),
				'P':(1.0e+4,1.5e+4,0.0,1.0,GFX_PATH_PLANETS+"IcePlanet.NIF"		),
				'Q':(0.4e+4,1.5e+4,0.0,2.0,GFX_PATH_PLANETS+"LavenderPlanet.NIF"	),
				'R':(0.4e+4,1.5e+4,0.0,4.0,GFX_PATH_PLANETS+"SlimeGreenPlanet.NIF"	),
				'S':(2.0e+6,3.0e+6,2.0,5.0,GFX_PATH_PLANETS+"Uranus.NIF"		),
				'T':(2.0e+6,3.0e+6,2.0,5.0,GFX_PATH_PLANETS+"Uranus.NIF"		),
				'Y':(5.0e+3,5.0e+4,0.0,2.0,GFX_PATH_PLANETS+"TanGasPlanet.NIF"		)
			}

	ClassCache = { }
				
	
	def __init__(self,ID=None):
		Holder.__init__(self,ID)

		self.Gfx=[90.0, "data/models/environment/TanGasPlanet.nif"]
		self.Class="Y"
		self.Pop=0.0
		
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Planet("+str(self.ID)+")")

		## Upperclass
		Holder.save(self,FALSE)

		## Our lines
		write_save_file("self.Gfx = "+str(self.Gfx))
		write_save_file("self.Class = \""+str(self.Class)+"\"")
		write_save_file("self.Pop = "+str(self.Pop))

	def SetClass(self,pChar):
		self.Class=pChar

	def GetClass(self):
		return self.Class

	def SetPopulation(self,fVal):
		self.Pop=fVal
	
	def GetPop(self):
		return self.Pop

	def GetPopulation(self):
		return self.Pop

	def SetGfx(self,fRadius,sTexture):
		self.Gfx=[fRadius*scale*planetscale,sTexture]


	def Bind(self,pSun,cClass='K',sName="",fPop=0.0):
		## Add ourself to the sun
		self.Move(pSun)

		## Name
		if not sName:
			sName=pSun.GetSolar().sName+" "+NumToRoman[pSun.GetNumPlanets()]
		self.sName = sName
		
		## Our Class
		self.Class = cClass

		## Pop
		if not fPop:
			fPop = 0.0
		self.Pop = fPop	

		## Folder structure with the gfx
		sFolder = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Planets/'+self.Class+'-Class'
	
		## Some stats
		LR,UR,LM,UM,GFX = Planet.ClassToStats[self.Class]

		## Radius
		fRadius = self.GetRandom(LR,UR)

		## Number or moons
		iMoons = int(self.GetRandom(LM,UM+1))

		## Cached ?
		if Planet.ClassCache.has_key(self.Class):
			lsFileNames = Planet.ClassCache[self.Class]
		else:
			## What files are in the folder ?
			import Foundation
			try:
				lssFileNames = Foundation.GetFileNames(sFolder,'nif')
			except OSError:
				raise RuntimeError, "Corrupted Gfx/Planets folders"

			## Modify them
			lsFileNames = []
			for sFile in lssFileNames:
				if string.find(sFile,'_vox') != -1:
					continue
				lsFileNames.append(sFile)

			## Remember
			Planet.ClassCache[self.Class] = lsFileNames				

		## Modify the name for " " (NIF doesn't support names with whitespaces)
		sName = string.replace(sName,' ','_')

		## Find our model
		if lsFileNames:
			## We found a list with name
			if lsFileNames.count(sName+'.NIF'):
				fModel = sFolder + '/' + sName + '.NIF'
			else:
				## Take a random gfx
				i = int(self.GetRandom(0.0,len(lsFileNames)))
				fModel = sFolder + '/' + lsFileNames[i]
		else:
			fModel = GFX			
		
		## Gfx
		self.SetGfx(fRadius,fModel)				
		
		#debug("Finished creating an "+self.Class+" Planet.")
			
	def Render(self,pSet):
		## Own
		## Modify name
		sName = string.replace(self.sName,' ','_')

		debug('rendering '+self.sName)

		## Create this special file 
		if self.Class == 'M':# and FALSE:
			from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
			open_save_file(sfilename=sName+".py",sfilepath="scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\PlanetDef\\NodeDef")		
			write_save_file("import App")
			write_save_file("def GetShipStats():")
			write_save_file("kShipStats = {",1)
			write_save_file("\"FilenameHigh\": \""+self.Gfx[1]+"\",",1)
			write_save_file("\"FilenameMed\": \""+self.Gfx[1]+"\",")
			write_save_file("\"FilenameLow\": \""+self.Gfx[1]+"\",")
			write_save_file("\"Name\": \""+self.sName+"\",")
			write_save_file("\"HardpointFile\": \""+"StandardPlanet"+"\",")
			write_save_file("\"Species\": 0 }")
			write_save_file("return kShipStats",-1)
			write_save_file("def LoadModel(bPreLoad = 0):",-99)
			write_save_file("pStats = GetShipStats()",1)
			write_save_file("if (not App.g_kLODModelManager.Contains(pStats[\"Name\"])):",0)
			write_save_file("pLODModel = App.g_kLODModelManager.Create(pStats[\"Name\"])",1)
			write_save_file("pLODModel.AddLOD(pStats[\"FilenameHigh\"], 10,  40.0, 15.0, 15.0, 400, 900, \"_glow\", None, \"_specular\")",0)
			write_save_file("pLODModel.AddLOD(pStats[\"FilenameMed\"], 10,  40.0, 15.0, 15.0, 400, 900, \"_glow\", None, \"_specular\")",0)
			write_save_file("pLODModel.AddLOD(pStats[\"FilenameLow\"], 10,  40.0, 15.0, 15.0, 400, 900, \"_glow\", None, \"_specular\")",0)
			write_save_file("if (bPreLoad == 0):",0)
			write_save_file("pLODModel.Load()",1)
			write_save_file("else:",-1)
			write_save_file("pLODModel.LoadIncremental()",1)
			write_save_file("def PreLoadModel():",-99)
			write_save_file("LoadModel(1)",1)		
			close_save_file()		

		## Own stuff
		assert pSet
		if not self.IsRendered():			
			if self.Class == 'M'and FALSE:
				## Centralised waypoint
				# pWay = self.GetSolar().GetDummyWaypoint()
				
				## A planet is a ship now
				# self.Node = loadspacehelper.CreateShip(sName,pSet,self.sName,pWay.Node.GetName())
				self.Node = loadspacehelper.CreateShip(sName,pSet,self.sName,'')
				self.Node.SetScale(self.Gfx[0])

			else:
				self.Node = App.Planet_Create(self.Gfx[0],self.Gfx[1])
				self.Node.SetAtmosphereRadius(0.0*self.Node.GetRadius())
				pSet.AddObjectToSet(self.Node,self.sName)

		debug('end rendering '+self.sName)

		## Base
		Holder.Render(self,pSet)		

		## Node cache
		self.EnterNodeCache()

	# def Unrender(self):
	#	return

	def Randomise(self):
		## Base
		Holder.Randomise(self,FLEET,5.0)
		Holder.Randomise(self,MOON,3.5)
		Holder.Randomise(self,SUBWORMHOLE,18.0,0.0,25.0)
		Holder.Randomise(self,BLACKHOLE,18.0,0.0,25.0)	


		

class Moon(Planet):
	def __init__(self,ID=None):
		Planet.__init__(self,ID)

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Moon("+str(self.ID)+")")

		## Upperclass
		Planet.save(self,FALSE)

	def SetGfx(self,fRadius,sTexture):
		self.Gfx=[fRadius*scale*moonscale,sTexture]

	def Bind(self,pPlanet,cClass=None,sName=None,fPop=None):
		## Set the home planet
		self.Migrate(pPlanet.GetFather())
		self.Move(pPlanet)

		## Name
		if not sName:
			sName=pPlanet.GetName()+NumToAlpha[pPlanet.GetNumMoons()-1]
		self.sName = sName

		## Class
		if not cClass:
			cClass = "D"
		self.Class = cClass

		## Pop
		if not fPop:
			fPop = 0.0
		self.Pop = fPop
		
		## Radius
		fRadius=self.GetRandom(1.0e+2,1.0e+3)
		i=0
		while fRadius*km*scale>0.25*pPlanet.Gfx[0]:
			fRadius=self.GetRandom(1.0e+2,1.0e+3)
			i=i+1
			if i==100:
				break

		## Folder structure with the gfx
		sFolder = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Planets/D-Class'
	
		## Cached ?
		if Planet.ClassCache.has_key(self.Class):
			lsFileNames = Planet.ClassCache[self.Class]
		else:
			## What files are in the folder ?
			import Foundation
			try:
				lssFileNames = Foundation.GetFileNames(sFolder,'nif')
			except OSError:
				raise RuntimeError, "Corrupted Gfx/Planets folders"

			## Modify them
			lsFileNames = []
			for sFile in lssFileNames:
				if string.find(sFile,'_vox') != -1:
					continue
				lsFileNames.append(sFile)
	
			## Cache
			Planet.ClassCache[self.Class] = lsFileNames

		## Find our model
		fModel = ""
		if lsFileNames:
			## We found a list with names
			if lsFileNames.count(sName+'.NIF'):
				fModel = sFolder + '/' + sName + '.NIF'			
			else:
				## Take a random gfx
				if self.GetRandomSign() == -1.0:
					i = int(self.GetRandom(0.0,len(lsFileNames)))
					fModel = sFolder + '/' + lsFileNames[i]
		
		if not fModel:
			r=int(self.GetRandom(0.0,11.0))		
			if r==0:
				fModel=GFX_PATH_PLANETS+"Ariel.NIF"
			elif r==1:
				fModel=GFX_PATH_PLANETS+"Callisto.NIF"
			elif r==2:
				fModel=GFX_PATH_PLANETS+"Charon.NIF"
			elif r==3:
				fModel=GFX_PATH_PLANETS+"Ganymede.NIF"
			elif r==4:
				fModel=GFX_PATH_PLANETS+"Io.NIF"
			elif r==5:
				fModel=GFX_PATH_PLANETS+"Oberon.NIF"
			elif r==6:
				fModel=GFX_PATH_PLANETS+"Tethys.NIF"
			elif r==7:
				fModel=GFX_PATH_PLANETS+"Titan.NIF"
			elif r==8:
				fModel=GFX_PATH_PLANETS+"Titania.NIF"
			elif r==9:
				fModel=GFX_PATH_PLANETS+"Triton.NIF"
			elif r==10:
				fModel=GFX_PATH_PLANETS+"Umbriel.NIF"
			else:
				fModel=GFX_PATH_PLANETS+"Umbriel.NIF"

		## Gfx
		self.SetGfx(fRadius,fModel)
				
		#debug("Finished creating an "+self.Class+" Moon.")

	def Render(self,pSet):
		## Base
		Holder.Render(self,pSet)
		
		debug('rendering '+self.sName)

		##OWn
		if not self.IsRendered():
			self.Node = App.Planet_Create(self.Gfx[0],self.Gfx[1])
			self.Node.SetAtmosphereRadius(0.0)
			pSet.AddObjectToSet(self.Node,self.GetName())

		debug('end rendering '+self.sName)

		## Node cache
		self.EnterNodeCache()

	def Randomise(self):
		## Base
		Holder.Randomise(self,FLEET,8.0)
		Holder.Randomise(self,MOON,18.0)
		Holder.Randomise(self,SUBWORMHOLE,18.0)
		Holder.Randomise(self,BLACKHOLE,18.0,0.0,25.0)
		
	

def GetDistance(pSet1,pSet2):
	pSolarA=GetByNode(pSet1)
	pSolarB=GetByNode(pSet2)

	if pSolarA and pSolarB:
		X=pSolarA.GetLoc()
		Y=pSolarB.GetLoc()
		X.Subtract(Y)
		return X.Length()*20.0
	else:
		return -1.0
		
def GetWarpSpeed(pNode):
	pShip=GetByNode(pNode)

	return WarpSpeedToLyd(9.0)

	if not pShip:
		return -1.0
	
	return pShip.GetWarpSpeed()

def GetWarpTravelTime(pShip):
	return 30.0


def WarpSpeedToLyd(fVal):
	#Warpspeed to lightyears per day
	#Equations taken from http://www.stdimension.de/int/Cartography/index.htm
	alpha=1/365.0

	if fVal < 0:
		return 0.0
	elif fVal >=10.0:
		return 1.0e+20
	elif fVal <9.0:
		return pow(fVal,10.0/3.0)*alpha
	elif fVal>=9.0:
		return (pow(fVal,10.0/3.0)+pow(10.0-fVal,-11.0/3.0))*alpha

def IsWarping(pShip):
	if not pShip:
		return FALSE

	pWarp = pShip.GetWarpEngineSubsystem()
	if not pWarp:
		return FALSE

	if pWarp.GetWarpSequence():
		return TRUE

	return FALSE