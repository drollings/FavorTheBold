# Foundation Triggers Extension 20030305 for Bridge Commander
# Written March 5, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import Foundation

if int(Foundation.version[0:8]) < 20030305:


	import FoundationTriggers
	import DummyApp
	App = DummyApp.DummyApp()
	# import App


	Foundation.NonSerializedObjects = Foundation.__dict__.keys()
	print 'Outdated Foundation, updating functions'


	class TriggerDef(Foundation.MutatorElementDef):
		def __init__(self, name, eventKey, dict = {}):
			self.eventKey = eventKey
			self.count = 0
			key = name + str(eventKey)
			FoundationTriggers.__dict__[name + str(eventKey)] = self
			Foundation.MutatorElementDef.__init__(self, name, dict)

		def AddToMutator(self, toMode):
			toMode.overrides.append(self)
			toMode.elements.append(self)

		def __call__(self, pObject, pEvent):
			# print pEvent.GetEventType(), pEvent.GetRefCount()
			pObject.CallNextHandler(pEvent)

		def ImmediateActivate(self):		pass
		def ImmediateDeactivate(self):		pass

		def Activate(self):
			if not self.count:
				pGame = App.Game_GetCurrentGame()
				App.g_kEventManager.AddBroadcastPythonFuncHandler(self.eventKey, pGame, 'FoundationTriggers.' + self.name + str(self.eventKey))
			self.count = self.count + 1

		def Deactivate(self, soft = 0):
			if self.count:
				self.count = self.count - 1
				if not self.count:
					print 'Shutting down listener for', self.name
					pGame = App.Game_GetCurrentGame()
					App.g_kEventManager.RemoveBroadcastHandler(self.eventKey, pGame, 'FoundationTriggers.' + self.name + str(self.eventKey))



	Foundation.TriggerDef = TriggerDef

	Foundation.TriggerDef.ET_FND_CREATE_SHIP = App.UtopiaModule_GetNextEventType()
	Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP = App.UtopiaModule_GetNextEventType()

	Foundation.version = '20030221p'



