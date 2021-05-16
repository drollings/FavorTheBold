import App

FALSE=0
TRUE=1

#from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
#from Custom.AdvancedTechnologies.Data.ATP_Config import *

class ATP_Handler:
	EventDict = {}
	Dict = {}
	
	## Class related functions
	def __init__(self):
		## Find an unique ID
		ID=0		
		while (TRUE):
			if not ATP_Handler.Dict.has_key(ID):
				break
			ID=ID+1
		self.ID=ID

		## Create an entry in the Dict
		ATP_Handler.Dict[self.ID] = self

		## Game communication
		self.Wrapper 	= App.TGPythonInstanceWrapper()
		self.Wrapper.SetPyWrapper(self)
		self.timers={}
		self.handlers=[]

	def delete(self):
		## Remove wrapper related things
		for key in self.timers.keys():
			self.RemoveClock(key)
		for eventType,sFunctionHandler in self.handlers[:]:
			self.RemoveHandler(eventType,sFunctionHandler)
		
		## All attirbutes to null
		del self.timers
		del self.handlers
		del self.Wrapper

	## Game communication part		
	def AddHandler(self,eventType,sFunctionHandler):
		## Dict
		EventDict = ATP_Handler.EventDict

		## Wrapper event
		self.Wrapper.RemoveHandlerForInstance         (eventType,sFunctionHandler)
		self.Wrapper.AddPythonMethodHandlerForInstance(eventType,sFunctionHandler)
		
		## Game Event
		App.g_kEventManager.RemoveBroadcastHandler       	(eventType,App.Game_GetCurrentGame(),__name__+".Redirect")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,App.Game_GetCurrentGame(),__name__+".Redirect")

		## If it is already here don't add it
		if self.handlers.count((eventType,sFunctionHandler))==0:
			self.handlers.append((eventType,sFunctionHandler))

		## Indirect call mechanism
		if not EventDict.has_key(eventType):
			EventDict[eventType] = []
		if EventDict[eventType].count(self.Wrapper)==0:
			EventDict[eventType].append(self.Wrapper)
			
	def RemoveHandler(self,e,sFunctionHandler):
		## Dict
		EventDict = ATP_Handler.EventDict
		
		## Remove instances
		self.Wrapper.RemoveHandlerForInstance(e,sFunctionHandler)				
		if self.handlers.count((e,sFunctionHandler)):
			self.handlers.remove((e,sFunctionHandler))

		## Update indirect call mechanism
		if EventDict.has_key(e):
			for Wrapper in EventDict[e][:]:
				if Wrapper.GetObjID() == self.Wrapper.GetObjID():
					EventDict[e].remove(Wrapper)
			if len(EventDict[e])==0:
				App.g_kEventManager.RemoveBroadcastHandler(e,App.Game_GetCurrentGame(),__name__+".Redirect")
				del EventDict[e]

	def AddClock(self,sFunctionHandler,fGranulation=1.0):
		## Make sure there is only one entry
		self.RemoveClock(sFunctionHandler)

		## Create and event, and add it to the game
		e=App.Game_GetNextEventType()		
		pEvent = App.TGIntEvent_Create()
		pEvent.SetInt(self.ID)
		pEvent.SetEventType(e)
		pEvent.SetDestination(self.Wrapper)
		
		timer=App.TGTimer_Create()
		timer.SetEvent(pEvent)
		timer.SetTimerStart(App.g_kUtopiaModule.GetGameTime()+fGranulation)
		timer.SetDelay(fGranulation)
		timer.SetDuration(-1.0)
		
		self.timers[sFunctionHandler]=timer.GetObjID(),e
		App.g_kTimerManager.AddTimer(timer)

		self.Wrapper.AddPythonMethodHandlerForInstance(e,sFunctionHandler)
		if self.handlers.count((e,sFunctionHandler))==0:
			self.handlers.append((e,sFunctionHandler))		

	def RemoveClock(self,sFunctionHandler):
		if not self.timers.has_key(sFunctionHandler):
			return

		ID = self.timers[sFunctionHandler][0]
		e  = self.timers[sFunctionHandler][1]
		
		self.Wrapper.RemoveHandlerForInstance(e,sFunctionHandler)
		self.handlers.remove((e,sFunctionHandler))

		App.g_kTimerManager.DeleteTimer(ID)
		del self.timers[sFunctionHandler]					

	def Raise(self,e):
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(e)
		App.Game_GetCurrentGame().ProcessEvent(pEvent)		
	
	def GetWrapper(self):
		return self.Wrapper	
	
def Redirect(pGame,pEvent):
	## Needed to fix a not called bug
	EventDict = ATP_Handler.EventDict	
	e = pEvent.GetEventType()
	if EventDict.has_key(e):
		for Wrapper in EventDict[e]:
			Wrapper.ProcessEvent(pEvent)

def GetByID(ID):
	if ATP_Handler.Dict.has_key(ID):
		return ATP_Handler.Dict[ID]
	return None