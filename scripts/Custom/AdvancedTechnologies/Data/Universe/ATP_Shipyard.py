import App
import math
import string
import loadspacehelper
import MissionLib

from ATP_Object   import *
from ATP_Vessels  import *
from Custom.AdvancedTechnologies.Data.ATP_Tools   import *
from Custom.AdvancedTechnologies.Data.ATP_Config  import *

ATP_GUIUtils = __import__(ATP_GUIUTILS)


class Shipyard(Ship):
	# A shipyard will be selffunctional
	#
	# Each clocktick it will continue building its the current ship, when done, it will release it
	# call the host empire for new orders

	def __init__(self):
		Ship.__init__(self)
					
		self.BuildSpeed 	= SHIPYARD_BUILDSPEED/5.0
		self.ET_SHIP_RELEASED 	= App.UtopiaModule_GetNextEventType()

		## What must we build ?
		#Ask for new orders in 5 secs
		self.AddClock("AskForOrders",15.0)

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Shipyard("+str(self.ID)+")")

		## Upperclass
		Ship.save(self,FALSE)

		## Our lines
		write_save_file("self.BuildSpeed = "+str(self.BuildSpeed))
	
	def GetShipReleasedEvent(self):
		return self.ET_SHIP_RELEASED

	def FleetDestroyed(self,pFleet):
		## Remove the clock
		self.RemoveClock("constructionClock")		

		## Upcall
		Ship.FleetDestroyed(self,pFleet)

	def AddShipToBuild(self,sGfxName,sShipName=""):
		pSingular=SingularFleet()	
		pSingular.Bind(self.GetRace(),self,sGfxName,sShipName)
		pSingular.SetPosition(self.GetPosition())
		pChild = pSingular.GetShips()[0]		
		pChild.SetBuildPercentage(0.0)
		pChild.SetHullPercentage(0.2)

		if self.GetNode():
			pSingular.Render(self.GetSolar().GetNode())
			self.Randomise()
			
			self .Node.EnableCollisionsWith(pChild.Node ,FALSE)
			pChild.Node.EnableCollisionsWith(self .Node ,FALSE)

			pSingular.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT])


	def constructionClock(self,pEvent):
		Children = self.GetChildren(FLEET)
		if not Children:
			self.RemoveClock("constructionClock")
			
		for pFleet in self.GetChildren(FLEET):
			pChild = pFleet.GetShips()[0]

			#For now our hull will indicate our build speed mod
			add=self.BuildSpeed*self.HullPercentage
			pChild.AddBuildPoints(add)
			pChild.DamageHull(-add/pChild.GetBuildPoints()*self.GetHull()*0.8)

			if pChild.GetBuildPercentage()==1.0:
				#Release the ship/fleet
				if self.GetNode():
					pFleet.AssignAI([AI_PATH+".ATP_LeaveShipyardAI",self,self.ET_SHIP_RELEASED])				
				
				#Prepare an event
				self.AddHandler(self.ET_SHIP_RELEASED,"ReleaseShip")

				#Ship out of database
				pChild.GetFleet().Move(self.GetHolder())

		
	def ReleaseShip(self,pEvent):
		## Get the ship out the event
		pShip = GetByID(pEvent.GetInt())
		assert pShip
		
		## Release the ship totally	
		pShip.GetFleet().AssignAI()			

		## Reinstate collisions
		self .Node.EnableCollisionsWith(pShip.Node ,TRUE)
		pShip.Node.EnableCollisionsWith(self .Node ,TRUE)

		## Remove the handler
		self.RemoveHandler(self.ET_SHIP_RELEASED,"ReleaseShip")

		## Ask for new orders in 15 secs
		self.AddClock("AskForOrders",15.0)

	def AskForOrders(self,pEvent=None):
		#Ask the race for orders
		sGfx,sShipName=self.GetRace().ShipyardAskForOrders(self)
	
		if sGfx:
			#End the timer
			self.RemoveClock("AskForOrders")
	
			#New orders received
			self.AddShipToBuild(sGfx,sShipName)			
		
			
	def Randomise(self,type=UNIVERSE_ELEMENT,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		#debug("Randomising "+self.sName + " for type "+type)
			
		for pFleet in self.GetFleets():
			pFleet.Randomise()
			pFleet.SetRelativePositionXYZ(0.0,0.0,0.0,self)

			for pShip in pFleet.GetShips():
				pShip.SetRelativePositionXYZ(0.0,0.0,0.0,self)


	def SetBuildSpeed(self,fVal):
		self.BuildSpeed=fVal
	
	def GetBuildSpeed(self):
		return self.Speed	

	def WarpToSolar(self,pSolar,pcPlacementName):
		raise RuntimeError

	def CanWarp(self):
		return FALSE

	def AssignAI(self,kArgs=None,force=FALSE):
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]

		#debug("Assigning AI for "+self.sName)

		## Own AI
		Ship.AssignAI(self,kArgs,force)

		##Children AI
		for pFleet in self.GetFleets():
			pFleet.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],force)
