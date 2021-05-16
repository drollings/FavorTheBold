##########################################################
# Foundation Technologies
##########################################################
# Date:  March 19, 2004
# Author:  Daniel Rollings AKA Dasher42
##########################################################
# This is a project to create an integrated framework for the
# scripting of ships, technologies, special abilities, conditions;
# to refine the concept of Apollo's Advanced Technologies,
# particularly the QuickBattle addon; and most importantly, to
# do it in the modular, extensible idiom of the Foundation.
##########################################################


##########################################################
# Imports and global data structures
##########################################################

import App
# import DummyApp
# App = DummyApp.DummyApp()

import Foundation
import FoundationTriggers
import MissionLib
import Registry
import string

##########################################################
# Global variables
##########################################################

mode = Foundation.MutatorDef.FTB
# mode = Foundation.MutatorDef('Foundation Technologies')
dMode = { 'modes': [ mode ] }


dShips = {}			# Dictionary of ShipInstances, Python objects paired with App.ShipClass objects
dYields = {}		# Dictionary of weapon yields, placed here by projectile .py's for lookup
dOnFires = {}		# Dictionary of on-fire effects, placed here by projectile .py's for lookup


dDisplays = {}		# Kludgy, this, but this is a list of displays yet to be attached to a ShipInstance.
					# "Player" has a SetShipID() call before Foundation Tech's listeners start,
					# so this is necessary.


##########################################################
# A placeholder for the main event loop.
##########################################################
ET_FND_TECH_EVENT = App.Mission_GetNextEventType()


# With thanks to MLeoDaalder - Dasher42
class CloakTriggerDef(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent):
		App.CloakingSubsystem_SetCloakTime(3.5)
		pObject.CallNextHandler(pEvent)

CloakTriggerDef('Cloak Timing', App.ET_CLOAK_BEGINNING)
CloakTriggerDef('Decloak Timing', App.ET_DECLOAK_BEGINNING)

# App.UtopiaModule_SetGameUnitConversionFactor(0.17999997)



##########################################################
# Reference points for optional external API's.
# FTB will add effects of its own, so while NanoFX is
# nice, there are some cases where we need to make sure
# our own effects are installed too.
#
# Regardless, Nano has made the definitive Effects library
# and we should stay API-compatible with it and build on it.
##########################################################
EffectsLib = None
try:
	EffectsLib = __import__('Custom.NanoFXv2Lite.NanoFX_Lib')
except:
	pass

BridgeFX = None
try:
	BridgeFX = __import__('Custom.AdvancedTechnologies.Data.BridgeFX.ATP_BridgeFX')
except:
	pass


##########################################################
# Base classes
##########################################################


##########################################################
# An Propertied object is a type of object that carries a minimum
# of local variables, deferring to its prototype calls for most
# data members.  It is also meant to be able to apply its pro
# classes should use a copy-on-write scheme for updating member
# objects.
# TODO:  code
##########################################################
class Propertied:
	def __init__(self, proto):
		self.SetProto(proto)
		self._dProperties = {}

	def SetProto(self, proto):
		self.pProto = proto

	def __getitem__(self, i):
		try:
			return self._dProperties[i]
		except KeyError:
			if self.pProto._dProperties.has_key(i):
				return self.pProto._dProperties[i]


##########################################################
# Akin to a Mutator, this holds list of Technology Elements that
# have different effects.  It inherits OverrideDef's ability to
# participate in the organized creation and destruction of game
# modes associated with mutators.  As a subclass of Registry, it
# is a master broker of active technologies in the game.
##########################################################
class TechnologyListDef(Foundation.OverrideDef, Registry.Registry):
	def __init__(self, name, dict = dMode):
		Registry.Registry.__init__(self)

		# We don't need the overhead of an override, just its placement in a Mutator
		# with routines to activate and deactivate.  So, bypass the override __init__.
		Foundation.MutatorElementDef.__init__(self, name, dict)


	##########################################################
	# MutatorElement methods which establish this class's role as a
	# singleton holding the active technologies.
	def Activate(self):
		Foundation.oTechs = self
		# print 'Activating tech list', self, Foundation.oTechs

	def Deactivate(self):
		global dShips, dYields, dOnFires, dDisplays, oEventQueue
		dShips = {}
		dYields = {}
		dOnFires = {}
		dDisplays = {}
		oEventQueue.CancelQueued()
		self._keyList = {}

		Foundation.oTechs = None

	##########################################################
	# This looks up a technology that has a given method, i.e.
	# an OnFire or OnYield method.
	def Get(self, sName, sProperty):
		# # print 'Checking tech for', sName, ',', sProperty, self._keyList.keys()
		try:
			oTech = self._keyList[sName]
			if oTech.__class__.__dict__.has_key(sProperty):
				return oTech
		except:
			return None


##########################################################
# This might be vestigial, and need to be retired.
##########################################################
oTechs = TechnologyListDef('Foundation Tech List')


##########################################################
# The cat's out of the bag on this one already, as TriggerDefs
# have found their way into NanoFX.  They are an event listener
# encapsulated into a contained MutatorElement object, able to
# be created and shut down easily.
##########################################################
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

	def Deactivate(self, force = 0):	# Here is where we have a fix for the previous implementation
		if self.count:
			self.count = self.count - 1
			if force or not self.count:
				print 'Shutting down listener for', self.name
				pGame = App.Game_GetCurrentGame()
				App.g_kEventManager.RemoveBroadcastHandler(self.eventKey, pGame, 'FoundationTriggers.' + self.name + str(self.eventKey))



Foundation.TriggerDef = TriggerDef

Foundation.TriggerDef.ET_FND_CREATE_SHIP = App.UtopiaModule_GetNextEventType()
Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP = App.UtopiaModule_GetNextEventType()



##########################################################
# This is a TriggerDef meant to only be active when needed.
# It is currently BROKEN, but when it is fixed, TimerDef and
# EventQueue will subclass from it instead of TriggerDef.
##########################################################
class DemandTriggerDef(TriggerDef):

	##########################################################
	# The Start and Stop methods reimplement what was the domain of
	# TriggerDef's Activate and Deactivate, making a distinction
	# between what is available and what is automatically active.
	def Start(self):
		TriggerDef.Activate(self)

	def Stop(self, force = 0):
		TriggerDef.Deactivate(self, force)


	##########################################################
	# MutatorElement functions.  These are overridden to prevent
	# automatic activation.
	def Activate(self):
		pass

	def Deactivate(self, soft = 0):
		self.Stop(1)



##########################################################
# Here, we get into timers, which by their nature ought to be
# active only when needed, and be as efficient as possible in
# their implementation.
##########################################################
class TimerDef(DemandTriggerDef):
	def __init__(self, name, eventKey, tInterval, tDuration, dict = {}):
		self.eventKey = eventKey
		self.count = 0
		self.idTimer = None
		self.tInterval = tInterval
		self.tDuration = tDuration
		key = name + str(eventKey)
		FoundationTriggers.__dict__[name + str(eventKey)] = self
		Foundation.MutatorElementDef.__init__(self, name, dict)

	def __call__(self, pObject, pEvent):
		pass

	def Start(self):
		print 'Start:  self.__dict__', self.__dict__

		if self.count == 0:
			print 'Making a timer', self.__dict__

			sFunc = 'FoundationTriggers.' + self.name + str(self.eventKey)
			pTimer = MissionLib.CreateTimer(self.eventKey, sFunc, App.g_kUtopiaModule.GetGameTime(), self.tInterval, self.tDuration)
			self.idTimer = pTimer.GetObjID()

		print 'Start:  self.__dict__', self.__dict__

		self.count = self.count + 1

	def Stop(self, force = 0):
		if self.count:
			self.count = self.count - 1
			if (force or self.count == 0) and self.idTimer:
				# print 'Shutting down listener for', self.name
				App.g_kTimerManager.DeleteTimer(self.idTimer)
				self.idTimer = None
				self.count = 0
			DemandTriggerDef.Stop(self, force)

	def Activate(self):
		pass

	def Deactivate(self):
		self.Stop(1)


class EventQueueDef(TimerDef):
	def __init__(self, name, eventKey, tInterval, tDuration, dict = {}):
		TimerDef.__init__(self, name, eventKey, tInterval, tDuration, dict = {})
		self.dEvents = {}
		self.empty = 0

	def __call__(self, pObject, pEvent):
		now = int(App.g_kUtopiaModule.GetGameTime())

		print now, self.__dict__
		if self.dEvents.has_key(now):
			for i in self.dEvents[now]:
				if i._when != now:	# This generally supports delays
					continue
				next = i(now)
				if next:
					i._when = next
					self.Queue(i)
				else:
					i.Cancel(1)

			self.empty = 0
			del self.dEvents[now]

		elif len(self.dEvents.keys()) == 0:
			self.empty = self.empty + 1

		if self.empty == 5:		# We've been empty for five pulses, let's stop now.
			self.empty = 0
			self.Stop()

	def Queue(self, oEvent):
		oEvent._queue = self
		when = int(App.g_kUtopiaModule.GetGameTime() + oEvent._when)
		oEvent._when = when
		print 'Queuing', oEvent, when

		try:
			self.dEvents[when].append(oEvent)
		except KeyError:
			self.dEvents[when] = [ oEvent ]

		if not self.idTimer:
			self.Start()

	def CancelQueued(self, oEvent = None):
		if oEvent:
			self.dEvents[oEvent._when].remove(oEvent)
		else:
			self.dEvents = {}
			self.Stop(1)


oEventQueue = EventQueueDef('FTB Event Loop', ET_FND_TECH_EVENT, 1.0, -1.0)


class FTBEvent:
	def __init__(self, source, when):
		self._source = source
		self._when = when
		source._lEvents.append(self)

	def __call__(self, now):
		pass

	def Cancel(self, bFromqueue = 0):
		if not bFromqueue:
			self._queue.CancelQueued(self)
		self._when = 0
		# # print 'Cancelling', self, self._source._lEvents
		if self._source:
			self._source._lEvents.remove(self)

class DisableEvent(FTBEvent):
	def __init__(self, source, when, pSubSys):
		FTBEvent.__init__(self, source, when)
		self.pSubSys = pSubSys

	def __call__(self, now):
		if self._source:
			self._source.Enable(self.pSubSys)


class DistanceEvent(FTBEvent):
	def __init__(self, pFirstID, pSecondID, oEvent, distance, when):
		self._source = None			# No pInstance to attach to
		self._when = when
		self.interval = when		#
		self.pFirstID = pFirstID
		self.pSecondID = pSecondID
		self.oEvent = oEvent
		self.distance = distance

	def __call__(self, now):
		pFirst = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(self.pFirstID))
		if not pFirst:
			return

		pSecond = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(self.pSecondID))
		if not pSecond:
			return

		kDist = pFirst.GetWorldLocation()
		kDist.Subtract(pSecond.GetWorldLocation())
		distance = kDist.Length()

		if distance < self.distance:
			self.oEvent(now)
		else:
			return self.interval


class FTBEventUser:
	def __init__(self):
		self._lEvents = []

	def CancelEvents(self):
		for i in self._lEvents:
			oEventQueue.dEvents[i._when].remove(i)
		self._lEvents = []


# A TechDef inherits from Override and makes
class TechDef(Foundation.OverrideDef):
	def __init__(self, name, dict = dMode):
		# We don't need the overhead of an override, just its placement in a Mutator
		# with routines to activate and deactivate.  So, bypass the override __init__.
		Foundation.MutatorElementDef.__init__(self, name, dict)
		self.num = oTechs.Register(self, name)

	def AddToMutator(self, toMode):
		# # print 'Adding override %s to mode %s' % (self.name, toMode.name)
		toMode.overrides.append(self)
		toMode.elements.append(self)

	def Activate(self):
		pass
		# # print 'Activating', self.name, oTechs

	def Deactivate(self):
		pass

	def Attach(self, pInstance):
		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		pInstance.lTechs.remove(self)

	# This should be used for ships that have actual ShipClass instances
	def AttachShip(self, pShip, pInstance):
		pass

	def DetachShip(self, pShip, pInstance):
		pass

	def IsDrainYield(self):				return 0
	def IsPhaseYield(self):				return 0



kHullFillColor = App.TGColorA()
kHullFillColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
kHullEmptyColor = App.TGColorA()
kHullEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r,App.g_kSubsystemEmptyColor.g,App.g_kSubsystemEmptyColor.b,App.g_kSubsystemEmptyColor.a)

class GaugeTechDef(TechDef):
	def __init__(self, name, dict = dMode):
		TechDef.__init__(self, name, dict)

	def GetSystemName(self):
		return 'Hull'
		
	def GetSystemPointer(self):
		return 'pHull'
		
	def AttachShip(self, pShip, pInstance):
		item = pInstance.__dict__[self.name]
		print 'GaugeTechDef.AttachShip', self.name, 'to ship', pInstance.sName

		pSystem = None

		pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

	 	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		while pSubsystem != None:
			if pSubsystem.GetName() == self.GetSystemName():
				pSystem = pSubsystem
				pShip.EndGetSubsystemMatch(pIterator)
				break
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		pShip.EndGetSubsystemMatch(pIterator)
		
		if pSystem:
			# print pSystem, item
			# pSystem.SetMaxCondition(item)
			# pSystem.SetCondition(item)
			pInstance.lHealthGauge.append(self)
			pInstance.__dict__[self.GetSystemPointer()] = pSystem
			print pInstance.lHealthGauge

	def DetachShip(self, pShip, pInstance):
		# print 'GaugeTechDef.DetachShip', self.name
		pInstance.lHealthGauge.remove(self)
		pInstance.__dict__[self.GetSystemPointer()] = None

	def GetFillColor(self):
		global kHullFillColor
		return kHullFillColor

	def GetEmptyColor(self):
		global kHullEmptyColor
		return kHullEmptyColor

	def SetGauge(self, pShip, pInstance, pHealthGauge):
		print 'GaugeTechDef.SetGauge', self.name, pShip, pInstance, pHealthGauge, ':',
		try:
			pSystem = pInstance.__dict__[self.GetSystemPointer()]
			print 'pSystem', pSystem, pHealthGauge, ':',
			pHealthGauge.SetObject(pSystem)
			print 'SetObject', ':',
			pHealthGauge.SetEmptyColor(self.GetEmptyColor())
			print 'SetEmpty', ':',
			pHealthGauge.SetFillColor(self.GetFillColor())
			print 'succeeded'
		except:
			print 'failed'
			pass


class HullGaugeTechDef(GaugeTechDef):
	def SetGauge(self, pShip, pInstance, pHealthGauge):
		# print 'HullGaugeTechDef.SetGauge', self.name, pShip, pInstance, pHealthGauge, ':',
		try:
			pSystem = pShip.GetHull()
			# print 'pSystem', pSystem, pHealthGauge, ':',
			pHealthGauge.SetObject(pSystem)
			# print 'SetObject', ':',
			pHealthGauge.SetEmptyColor(self.GetEmptyColor())
			# print 'SetEmpty', ':',
			pHealthGauge.SetFillColor(self.GetFillColor())
			# print 'succeeded'
		except:
			# print 'failed'
			pass


oHullGauge = HullGaugeTechDef('Hull')


##########################################################
# Management of addition and removal of ships
##########################################################


# This class is responsible for the variables associated with an individual ship.
# Attention Apollo!  This class should probably be reviewed for ATP Dimensions,
# and converge with existing structures where appropriate.
# -Dasher42
class ShipInstance(Propertied, FTBEventUser):
	def __init__(self, sName, pShipID, proto = None):
		Propertied.__init__(self, proto)
		FTBEventUser.__init__(self)
		self.sName = sName
		self.dDisabled = {}
		self.lSecondaryTargets = []
		self.pShipID = pShipID

		# self.nExtraDrain = 0.0
		self.lTechs = []

		# Affected flags
		# self.blWeapons = Foundation.Flags()
		# self.blEngines = Foundation.Flags()
		# self.blSensors = Foundation.Flags()
		# self.blShields = Foundation.Flags()

		# self.blAffected = Foundation.Flags()

		global kHullFillColor, kHullEmptyColor
		# For actively running technologies
		self.lBeamDefense = []
		self.lTractorDefense = []
		self.lPulseDefense = []
		self.lTorpDefense = []
		self.lHealthGauge = [ oHullGauge ]

		if proto and proto.__dict__.has_key('dTechs'):
			self.__dict__.update(proto.dTechs)
			for i in proto.dTechs.keys():
				t = oTechs[i]
				t.Attach(self)

	# Unfinished:  this should reset the ship to its prototype specs
	def RevertToProto(self, pShip, pInstance, pShipDef):
		pass

	def DefendVSBeam(self, pShip, pEvent):
		try:
			pEmitter = App.BeamBeamEmitter_Cast(pEvent.GetSource())
			sName = pEmitter.GetFireSound()
			oYield = dYields[sName]
		except:
			oYield = None

		for i in self.lBeamDefense:
			if i.OnBeamDefense(pShip, self, oYield, pEvent):
				return

		if oYield:
			oYield.OnYield(pShip, self, pEvent)

	def DefendVSTractor(self, pShip, pEvent):
		try:
			pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
			sName = pProjector.GetFireSound()
			oYield = dYields[sName]
		except:
			oYield = None

		for i in self.lTractorDefense:
			if i.OnTractorDefense(pShip, self, oYield, pEvent):
				return

		if oYield:
			oYield.OnYield(pShip, self, pEvent)


	def DefendVSPulse(self, pShip, pEvent, pTorp):
		try:
			sName = pTorp.GetModuleName()
			oYield = dYields[sName]
		except:
			oYield = None

		for i in self.lPulseDefense:
			if i.OnPulseDefense(pShip, self, pTorp, oYield, pEvent):
				return

		if oYield:
			oYield.OnYield(pShip, self, pEvent, pTorp)

	def DefendVSTorp(self, pShip, pEvent, pTorp):
		try:
			sName = pTorp.GetModuleName()
			oYield = dYields[sName]
		except:
			oYield = None

		for i in self.lTorpDefense:
			if i.OnTorpDefense(pShip, self, pTorp, oYield, pEvent):
				return

		if oYield:
			oYield.OnYield(pShip, self, pEvent, pTorp)


	##########################################################
	## These are for the adjustment of ship subsystems.  Making the 
	## ShipInstance the broker of this allows us to keep track of things.
	def AdjustPowerOutput(self, pShip, pPower, num):
		pProp = pPower.GetProperty()
		pProp.SetPowerOutput(num)

	def AdjustMainBattery(self, pShip, pPower, num):
		pPower.SetMainBatteryPower(num)

	def AdjustBackupBattery(self, pShip, pPower, num):
		pPower.SetBackupBatteryPower(num)

	def Enable(self, pSubSystem):
		# # print 'Trying to enable', pSubSystem, self.dDisabled
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), self.pShipID)
		if pShip:
			pSubSystemProp = pSubSystem.GetProperty()
			pSubSystemProp.SetDisabledPercentage(self.dDisabled[pSubSystem][1])
			pShields = pShip.GetShields()
			if pSubSys == pShip.GetShields():
				n = 0
				for i in self.dDisabled[pSubSystem][2]:
					pShields.SetCurShields(n, i)
					n = n+1
		del self.dDisabled[pSubSystem]

	def Disable(self, pShip, pSubSys, time):
		if self.dDisabled.has_key(pSubSys):
			scheduled = self.dDisabled[pSubSys][0]._when
			when = time
			if scheduled < when:
				self.dDisabled[pSubSys][0]._when = when
		else:
			pSubSys.SetCondition(0.999 * pSubSys.GetCondition())
			pSubSystemProp = pSubSys.GetProperty()
			fDisabled = pSubSystemProp.GetDisabledPercentage()
			pSubSystemProp.SetDisabledPercentage(1.1)
			oEvent = DisableEvent(self, time, pSubSys)
			if pSubSys == pShip.GetShields():
				tShieldDirs = pShields.GetCurShields(pShields.FRONT_SHIELDS), pShields.GetCurShields(pShields.REAR_SHIELDS), pShields.GetCurShields(pShields.TOP_SHIELDS), pShields.GetCurShields(pShields.BOTTOM_SHIELDS), pShields.GetCurShields(pShields.LEFT_SHIELDS), pShields.GetCurShields(pShields.RIGHT_SHIELDS)
				self.dDisabled[pSubSys] = (oEvent, fDisabled, tShieldDirs)
			else:
				self.dDisabled[pSubSys] = (oEvent, fDisabled)
			oEventQueue.Queue(oEvent)


	def DisableSubSys(self, pShip, pSubSys, time):
		iChildren = pSubSys.GetNumChildSubsystems()

		if (iChildren > 0):
			for i in range(iChildren):
				pChild = pSubSys.GetChildSubsystem(i)
				self.Disable(pShip, pChild, time)
		else:
			self.Disable(pShip, pSubSys, time)

	##########################################################
	## These functions are for the clean removal of technology items
	## from a ShipInstance, and should be called when a ship is destroyed.
	## DetachShipTechs() calls are used for a ship that leaves the set, but
	## still exists; its ShipInstance should remain, with a dictionary of 
	## Technologies, but App objects associated with them should be unloaded.
	## DetachTechs() clears the ShipInstance of all technology references.
	def DetachTechs(self):
		if self.pShipID:
			self.DetachShipTechs()
		
		for i in self.lTechs:
			i.Detach(self)

	def DetachShipTechs(self):
		for i in self.lTechs:
			i.DetachShip(self.pShipID, self)


	##########################################################
	## Here we integrate Sleight42's methods for his ftb.Ship.Ship
	## class.  Sleight, if you're watching, you rock.  - Dasher42
	def __SetSecondaryTargets(self,lTargets):
		self.lSecondaryTargets = lTargets

	def GetSecondaryTargetsRef(self):
		return self.lSecondaryTargets

	def GetSecondaryTargets(self):
		return self.lSecondaryTargets[:]

	def HasAsSecondaryTarget(self,pShip):
		###########################################################
		## I preserve this for instructional purposes.  When Sleight and I
		## were collaborating on early BC modding projects, we were both new
		## to Python, and our coding techniques often reflected our backgrounds
		## with C++ and Java.  The code below is the correct approach in those
		## lower level languages.
		##
		## When dealing with a language like Python, interpreting the byte
		## code and dealing with complex algorithms incurs overhead, yet
		## often when dealing with common problems, there is already code
		## built into the language's interpreter that does this with
		## machine-compiled code, far more efficient than bytecode.
		## It is best to take advantage of this, both for efficiency and
		## conciseness.
		##
		## Lesson:  avoid coding boilerplate in a language designed to free
		## you from that chore.
		###########################################################
		## retval = 0
		## for pTarget in self.lSecondaryTargets:
		## 	if pShip == pTarget:
		## 		retval = 1
		## return retval
		###########################################################
		return pTarget in self.lSecondaryTargets

	def ToggleSecondaryTarget(self,pShip):
		try:
			self.lSecondaryTargets.remove(pShip)
		except:
			self.lSecondaryTargets.append(pShip)

	def ClearSecondaryTargets(self):
		print "Clearing secondaries"
		self.lSecondaryTargets = []

	def FireWeaponsOnList(self, bFiring, eGroup):
		pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), self.pShipID)
		if not pShip:
			return
			
		TacticalInterfaceHandlers.FireWeapons( pShip, bFiring, eGroup)
		pSystem = pShip.GetWeaponSystemGroup( eGroup)
		if pSystem:
			# pGame = App.Game_GetCurrentGame()
			if bFiring:
				for pTarget in self.lSecondaryTargets:
					retval = pSystem.StartFiring( pTarget,pTarget.GetTargetOffsetTG())
					pSystem.SetForceUpdate( 1) # update and fire immediately
			else:
				pSystem.StopFiring()


# Sets a ship up when it is put into the game
class AddShip(TriggerDef):
	def __call__(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if not pShip:	return

		sName = pShip.GetName()
		sClassName = pShip.GetShipProperty().GetShipName()
		pShipDef = None
#		try:
#			pShipDef = Foundation.shipList[sClassName]
#		except:
#			pass

		print 'AddShip:', sClassName, sName, pShip.GetScript()

		if Foundation.shipList.has_key(sClassName):
			pShipDef = Foundation.shipList[sClassName]
			# if (pShipDef.shipPrefix + pShipDef.shipFile) != pShip.GetScript():
			# 	pShipDef = Foundation.shipList[sShipScript]
		else:
			lShipScript = string.split(pShip.GetScript(), '.')
			sShipScript = lShipScript[-1]
		
			if Foundation.shipList.has_key(sShipScript):
				pShipDef = Foundation.shipList[sShipScript]

		print 'Making', sName, 'from', sClassName, ':', pShipDef.__dict__

		try:
			pInstance = dShips[sName]
			pInstance.pShipID = pShip.GetObjID()
		except:
			pInstance = ShipInstance(sName, pShip.GetObjID(), pShipDef)
			dShips[sName] = pInstance
			# print sName, 'assigned to', pInstance, dShips[sName]

		# Texture replacement support (i.e. registries) here.  -Dasher42
		pModule = Foundation.FolderManager('ship', pShipDef.shipFile)
		if pModule and pModule.__dict__.has_key('OnLoad'):
			#try:
			# sTexture = string.split(sName, '-')[0]
			# print 'AddShip:', sTexture
			sTexture = pShipDef.name
			pModule.OnLoad(sTexture, pShip, None, pShipDef = pShipDef)
			#except:
			#	pass

		# dDisplays is there to show ships with active displays that have not 
		# yet been attached to a ShipInstance.  We should only catch 'Player'
		# when the game is started.  
		global dDisplays
		try:
			# print 'AddShip:  trying to SetShipID', sName, dDisplays
			pInstance.pDisplay = dDisplays[pInstance.pShipID]
			del dDisplays[pInstance.pShipID]
			SetShipID(pInstance.pDisplay, pInstance.pShipID)
		except:
			pass

		for i in pInstance.lTechs:
			i.AttachShip(pShip, pInstance)

		# Yay for no drag!  Of course, I could see justification for a very
		# small value for gameplay purposes.
		pShip.SetDisabledEngineDeceleration(0.0)

		pObject.CallNextHandler(pEvent)


# This is here specifically to be overridden.  What if we want to store the ship?
# For example, Apollo's Dimensions could override this with something to save the ShipInstance.
def ClearShip(dShips, sName):
	del dShips[sName]


# Removes a ships and shuts down its properties
class RemoveShip(TriggerDef):
	def __call__(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if not pShip:	return

		sName = pShip.GetName()
		try:
			pInstance = dShips[sName]
			pInstance.DetachShipTechs()
			pInstance.DetachTechs()
			# del pInstance.pShipID
			pInstance.pShipID = None
			ClearShip(dShips, sName)
		except KeyError:
			pass

		pObject.CallNextHandler(pEvent)

oAddShip = AddShip('AddShip', Foundation.TriggerDef.ET_FND_CREATE_SHIP, dMode)
oRemoveShip = RemoveShip('RemoveShip', App.ET_OBJECT_DESTROYED, dMode)


class WeaponHit(TriggerDef):
	def __call__(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pInstance = dShips[pShip.GetName()]

		if pEvent.GetWeaponType() == pEvent.PHASER:
			pInstance.DefendVSBeam(pShip, pEvent)
		elif pEvent.GetWeaponType() == pEvent.TRACTOR_BEAM:
			pInstance.DefendVSTractor(pShip, pEvent)
		else:
			pTorp = App.Torpedo_Cast(pEvent.GetSource())
			if pTorp:
				# # print 'pTorp.GetGuidanceLifeTime()', pTorp.GetGuidanceLifeTime()
				if pTorp.GetGuidanceLifeTime() > 0.0:
					pInstance.DefendVSTorp(pShip, pEvent, pTorp)
				else:
					pInstance.DefendVSPulse(pShip, pEvent, pTorp)

		pObject.CallNextHandler(pEvent)


oWeaponHit = WeaponHit('WeaponHit', App.ET_WEAPON_HIT, dMode)


class TorpedoFired(TriggerDef):
	def __call__(self, pObject, pEvent):
		pTorp = App.Torpedo_Cast(pEvent.GetSource())
		if not pTorp:
			return

		# print 'TorpedoFired'
		try:
			oFire = dOnFires[pTorp.GetModuleName()]
			oFire.OnFire(pEvent, pTorp)
		except:
			pass

		pObject.CallNextHandler(pEvent)


oTorpedoFired = TorpedoFired('TorpedoFired', App.ET_TORPEDO_FIRED, dMode)


###############################################################################
## Dasher42's addition - leave a derelict
###############################################################################
def MakeDerelict(pShip):
	if not pShip:
		return

	import MissionLib
	pMission = MissionLib.GetMission()
	if not pMission:
		return

	sName = pShip.GetName()

	pNeutrals	= pMission.GetNeutralGroup()
	pEnemies	= pMission.GetEnemyGroup()
	pFriendlies	= pMission.GetFriendlyGroup()

	bChanged = 0

	if pFriendlies.IsNameInGroup(sName):
		pFriendlies.RemoveName(sName)
		bChanged = 1
	elif pEnemies.IsNameInGroup(sName):
		pEnemies.RemoveName(sName)
		bChanged = 1

	if not bChanged:
		return

	pNeutrals.AddName(sName)

	# Affiliation colors sometimes don't get set correctly here (by the normal mechanisms). Reset
	# them, just in case.
	# pTargetMenu = App.STTargetMenu_GetTargetMenu()
	# if pTargetMenu:
	# 	pTargetMenu.ResetAffiliationColors()


###############################################################################
#	FireWeapons(pShip, eGroup)
#
#	Fires the specified weapon system group. (primary, secondary, tertiary)
#
#	Args:	pShip		- the ship that is firing
#			bFiring		- whether we are starting or stopping firing
#			eGroup		- the weapon system group to look for
#						  (i.e. App.ShipClass.WG_PRIMARY, WG_SECONDARY,
#						  WG_TERTIARY)
#
#	Return:	none
###############################################################################
# Based on SneakerFireWeapons, from Sneaker's innaccurate phaser mod.

def FireWeapons(pShip, bFiring, eGroup):
	if pShip == None:
		return

	# Check if we're starting or stopping...
	if bFiring != 1:
		# Stopping.
		pSystem = pShip.GetWeaponSystemGroup(eGroup)
		if (pSystem != None):
			pSystem.StopFiring()
		return

	# Starting.  Check if we have a target..
	pSystem = pShip.GetWeaponSystemGroup(eGroup)
	if pSystem:

		# Sneaker98 changes, with Dasher42 revisions
		pPhasers = pShip.GetPhaserSystem()
		# if not (pPhasers and pPhasers.IsTryingToFire()):
		# 	return
		if not pPhasers:
			return

		pTarget = App.PhysicsObjectClass_Cast(pShip.GetTarget())
		if not pTarget:
			return

		InaccurateFire(pShip, pSystem, pTarget)


# Dasher42's slightly adjusted and refactored Inaccurate phasers
def InaccurateFire(pShip, pSystem, pTarget):
	fMiss = 0.0
	fSensorRange = 200.0

	vAngle = pTarget.GetAngularVelocity()
	fAngleDiff = vAngle.x + vAngle.y + vAngle.z
	vAngle = pTarget.GetAcceleration()
	fAngleDiff = fAngleDiff + vAngle.x + vAngle.y + vAngle.z

	if fAngleDiff < 0.0:		fAngleDiff = fAngleDiff * -5.0
	else:						fAngleDiff = fAngleDiff * 5.0

	vTargetLocation = pTarget.GetWorldLocation()
	vTargetLocation.Subtract(pSystem.GetWorldLocation())
	fObjectDistance = vTargetLocation.Unitize()

	# fSizeFactor = 1.5 / (pTarget.GetRadius() + 0.01)
	pSensor = pShip.GetSensorSubsystem()
	if pSensor:
		fSensorRange = pSensor.GetSensorRange()

	if fSensorRange:
		fMiss = (fAngleDiff * 0.5 + fObjectDistance * 0.5) / ((fSensorRange / 20.0) + 1.0)
	else:
		fMiss = 1.0

	# print 'miss', fMiss, ': a', fAngleDiff, 'd', fObjectDistance, 's', fSensorRange

	if fMiss <= 0.0:
		pSystem.StartFiring(pTarget, pShip.GetTargetOffsetTG())
		pSystem.SetForceUpdate(1) # update and fire immediately

	else:
		if fMiss > 2.0:
			fMiss = 2.0

		# print 'Off target', fMiss

		kNewLocation = App.TGPoint3_GetRandomUnitVector()
		# fMinDistance = 0.0
		# fDistance = fMinDistance + (fMaxDistance - fMinDistance) * fMiss

		# Scale the direction by the distance to get the position...
		kNewLocation.Scale(fMiss)
		kLocation = pShip.GetTargetOffsetTG()
		kLocation.Add(kNewLocation)

		pSystem.StartFiring(pTarget, kLocation)
		pSystem.SetForceUpdate(1) # update and fire immediately


# Awesome work, Leo. -Dasher42
class InacAITrigger(TriggerDef):
	def __init__(self, dict = dMode):
		TriggerDef.__init__(self, "AI Inaccurate Weapons", App.ET_WEAPON_FIRED, dict)

	def __call__(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pTarget = App.ShipClass_Cast(pShip.GetTarget())
		if not pTarget:
			return

		if pShip.GetPhaserSystem() != None and pShip.GetPhaserSystem().IsFiring():
			pSystem = pShip.GetPhaserSystem()
		elif pShip.GetTorpedoSystem() != None and pShip.GetTorpedoSystem().IsFiring():
			pSystem = pShip.GetTorpedoSystem()
		elif pShip.GetPulseWeaponSystem() != None and pShip.GetPulseWeaponSystem().IsFiring():
			pSystem = pShip.GetPulseWeaponSystem()
		else:
			return
#		pSystem.StopFiring()
		InaccurateFire(pShip, pSystem, pTarget)

oAiInacTrigger = InacAITrigger()

bFail = 0

###############################################################################
#	SetShipID(pDisplay)
#	
#	Sets the ID of the ship in the display.
#	
#	Args:	pDisplay	- the display
#			idNewShip	- the ID of the new ship in the display
#	
#	Return:	none
###############################################################################
def SetShipID(pDisplay, pShipID):
	# Get the game object.
	pGame = App.Game_GetCurrentGame()

	idShip = pDisplay.GetShipID()
	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

	pShieldsDisplay = pDisplay.GetShieldsDisplay()
	pDamageDisplay = pDisplay.GetDamageDisplay()
	pHealthGauge = pDisplay.GetHealthGauge()

	print 'SetShipID', pDisplay, pShipID

	# If we currently have a valid ship ID, remove events for it.
	if idShip != App.NULL_ID:
		# Remove display specific events before setting new ShipID.
		pShieldsDisplay.RemoveEvents()
		pDamageDisplay.RemoveEvents()

	# Set new ship ID.
	pDisplay.SetShipIDVar(pShipID)

	# If valid ship ID.
	if pShipID != App.NULL_ID:
		pHealthGauge.SetVisible(0)
	else:
		# No ship.
		pHealthGauge.SetNotVisible(0)

	# Update displays for new ship.
	pShieldsDisplay.UpdateForNewShip()
	pDamageDisplay.UpdateForNewShip()

	if pShip == None:
		pHealthGauge.SetObject(pShip)
		return

	try:
		pInstance = dShips[pShip.GetName()]
		print 'pInstance:', pInstance.lHealthGauge
		oTechGauge = pInstance.lHealthGauge[-1]
		oTechGauge.SetGauge(pShip, pInstance, pHealthGauge)
		if dDisplays.has_key(pShipID):
			if pDisplay not in dDisplays[pShipID]:
				dDisplays[pShipID].append(pDisplay)
		else:
			dDisplays[pShipID] = [ pDisplay ]
			
	except:
		# print 'No ShipInstance for "%s"' % (pShip.GetName()), dShips
		# dDisplays[pShipID] = pDisplay
		# pHealthGauge.SetObject(pShip.GetHull())
		pass

	global bFail
	if bFail:
		for i in dShips.items():
			print i[0], i[1].__dict__
		pInstance = dShips['bah']



oSetShipID = Foundation.OverrideDef('SetShipID', 'Tactical.Interface.ShipDisplay.SetShipID', 'FoundationTech.SetShipID', dMode )


print 'Foundation Tech loaded'
