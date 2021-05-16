import App
import math
import string
import loadspacehelper
import MissionLib

from ATP_Object import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

sShipnameFile = 'scripts/Custom/AdvancedTechnologies/Data/Universe/UniverseState/DefaultShipnames.dat'
sCharnameFile = 'scripts/Custom/AdvancedTechnologies/Data/Universe/UniverseState/DefaultCharacternames.dat'

class Race(UniverseElement):

	def __init__(self,ID=None):
		UniverseElement.__init__(self,ID)

		self.Allies	= []
		self.Enemies	= []
		self.HomeSystem	= None
		self.FleetTemplateDict	= {}
		self.ClassTemplateDict	= {}
		self.dClassTemplate = {}
		self.dCharacters = {}
		self.dVessels = {}
	
		## Ship names
		self.addReadFile('shipnames',sShipnameFile,TRUE)		
		self.addReadFile('charnames',sCharnameFile,TRUE)		

		## The race colour
		self.Colour = App.NiColorA()
		self.Colour.r = 1.0
		self.Colour.g = 1.0
		self.Colour.b = 1.0
		self.Colour.a = 1.0

		# Register at the universe
		self.Migrate(GetUniverse())			
			

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Race("+str(self.ID)+")")

		## Upperclass
		UniverseElement.save(self,FALSE)

		## Our lines
		write_save_file("self.Allies            = "+str(self.Allies))
		write_save_file("self.Enemies           = "+str(self.Enemies))
		write_save_file("self.HomeSystem        = "+str(self.HomeSystem))
		write_save_file("self.FleetTemplateDict = "+str(self.FleetTemplateDict))
		write_save_file("self.ClassTemplateDict = "+str(self.ClassTemplateDict))
		write_save_file("self.Colour            = App.NiColorA()")
		write_save_file("self.Colour.r          = "+str(self.Colour.r))
		write_save_file("self.Colour.g          = "+str(self.Colour.g))
		write_save_file("self.Colour.b          = "+str(self.Colour.b))
		write_save_file("self.Colour.a          = "+str(self.Colour.a))
		

	def SetColour(self,r,g,b,a=1.0):
		self.Colour = App.NiColorA()
		self.Colour.r = r
		self.Colour.g = g
		self.Colour.b = b
		self.Colour.a = a

	def GetColour(self):
		c = App.NiColorA()
		c.r = self.Colour.r
		c.g = self.Colour.g
		c.b = self.Colour.b
		c.a = self.Colour.a
		return c			

	def GetEnemies(self):
		ret = []
		for ID in self.Enemies:
			pRace=GetByID(ID)
			assert pRace
			ret.append(pRace)			
		return ret

	def GetAllies(self):
		ret = []
		for ID in self.Allies:
			pRace=GetByID(ID)
			assert pRace
			ret.append(pRace)		
		return ret	

	def IsEnemy(self,pRace):
		for pEnemyID in self.Enemies:
			if pEnemyID==pRace.GetID():
				return TRUE
		return FALSE

	def IsAlly(self,pRace):
		if self.ID==pRace.GetID():
			return TRUE

		for pAllyID in self.Allies:
			if pAllyID==pRace.GetID():
				return TRUE
		return FALSE

	def IsNeutral(self,pRace):
		return not self.IsAlly(pRace) and not self.IsEnemy(pRace)

	def GetHomeSystem(self):
		return GetByID(self.HomeSystem)

	def SetAlly(self,pRace):
		self.RemoveAlly(pRace)
		self.Allies.append(pRace.ID)

	def RemoveAlly(self,pRace):
		ID = pRace.ID
		if self.Allies.count(ID):
			self.Allies.remove(ID)
	
	def SetEnemy(self,pRace):
		self.RemoveEnemy(pRace)
		self.Enemies.append(pRace.ID)

	def RemoveEnemy(self,pRace):
		for ID in self.Enemies:
			if ID==pRace.ID:
				self.Enemies.remove(ID)
				break
	
	def SetHomeSystem(self,pSolar):
		self.HomeSystem=pSolar.ID
	
	## Fleets
	#############################################"

	def AddFleetTemplate(self,sName,*lArgs):
		#eg "Offensive" , "BB@1;DN@2;CC@4"
		lsGroup = []
		for sGroup in lArgs:
			lsGroup.append(sGroup[:])			

		self.FleetTemplateDict[sName[:]]=lsGroup

	def GetFleetTemplate(self,sName):
		if self.FleetTemplateDict.has_key(sName):
			return self.GetRandomItem(self.FleetTemplateDict[sName])
		return None	

	## Class
	##############################################
	def GetClassTemplate(self,sClass):
		## Cached query
		if self.dClassTemplate.has_key(sClass):
			return self.GetRandomItem(self.dClassTemplate[sClass])
		else:
			dVessels = self.dVessels
			ret = []
			for key in dVessels.keys():
				if sClass == dVessels[key].sClass:
					ret.append(key)
			self.dClassTemplate[sClass] = ret
			return self.GetRandomItem(ret)

	## Ships
	#################################################"
	
	def SetVesselType(self,sGfx,sClass,sNameTemplate,sBridgeType,fBuildPoints,bObsolete,bStationary):
		self.dVessels[sGfx] = VesselType(sClass,sNameTemplate,sBridgeType,fBuildPoints,bObsolete,bStationary)
		
	def GetVesselType(self,sGfx):
		return self.dVessels[sGfx]

	def GetVesselClass(self,sGfx):
		return self.dVessels[sGfx].sClass

	def IsVesselStationary(self,sGfx):
		return self.dVessels[sGfx].bStationary

	def GetRandomVesselType(self,bStationary=FALSE):
		for i in range(50):
			key = self.GetRandomItem(self.dVessels.keys())
			pVesselType = self.dVessels[key]
			if pVesselType.bStationary == bStationary:
				return key
		return None
			 

	#Universe interaction functions:

	def SetTargetFleetCount(self,iVal):
		self.iGoalFleetCount	= iVal
		self.iFleetCount	= 1
	
		self.A = GetUniverse().GetChildByName("Balancar")
		self.B = GetUniverse().GetChildByName("Ferenginar")

		self.AddClock('FleetBuild',0.20)	

	
	def FleetBuild(self,gEvent):
		import ATP_Vessels
		pFleet = ATP_Vessels.Fleet()
		pFleet.Bind(self,self.B,"Merchant Fleet "+str(self.iFleetCount),"HEAVY_COMMERCE_LINE")
		pFleet.SetupSpaceline([self.A,self.B])
		self.iFleetCount = self.iFleetCount + 1
		if self.iFleetCount > self.iGoalFleetCount:
			self.RemoveClock('FleetBuild')

	def ShipyardAskForOrders(self,pYard):
		## For now just return a random ship
		return self.GetRandomVesselType(),''

	## Rections
	def FleetDestroyed(self,pFleet):
		debug("fleet "+pFleet.sName+" was destroyed in me, "+self.sName)

		## Check
		assert self.HasChild(pFleet)

		## Detach it
		pFleet.Migrate(None)

	def ShipDestroyed(self,pShip,pFleet):
		debug("ship "+pShip.sName+" was destroyed in me, "+self.sName)

	## Dynamic music
	###################################
	def SetEnterMusic(self,sMusic):
		self.sEnterMusic = sMusic

	def GetEnterMusic(self):
		if hasattr(self,'sEnterMusic'):
			return self.sEnterMusic
		else:
			return ''

	## Bridges and characters
	#######################################

	def SetCharacters(self,sGroup , sNameTemplate, sGender , lsHeads , lsBodies):
		if sGender =='X':
			self.dCharacters[sGroup,'M'] = lsHeads , lsBodies , sNameTemplate
			self.dCharacters[sGroup,'F'] = lsHeads , lsBodies , sNameTemplate
		else:
			self.dCharacters[sGroup,sGender] = lsHeads , lsBodies , sNameTemplate

	def GetCharacterData(self,sGroup,sGender=''):
		## A gender
		if not sGender:
			sGender = self.GetRandomItem(('M','F'))

			## Get the data
			if not self.dCharacters.has_key(sGroup,sGender):
				dTrans = { 'M':'F','F':'M' }
				sGender = dTrans[sGender]
				if not self.dCharacters.has_key(sGroup,sGender):
					return None,None

		else:
			if not self.dCharacters.has_key(sGroup,sGender):
				return None,None

		## Data
		pData = self.dCharacters[sGroup,sGender]

		## Modify the name
		sNameTemplate = pData[2]

		## Replace
		sName = self.GetNextCharacterName()
		sNameTemplate = string.replace(sNameTemplate,'$$',sName)
		
		## Random data
		return self.GetRandomItem(pData[0]) , self.GetRandomItem(pData[1]) , sNameTemplate	

	## Names
	########################################
	def SetShipnameFile(self,sFile):
		self.closeFile('shipnames')
		self.addReadFile('shipnames',sFile,TRUE)
	
	def GetNextShipName(self,sGfx):
		## File acces
		sBaseName = self.readNextLine('shipnames')

		## Class specs
		sTemplate = self.GetVesselType(sGfx).sNameTemplate

		## Change the $$ token with the provided name
		## 'USS $$' --> 'USS Jupiter'
		return string.replace(sTemplate,'$$',sBaseName)
		
	def SetCharacternameFile(self,sFile):
		self.closeFile('charnames')
		self.addReadFile('charnames',sFile,TRUE)

	def GetNextCharacterName(self):
		## File acces
		return self.readNextLine('charnames')
	


class VesselType:
	def __init__(self,sClass='CC',sNameTemplate='$$',sBridgeType='Galaxy',fBuildPoints=1000.0,bObsolete=FALSE,bStationary=FALSE):
		## Attr
		self.sClass = sClass
		self.sNameTemplate = sNameTemplate
		self.sBridgeType = sBridgeType
		self.fBuildPoints = fBuildPoints
		self.bStationary = bStationary
		self.bObsolete = bObsolete

class Mission(UniverseElement):
	def __init__(self):
		UniverseElement.__init__(self)

		

	 

	