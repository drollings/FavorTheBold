# Foundation Triggers Extension 20030305 for Bridge Commander
# Written March 5, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import App
import Foundation
import Actions.EffectScriptActions 
import string
import nt

mode = Foundation.MutatorDef.FTB

class Dummy:
	pass

if int(Foundation.version[0:8]) < 20040715:

	def Clone(self):
		other = Dummy()
		other.__class__ = self.__class__
		other.__dict__.update(self.__dict__)
		return other

	Foundation.MutatorElementDef.Clone = Clone

	Foundation.version = '20040715p'

	print __name__, 'loaded'
else:
	print __name__, 'ignored'



def PreloadShip(sModelName, iNumToLoad = 0):
	# Mark the model for preloading.
	pMod = Foundation.FolderManager('ship', sModelName)
	# pMod = __import__("ships.%s" % sModelName)
	pMod.PreLoadModel()

	# Before the mission is initialized, we'll want to create a
	# bunch of these ships.
	if iNumToLoad > 0:
		import MissionLib
		pMission = MissionLib.GetMission()
		if not pMission:
#			debug("No mission in PreloadShip.  Can't precreate ships (but models will be preloaded)")
			return

		pMission.AddPrecreatedShip(sModelName, iNumToLoad)


def AdjustShipForDifficulty(pShip, pcHardpointFile):
	if (pShip == None):
		return
	if (pcHardpointFile == None):
		return

	fOFactor = App.Game_GetOffensiveDifficultyMultiplier()
	fDFactor = App.Game_GetDefensiveDifficultyMultiplier()
#	debug("Adjusting ship, o factor: " + str(fOFactor) + ", d factor: " + str(fDFactor))

	pShipSet = pShip.GetPropertySet()
	pNewSet = App.TGModelPropertySet()
	# Load hardpoints.
	mod = Foundation.FolderManager('hp', pcHardpointFile)
	if not mod:
		return
	# try:
	# 	mod = __import__("ships.Hardpoints." + pcHardpointFile)
	# except ImportError:
#		debug("Tried to load hardpoint file ships.Hardpoints." + pcHardpointFile + " and failed miserably")
	# 	return

	reload (mod)
	mod.LoadPropertySet(pNewSet)

	# Modify all subsystem strengths.
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pNewList = pNewSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	pShipList.TGBeginIteration()
	pNewList.TGBeginIteration()

	for i in range(pShipList.TGGetNumItems()):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pNewProperty = App.SubsystemProperty_Cast(pNewList.TGGetNext().GetProperty())

		pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

		if (pSubsystem != None):
			import loadspacehelper
			loadspacehelper.ProcessSubsystemForDifficulty(pSubsystem, pShipProperty, pNewProperty)

	pShipList.TGDoneIterating()
	pNewList.TGDoneIterating()
	pShipList.TGDestroy()
	pNewList.TGDestroy()

	# This is done to compensate for the AI's poor handling of low power quantities
	pPower = pShip.GetPowerSubsystem()
	if pPower:
		pPower.SetPowerOutput(pPower.GetPowerOutput() * 1.5)


def CreateShip(pcScript, pSet, pcIdentifier, pcLocationName, iWarpFlash = 0, bGrabPreloaded = 1, shipDef = None):
	import App
	# Creates a new ship

	# Check if a ship of this type has been pre-created for us.
	pShip = None
	if bGrabPreloaded:
		import MissionLib
		pMission = MissionLib.GetMission()
		if pMission:
			pShip = pMission.GetPrecreatedShip(pcScript)

	if not pShip:
		# FIX ME:  This is back-arsewards in that the ship script is gotten from kStats
		# which was gotten from the ship script in the first place.  But this is the
		# least intrusive fix I can think of

		pModule = Foundation.FolderManager('ship', pcScript)

		# if Foundation.bTesting:
		# 	print pcScript, pModule
		pModule.LoadModel ()
		kStats = pModule.GetShipStats ()

		pShip = App.ShipClass_Create( kStats['Name'] )
		# print 'pModule name', pModule.__name__
		pShip.SetScript(pModule.__name__)

		if (kStats.has_key('DamageRadMod')):
			pShip.SetVisibleDamageRadiusModifier( kStats['DamageRadMod'] )

		if (kStats.has_key('DamageStrMod')):
			pShip.SetVisibleDamageStrengthModifier( kStats['DamageStrMod'] )

		if (kStats.has_key('SpecularCoef')):
			pShip.SetSpecularKs( kStats['SpecularCoef'] )

		pPropertySet = pShip.GetPropertySet()
		# Load hardpoints.
		mod = Foundation.FolderManager('hp', kStats['HardpointFile'])
		App.g_kModelPropertyManager.ClearLocalTemplates()
		reload(mod)
		mod.LoadPropertySet(pPropertySet)

		if kStats.has_key('Rescale'):
			pShip.SetScale(kStats['Rescale'])

		pShip.SetupProperties()

		# Set the default splash damage based on the size of the ship
		# and the strength of its hull.
		pHull = pShip.GetHull()
		if pHull:
			pShip.SetSplashDamage(pHull.GetMaxCondition() * 0.1, pShip.GetRadius() * 2.0)
			#debug("Setting splash damage for %s to (%f, %f)" % (pShip.GetName(), pShip.GetSplashDamage(), pShip.GetSplashDamageRadius()))

		pShip.SetNetType (kStats['Species'])

		if shipDef:
			sName = shipDef.name	
		else:
			sName = kStats['Name']

	if pSet:
		if not pSet.AddObjectToSet( pShip, pcIdentifier ):
#			debug("Unable to add ship %s to set %s" % (pcIdentifier, pSet.GetName()))

			# Delete the ship.
			pDeletionEvent = App.TGEvent_Create()
			pDeletionEvent.SetEventType(App.ET_DELETE_OBJECT_PUBLIC)
			pDeletionEvent.SetDestination(pShip)
			App.g_kEventManager.AddEvent(pDeletionEvent)

			return None

		# Place the object at the specified location.
		if pcLocationName:
			pShip.PlaceObjectByName( pcLocationName )

		pShip.UpdateNodeOnly()

		if (iWarpFlash != 0):
			pWarp = pShip.GetWarpEngineSubsystem()
			if (pWarp != None) and (pcLocationName != None) and (pcLocationName != ""):
				pSequence = Actions.EffectScriptActions.CreateEndWarpSequence(pShip.GetObjID(), pcLocationName)
				pSequence.Play()
			else:
				# Just create a warp flash wherever the thing appears.
				pAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
				pSequence = App.TGSequence_Create()
				pSequence.AddAction(pAction)
				pSequence.Play()

	# The Foundation requires that added ships select a species number that corresponds to an icon.
	# As icons are loaded, they are issued numbers by the Foundation.  This makes sure that a ship
	# has the species number that corresponds to the icon. -Dasher42

	pShipProperty = pShip.GetShipProperty()


	if pShipProperty:
		sName = pShipProperty.GetShipName()
		if shipDef:
			pShipProperty.SetSpecies(shipDef.GetIconNum())
			pShipProperty.SetShipName(shipDef.name)
			sName = shipDef.name
		elif Foundation.shipList._keyList.has_key(pcScript):
			pShipProperty.SetSpecies(Foundation.shipList[pcScript].GetIconNum())
			
	else:
		sName = kStats['Name']
		print 'ERROR:  Cannot get ship property for %s, check hardpoints!' % (pcScript)

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_SHIP)
	pEvent.SetDestination(pShip)
	App.g_kEventManager.AddEvent(pEvent)

	return pShip



def CreatePlayerShip(sShipClass, pSet, pcName, sWaypoint, bUnloadShip = 0):
	import App
	import loadspacehelper
	pGame = App.Game_GetCurrentGame()

	#
	# Ugly, Ugly, Ugly
	#
	# Until we fix the type vs. string typing issue, we can't know if what they
	# want (string) is the same as what we have (type) without doing a big 'if'
	# check, which of course limits us.
	#

	# Don't show an entering banner this time..
	import Bridge.HelmMenuHandlers
	Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0

	bCreateNewShip = 1
	pPlayer = pGame.GetPlayer()
	if pPlayer:
		pOldSet = pPlayer.GetContainingSet()
		# Player exists...   But are they about to die?  If they're
		# Dead and they're not in a set, assume that they're about to
		# be deleted, and create a new player.
		if (not pPlayer.IsDead()):
			# Player isn't dead.  Check the player's ship to see if
			# a new one should be created.
			kSpecies = pPlayer.GetShipProperty().GetSpecies()

			if (((kSpecies == App.SPECIES_GALAXY) and (sShipClass != "Galaxy")) or
				((kSpecies == App.SPECIES_SOVEREIGN) and (sShipClass != "Sovereign"))):
				# Remove any old menus/handlers before setting up the new ship
				DetachCrewMenus()

				pOldSet.DeleteObjectFromSet(pPlayer.GetName())
			else:
				bCreateNewShip = 0
		else:
			if (pOldSet != None):
				# Remove any old menus/handlers before setting up the new ship
				DetachCrewMenus()

				pOldSet.DeleteObjectFromSet(pPlayer.GetName())

	# If the ships aren't the same (or no previous ship), create the new one
	if (bCreateNewShip == 1):
		# pShipMod = __import__("ships." + sShipClass)
		pShipMod = Foundation.FolderManager('ship', sShipClass)
		# kShipStats = pShipMod.GetShipStats()
		pPlayer = loadspacehelper.CreateShip(sShipClass, pSet, pcName, sWaypoint)

		if (pPlayer != None):
			pGame.SetPlayer(pPlayer)
			#
			# If a federation ship, give it a default NCC
			# if (sShipClass == "Sovereign"):
			# 	pPlayer.ReplaceTexture("Data/Models/Ships/Sovereign/Sovereign.tga", "ID")
			# elif (sShipClass == "Galaxy"):
			# 	pPlayer.ReplaceTexture("Data/Models/SharedTextures/FedShips/Dauntless.tga", "ID")
			# elif (sShipClass == "Nebula"):
			# 	pPlayer.ReplaceTexture("Data/Models/SharedTextures/FedShips/Berkeley.tga", "ID")
			# elif (sShipClass == "Akira"):
			# 	pPlayer.ReplaceTexture("Data/Models/Ships/Akira/Geronimo.tga", "ID")
			# elif (sShipClass == "Ambassador"):
			# 	pPlayer.ReplaceTexture("Data/Models/Ships/Ambassador/Zhukov.tga", "ID")
			
			#try:
			#	pShipMod.ReplaceShipTextures(pPlayer, sShipClass)
			#except:
			#	pass

			# Set the variable for the player's hardpoint file, so we can use
			# it later if the difficulty level is changed.
			# print 'hardpoints', pShipMod.GetShipStats()["HardpointFile"], sShipClass
			App.Game_SetPlayerHardpointFileName(pShipMod.GetShipStats()["HardpointFile"])
			# This is broken.  Fix it! - Dasher42
			# loadspacehelper.AdjustShipForDifficulty(pPlayer, App.Game_GetPlayerHardpointFileName())
			pPlayer.SetAlertLevel(App.ShipClass.GREEN_ALERT)

			pTorpSys = pPlayer.GetTorpedoSystem()
			if(pTorpSys):
				if (bUnloadShip != 0):
					# Unloads all torps, and resets the current loads to 0
					pTorpSys.SetAmmoType(0, 0)

					# Unload all other torps from the system
					iNumTypes = pTorpSys.GetNumAmmoTypes()
					for iType in range(iNumTypes):
						pTorpType = pTorpSys.GetAmmoType(iType)

						# Unload current load
						pTorpSys.LoadAmmoType(iType, -pTorpSys.GetNumAvailableTorpsToType(iType))


	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP)
	pEvent.SetDestination(pPlayer)
	App.g_kEventManager.AddEvent(pEvent)


	return (pPlayer)


Foundation.CreateShip = CreateShip
Foundation.AdjustShipForDifficulty = AdjustShipForDifficulty
Foundation.PreloadShip = PreloadShip
Foundation.CreatePlayerShip = CreatePlayerShip

oCreateShip = Foundation.OverrideDef('oCreateShip', 'loadspacehelper.CreateShip', 'Foundation.CreateShip', { 'modes': [mode] })
oAdjustShipForDifficulty = Foundation.OverrideDef('oAdjustShipForDifficulty', 'loadspacehelper.AdjustShipForDifficulty', 'Foundation.AdjustShipForDifficulty', { 'modes': [mode] })
oPreloadShip = Foundation.OverrideDef('oPreloadShip', 'loadspacehelper.PreloadShip', 'Foundation.PreloadShip', { 'modes': [mode] })
oCreatePlayerShip = Foundation.OverrideDef('oCreatePlayerShip', 'MissionLib.CreatePlayerShip', 'Foundation.CreatePlayerShip', { 'modes': [mode] })

