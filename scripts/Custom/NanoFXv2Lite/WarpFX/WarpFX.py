###############################################################################
##	Filename:	NanoFXv2.py
##
##	Nano's Warp Sequence Version 1.0
##
##	Created:	03/26/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################

import App 
import string
import TacticalInterfaceHandlers
import Foundation
import Custom.NanoFXv2Lite.NanoFX_Lib
import Custom.NanoFXv2Lite.NanoFX_Config
import Custom.NanoFXv2Lite.NanoFX_ScriptActions
import WarpFX_GUI
import Effects

g_Distance		 = 5.0
g_ShipSpeed		 = 0.0
g_ShipAccel		 = 0.0

TRUE = 1
FALSE = 0

Effects.g_pcWarpTrailTextureName = "Custom/NanoFXv2/WarpFX/Gfx/StarStreaks_Nano.tga"
Effects.g_fWarpTrailWidth = 0.175
Effects.g_fWarpTrailHeight = 11.00 + WarpFX_GUI.GetWarpSpeed()

###############################################################################
##  Create Warp Nacelle Power up Flash Sequence
###############################################################################
def CreateNacelleFlashSeq(pShip, fSize):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	###
	### Setup for Effect
	fFlashColor   = Custom.NanoFXv2Lite.NanoFX_Lib.GetOverrideColor(pShip, "WarpFX")
	if (fFlashColor == None):
		sRace         = Custom.NanoFXv2Lite.NanoFX_Lib.GetSpeciesName(pShip)
		fFlashColor   = Custom.NanoFXv2Lite.NanoFX_Lib.GetRaceTextureColor(sRace)
	sOutterFile   = "Custom/NanoFXv2/WarpFX/Gfx/NacelleFlash/NacelleFlash_Outter.tga"
	sCoreFile     = "Custom/NanoFXv2/WarpFX/Gfx/NacelleFlash/NacelleFlash_Core.tga"
	pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	pAttachTo     = pShip.GetNode()
	pWarpSystem   = pShip.GetWarpEngineSubsystem()
	if pWarpSystem:
		iNumWarpDrive = pWarpSystem.GetNumChildSubsystems()
	###
	### Get Flash Positions on Each Nacelle
	try:
		from Custom.AdvancedTechnologies.Data import ATP_Lib
		lNacellePositions = ATP_Lib.GetNacellePositions(pShip)
	except:
		retList=[]
		if iNumWarpDrive > 0:
			for i in range(iNumWarpDrive):
				pChild = pWarpSystem.GetChildSubsystem(i)
				if pChild:
					vLoc=pChild.GetPosition()
					retList.append(vLoc)

		lNacellePositions = retList[:]
	###
	### Create Flash on Each Nacelle
	for vWarpEngEmitPos in lNacellePositions:

		pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sOutterFile, pEmitFrom, pAttachTo, fSize * 2.0, vWarpEngEmitPos, iTiming = 11, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.6)
		pSequence.AddAction(pFlash)

		pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sCoreFile, pEmitFrom, pAttachTo, fSize * 2.0, vWarpEngEmitPos, iTiming = 11, fBrightness = 0.5)
		pSequence.AddAction(pFlash)		
	###
	return pSequence
	
def ETA(pAction, sString, fPosY, fTimer, iSize = 16):
	
	pSequence = App.TGSequence_Create()
	
	pString = App.TGString()
	pString.SetString(sString)
	
	pAction = App.TGScriptAction_Create("MissionLib", "TextBanner", pString, 0, fPosY, fTimer, iSize)
	pSequence.AddAction(pAction)
	
	pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence))
	pSequence.Play()
	
	return 0
	
def DestinationCutscene(pWarpSeq, pShip):

	pSequence = App.TGSequence_Create()
		
	InitWarpSetLighting("warp")
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut", 1))
		
	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "warp")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "warp")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", "warp", pShip.GetName())
	pSequence.AppendAction(pAction)
	
			
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeIn", 1))
	
	pcDest = None
	pcDestModule = pWarpSeq.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule
	pAction = App.TGScriptAction_Create(__name__, "ETA", "En Route to... " + pcDest, 0.04, 5.0)
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 1.0)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "warp")	
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
	pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
		
	pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
	pSequence.AddAction(pAction, App.TGAction_CreateNull(), 8.0)
	
	#pAction = App.TGScriptAction_Create(__name__, "FixBlinkers", pShip)
	#pSequence.AppendAction(pAction)
	
	return pSequence
	
def FixBlinkers(pAction, pShip):
	import Custom.NanoFXv2Lite.SpecialFX.BlinkerFX
	Custom.NanoFXv2Lite.SpecialFX.BlinkerFX.CreateBlinkerFX(pShip)
	
	return 0
	
###############################################################################
## Engage... Assemble Pre-Warp Sequence
###############################################################################
def EngageWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip):
	
	### Setup Sequences ###
	pPreWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.PRE_WARP_SEQUENCE))
	pWarpBeginAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_BEGIN_ACTION)
	pWarpEndAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_END_ACTION)
	pMoveAction1 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_1)
	###
	Effects.g_fWarpTrailHeight = 11.00 + WarpFX_GUI.GetWarpSpeed()
	fEntryDelayTime = 6.0 + pShip.GetRadius() / 2.0
	pWarpSoundAction1 = None
	###
	### If Player ship, setup for that ###
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		### Clear the player's target ###
		TacticalInterfaceHandlers.ClearTarget(None, None)
		###
		pSequence = DestinationCutscene(pWarpSeq, pShip)	
		pWarpSeq.AddActionDuringWarp(pSequence, 1.2)
		pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"), pPreWarp)
		
	### If Ship has Moving Nacelles (Voyager) move them
	try:
		from Custom.AdvancedTechnologies.Data import ATP_Lib
		pMoveNacellesAction = App.TGScriptAction_Create("Custom.AdvancedTechnologies.Data.ATP_Lib", "ForceNacelles", pShip, "Up")
		pWarpSeq.AddAction(pMoveNacellesAction, pPreWarp, fEntryDelayTime - 2.8)
	except:
		ERROR = "No ATP3"
	###		
	### Engage Engine Sound
	sRace = Custom.NanoFXv2Lite.NanoFX_Lib.GetSpeciesName(pShip)
	if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		pWarpSoundAction1 = App.TGSoundAction_Create(sRace + "EnterWarp")
		pWarpSoundAction1.SetNode(pWarpSet.GetEffectRoot())
		### Force Full Impulse ###
		pWarpSeq.AddAction(App.TGScriptAction_Create(__name__, "SetShipImpulse", pShip, 1.000000, TRUE), pPreWarp)
		fCount = 0.0
		while (fCount < fEntryDelayTime):
			pCoastAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetImpulse", pShip.GetObjID(), 1.0)
			pWarpSeq.AddAction(pCoastAction, pPreWarp, fCount)
			fCount = fCount + 0.1
	###
	else:
		pWarpSoundAction1 = App.TGSoundAction_Create(sRace + "EnterWarp", App.TGSAF_DEFAULTS, pWarpSeq.GetOrigin().GetName())
		pWarpSoundAction1.SetNode(pShip.GetNode())
	###
	pWarpSeq.AddAction(pWarpSoundAction1, pPreWarp, fEntryDelayTime - 2.8)
	pWarpSeq.AddAction(CreateNacelleFlashSeq(pShip, pShip.GetRadius()), pPreWarp, fEntryDelayTime - 0.9)
	###	
	### Begin Warping at the Delay Time ###
	pWarpSeq.AddAction(pWarpBeginAction, pPreWarp, fEntryDelayTime)
	###
	### Move the ship ###
	pWarpSeq.AddAction(pWarpEndAction, pWarpBeginAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 4.0)
	###
	### Create the warp flash ###
	pFlashAction1 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
	pWarpSeq.AddAction(pFlashAction1, pWarpEndAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 4.0)
	###
	### Hide the ship ###
	pWarpSeq.AppendAction(App.TGScriptAction_Create(__name__, "HideShip", pShip.GetObjID(), TRUE))
	###
	### Place the ship in the warp set, shortly after WarpFlash ###
	pWarpSeq.AddAction(pMoveAction1, pFlashAction1, 0.1)
	###
###############################################################################
## Travelling at Warp 9 Captain.... Assemble During Warp Sequence
###############################################################################
def DuringWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip):
	
	### Setup Sequences ###
	pWarpEnterAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.WARP_ENTER_ACTION)
	pDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.DURING_WARP_SEQUENCE))
	pPostDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_DURING_WARP_SEQUENCE))
	pMoveAction1 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_1)
	###
	pPreDuringWarpAction = pMoveAction1
	###
	pAction = App.TGScriptAction_Create(__name__, "HideShip", pShip.GetObjID(), FALSE)
	pWarpSeq.AppendAction(pAction)
	pWarpSeq.AddAction(pWarpEnterAction, pMoveAction1)
	if (pPlayer != None) and (pShip.GetObjID() != pPlayer.GetObjID()):
		pAction = App.TGScriptAction_Create(__name__, "SetRandomLocation", pShip)
		pWarpSeq.AddAction(pAction, pWarpEnterAction)
	###
	### If this is the player, add the action that will wait until queued sequences are done ###
	pPrevious = pPreDuringWarpAction
	###
	### Trigger during-warp actions ###
	pWarpSeq.AddAction(pDuringWarp, pPrevious, 0.1)
	###
	### Add sequence for post-during warp actions ###
	###
	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		try:
			iWarpSpeed = WarpFX_GUI.GetWarpSpeed()
		except:
			iWarpSpeed = 7
		iTimeToWarp = App.g_kSystemWrapper.GetRandomNumber(Custom.NanoFXv2Lite.NanoFX_Config.wFX_MaxRandomDistance)
		iTimeToWarp = iTimeToWarp * 9 / iWarpSpeed
		#print "Warp Speed is at Warp " + str(iWarpSpeed) + " ETA is " + str(iTimeToWarp + 5.0) + " seconds"
		### Set Distance so AI ships can Arrive right after you ###
		global g_Distance
		g_Distance = iTimeToWarp
		### Set up ETA Counter ###
		pcDest = None
		pcDestModule = pWarpSeq.GetDestination()
		if (pcDestModule != None):
			pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
			if (pcDest == None):
				pcDest = pcDestModule
		pAction = App.TGScriptAction_Create(__name__, "ETA", "Destination: " + pcDest, 0.02, iTimeToWarp + 4.8, 12)
		pWarpSeq.AddAction(pAction, pDuringWarp)
		pAction = App.TGScriptAction_Create(__name__, "ETA", "Warp Speed: Warp " + str(iWarpSpeed), 0.06, iTimeToWarp + 4.8, 12)
		pWarpSeq.AddAction(pAction, pDuringWarp)
		fCount = iTimeToWarp + 5
		while (fCount > 0):
			pAction = App.TGScriptAction_Create(__name__, "ETA", "ETA: " + str(fCount) + " seconds", 0.10, 0.8, 12)
			pWarpSeq.AddAction(pAction, pDuringWarp, 5 + iTimeToWarp - fCount)
			fCount = fCount - 1
		###			
		pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"), pDuringWarp, iTimeToWarp + 4.5)
		###
	else:
		### AI Ships use this Time to Arrive right after Player Ship ###
		iTimeToWarp = g_Distance - 2.0
		###
	###
	pWarpSeq.AddAction(pPostDuringWarp, pDuringWarp, iTimeToWarp)
	###
	pWarpSeq.AddAction( App.TGScriptAction_Create("WarpSequence", "BridgeCameraForward"), pPostDuringWarp)
	###
###############################################################################
## Dropping out of Warp Captain..... Assemble Exit Warp Sequence
###############################################################################
def ExitWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip):

	### Get the destination set name from the module name, if applicable ###
	pcDest = None
	pcDestModule = pWarpSeq.GetDestination()
	if (pcDestModule != None):
		pcDest = pcDestModule[string.rfind(pcDestModule, ".") + 1:]
		if (pcDest == None):
			pcDest = pcDestModule
	###
	### Setup Sequences ###
	pPostDuringWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_DURING_WARP_SEQUENCE))
	pPostWarp = App.TGSequence_Cast(pWarpSeq.GetWarpSequencePiece(pWarpSeq.POST_WARP_SEQUENCE))
	pDewarpBeginAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_BEGIN_ACTION)
	pDewarpEndAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_END_ACTION)
	pDewarpFinishAction = pWarpSeq.GetWarpSequencePiece(pWarpSeq.DEWARP_FINISH_ACTION)
	pMoveAction2 = pWarpSeq.GetWarpSequencePiece(pWarpSeq.MOVE_ACTION_2)
	pFinalAction = pMoveAction2
	###
	fExitDelayTime = 7.0
	###

	if (App.g_kUtopiaModule.IsMultiplayer() == 0):
		# Add the action for setting the destination placement in the warp subsystem. This
		# has to go after the during-warp action, since mission changing may load new systems.
		pSetPlacementAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetWarpPlacement",
														pShip.GetObjID(), pcDest, pWarpSeq.GetPlacementName())
		pPostDuringWarp.AddAction(pSetPlacementAction)
	else:
		pSet = pWarpSeq.GetDestinationSet()
		fRadius = pShip.GetRadius() * 1.25

		while (1):
			# Set an exit point instead.  Randomly generate an exit point.
			kExitPoint = App.TGPoint3()
			kExitPoint.x = App.g_kSystemWrapper.GetRandomNumber(200)
			kExitPoint.x = kExitPoint.x - 100.0
			kExitPoint.y = App.g_kSystemWrapper.GetRandomNumber(200)
			kExitPoint.y = kExitPoint.y - 100.0
			kExitPoint.z = App.g_kSystemWrapper.GetRandomNumber(200)
			kExitPoint.z = kExitPoint.z - 100.0

			if (pSet == None):
				break
			elif (pSet.IsLocationEmptyTG (kExitPoint, fRadius)):
				pWarpSeq.SetExitPoint(kExitPoint)
				break

		pSetExitPointAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetWarpExitPoint",
														pShip.GetObjID(), pcDest,
														kExitPoint.x, kExitPoint.y, kExitPoint.z)
		pPostDuringWarp.AddAction(pSetExitPointAction)

	# Move the ship from the warp set to the destination set
	# after the warp delay.  If the new set is None, this just
	# deletes the object.
	pPostDuringWarp.AddAction( App.TGScriptAction_Create("WarpSequence", "CheckWarpInPath", pWarpSeq, pShip.GetObjID()), None, pWarpSeq.GetTimeToWarp() )
	pPostDuringWarp.AppendAction(pDewarpBeginAction)
	pPostDuringWarp.AppendAction(pMoveAction2)

	# Add the actions for exiting warp only if the destination set exists.
	if(pWarpSeq.GetDestinationSet() != None):
		fFlashDelay = pWarpSeq.GetTimeToWarp() - 0.5
		if(fFlashDelay < 0.0):
			fFlashDelay = 0.0
		fSwitchSetsDelay = fFlashDelay - 0.1
		if(fSwitchSetsDelay < 0.0):
			fSwitchSetsDelay = 0.0

		# If the player is the one warping, change the rendered set to the
		# player's new set.  Do this before the warp flash is created, so
		# the warp flash sound plays.  Also do it before the warp exit sound,
		# for the same reason.
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			pCRSA2 = App.ChangeRenderedSetAction_Create(pcDestModule)
			pPostDuringWarp.AddAction(pCRSA2, App.TGAction_CreateNull(), fSwitchSetsDelay)

			# Setup a cutscene camera for the destination set.
			pCutsceneCameraBegin = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin",
															 pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera")
			pPostDuringWarp.AddAction(pCutsceneCameraBegin, pCRSA2)

			# Add actions to move the camera in the destination set to watch the placement,
			# so we can watch the ship come in.
			# Initial position is reverse chasing the placement the ship arrives at.
			if (App.g_kUtopiaModule.IsMultiplayer()):
				# Multiplayer watches the exit point rather than the exit placement
				# Create a placement object at the exit point.
				pMPPlacement = App.PlacementObject_Create(pShip.GetName() + "MPWarp1" + str(App.g_kUtopiaModule.GetGameTime()), pcDest, None)
				pMPPlacement2 = App.PlacementObject_Create(pShip.GetName() + "MPWarp2" + str(App.g_kUtopiaModule.GetGameTime()), pcDest, None)

				kPlayerFwd = pPlayer.GetWorldForwardTG()
				pMPPlacement.SetTranslateXYZ(kExitPoint.x, kExitPoint.y + (kPlayerFwd.y * 700.0), kExitPoint.z)
				pMPPlacement2.SetTranslateXYZ(kExitPoint.x, kExitPoint.y, kExitPoint.z)

				# look at where the player will come in
				pCameraAction3 = App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pcDest, pMPPlacement.GetName(), pMPPlacement2.GetName())
				pPostDuringWarp.AddAction(pCameraAction3, pCutsceneCameraBegin)
				# then, look at the player
				pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pcDest, pMPPlacement.GetName(), pPlayer.GetName(), 0)
				pPostDuringWarp.AddAction(pCameraAction4, pMoveAction2)
			else:
				if(pWarpSeq.GetPlacementName() != None):
					fSideOffset = (App.g_kSystemWrapper.GetRandomNumber(700) - 350) / 100.0

					pCameraAction4 = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch",
															   pcDest, pWarpSeq.GetPlacementName())
					pPostDuringWarp.AddAction(pCameraAction4, pCutsceneCameraBegin)
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "AwayDistance", -1.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "ForwardOffset", 3.5))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "SideOffset", fSideOffset))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle1", 70.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle2", 110.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle3", -20.0))
					pPostDuringWarp.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
																		   pWarpSeq.GetDestinationSet().GetName(), "WarpCutsceneCamera", "DropAndWatch",
																		   "SetAttrFloat", "RangeAngle4", 20.0))


		# Create the second warp flash, slightly before the ship gets there.
		pFlashAction2 = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlashEnterSet",
												  pcDestModule, pShip.GetObjID())
		pPostDuringWarp.AddAction(pFlashAction2, App.TGAction_CreateNull(), fFlashDelay)

		# Actions for the de-warping effect. The initiate action happens earlier.
		pPostDuringWarp.AddAction(pDewarpEndAction, pDewarpBeginAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 2.0)
		pPostDuringWarp.AddAction(pDewarpFinishAction, pDewarpEndAction, App.WarpEngineSubsystem_GetWarpEffectTime() / 2.0)

		# Start the warp exit sound
		sRace = Custom.NanoFXv2Lite.NanoFX_Lib.GetSpeciesName(pShip)
		if (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
			pWarpSoundAction2 = App.TGSoundAction_Create(sRace + "ExitWarp")
			pWarpSoundAction2.SetNode(pWarpSet.GetEffectRoot())
		else:
			pWarpSoundAction2	= App.TGSoundAction_Create(sRace + "ExitWarp", App.TGSAF_DEFAULTS, pWarpSeq.GetOrigin().GetName())
			pWarpSoundAction2.SetNode(pShip.GetNode())
		pPostDuringWarp.AddAction(pWarpSoundAction2, App.TGAction_CreateNull(), pWarpSeq.GetTimeToWarp() + 0.70)
		
		### If Ship has Moving Nacelles (Voyager) move them
		try:
			from Custom.AdvancedTechnologies.Data import ATP_Lib
			pMoveNacellesAction = App.TGScriptAction_Create("Custom.AdvancedTechnologies.Data.ATP_Lib", "ForceNacelles", pShip, "Down")
			pPostDuringWarp.AddAction(pMoveNacellesAction, pFlashAction2, 3.0)
		except:
			ERROR = "No ATP3"
		###
	# Drop out of cinematic mode, if we were in cinematic mode.
	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		### Force Full Impulse ###
		pPostDuringWarp.AddAction(App.TGScriptAction_Create(__name__, "SetShipImpulse", pShip, 10.000000, FALSE), pFlashAction2)
		fCount = 0.0
		while (fCount < fExitDelayTime):
			pCoastAction = App.TGScriptAction_Create("Actions.ShipScriptActions", "SetImpulse", pShip.GetObjID(), 0.5)
			pPostDuringWarp.AddAction(pCoastAction, pDewarpFinishAction, fCount)
			fCount = fCount + 0.1
		###	
		pCheckAction = App.TGScriptAction_Create("WarpSequence", "CheckForCameraChange")
		pPostDuringWarp.AddAction(pCheckAction, pDewarpFinishAction, fExitDelayTime)
	###
	# Do post-warp actions.
	pWarpSeq.AddAction(pPostWarp, pPostDuringWarp)

	if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
		pWarpSeq.AddAction(App.TGScriptAction_Create("Bridge.HelmMenuHandlers", "PostWarpEnableMenu"), pPostWarp)
		pWarpSeq.AddAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"), pPostWarp)
		pWarpSeq.AddAction(App.TGScriptAction_Create(__name__, "ResetShipImpulse", pShip, pPlayer), pPostWarp)

###############################################################################
## Assemble the Warp Sequence...
###############################################################################
def NanoWarpSeq(pWarpSeq):

	### Setup ###
	pShip    = pWarpSeq.GetShip()
	pPlayer  = App.Game_GetCurrentPlayer()
	pWarpSet = App.WarpSequence_GetWarpSet()
	###
	### If not a Ship... Bail! ###
	if (pShip == None):
		return
	###
	### Picard says:  Engage! ###
	EngageWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip)
	###
	### We are Warping!!!!!
	DuringWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip)
	###
	### Dropping Out of Warp ###
	ExitWarpSeq(pWarpSeq, pWarpSet, pPlayer, pShip)
	###
	
	
###############################################################################
#	WarpFlash(pAction, iShipID, fTime)
#	
#	Creates the warp flash. Should be called before the ship leaves its
#	current set.
#	
#	Args:	pAction			- the action, passed in automatically
#			iShipID			- the ID of the ship being affected
#			fTime			- the amount of time the flash should take
#	
#	Return:	zero for end.
###############################################################################
def WarpFlash(pAction, iShipID, fTime = None):
	"Creates a warp flash."

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if (pShip == None):
		return(0)

	# fixes problem where ships get orphaned if the mission is terminated
	# while they're warping.
	if (pShip.GetContainingSet() == None):
		return(0)

	if (fTime != None):
		pFlash = App.WarpFlash_Create(pShip, fTime)
	else:
		pFlash = App.WarpFlash_Create(pShip)

	return(0)

###############################################################################
#	WarpFlashEnterSet(pAction, pcSetName, iShipID, fTime = None)
#	
#	Creates a warp flash for a ship entering a set. Queries the ship as to
#	where it will be exiting warp, and the rotation, etc. so we know where
#	to place the flash.
#	
#	Args:	pAction			- the action, passed in automatically
#			pcSetName		- the name of the module for the destination set
#			iShipID			- the ID of the ship being affected
#			fTime			- the amount of time the flash should take
#	
#	Return:	zero for end.
###############################################################################
def WarpFlashEnterSet(pAction, pcSetName, iShipID, fTime = None):
	"Creates a warp flash for a ship entering a set."

#	kDebugObj.Print("WarpFlashEnterSet(): " + pcSetName)

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if (pShip == None):
		return(0)

	pSetModule = __import__(pcSetName)
	pSet = pSetModule.GetSet()

	if (pSet == None):
#		kDebugObj.Print("WarpFlashEnterSet(): no set")
		return(0)

	pWarp = pShip.GetWarpEngineSubsystem()

	if (pWarp == None):
#		print "In WarpFlashEnterSet(): no warp engine subsystem for use"
		return(0)

	pLocation = pWarp.GetWarpExitLocation()
	pRotation = pWarp.GetWarpExitRotation()
	fRadius = pShip.GetRadius()

	if (fTime == None):
		pFlash = App.WarpFlash_CreateWithoutShip(pSet, pLocation, pRotation, fRadius)
	else:
		pFlash = App.WarpFlash_CreateWithoutShip(pSet, pLocation, pRotation, fRadius, fTime)

	return(0)
	
###############################################################################
#	HideShip(pAction, iShipID)
#	
#	Hides a ship. Used to mask the ship during the warp flash.
#	
#	Args:	pAction	- the action
#			iShipID	- the ID of the ship
#	
#	Return:	zero for end
###############################################################################
def HideShip(pAction, iShipID, iHide):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
	if pShip:
		pShip.SetHidden(iHide)

	return 0
	
def DebugCutscene(pAction):
	
	print "I am here"
	return 0
###############################################################################
## Set a Random Location
###############################################################################
def SetRandomLocation(pAction, pShip):
	
	vPoint = App.TGPoint3()
	vPoint.SetX(App.g_kSystemWrapper.GetRandomNumber(71) - 35)
	vPoint.SetY(App.g_kSystemWrapper.GetRandomNumber(71) - 35)
	vPoint.SetZ(App.g_kSystemWrapper.GetRandomNumber(71) - 35)

	pShip.SetTranslate(vPoint)
	pShip.UpdateNodeOnly()
	
	return 0	
	
###############################################################################
## Force Impulse Settings for a Good "Show"
###############################################################################
def SetShipImpulse(pAction, pShip, fAccel, bBackupSettings = 1):
	
	if (pShip):
		
		pImpulse = pShip.GetImpulseEngineSubsystem().GetProperty()

		if (bBackupSettings == 1):
			global g_ShipSpeed
			global g_ShipAccel		
		
			g_ShipSpeed = pImpulse.GetMaxSpeed()
			g_ShipAccel = pImpulse.GetMaxAccel()
	
		pImpulse.SetMaxSpeed(7.000000)
		pImpulse.SetMaxAccel(fAccel)

	return 0
###############################################################################
## Reset our Impulse Settings
###############################################################################
def ResetShipImpulse(pAction, pShip, pPlayer):
	
	if (pShip):
		pImpulse = pShip.GetImpulseEngineSubsystem().GetProperty()
		
		pImpulse.SetMaxSpeed(g_ShipSpeed)
		pImpulse.SetMaxAccel(g_ShipAccel)
		
		if pPlayer and (pShip.GetObjID() == pPlayer.GetObjID()):
			pTop = App.TopWindow_GetTopWindow()
			pTop.ForceBridgeVisible()
		
	return 0

def InitWarpSetLighting(sSetName): 
   # Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3.816000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.100000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.844013, 0.398183, 0.359295)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.510363, 0.390388, 0.766242)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.900000, 0.900000, 0.600000, 0.200000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"
	
	# Light position "Directional Light 2"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-7.561178, -13.532564, -0.087336)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.808193, 0.132823, -0.573744)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.532103, 0.582186, -0.614757)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.800000, 0.700000, 0.700000, 0.600000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light 2"
   
###############################################################################
## End of WarpFX
###############################################################################