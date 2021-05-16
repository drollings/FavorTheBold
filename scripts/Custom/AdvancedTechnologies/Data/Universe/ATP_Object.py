import App
import math
import string

FALSE=0 
TRUE=1

TREE_ELEMENT	= 'TreeElement'
UNIVERSE_ELEMENT= 'UniverseElement'
UNIVERSE	= 'Universe'
RACE		= 'Race'
SOLAR		= 'SolarSystem'
STARBASE_SYSTEM = 'StarbaseSystem'
NEBULA		= 'Nebula'
SUN		= 'Sun'
PLANET		= 'Planet'
MOON    	= 'Moon'
FLEET		= 'Fleet'
SUPPLY_FLEET	= 'SupplyFleet'
PLAYER_FLEET	= 'PlayerFleet'
SHIP		= 'Ship'
PLAYER_SHIP	= 'PlayerShip'
SHIPYARD	= 'Shipyard'
STARBASE	= 'Starbase'
EXTRA		= 'Extra'
WORMHOLE	= 'Wormhole'
SUBWORMHOLE	= 'SubWormhole'
HOLDER		= 'Holder'
COMET		= 'Comet'
WAYPOINT	= 'Waypoint'
BRIDGE		= 'Bridge'
CHARACTER	= 'Character'
SINGULAR_FLEET	= 'SingularFleet'
BLACKHOLE	= 'Blackhole'
BLACKHOLE_SYSTEM= 'BlackholeSystem'


UNIVERSE_GAME_ID	= 1
UNIVERSE_ID		= 2
ARCHITECT_ID		= 3
MATRIX_ID		= 4
PLAYER_FLEET_ID		= 5
PLAYER_SHIP_ID		= 6
STARCHARTS_ID		= 7
PLAYER_BRIDGE_ID	= 8
SOLAR_INTERFACE_ID	= 9
INTERSTELLAR_INTERFACE_ID = 10
MUSIC_ID		  = 11
CAMERA_MANAGER_ID	  = 12
ANIMATION_MANAGER_ID	  = 13
GALAXY_MAP_ID		  = 14


ACK	= 1
NAK	= 2

NORMAL = 1
INSIDE = 2
WARPING = 3
INTERCEPTING = 4
ENTERING = 5
EXITING	 = 6
DEAD	= 7
BUILDING = 8
REPAIR = 9	
	
IDLE = 101
VOYAGING = 102
VOYAGE_ERROR = 103

NumToRoman = {	0:"0",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",
              	15:"XV",16:"XVI",17:"XVII",18:"XVIII",19:"XIX",20:"XX",21:"XXI",22:"XXII",23:"XXIII",24:"XXIV",25:"XXV",26:"XXVI",
		27:"XXVII",28:"XXVIII" }
NumToAlpha = string.lowercase[:]
NumToUpperAlpha = string.uppercase[:]

NumToGreek = { 0:'',1:'Alpha',2:'Beta',3:'Gamma',4:'Delta',5:'Epsilon',6:'Zeta',7:'Eta',8:'Theta',9:'Iota'}

from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *
from ATP_UniverseConfig import *


class ATP_EventHandlerObject:
	dEventTypes = {}
	lEventTypes = []
	EventDict = {}
	Dict = {}

	def __init__(self,ID = None):
		
		## Find an unique ID
		if not ID:
			ID = 100 ## smaller then 100 is reserved
			while (TRUE):
				if not ATP_EventHandlerObject.Dict.has_key(ID):
					break
				ID=ID+1
		self.ID=ID

		## Game communication
		self.Wrapper 	= App.TGPythonInstanceWrapper()
		self.Wrapper.SetPyWrapper(self)
		self.Timers   = {}
		self.Handlers = {}

		## Random numbers
		self.Random	= self.ID	

		## Create an entry in the Dict
		ATP_EventHandlerObject.Dict[self.ID] = self

	def delete(self):
		## Remove wrapper related things
		for e,f in self.Timers.keys():
			self.RemoveClock(f,e)
		for e,s in self.Handlers.keys():
			self.RemoveHandler(e,s)

		## Files
		if hasattr(self,'dFiles'):
			for key in self.dFiles.keys():
				fFile = self.dFiles[key]
				fFile.close()
			self.dFiles = {}

		## The dict entry
		if ATP_EventHandlerObject.Dict.has_key(self.ID):
			del ATP_EventHandlerObject.Dict[self.ID]		

	def exit_game_delete(self):
		## Remove wrapper related things
		for e,f in self.Timers.keys():
			self.RemoveClock(f,e)
		for e,s in self.Handlers.keys():
			self.RemoveHandler(e,s)

		## Files
		if hasattr(self,'dFiles'):
			for key in self.dFiles.keys():
				fFile = self.dFiles[key]
				fFile.close()
			self.dFiles = {}

		## The dict entry
		if ATP_EventHandlerObject.Dict.has_key(self.ID):
			del ATP_EventHandlerObject.Dict[self.ID]

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *

		if first:
			write_save_file('self = ATP_EventHandlerObject('+str(self.ID)+')' )

		## Attrs
		write_save_file('self.Random    	='+str(self.Random))				

	def post_save(self):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *

		## Anything to save?
		if not self.Timers and not self.Handlers:
			return
		
		for e,sFunctionHandler in self.Timers.keys():
			element 	= self.Timers[e,sFunctionHandler]
			pTimer		= element[0]
			fGranulation 	= element[1]
			myEvent 	= element[2]
			bDelay 		= element[3]
				
			## Source and destination
			Source = myEvent.GetSource()
			Destination = myEvent.GetDestination()
			
			## Savestring
			s = ''

			if not bDelay:
				s = s + 'self.AddClock('
			else:
				s = s + 'self.AddDelay('
			
			s = s + '\'' + sFunctionHandler +'\'' +','

			if not bDelay:
				s = s + str(fGranulation) + ','
			else:
				s = s + str(pTimer.GetTimerStart()-App.g_kUtopiaModule.GetGameTime()) + ','

			if Source:
				s = s + 'GetByID(' + str(Source.ID) +')' + ','
			else:
				s = s + 'None' + ','

			if Destination:
				s = s + 'GetByID(' + str(Destination.ID) +')'
			else:
				s = s + 'None'

			s = s + ')'
			
			## Save
			write_save_file(s)

		for e,sFunctionHandler in self.Handlers.keys():
			## Savestring
			s = ''
			s = s + 'self.AddHandler('
			s = s + str(e) + ','
			s = s + '\'' + sFunctionHandler +'\'' +')'
			
			## Save			
			write_save_file(s)
	
	def IsSaveable(self):
		return FALSE

	def GetID(self):	
		return self.ID	

	## Game API and Dynamics
	##########################		
	def AddHandler(self,eventType,sFunctionHandler):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('AddHandler(self,eventType,sFunctionHandler)')

		## Dict
		EventDict = ATP_EventHandlerObject.EventDict

		## Already definined
		if self.Handlers.has_key(eventType,sFunctionHandler):
			return

		## Wrapper event
		self.Wrapper.RemoveHandlerForInstance         (eventType,sFunctionHandler)
		self.Wrapper.AddPythonMethodHandlerForInstance(eventType,sFunctionHandler)

		## Register the event
		self.Handlers[eventType,sFunctionHandler] = 0
		
		## Indirect call mechanism
		if not EventDict.has_key(eventType):
			EventDict[eventType] = {}

			## Register the game event
			App.g_kEventManager.RemoveBroadcastHandler       (eventType,App.Game_GetCurrentGame(),__name__+'.Redirect')
			App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,App.Game_GetCurrentGame(),__name__+'.Redirect')

		## Register it for Redirect
		EventDict[eventType][self.Wrapper.GetObjID()] = self.Wrapper,self

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)
			
	def RemoveHandler(self,e,sFunctionHandler):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('RemoveHandler(self,e,sFunctionHandler)')

		## Dict
		EventDict = ATP_EventHandlerObject.EventDict
		
		## Remove instances
		self.Wrapper.RemoveHandlerForInstance(e,sFunctionHandler)

		## Unregister the event
		if self.Handlers.has_key(e,sFunctionHandler):
			del self.Handlers[e,sFunctionHandler]				
		
		## Update the indirect call mechanism
		if EventDict.has_key(e):
			listeners = EventDict[e]
			WID = self.Wrapper.GetObjID()
			if listeners.has_key(WID):
				del listeners[WID]				
			if not listeners:
				# App.g_kEventManager.RemoveBroadcastHandler(e,App.Game_GetCurrentGame(),__name__+'.Redirect')
				del EventDict[e]

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)


	def PurgeHandlers(self):
		for e,s in self.Handlers.keys():
			self.RemoveHandler(e,s)


	def AddClock(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('AddClock(self,sFunctionHandler)')

		## Create an event
		e=GetNextEventType()

		## Indirect ATP_Event
		myEvent = ATP_Event(e,pSource,pDestination)

		## Game event
		pEvent = App.TGIntEvent_Create()
		pEvent.SetInt(myEvent.GetID())
		pEvent.SetEventType(e)
		#pEvent.SetDestination(self.Wrapper)
		
		## Timer
		timer=App.TGTimer_Create()
		timer.SetEvent(pEvent)
		timer.SetTimerStart(App.g_kUtopiaModule.GetGameTime()+fGranulation)
		timer.SetDelay(fGranulation)
		timer.SetDuration(-1.0)
		if not bRealtime:
			App.g_kTimerManager.AddTimer(timer)
		else:
			App.g_kRealtimeTimerManager.AddTimer(timer)
		
		## Register it to ourself
		self.Timers[e,sFunctionHandler]=timer,fGranulation,myEvent,FALSE,bRealtime
		
		## Regiser it to the game
		# self.Wrapper.AddPythonMethodHandlerForInstance(e,sFunctionHandler)
		self.AddHandler(e,sFunctionHandler)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def AddSpaceClock(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		self.AddClock(sFunctionHandler,fGranulation,pSource,pDestination,bRealtime)

	def AddGameClock(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		self.AddClock(sFunctionHandler,fGranulation,pSource,pDestination,bRealtime)

	def AddDelay(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('AddDelay()')

		## Create an event
		e=GetNextEventType()

		## Indirect ATP_Event
		myEvent = ATP_Event(e,pSource,pDestination)

		## Game event
		pEvent = App.TGIntEvent_Create()
		pEvent.SetInt(myEvent.GetID())
		pEvent.SetEventType(e)
		#pEvent.SetDestination(self.Wrapper)
		
		## Timer
		timer=App.TGTimer_Create()
		timer.SetEvent(pEvent)
		timer.SetTimerStart(App.g_kUtopiaModule.GetGameTime()+fGranulation)
		timer.SetDelay(fGranulation)
		timer.SetDuration(-1.0)
		if not bRealtime:
			App.g_kTimerManager.AddTimer(timer)
		else:
			App.g_kRealtimeTimerManager.AddTimer(timer)
		
		## Register it to ourself
		self.Timers[e,sFunctionHandler]=timer,fGranulation,myEvent,TRUE,bRealtime
		
		## Register it to the game
		# self.Wrapper.AddPythonMethodHandlerForInstance(e,sFunctionHandler)
		self.AddHandler(e,sFunctionHandler)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def AddGameDelay(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		self.AddDelay(sFunctionHandler,fGranulation,pSource,pDestination,bRealtime)

	def AddSpaceDelay(self,sFunctionHandler,fGranulation=1.0,pSource=None,pDestination=None,bRealtime=FALSE):
		self.AddDelay(sFunctionHandler,fGranulation,pSource,pDestination,bRealtime)

	def RemoveDelay(self,e):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('RemoveDelay(self,e)')

		for le,lsFunctionHandler in self.Timers.keys():
			if le == e:
				if self.Timers[le,lsFunctionHandler][3]:
					self.RemoveClock(lsFunctionHandler,le)

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)
				

	def RemoveClock(self,sFunctionHandler,e=None,pSource=None,pDestination=None):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('RemoveClock(self,e)')

		## If e is not specified remove all clocks on sFunctionHandler
		if not e:
			for le,lsFunctionHandler in self.Timers.keys():
				if lsFunctionHandler == sFunctionHandler:
					node = self.Timers[le,lsFunctionHandler]
					
					## ATP_Event no longer needed
					myEvent = node[2]
					if pSource:
						if pSource.ID != myEvent.GetSource().ID:
							continue
					if pDestination:
						if pDestination.ID != myEvent.GetDestination().ID:
							continue
											
					## Remove the handler
					# self.Wrapper.RemoveHandlerForInstance(le,lsFunctionHandler)
					self.RemoveHandler(le,sFunctionHandler)
					
					## Delete the timer
					if not node[4]:
						App.g_kTimerManager.DeleteTimer(node[0].GetObjID())
					else:
						App.g_kRealtimeTimerManager.DeleteTimer(node[0].GetObjID())

					
					## Unregister it
					del self.Timers[le,lsFunctionHandler]

					myEvent.delete()				

		## Remove a specific clock
		else:
			if self.Timers.has_key(e,sFunctionHandler):
				node = self.Timers[e,sFunctionHandler]
				
				## ATP_Event no longer needed
				myEvent = node[2]

				## Match ?
				if pSource:
					if pSource.ID != myEvent.GetSource().ID:
						## Stop local profiling
						App.TGProfilingInfo_StopTiming(idProfiling)
						return
				if pDestination:
					if pDestination.ID != myEvent.GetDestination().ID:
						## Stop local profiling
						App.TGProfilingInfo_StopTiming(idProfiling)
						return

				myEvent.delete()
						
				## Remove the handler
				self.RemoveHandler(e,sFunctionHandler)
		
				## Delete the timer
				App.g_kTimerManager.DeleteTimer(node[0].GetObjID())
				
				## Unregister it
				del self.Timers[e,sFunctionHandler]

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

	def PurgeClocks(self):
		for e,s in self.Timers.keys():
			self.RemoveClock(s,e)


	def Raise(self,e,pSource=None,pDestination=None):
		## Create and ATP_Event
		myEvent = ATP_Event(e,pSource,pDestination)

		## Create a game event
		gEvent = App.TGIntEvent_Create()
		gEvent.SetEventType(e)		
		gEvent.SetInt(myEvent.GetID())

		## Redirect the game event
		Redirect(App.Game_GetCurrentGame(),gEvent)

		## Delete the temporarely event
		myEvent.delete()

		return gEvent


	def RaiseEvent(self,e,pEvent):
		## ATP_Event given as argument

		## Create a game event
		gEvent = App.TGIntEvent_Create()
		gEvent.SetEventType(e)		
		gEvent.SetInt(pEvent.GetID())
		
		Redirect(App.Game_GetCurrentGame(),gEvent)
		
		return gEvent


	def FakeEvent(self,e=0,pSource=None,pDestination=None):
		## Create and ATP_Event
		myEvent = ATP_Event(e,pSource,pDestination)

		## Create a game event
		gEvent = App.TGIntEvent_Create()
		gEvent.SetEventType(e)		
		gEvent.SetInt(myEvent.GetID())
		return gEvent,myEvent


	def GetWrapper(self):
		return self.Wrapper

	## Files
	########################################
	def addReadFile(self,sName,sFile,bLoop=FALSE):
		## Modify
		import string
		sFile = string.replace(sFile,'/','\\')

		## Dict
		if not hasattr(self,'dFiles'):
			self.dFiles = {}
		if self.dFiles.has_key(sName):
			raise OSError , 'file '+sName+' already open'

		## Loop ?
		self.bLoop = bLoop

		## File
		import nt
		iFile = nt.open(sFile,nt.O_RDONLY)		
		self.dFiles[sName] = nt.fdopen(iFile)

	def readNextLine(self,sName):
		## Check
		if not self.dFiles.has_key(sName):
			raise OSError , 'file '+sName+' not open'

		## Read
		fFile = self.dFiles[sName]
		s = fFile.readline()

		## EOF ?
		if not s:
			if self.bLoop:
				fFile.seek(0)
				return self.readNextLine(sName)
			else:
				return None
		else:
			return s[:-1]
			

	def addWriteFile(self,sName,sFile):
		## Modify
		import string
		sFile = string.replace(sFile,'/','\\')

		## Dict
		if not hasattr(self,'dFiles'):
			self.dFiles = {}
		if self.dFiles.has_key(sName):
			raise OSError , 'file '+sName+' already open'

		## File
		import nt		
		iFile = nt.open(sFile,nt.O_WRONLY|nt.O_TRUNC|nt.O_CREAT)
		self.dFiles[sName] = nt.fdopen(iFile)

	def writeNextLine(self,sName,sLine):
		## Check
		if not self.dFiles.has_key(sName):
			raise OSError , 'file '+sName+' not open'

		## Read
		fFile = self.dFiles[sName]
		fFile.write(sLine)
			

	def closeFile(self,sName):
		##Check
		if not self.dFiles.has_key(sName):
			raise OSError , 'file '+sName+' not open'
		
		## Close it
		fFile = self.dFiles[sName]
		fFile.close()		

		## Forget it
		del self.dFiles[sName]


	## Random number generator
	##############################
	def GetRandom(self,fVal1=1.0,fVal2=0.0):		
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('Jitter()')

		self.Random = ( self.Random * 10000 ) % 10007 ## 10007 is a prime number		
		f = float(self.Random)/10007.0
		ret = (fVal2 * f + fVal1 * (1-f))
		
		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		return ret

	def GetRandomSign(self):
		if self.GetRandom(-1.0,1.0) <= 0.0:
			return -1.0
		return 1.0		

	def EvolveRandom(self,i):
		for j in range(i):
			self.GetRandom()

	def GetRandomItem(self,lList):
		if not lList:
			return None
		return lList[int(self.GetRandom(0,len(lList)))]

	def GetRandomInt(self,iL,iU):
		return int(self.GetRandom(iL,iU))

	def GetRandomVector(self,fRad):
		fRad = fRad * math.sqrt(3.0)/3.0
		return Vector(self.GetRandom(-fRad,fRad),self.GetRandom(-fRad,fRad),self.GetRandom(-fRad,fRad))

	def Jitter(self,fVal,fPer=50.0):
		fPer = fPer / 100.0
		return fVal * self.GetRandom(1-fPer,1+fPer)

	## Tools
	IsTypeOfCache = {}
	def IsTypeOf(self,type):
		s = self.__class__.__name__
		if TreeElement.IsTypeOfCache.has_key(s,type):
			return TreeElement.IsTypeOfCache[s,type]			
		seq = [self.__class__.__name__]
		seq = seq + GetAllParentClasses(self.__class__)
		ret = FALSE
		for pClass in seq:
			if pClass == type:
				ret = TRUE
				break		
		TreeElement.IsTypeOfCache[s,type] = ret
		return ret

	def IsExactTypeOf(self,type):
		return (type == self.__class__.__name__)

	

class TreeElement(ATP_EventHandlerObject):
		
	def __init__(self,ID = None):
		self.Parents	= []
		self.Children	= []		

		## Superclass class
		ATP_EventHandlerObject.__init__(self,ID)

	def __str__(self):
		return self.__class__.__name__+'_'+str(self.ID)

	def __repr__(self):
		return self.__class__.__name__

	## Delete
	############################################
	def exit_game_delete(self):
		## Delete all children
		for Child in self.GetChildren():
			Child.exit_game_delete()

		## Decouple us
		for Parent in self.GetDirectParents():
			Parent.RemoveChild(self)		

		## Upclass
		ATP_EventHandlerObject.exit_game_delete(self)

	def delete(self):
		## Delete all children
		for Child in self.GetChildren():
			Child.delete()

		## Decouple us
		for Parent in self.GetDirectParents():
			Parent.RemoveChild(self)		

		## Superclass
		ATP_EventHandlerObject.delete(self)


	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		if first:
			write_save_file('self = TreeElement('+str(self.ID)+')')

		## Superclass
		ATP_EventHandlerObject.save(self,FALSE)

		## Filter children
		saveChildren = []
		for Child in self.GetChildren():
			if Child:
				if Child.IsSaveable():
					saveChildren.append(Child.ID)
		saveParents = []
		for Parent in self.Parents:
			Parent = GetByID(Parent)
			if Parent:
				if Parent.IsSaveable():
					saveParents.append(Parent.ID)		

		write_save_file('self.Parents ='+str(saveParents))
		write_save_file('self.Children ='+str(saveChildren))

	def post_save(self):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *

		## Call ourself
		write_save_file('self = GetByID('+str(self.ID)+')')

		## Superclass
		ATP_EventHandlerObject.post_save(self)

	def IsSaveable(self):
		return TRUE	
		
	## Tree related functions
	def GetParent(self,type=TREE_ELEMENT):
		for ParentID in self.Parents:
			Parent = GetByID(ParentID)
			assert Parent
			if Parent.IsTypeOf(type):
				return Parent

		for ParentID in self.Parents:
			Parent = GetByID(ParentID)
			res = Parent.GetParent(type)
			if res:
				return res
		return None

	def GetDirectParent(self,type=TREE_ELEMENT):
		for ParentID in self.Parents:
			Parent = GetByID(ParentID)
			assert Parent
			if Parent.IsTypeOf(type):
				return Parent		
		return None

	def GetDirectParents(self):
		ret = ()
		for ParentID in self.Parents:
			Parent = GetByID(ParentID)
			assert Parent
			ret = ret + (Parent,)
		return ret

	def AddParent(self,Parent):
		if self.Parents.count(Parent.ID):
			raise RuntimeError, "Parent already defined"
		self.Parents.append(Parent.ID)		

	def RemoveParent(self,Parent):
		PID = Parent.ID
		for ParentID in self.Parents:
			if ParentID == PID:
				self.Parents.remove(PID)
				break

	def GetChildren(self,type=TREE_ELEMENT):
		retList =[]
		for ChildID in self.Children:
			Child = GetByID(ChildID)
			assert Child
			if Child.IsTypeOf(type):
				retList.append(Child)
		return retList

	def GetAllChildren(self,type=TREE_ELEMENT):
		retList =[]
		for ChildID in self.Children:
			Child = GetByID(ChildID)
			if Child.IsTypeOf(type):
				retList.append(Child)
			retList = retList + Child.GetAllChildren(type)							
		return retList

	def AddChild(self,Object):
		if self.Children.count(Object.ID):
			raise RuntimeError, "Child already defined"
		self.Children.append(Object.ID)
		Object.AddParent(self)

	def RemoveChild(self,Object):
		OID = Object.ID
		for ChildID in self.Children:
			if ChildID == OID:
				self.Children.remove(ChildID)
				break
		Object.RemoveParent(self)

	def HasChild(self,obj):
		OID = obj.ID
		for CID in self.Children:
			if OID == CID:
				return TRUE
		return FALSE
	
				 

class UniverseElement(TreeElement):	
	NodeCache = {}
		
	## Class related functions
	##############################
	def __init__(self,ID = None):
		## Parent class constructor
		TreeElement.__init__(self,ID)

		## Own data members
		self.sName	= self.__class__.__name__+str(self.ID)
		self.sShortName = ''
		self.vPosition	= App.TGPoint3()
		self.vPosition.SetXYZ(0.0,0.0,0.0)
		self.Node	= None
		self.CachedSolar = None		

	def __str__(self):
		return self.sName

	def delete(self):
		## Don't remember our node
		self.Unrender()
		
		## Base class delete
		TreeElement.delete(self)

	def exit_game_delete(self):
		## Base class delete
		TreeElement.exit_game_delete(self)

	def PurgeCache(self):
		UniverseElement.NodeCache = {}

	def log(self,indent=0):
		#debug('\t'*indent+self.sName+'-->')
		for ID in self.Children:
			GetByID(ID).log(indent+2)

	def poslog(self,indent=0):
		hol= self.GetHolder()
		if hol:
			#debug('\t'*indent+self.sName+'-->'+printVector(self.GetRelativePosition(hol)))
			pass
		else:
			#debug('\t'*indent+self.sName+'-->')
			pass

		for ID in self.Children:
			GetByID(ID).poslog(indent+2)

	## Save function
	###########################
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file('self = UniverseElement('+str(self.ID)+')')

		## Upperclass
		TreeElement.save(self,FALSE)

		## Our lines
		write_save_file('self.sName     	=\''+str(self.sName)+'\'')
		write_save_file('self.sShortName	=\''+str(self.sShortName)+'\'')
		write_save_file('self.SetPositionXYZ( '+str(self.vPosition.GetX())+' , '+str(self.vPosition.GetY())+' , '+str(self.vPosition.GetZ())+' )')		

	def post_save(self):
		## Superclass
		TreeElement.post_save(self)

	## Tree additions
	#############################
	def GetBrothers(self):
		pFather = self.GetFather()
		if pFather:
			lChildren = pFather.GetChildren(self.__class__.__name__)
			lChildren.remove(self)
			return lChildren
		else:
			return []

	## Accessors and modifiers
	#############################
	def GetNode(self):
		return self.Node

	def SetNode(self,Node):
		self.PurgeNodeCache()
		self.Node=Node
		self.EnterNodeCache()

	def GetName(self):
		return self.sName[:]

	def SetName(self,sName):
		self.sName=sName[:]
	
	def GetShortName(self):
		if self.sShortName:
			return self.sShortName[:]
		else:
			return self.sName[:]

	## Static Holder and Father Methods
	################################
	def AddRace(self,pChild):
		self.AddChild(pChild)
	
	def GetRace(self):
		return self.GetParent(RACE)
	
	def GetRaces(self):
		return self.GetChildren(RACE)

	def GetNumRaces(self):
		return len(self.GetRaces())

	def AddSolar(self,pChild):
		self.AddChild(pChild)
	
	def GetSolar(self):
		if self.CachedSolar:
			return self.CachedSolar
		ret = self.GetParent(SOLAR)
		self.CachedSolar = ret		
		return ret

	def GetSolarID(self):
		if self.CachedSolar:
			return self.CachedSolar.ID
		else:
			return self.GetSolar().ID
		
	def GetSolars(self):
		return self.GetChildren(SOLAR)

	def GetNumSolars(self):
		return len(self.GetSolars())

	def AddSun(self,pChild):
		self.AddChild(pChild)
	
	def GetSun(self):
		return self.GetParent(SUN)
	
	def GetSuns(self):
		return self.GetChildren(SUN)

	def GetAllSuns(self):
		return self.GetAllChildren(SUN)

	def GetNumSuns(self):
		return len(self.GetSuns())

	def GetNumAllSuns(self):
		return len(self.GetAllSuns())

	def AddPlanet(self,pChild):
		self.AddChild(pChild)
	
	def GetPlanet(self):
		return self.GetParent(PLANET)
	
	def GetPlanets(self):
		return self.GetChildren(PLANET)

	def GetAllPlanets(self):
		return self.GetAllChildren(PLANET)

	def GetNumPlanets(self):
		return len(self.GetPlanets())

	def GetNumAllPlanets(self):
		return len(self.GetAllPlanets())

	def AddMoon(self,pChild):
		self.AddChild(pChild)
	
	def GetMoon(self):
		return self.GetParent(MOON)
	
	def GetMoons(self):
		return self.GetChildren(MOON)

	def GetNumMoons(self):
		return len(self.GetMoons())

	def AddFleet(self,pChild):
		self.AddChild(pChild)
	
	def GetFleet(self):
		return self.GetParent(FLEET)
	
	def GetFleets(self):
		return self.GetChildren(FLEET)

	def GetAllFleets(self):
		return self.GetAllChildren(FLEET)

	def GetNumFleets(self):
		return len(self.GetFleets())

	def GetNumAllFleets(self):
		return len(self.GetAllChildren(FLEET))

	def AddShip(self,pChild):
		self.AddChild(pChild)
	
	def GetShip(self):
		return self.GetParent(SHIP)
	
	def GetShips(self):
		return self.GetChildren(SHIP)

	def GetAllShips(self):
		return self.GetAllChildren(SHIP)

	def GetNumAllShips(self):
		return len(self.GetAllChildren(SHIP))

	def GetNumShips(self):
		return len(self.GetShips())

	def AddDock(self,pChild):
		self.AddChild(pChild)
	
	def GetDock(self):
		return self.GetParent(DOCK)
	
	def GetDocks(self):
		return self.GetChildren(DOCK)

	def GetNumDocks(self):
		return len(self.GetDocks())

	def AddStarbase(self,pChild):
		self.AddChild(pChild)
	
	def GetStarbase(self):
		return self.GetParent(STARBASE)
	
	def GetStarbases(self):
		return self.GetChildren(STARBASE)

	def GetAllStarbases(self):
		return self.GetAllChildren(STARBASE)

	def GetShipyard(self):
		return self.GetParent(SHIPYARD)
	
	def GetShipyards(self):
		return self.GetChildren(SHIPYARD)

	def GetAllShipyards(self):
		return self.GetAllChildren(SHIPYARD)

	def GetAllComets(self):
		return self.GetAllChildren(COMET)

	def GetNebula(self):
		return self.GetParent(NEBULA)
		
	def GetNebulas(self):
		return self.GetChildren(NEBULA)

	def GetWormhole(self):
		return self.GetParent(WORMHOLE)
		
	def GetWormholes(self):
		return self.GetChildren(WORMHOLE)

	def GetAllWormholes(self):
		return self.GetAllChildren(WORMHOLE)

	def GetSolarWormhole(self):
		return self.GetParent(SUBWORMHOLE)

	def GetAllBlackholes(self):
		return self.GetAllChildren(BLACKHOLE)

	def GetBlackholes(self):
		return self.GetChildren(BLACKHOLE)
		
	def GetSolarWormholes(self):
		return self.GetChildren(SUBWORMHOLE)		
	
	def GetAllSolarWormholes(self):
		return self.GetAllChildren(SUBWORMHOLE)
	
	def GetNumStarbases(self):
		return len(self.GetStarbases())

	def GetNumAllStarbases(self):
		return len(self.GetAllStarbases())

	def GetCharacters(self):
		return self.GetChildren(CHARACTER)
	
	def GetHolders(self):
		return self.GetChildren(HOLDER)

	def GetAllHolders(self):
		return self.GetAllChildren(HOLDER)

	def GetChildByName(self,s):
		for Child in self.GetChildren():
			if Child.sName == s:
				return Child
		for Child in self.GetChildren():
			res = Child.GetChildByName(s)
			if res:
				return res
		return None

	def GetChildrenByName(self,s):
		ret = []
		for Child in self.GetChildren():
			if Child.sName == s:
				ret.append(Child)
		for Child in self.GetChildren():
			res = Child.GetChildByName(s)
			if res:
				ret.append(res)
		return ret

	def GetDirectChildByName(self,s):
		for Child in self.GetChildren():
			if Child.sName == s:
				return Child		
		return None

	def GetDirectChildrenByName(self,s):
		ret = []
		for Child in self.GetChildren():
			if Child.sName == s:
				ret.append(Child)		
		return ret	

	def GetHolder(self):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('GetHolder(self)')

		## First we try to find a shiplike parent, if not we move up in the logical tree
		ret = self.GetParent(SHIP)
		if not ret:
			ret = self.GetParent(MOON)
			if not ret:
				ret = self.GetParent(PLANET)
				if not ret:
					ret = self.GetParent(SUN)
					if not ret:
						ret = self.GetParent(SOLAR)
						if not ret:
							ret = self.GetParent(UNIVERSE)
							if not ret:
								ret = None
		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		return ret		

	def Move(self,newHolder):
		oldHolder = self.GetHolder()
		if oldHolder:
			oldHolder.RemoveChild(self)
		if newHolder:
			newHolder.AddChild(self)

	def SetHolder(self,newHolder):
		self.Move(newHolder)	

	def GetFather(self):
		## Profiling
		idProfiling = App.TGProfilingInfo_StartTiming('GetFather(self)')

		## First we try to find a fleet like parent, if not we move up in the logical tree
		ret = self.GetParent(FLEET)
		if not ret:
			ret = self.GetParent(RACE)
			if not ret:
				ret = None

		## Stop local profiling
		App.TGProfilingInfo_StopTiming(idProfiling)

		return ret

	def Migrate(self,newParent):
		oldParent = self.GetFather()
		if oldParent:
			oldParent.RemoveChild(self)
		if newParent:
			newParent.AddChild(self)
	
	def SetFather(self,f):
		self.Migrate(f)

	## Geometrical functions
	#########################################
	def GetRadius(self,type=TREE_ELEMENT):
		#debug('Finding radius for '+self.sName)
		ret=[self.GetOwnRadius()]
		for pChild in self.GetChildren(type):
			d = pChild.GetRelativePosition(self).Length() + pChild.GetRadius() * math.sqrt(2)
			#debug('Radius = '+str(d)+ ' for '+pChild.sName)
			ret.append(d)
		ret.sort()
		#debug('Found radius for '+self.sName+' : '+str(ret[-1]))
		return ret[-1]

	def GetOwnRadius(self):
		if self.Node:
			return self.Node.GetRadius()
		return 0.0

	def SetPositionXYZ(self,x,y,z):
		V=App.TGPoint3()
		V.SetXYZ(x,y,z)
		self.SetPosition(V)

	def GetPosition(self):
		if not self.IsTypeOf(SOLAR) and self.Node:
			return self.Node.GetWorldLocation()
		return copyVector(self.vPosition)
	
	def SetPosition(self,V):
		D = copyVector(V)
		D.Subtract(self.vPosition)
		self.vPosition = copyVector(V)
		if self.Node:
			self.Node.SetTranslate(V)
			self.Node.UpdateNodeOnly()

		for Child in self.GetChildren():
			U = Child.GetPosition()
			U.Add(D)
			Child.SetPosition(U)

		## #debugging
		# #debug('setting position of '+self.sName+' to '+printVector(self.vPosition))

	def GetRelativePosition(self,Parent):
		P = self.GetPosition()
		P.Subtract(Parent.GetPosition())
		return P

	def SetRelativePosition(self,V,Parent):
		U = Parent.GetPosition()
		U.Add(V)
		self.SetPosition(U)
	
	def SetRelativePositionXYZ(self,x,y,z,Parent):
		V=App.TGPoint3()
		V.SetXYZ(x,y,z)
		self.SetRelativePosition(V,Parent)	

	## Rendering functions
	##########################
	def Render(self,pSet=None):
		debug('Rendering '+self.sName)
		
		## Force everything to position zero
		self.SetPositionXYZ(0.0,0.0,0.0)

		## Render all children
		for Child in self.GetChildren():
			Child.Render(pSet)

		debug('end Rendering '+self.sName)

		
	def Unrender(self):
		#debug('unrendering '+self.sName)

		## Remove all clocks and handlers
		if self.IsRendered():
			self.PurgeClocks()
			self.PurgeHandlers()
		
		## Render all children
		for Child in self.GetChildren():
			Child.Unrender()

		if self.Node:
			##Delete the node
			if self.Node.IsTypeOf(App.CT_BASE_OBJECT):
				pSet = self.Node.GetContainingSet()
				if pSet:
					pSet.RemoveObjectFromSet(self.Node.GetName())
					self.Node.SetDeleteMe(TRUE)
		
			#debug('Done unrendering '+self.sName)

		self.PurgeNodeCache(self.Node)
		self.Node = None

	
	def Randomise(self,type=UNIVERSE_ELEMENT,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		#debug('Randomising '+self.sName + ' for type '+type)
		
		fMinAngle, fMaxAngle = toRad(fMinAngle), toRad(fMaxAngle)
		P=radix*self.GetOwnRadius()*1.25
		r=App.TGPoint3()
		M=App.TGMatrix3()		
		
		lParts=self.GetChildren(type)
		for pObj in lParts:
			pObj.Randomise()
			#debug('Moving '+pObj.sName)

			R=pObj.GetRadius()
			r.SetXYZ(0.0,self.GetRandom(P+1.0*R,P+1.5*R),self.GetRandom(-R,R))
			P=P+2.0*radix*R

			M.MakeIdentity()		
			M.MakeZRotation(self.GetRandom(fMinAngle,fMaxAngle)*self.GetRandomSign())
			r.MultMatrixLeft(M)
						
			pObj.SetRelativePosition(r,self)

		#debug('\tEND Randomising '+self.sName + ' for type '+type)

	def IsRendered(self):
		if self.Node:
			return TRUE
		return FALSE

	def RandomiseFromList(self,oList,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		fMinAngle, fMaxAngle = toRad(fMinAngle), toRad(fMaxAngle)
		P=radix*self.GetRadius()
		r=App.TGPoint3()
		M=App.TGMatrix3()		
		
		for pObj in oList:
			pObj.Randomise()
			#debug('Moving '+pObj.sName)

			R=pObj.GetRadius()
			r.SetXYZ(0.0,self.GetRandom(P+1.0*R,P+1.5*R),self.GetRandom(-R,R))
			P=P+2.0*radix*R
			
			M.MakeIdentity()		
			M.MakeZRotation(self.GetRandom(fMinAngle,fMaxAngle)*self.GetRandomSign())
			r.MultMatrixLeft(M)
						
			pObj.SetRelativePosition(r,self)

	def Enhance(self):
		## Children
		for Child in self.GetChildren():
			Child.Enhance()

	def AssignAI(self,kArgs=None,force=FALSE):
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]

		#debug('Assigning AI for '+self.sName)

		## Assign for all children
		for Child in self.GetChildren():
			Child.AssignAI(kArgs[:],force)	
		
	def RenderAndRandomise(self,pSet=None):
		self.Render(pSet)
		self.Randomise()
		self.Enhance()
		self.AssignAI()					

	def EnterNodeCache(self,Node=None):
		if not Node:
			Node = self.Node		
		if Node:
			UniverseElement.NodeCache[Node.GetObjID()] = self 

	def PurgeNodeCache(self,Node = None):
		if not Node:
			UniverseElement.NodeCache = {}
		else:
			## Delete the cache entry
			ID = Node.GetObjID()
			if UniverseElement.NodeCache.has_key(ID):
				del UniverseElement.NodeCache[ID]	

	def FindSuitablePosition(self,r,d=0.0):
		## Vector
		R=App.TGPoint3()
		R.SetXYZ(0.0,0.0,0.0)

		## Solar
		pSolar = self.GetSolar()
		if not pSolar:
			return R
		pSet = pSolar.Node

		## Our spot
		V = self.GetPosition()
		M = App.TGMatrix3()
		rr = self.GetOwnRadius()
		if d==0.0:
			d  = max(100.0*km,rr)
		
		while(TRUE):
			R.SetXYZ(0.0,self.GetRandom(d,d*1.5),self.GetRandom(-rr,rr))
			M.MakeIdentity()
			M.MakeZRotation(toRad(self.GetRandom(0.0,360.0)))
			R.MultMatrixLeft(M)
			R.Add(V)								
			if pSet.IsLocationEmptyTG (R,r):
				return R
			d = 1.5 * d


class Holder(UniverseElement):

	## Class related functions
	##############################
	def __init__(self,ID = None):
		## Parent class constructor
		UniverseElement.__init__(self,ID)

		## Own data members
		self.fExitDelay = 0.0
		self.fEnterDelay = 0.0

	## Save function
	###########################
	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file('self = Holder('+str(self.ID)+')')

		## Upperclass
		UniverseElement.save(self,FALSE)

		## Our lines
		write_save_file('self.fExitDelay   	='+str(self.fExitDelay))
		write_save_file('self.fEnterDelay   	='+str(self.fEnterDelay))

	## Dynamical Holder Methods
	################################
	def CanEnterFleet(self,pFleet):
		## default TRUE	
		return TRUE

	def CanExitFleet(self,pFleet):
		## default TRUE
		return TRUE

	### Enterfleet
	################################
	def EnterFleet(self,pFleet):
		## Necesarry states
		#assert pFleet
		#assert pFleet.VoyageState	== VOYAGING	## no warp without voyage
		#assert pFleet.State 		== NORMAL	## valid state
		#assert pFleet.GetHolder().ID	== self.ID 	## same HOLDER required

		## Can we enter it?
		if not self.CanEnterFleet(pFleet):
			return NAK

		## #debug
		#debug('fleet '+pFleet.sName+' is entering me, '+self.sName)

		## Change the state
		pFleet.SetState(ENTERING)

		if not self.IsRendered():
			## Conceptual entry
			self.ConceptualEnterFleet(pFleet)
		else:
			## The fleet must be rendered at this point
			#assert pFleet.IsRendered()

			## Physical entry
			self.RenderedEnterFleet(pFleet)					
		
		## Succes
		return ACK

	def ConceptualEnterFleet(self,pFleet):
		## Conceptually enter the ships
		for pShip in pFleet.GetShips():
			#assert pShip.State == NORMAL	## valid state
			pShip.SetState(ENTERING)
			if self.fEnterDelay:
				self.AddDelay('DelayedEnterDone',self.fEnterDelay,pShip,self)
			else:
				self.EnterDone(pShip)

	def DelayedEnterDone(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip =  pEvent.GetSource()
		if not pShip:
			return

		## Handler
		self.EnterDone(pShip)

	def RenderedEnterFleet(self,pFleet):
		## Immediate in default mode
		for pShip in pFleet.GetShips():
			#assert pShip.State == NORMAL	## valid state
			pShip.SetState(ENTERING)
			self.EnterDone(pShip)

	def RUR_EnterFleet(self,pFleet):
		#assert pFleet.GetHolder().ID == self.ID ## correct location
		#assert pFleet.State == ENTERING	## exit must be in progress
		#assert not pFleet.IsRendered()		## must be already unrendered

		## Remove the clocks and call exitdone
		for pShip in pFleet.GetShips():
			if pShip.State == ENTERING:
				self.AddDelay('DelayedEnterDone',0.5,pShip,self)

	def URR_EnterFleet(self,pFleet):
		#assert pFleet.GetHolder().ID == self.ID 		## correct location
		#assert pFleet.State == ENTERING 	## enter must be in progress

		#debug('quick entering fleet '+pFleet.sName)

		## The fleet wants to quick wrap things up
		## Remove the clocks and call exitdone
		for pShip in pFleet.GetShips():
			if pShip.State == ENTERING:
				self.RemoveClock('DelayedEnterDone',None,pShip,self)
				self.AddDelay('DelayedEnterDone',0.05,pShip,self)

	def EnterDone(self,pShip):
		## #assertions
		#assert pShip
		#assert pShip.State == ENTERING	## valid state

		## Change the state
		pShip.SetState(INSIDE)

		debug('ship '+pShip.sName+' has entered me, '+self.sName)

		## All ships entered?
		for pOther in pShip.GetFleet().GetShips():
			if pOther.State != INSIDE:
				return

		debug('fleet '+pShip.GetFleet().sName+' has completely entered me, '+self.sName)

		## All ships entered
		pShip.GetFleet().SetState(INSIDE)

	
	### Exitfleet
	################################
	def ExitFleet(self,pFleet):
		## Necesarry states
		#assert pFleet
		#assert pFleet.VoyageState == VOYAGING		## no warp without voyage
		#assert pFleet.State == INSIDE			## valid state
		#assert pFleet.GetHolder().ID == self.ID 		## same HOLDER required
		
		## Can we enter it?
		if not self.CanExitFleet(pFleet):
			return NAK

		## #debug
		debug('fleet '+pFleet.sName+' is exiting me, '+self.sName)

		## Change the state
		pFleet.SetState(EXITING)

		if not self.IsRendered():
			## Conceptual entry
			self.ConceptualExitFleet(pFleet)
		else:
			## The fleet must be rendered at this point
			#assert pFleet.IsRendered()

			## Physical entry
			self.RenderedExitFleet(pFleet)					
		
		## Succes
		return ACK

	def ConceptualExitFleet(self,pFleet):
		## Conceptually enter the ships
		for pShip in pFleet.GetShips():
			#assert pShip.State == INSIDE	## valid state
			pShip.SetState(EXITING)
			if self.fExitDelay:
				self.AddDelay('DelayedExitDone',self.fExitDelay,pShip,self)
			else:
				self.ExitDone(pShip)

	def DelayedExitDone(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip =  pEvent.GetSource()
		if not pShip:
			return

		## Handler
		self.ExitDone(pShip)

	def URR_ExitFleet(self,pFleet):
		#assert pFleet.GetHolder().ID == self.ID ## correct location
		#assert pFleet.State == EXITING	## exit must be in progress
		#assert pFleet.IsRendered()	## must be already rendered

		## The fleet wants to quick wrap things up
		## Remove the clocks and call exitdone
		for pShip in pFleet.GetShips():
			if pShip.State == EXITING:
				self.RemoveClock('DelayedExitDone',None,pShip,self)
				self.AddDelay('DelayedExitDone',0.05,pShip,self)

	def RUR_ExitFleet(self,pFleet):
		#assert pFleet.GetHolder().ID == self.ID ## correct location
		#assert pFleet.State == EXITING	## exit must be in progress
		#assert not pFleet.IsRendered()	## must be already unrendered

		## Remove the clocks and call exitdone
		for pShip in pFleet.GetShips():
			if pShip.State == EXITING:
				self.AddDelay('DelayedExitDone',0.5,pShip,self)
		

	def RenderedExitFleet(self,pFleet):
		## Immediate in default mode
		for pShip in pFleet.GetShips():
			#assert pShip.State == INSIDE	## valid state
			pShip.SetState(EXITING)
			self.ExitDone(pShip)

	def ExitDone(self,pShip):
		## #assertions
		#assert pShip
		#assert pShip.State == EXITING	## valid state

		## Change the state
		pShip.SetState(NORMAL)

		debug('ship '+pShip.sName+' has exited me, '+self.sName)

		## All ships entered?
		for pOther in pShip.GetFleet().GetShips():
			if pOther.State != NORMAL:
				return

		debug('fleet '+pShip.GetFleet().sName+' has completely exited me, '+self.sName)

		## All ships entered
		pShip.GetFleet().SetState(NORMAL)


	## Destruction functions
	###############################
	def SelfDestroyed(self,gEvent):
		## Die
		self.Kill()

	def Kill(self):
		## We were killed, if we have children, do something about them
		for pObj in self.GetHolders():
			pObj.HolderDestroyed()

		for pFleet in self.GetFleets():
			pFleet.HolderDestroyed()

		## Destroy our node and explosion gfx
		if self.Node:
			self.VisualKill()
		self.Node = None	

		## Notify the solar
		self.GetSolar().ObjectDestruction(self)		
		
		## Delete ourself
		self.delete()

	def VisualKill(self):
		print 'Booooooooom '+self.sName

	def HolderDestroyed(self):
		## Sun(+) -> Planet
		self.Kill()
	
	def FleetDestroyed(self,pFleet):
		#debug('fleet '+pFleet.sName+' was destroyed in me, '+self.sName)

		## Check
		#assert self.HasChild(pFleet)

		## Detach it
		pFleet.Move(None)

		## Notify the solar
		self.GetSolar().ObjectDestruction(pFleet)		

	def ShipDestroyed(self,pShip,pFleet):
		#debug('ship '+pShip.sName+' was destroyed in me, '+self.sName)
		
		## Our destroyed ship
		SID = pShip.ID 
	
		## Notify the solar
		self.GetSolar().ObjectDestruction(pShip)

		if pShip.State == NORMAL:
			pass

		elif pShip.State == INTERCEPTING:
			pass

		elif pShip.State == WARPING:
			pass

		elif pShip.State == ENTERING:
			if not self.IsRendered():
				## Remove the delay
				self.RemoveClock('DelayedEnterDone',None,pShip,self)

			## Update the state
			## All ships entered?
			for pOther in pFleet.GetShips():
				if pOther.ID == SID:
					continue
				if pOther.State != INSIDE:
					return
			if len(pFleet.GetShips()) <= 1:
				return

			## All ships entered
			pFleet.SetState(INSIDE)
				
		elif pShip.State == INSIDE:
			pass

		elif pShip.State == REPAIR:
			if hasattr(self,'dRepair'):
				if self.dRepair.has_key(pShip.ID):
					## Remove it from the list
					del self.dRepair[pShip.ID]

					## Update the state
					## All ships entered?
					for pOther in pFleet.GetShips():
						if pOther.ID == SID:
							continue
						if pOther.State != INSIDE:
							return
					if len(pFleet.GetShips()) <= 1:
						return

					## All ships exited
					pFleet.SetState(INSIDE)

					## Ships left?
					if not self.dRepair:
						## Remove the clock
						self.RemoveClock('RepairCycle')

						## Remove the dict
						del self.dRepair
					

		elif pShip.State == EXITING:
			if not self.IsRendered():
				## Remove the delay
				self.RemoveClock('DelayedExitDone',None,pShip,self)

			## Update the state
			## All ships entered?
			for pOther in pFleet.GetShips():
				if pOther.ID == SID:
					continue
				if pOther.State != NORMAL:
					return
			if len(pFleet.GetShips())<=1:
				return

			## All ships exited
			pFleet.SetState(INSIDE)

		elif pShip.State == BUILDING:
			pass

		else:
			raise RuntimeError

		


	## Push and pull functions
	########################################
	def ExitPull(self):
		## We need to provide a ship, None for now
		return None

	def EnterPush(self,pShip):
		## a ship was pushed out of a module

		if pShip.State == ENTERING:
			## A ship entered
			self.EnterDone(pShip)
		elif pShip.State == EXITING:
			## A ship exited
			self.ExitDone(pShip)

		## We accept
		return ACK

	## Dynamic music
	###################################
	def SetEnterMusic(self,sMusic):
		self.sEnterMusic = sMusic

	def GetEnterMusic(self):
		if hasattr(self,'sEnterMusic'):
			return self.sEnterMusic
		else:
			## Ask our race
			return self.GetRace().GetEnterMusic()


	## Services
	###########################################
	def AbortService(self,pFleet):
		## Unswap the ships
		for pShip in pFleet.GetShips():
			pShip.UnswapForRepair(pShip)
	
		## Set state normal
		pFleet.SetState(INSIDE)

	## Repair
	###########################################
	CONCEPTUAL_REPAIR_TIME  = 50.0
	REPAIR_CYCLE		= 5.0


	def Repair(self,pFleet):		
		## Rendered
		if pFleet.IsRendered():
			## Set the state to repairing
			pFleet.SetState(REPAIR)

			## Repair the ships
			for pShip in pFleet.GetShips():
				self.SwapForRepair(pShip)

		## Unrendered
		else:
			## All repaired immediately
			for pShip in pFleet.GetShips():
				pShip.FullRepair()

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

		## Set the state
		pShip.SetState(REPAIR)		

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

		## Set the state
		pShip.SetState(INSIDE)

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

			## All ships of that fleet done
			pFleet = pShip.GetFleet()
			if self.IsRepairDone(pFleet):
				## Give a yell
				if pFleet.ID == PLAYER_FLEET_ID:
					GetPlayerBridge().GetEngineer().Speak('ge111') ## Repairs complete, sir				
				pFleet.SetState(INSIDE)

	def IsRepairDone(self,pFleet):
		## All ships done?
		for pShip in pFleet.GetShips():
			if pShip.State != INSIDE:
				return FALSE
		return TRUE			

	def RUR_Repair(self,pFleet):
		## Finish the repair
		for pShip in pFleet.GetShips():
			pShip.FullRepair()		

		## Set state done
		pFleet.SetState(INSIDE)		

	
def Redirect(pGame,pEvent):
	EventDict = ATP_EventHandlerObject.EventDict

	## Profiling
	idProfiling = App.TGProfilingInfo_StartTiming('Redirect(pGame,pEvent)')
	
	## Eventtype
	e = pEvent.GetEventType()
	
	## Find it in the register
	if EventDict.has_key(e):
		listeners = EventDict[e]
		## Iterate over all registered objects for this event
		for WID in listeners.keys():
			if listeners.has_key(WID):
				pObj = listeners[WID][1]
				listeners[WID][0].ProcessEvent(pEvent)

				## Delayed function removal
				pObj.RemoveDelay(e)

	## Stop local profiling
	App.TGProfilingInfo_StopTiming(idProfiling)

	

def Raise(e,pSource=None,pDestination=None):
	## Create and ATP_Event
	myEvent = ATP_Event(e,pSource,pDestination)

	## Create a game event
	gEvent = App.TGIntEvent_Create()
	gEvent.SetEventType(e)		
	gEvent.SetInt(myEvent.GetID())

	## Redirect the game event
	Redirect(App.Game_GetCurrentGame(),gEvent)

	## Delete the temporarely event
	myEvent.delete()

	return gEvent

def GetByID(ID):
	if not ID:
		return None
	if ATP_EventHandlerObject.Dict.has_key(ID):
		return ATP_EventHandlerObject.Dict[ID]
	return None

NumTot = 0
Hits = 0
def GetByNode(pObject):
	if not pObject:
		return None

	## Profiling
	idProfiling = App.TGProfilingInfo_StartTiming('GetByNode(pObject)')
	
	OID = pObject.GetObjID()		

	global NumTot
	global Hits
	NumTot = NumTot + 1

	## Consult the cache
	NodeCache = UniverseElement.NodeCache
	if NodeCache.has_key(OID):
		## A hit
		Hits = Hits + 1
		#debug('Cache Hit: Hitrate %2.2f %%' % ((Hits*100.0)/NumTot))
		return NodeCache[OID]
	
	## Find it in a hard way
	ret = None
	for ID in ATP_EventHandlerObject.Dict.keys():
		obj = ATP_EventHandlerObject.Dict[ID]
		if not obj.IsTypeOf(UNIVERSE_ELEMENT):
			continue
		if hasattr(obj,'Node'):
			if obj.Node:
				if obj.Node.GetObjID() == OID:
					ret = obj
					break
	#debug('Cache Miss: Hitrate %2.2f %%' % ((Hits*100.0)/NumTot))
	if ret:
		NodeCache[OID]=ret
	
	## Stop local profiling
	App.TGProfilingInfo_StopTiming(idProfiling)

	return ret


def GetByName(sName):
	## Profiling
	idProfiling = App.TGProfilingInfo_StartTiming('GetByName(sName)')	
	
	ret = None
	for ID in ATP_EventHandlerObject.Dict.keys():
		e = ATP_EventHandlerObject.Dict[ID]
		if e.sName == sName:
			ret = e

	## Stop local profiling
	App.TGProfilingInfo_StopTiming(idProfiling)

	return None
			 

class ATP_Event:
	Dict = {}
	
	def __init__(self,e,pSource = None,pDestination = None):
		## Find an unique ID
		ID=1		
		while (TRUE):
			if not ATP_Event.Dict.has_key(ID):
				break
			ID=ID+1
		self.ID=ID

		## Data
		self.Source 	 = pSource
		self.Destination = pDestination
		self.e = e

		ATP_Event.Dict[self.ID] = self

	def delete(self):
		del ATP_Event.Dict[self.ID]		

	def GetID(self):
		return self.ID

	def GetEventID(self):
		return self.e

	def GetSource(self):
		return self.Source
	
	def GetDestination(self):
		return self.Destination

def DecodeEvent(pEvent):
	EID = pEvent.GetInt()
	if ATP_Event.Dict.has_key(EID):
		return ATP_Event.Dict[EID]
	return None

def GetGame():
	return GetByID(UNIVERSE_GAME_ID)

def GetUniverse():
	return GetByID(UNIVERSE_ID)

def GetArchitect():
	return GetByID(ARCHITECT_ID)

def GetMatrix():
	return GetByID(MATRIX_ID)

def GetPlayerShip():
	return GetByID(PLAYER_SHIP_ID)

def GetPlayerFleet():
	return GetByID(PLAYER_FLEET_ID)

def GetPlayerBridge():
	return GetByID(PLAYER_BRIDGE_ID)

def GetStarCharts():
	return GetByID(STARCHARTS_ID)

def GetInterstellarInterface():
	return GetByID(INTERSTELLAR_INTERFACE_ID)

def GetSolarInterface():
	return GetByID(SOLAR_INTERFACE_ID)

def GetCameraManager():
	return GetByID(CAMERA_MANAGER_ID)

def GetAnimationManager():
	return GetByID(ANIMATION_MANAGER_ID)

def GetGalaxyMap():
	return GetByID(GALAXY_MAP_ID)


def GetPlayerRace():
	pFleet=GetPlayerFleet()
	if not pFleet:
		return None
	return pFleet.GetRace()

## We can manage the eventtypes ourself in case they got sparse
def SynchroniseWithGame():
	dEventTypes = ATP_EventHandlerObject.dEventTypes
	pGame = App.Game_GetCurrentGame()
	for i in range(5000):
		e = App.Game_GetNextEventType()
		if dEventTypes.has_key(e):
			raise RuntimerError , 'Game provides duplicate e: '+str(e)
		dEventTypes[e] = 0

		## Register the game event
		App.g_kEventManager.AddBroadcastPythonFuncHandler(e,App.Game_GetCurrentGame(),__name__+'.MaintainLock')
		#pGame.AddPythonMethodHandlerForInstance(e,__name__+'.MaintainLock')

	ATP_EventHandlerObject.lEventTypes = dEventTypes.keys()

def MaintainLock(self,gEvent):
	return 0

def GetNextEventType():
	#debug(str(len(ATP_EventHandlerObject.lEventTypes))+' events left')
	return ATP_EventHandlerObject.lEventTypes.pop()



			

