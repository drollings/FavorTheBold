# Foundation Technologies

# Date:  March 19, 2004
# Author:  Daniel Rollings AKA Dasher42 

# This is a project to refine the concept of Apollo's Advanced Technologies, 
# particularly the QuickBattle addon, and create a modular, extensible framework 
# in the idiom of the Foundation.


# NOTE:  TriggerDefs have internal reference counts, so we can 
# Activate() and Deactivate() them at will to affect events.


##########################################################
# Imports and global data structures
##########################################################

# import App
import DummyApp
App = DummyApp.DummyApp()

import Foundation
import Registry
import Flags

mode = Foundation.MutatorDef('Foundation Technologies')
modeDict = { 'modes': [ mode ] }

dShips = None
dTorps = None
oTechs = None


##########################################################
# Reference points for optional external API's
##########################################################
NanoFX_Lib = None
try:
	NanoFX_Lib = __import__('Custom.NanoFX.NanoFX_Lib')
except:
	pass

ATP_BridgeFX = None
try:
	ATP_BridgeFX = __import__('Custom.AdvancedTechnologies.Data.ATP_BridgeFX')
except:
	pass


##########################################################
# Base classes
##########################################################

# class Propertied:
# 	def __init__(self):
# 		self.lProperties = []
# 
# 	def Terminate(self):
# 		for i in self.lProperties:
# 			i.Deactivate()
# 		self.lProperties = []
# 
# 	def AddProperty(self, pProp):
# 		self.lProperties.append(pProp)
# 		pProp.Activate()
# 
# 	def RemoveProperty(self, pProp):
# 		self.lProperties.remove(pProp)
# 		pProp.Deactivate()


# Akin to a Mutator, this holds list of Technology Elements that have different effects.
# It is a master broker of active technologies in the game.
class TechnologyList(Registry.Registry):
	def __init__(self):
		Registry.Registry.__init__(self)

 	def Register(self, obj, name):
		Registry.Registry.Register(self, obj, name)


# A TechDef inherits from Override and makes 
class TechDef(Foundation.OverrideDef):
	def __init__(self, name):
		# We don't need the overhead of an override, just its placement in a Mutator
		# with routines to activate and deactivate.  So, bypass the override __init__.
		Foundation.MutatorElementDef.__init__(self, name, modeDict)

	def AddToMutator(self, toMode):
		# print 'Adding override %s to mode %s' % (self.name, toMode.name)
		toMode.overrides.append(self)
		toMode.elements.append(self)
		if toMode.__dict__.has_key('oTechs'):	
			toMode.oTechs.Register(self, self.name)
		else:
			toMode.oTechs = TechnologyList()

	def Activate(self):
		global oTechs, dTorps, dShips
		if not oTechs:	
			oTechs = Foundation.pCurrentMode.oTechs
			dShips = oTechs.dShips
			dTorps = oTechs.dTorps

	def Deactivate(self):
		global oTechs, dTorps, dShips
		if oTechs:
			oTechs = None
			dTorps = None
			dShips = None


class WeaponDef(TechDef):
	def __init__(self, name):
		TechDef.__init__(self, name)

	def Timer(self):
		pass
		

# A hypothetical class to pass around instances of between multiple functions
# class EventStub:
# 	def __init__(self):
# 		self.pShip = None
# 		self.pProp = None
# 		self.pShipInstance = None
# 		self.pAttacker = None
# 		self.oYield = None


##########################################################
# Management of addition and removal of ships
##########################################################


# This class is responsible for the variables associated with an individual ship
class ShipInstance:
	def __init__(self, sName, pShipDef = None):
		self.sName = sName
		self.pShipDef = pShipDef
		self.flagFeatures = Flags.Flags()
		self.flagActive = Flags.Flags()

		if pShipDef.__dict__.has_key('lProperties'):
			for i in pShipDef.lProperties:
				self.AddProperty(i)

	def DefendVSWeapon(self, pShip, pEvent, oYield):
		pass

	def DefendVSTorpedo(self, pShip, pEvent, oYield):
		pass


# Sets a ship up when it is put into the game
class AddShip(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if not pShip:	return

		sName = pShip.GetShipProperty().GetShipName()
		try:
			pShipDef = Foundation.shipList[sName]
			pInstance = ShipInstance(pShipDef)
			dShips[sName] = [ pShip, pShipDef ]
		except KeyError:
			dShips[sName] = [ pShip, None ]
	
		pObject.CallNextHandler(pEvent)

# Removes a ships and shuts down its properties
class RemoveShip(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if not pShip:	return

		sName = pShip.GetShipProperty().GetShipName()
		try:
			dShips[sName].Terminate()
			del dShips[sName]
		except KeyError:
			pass

		pObject.CallNextHandler(pEvent)

AddShip('AddShip', Foundation.TriggerDef.ET_FND_CREATE_SHIP, modeDict)
RemoveShip('RemoveShip', App.ET_OBJECT_DESTROYED, modeDict)



##########################################################
# Management of addition, impact, and removal of torpedoes
##########################################################

# This class is responsible for the variables associated with an individual ship
class TorpInstance:
	def __init__(self, pTorpedo, pTorpDef = None):
		self.pTorpDef = pTorpDef
		dTorps[pTorpedo.GetName()] = [ pTorpedo, pTorpedoDef ]


# Sets a Torpedo up when it is put into the game
class AddTorpedo(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pTorpedo = App.TorpedoClass_Cast(pEvent.GetDestination())
		pProp = pTorpedo.GetTorpedoProperty()
		try:
			pTorpedoDef = TorpedoList[pProp.GetTorpedoName()]
			pTorpedoDef.HandleFire(pTorpedo)			# TODO - implement the TorpedoDef
		except KeyError:
			pass

		pObject.CallNextHandler(pEvent)

# Removes a Torpedos and shuts down its properties
class RemoveTorpedo(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pTorpedo = App.TorpedoClass_Cast(pEvent.GetDestination())
		if pTorpedo:
			try:
				dTorps[pTorpedo.GetName()].Terminate()
				del dTorps[pTorpedo.GetName()]
			except KeyError:
				pass
		pObject.CallNextHandler(pEvent)


AddTorpedo('AddTorpedo', App.ET_TORPEDO_FIRED, modeDict)
RemoveTorpedo('RemoveTorpedo', App.ET_TORPEDO_EXITED_SET, modeDict)


class WeaponHit(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent):
		try:
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			pProp = pShip.GetShipProperty()
			pShipInstance = dShips[pProp.GetShipName()]

			# if pEvent.GetFiringObject():
			# 	pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
				
			oYield = None

			pTorp = App.Torpedo_Cast(pEvent.GetSource())
			if pTorp:
				oYield = oTechs.WeaponYield(pTorp.GetName())		# TODO - Implement the yields

				if oYield:
					if not pShipInstance.DefendVSTorp(pShip, pEvent, oYield):
						oYield(pShip, pObject, pEvent)				# TODO - Implement the yields
			else:
				pShipInstance.DefendVSWeapon(pShip, pEvent, oYield)	# TODO - get the defensive routines going
			
		except:
			print 'Error in TorpedoHit', pObject, pEvent, pShip, pProp, pShipInstance
			
		pObject.CallNextHandler(pEvent)


WeaponHit('WeaponHit', App.ET_WEAPON_HIT, modeDict)


##########################################################
# Weapon properties
##########################################################


class TorpedoProperty:
	def OnHit(self, pObject, pEvent):
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pInstance = dShips[pShip.GetName()]

		if not pInstance.OnHit(pShip, this):
			pass

		if not positionSelectorShip(pShip,2)==0:
			#Check if the tartget is immune to the drainerweapon (Klingon, Breen, Coalition (new shipline))
			return

		pPlayer = MissionLib.GetPlayer()
		if not pPlayer:
				return

		if pPlayer.GetObjID() == pShip.GetObjID():
			pSound = App.g_kSoundManager.GetSound("PowerDisabled")
			if pSound:
				pSound.Play()

		pPower = pShip.GetPowerSubsystem()
		if not pPower:		return

		pProp = pPower.GetProperty()
		pProp.SetPowerOutput(0.0)
		powerTest(pShip,0.0)				#Warp Core doesn't produce a single Watt anymore

		pShields = pShip.GetShields()			#Bye, shields
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			pShields.SetCurShields(ShieldDir,0.0)

		HasSufficientSpecialPower(pShip,0)
		AdjustSpecialPower(pShip,9999999) #No more special power

		MissionLib.MakeSubsystemsInvincible(pPower)
		pPower.SetCondition(0.0001*pPower.GetMaxCondition())

		pShip.SetDisabledEngineDeceleration(4.0)


class TorpSetup(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pTorp = App.Torpedo_Cast(pEvent.GetSource())
		if not pTorp:
			return

		if dTorpTypes.has_key(pTorp.GetNetType()):
			dTorps[pTorp.GetObjID()] = TorpInstanceord(dTorpTypes[pTorp.GetNetType()])

		print pTorp.GetModuleName(), pTorp.GetTargetID(), pTorp.GetParentID()
		pObject.CallNextHandler(pEvent)



class TorpedoFired(Foundation.TriggerDef):
	def __call__(self, pObject, pEvent, dict = {}):
		pTorp = App.Torpedo_Cast(pEvent.GetSource())
		if not pTorp:
			return

		if dTorpTypes.has_key(pTorp.GetNetType()):
			dTorps[pTorp.GetObjID()] = TorpInstanceord(dTorpTypes[pTorp.GetNetType()])

		print pTorp.GetModuleName(), pTorp.GetTargetID(), pTorp.GetParentID()
		pObject.CallNextHandler(pEvent)


if __name__ == '__main__':

	gameMode = Foundation.BuildGameMode()

	t = Foundation.TechDef()
	t.AddToMutator(gameMode):
