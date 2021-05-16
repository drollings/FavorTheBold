#########################################################################################################################
#### ADVANCED TECHNOLOGIES 3												#
#### MADE BY Alexis Rombaut aka Apollo 											#	
#### (c) 30/09/2003													#
####															#
#### Contact: Alexis.Rombaut@skynet.be											#
#########################################################################################################################

#########################################################################################################################
#	In order to recognize whether a ship has a certain technology we introduce a code, based on the			#
#	affilliation number (ShipProperty -> Affiliation in the Model Property Editor)					#
#															#
#															#
#	Structure of the AffilationNumber 										#
#	YYYYYYYYYY are diffent control numbers assigned for various assets as multivectral shielding,			#
#	ablative armour, breen drain weapon ...										#
#															#
#	current reference: AffilationNumber = ...JIHGFEDCBA								#
#															#
#	Breen Weapon: Implicit (launch sound of the torpedo must be "BreenTorpedoXL")					#
#	Ion Cannon: Implicit (launch sound of the pulse must be "Ion" or "IonHigh" or "IonLow")				#
#															#
#															#
#	A: Multivectral Shielding (Type 1 -> positionSelectorShip(pObject,1))						#
#		0: Off													#
#		1: On													#
#															#
#	B:Immune to Drainerweapon											#
#		0: No													#
#		1: Yes													#
#															#
#	C:Ablative Armour												#
#		AUTO													#	
#															#
#	D: Phase Cloak													#
#		AUTO													#		
#															#
#	E:Corbinite Reflector												#
#		0: No													#
#		1: Cast back torpedoes											#
#		2: Cast back torpedoes and disruptors									#
#															#
#	F:FREE														#
#															#
#	G:Life Support													#
#		AUTO													#
#########################################################################################################################
#########################################################################################################################
#	Torpedo Decoding Version 6											#
#															#
#	SpreadType:													#
#															#
#		0 - 	Normal Behaviour										#
#															#
#		1 - 	Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target#
#		    	The type of splitting is defined by SplitType. The spread starts after SpreadDelay seconds. 	#
#			The shape of the new projectiles is defined by SecondPath, default the same type of projectile.	#
#			If ShellPersist is set the original torpedo continues its course.				#
#															#
#		2 - 	Will scatter into a number of subtorpedoes specified by SpreadNumber, directed at different	#
#		    	targets. The spread starts after SpreadDelay seconds. The shape of the new projectiles is	#
#			defined by SecondPath, default the same type of projectile.					#
#			If ShellPersist is set the original torpedo continues its course.				#
#															#
#		3 - 	Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is	#
#			set friendly ships are aswell affected. No damage is applied, yet a yield is simulated and	#
#			executed e.g. an ion effect. The explosion starts after SpreadDelay seconds.			#
#			If ShellPersist is set the original torpedo continues its course.				#
#															#											#
#		4 - 	Will convert into a mine that deploys in SpreadDelay seconds, with a model specified by		#
#			SecondPath. Any ship that comes in SpreadRadius of the mine, will make it explode. If		#
#			SpreadSplash is set, allied and the firing ship can trigger the mine aswell.			#
#															#
#		5 - 	Will convert into a rocket with a model specified by SecondPath.				#
#															#
#		General:												#
#			ShellLive:	0 - The shell torpedo is removed after spreading				#
#					1 - The shell torpedo continues moving						#
#															#
#		Specific:												#
#			SpreadNumber: 	x - Number of subtorpedoes created						#
#															#
#			SecondPath:	Defines the tactical/projectiles/ path of the subtorpedoes			#
#					eg "Tactical.Projectiles.subMyTorpedo" OR					#
#					the "Ships/" path for shipmodels						#
#					eg "ATP_Rocket" !!! No "Ships." in this modelstring !!				#
#															#
#			SpreadDelay	x - Time(sec) before the torpedoes starts spreading				#
#															#
#			SplitType: 	0 - Nothing									#
#					1 - Conical Spread, SpreadDensity determines the inverse conical aperture	#
#					2 - Circular Spread, SpreadAngle(°) determines the angle of the circlesector	#
#															#
#			SpreadRadious:	x - the range in km of the wavetorpedo/mine					#
#															#
#			SpreadSplash:	0 - Allied ships not affected/trigger						#
#					1 - Allied ships affected/ trigger						#
#															#
#			ShellPersist:	0 - The Shell Torpedo is removed after spreading				#
#					1 - The Shell Torpedo remains and continues					#
#															#
#	ImpactType:													#
#		0 - Normal Behaviour											#
#		1 - Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
#		    that the torpedo isn't bounced									#
#		2 - Phased Torpedo - You need to create a shelltorpedo script with little damage (like 0.001) and	#
#		    ImpactType 2 set. Define a string SecondPath indicating the real torpedo script with the actual	#
#		    damage. That torpedo must NOT be set at ImpactType=2 or you might create on infinite loop(=crash). 	#
#		BounceYield:	x - torpedodamage is multiplied with this factor					#
#		BounceFail:	x - 1 on x chance that the weapon is absorbed						#
#															#
#															#
#	YieldType:													#
#		0 - Normal Behaviour											#
#		1 - Special Behaviour:											#
#			DrainerWeapon:		0 - Not active								#
#						1 - Targets shields and powercore fails					#
#			SensorBlast:		0 - Not active								#
#						1 - Sensors disabled for SensorDisabledTime seconds			#
#			ShieldDisruptor:	0 - Not active								#
#						1 - Target shields are disrupted for ShieldDisabledTime seconds		#
#			EngineJammer:		0 - Not active								#
#						1 - Target Engines are disabled for EngineDisabledTime seconds		#
#			IonCannon:		0 - Not active								#
#						1 - Random Subtarget disabled for IonCannonDisabledTime seconds		#
#						    with a 1 on IonCannonMiss to have no effect. The effect is executed #
#						    IonFrequency times.				 			#
#			CloakBurn:		0 - Not active								#
#						1 - Target CloakingSys is disabled for CloakDisabledTime seconds	#
#			PhalaniumWave:		0 - Not ACtive								#
#						1 - The Effect designed by DreamYards, now compatible with NanoFX	#
#			SpatialCharges:		0 - Not ACtive								#
#						1 - The Effect designed by Sneaker, now compatible with NanoFX		#
#															#
#	DepleteType:													#
#		0 - Normal Behaviour											#
#		1 - Torpedo will lose damage each second with a factor (100-DepletionPerSecond(in %))%, untill the	#
#		    damage is reduced to DepletedAtPercentage of the original damage.					#
#		GraphicsTuple: Set containing the grahical info about the torpedo					#
#		DepleteColour: 	0 - Not active										#
#			 	1 - The colour changes from green to red, while flying					#
#		DepleteShrink: 	0 - Not active										#
#			 	1 - The torpedo shrinks, while flying							#
#															#
#########################################################################################################################

import App

import math
import time

import MissionLib
import QuickBattle.QuickBattle

from GUI import ATP_GUIMain
from GUI import ATP_WeaponsControl
from GUI import ATP_PowerDisplay
from GUI import ATP_ShipDisplay
from BridgeFX import ATP_BridgeFX
from Actions import ATP_ActionDecoder
from AI import ATP_QuickBattleFriendlyAI
from AI import ATP_QuickBattleAI

from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

FALSE=0
TRUE=1

g_StatusDict	= {}
g_fTractorStartFiring	= 0.0
g_fTractorStartFiringList= []
g_tIon = {}
g_SpecialActive={}
pTimer=None
pTimer2=None
pTimer4=None
g_lifeList=[]
g_cloakList=[]
g_antiCloakList=[]
g_acTorpList=[]
g_spreadHandleList=[]
g_depleteHandleList=[]
g_FeedBackDict={}
g_RocketDict = {}

g_ArmourBarDict={}
g_specialPowerDict={}

g_lifeSound=0
g_sneakerPlasmaCheck=0
g_sneakerPlasmaConstant=0

TIME_START=0.0
TIME_USED=0.0
TORPEDOES_FIRED=0
WEAPON_HITS=0
WEAPON_DAMAGE=0.0
TIMES_CLOAKED=0
TRACTORS_FIRED=0

ET_CYCLE_CHECK	= App.Mission_GetNextEventType()
ET_CYCLE_CHECK2	= App.Mission_GetNextEventType()
ET_CYCLE_CHECK4	= App.Mission_GetNextEventType()
ET_SPECIAL_POWER_GUI = App.Mission_GetNextEventType()

CT_QUICKBATTLE_MODE	= FALSE
CT_TPE_MODE		= FALSE
CT_FTB_MODE		= FALSE
CT_MPMP_MODE		= FALSE
CT_EXTERN_MODE		= FALSE
CT_NANOFX_MODE		= FALSE
CT_UNIVERSE_MODE	= FALSE

MULTIVECTRAL_SHIELDS=1
MULTIVECTRAL_SHIELDS_OFF=2
MULTIVECTRAL_SHIELDS_II=3
MULTIVECTRAL_SHIELDS_II_OFF=4
IMMUNE_TO_DRAINER_WEAPON=5
ABLATIVE_ARMOUR=6
ABLATIVE_ARMOUR_OFF=7
PHASE_CLOAK=8
PHASE_CLOAK_OFF=9
CORBONITE_REFLECTOR=20
CORBONITE_REFLECT_STD=10
CORBONITE_REFLECT_STD_OFF=11
CORBONITE_REFLECT_EXT=12
CORBONITE_REFLECT_EXT_OFF=13
CORBONITE_DEFLECT_STD=14
CORBONITE_DEFLECT_STD_OFF=15
CORBONITE_DEFLECT_EXT=16
CORBONITE_DEFLECT_EXT_OFF=17
LIFE_SUPPORT=18
LIFE_SUPPORT_OFF=19
HIT_BY_DRAINER_WEAPON=21

PHASECLOAK_DRAIN=50.0
CORBONITE_REFLECTOR_DRAIN=50.0

DEBUG=FALSE
DEBUGION=FALSE
DEBUG_ERROR=FALSE



#########################################################################################################################
#	Advanced Technologies Importer											#								#
#															#
#	importAdvancedTechnologies():											#
#		Call the ATP for any mission by adding these two lines, when you setup the EventHandlers:		#
#															#
#		import Custom.AdvancedTechnologies.Data.QuickBattleAddon						#
#		Custom.AdvancedTechnologies.Data.QuickBattleAddon.importAdvancedTechnologies()				#
#															#
#	importAdvancedTechnologiesForMPMP:										#
#		Special function for the MPMP Mode									#
#															#
#	SetupEventHandlers():												#
#		This is the replacement for the EventHandlers,specific for QuickBattle.py				#
#															#
#															#
#########################################################################################################################
def welcomeMessage():
	print "Advanced Technologies 3 Enabled"
	if CT_EXTERN_MODE:
		print "\tExternal Import succesful"
	if CT_QUICKBATTLE_MODE:
		print "\tQuickBattle Mode Activated"
	if CT_MPMP_MODE:
		print "\tMultiplayer Mode Activated"
	if CT_NANOFX_MODE:
		print "\tNanoFX Joined Venture Activated"


def importAdvancedTechnologiesForMPMP():
	global CT_QUICKBATTLE_MODE
	global CT_MPMP_MODE
	global CT_EXTERN_MODE
	global CT_NANOFX_MODE

	CT_QUICKBATTLE_MODE=FALSE
	CT_MPMP_MODE=TRUE
	CT_EXTERN_MODE=TRUE
	
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT,			pMission, __name__ + ".WeaponHit"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING,		pMission, __name__ + ".CloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING,		pMission, __name__ + ".DecloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, 	pMission, __name__ + ".TractorStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, 	pMission, __name__ + ".TractorEnded"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED, 		pMission, __name__ + ".TorpedoLose"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED,		pMission, __name__ + ".ShipCreated"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION,		pMission, __name__ + ".Collision"	)

	#The game didn't provide proper garbage collection
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME,App.Game_GetCurrentGame(), __name__ + ".Terminate")

	global pTimer
	pTimer = MissionLib.CreateTimer(ET_CYCLE_CHECK, __name__ + ".CycleHandle",App.g_kUtopiaModule.GetGameTime(), 1, -1)
	try:
		import Custom.NanoFX.NanoFX_Lib
		CT_NANOFX_MODE=TRUE
	except:
		CT_NANOFX_MODE=FALSE
	
	welcomeMessage()
	


def importAdvancedTechnologies():
	global CT_QUICKBATTLE_MODE
	global CT_MPMP_MODE
	global CT_EXTERN_MODE
	global CT_NANOFX_MODE

	CT_QUICKBATTLE_MODE=FALSE
	CT_MPMP_MODE=FALSE
	CT_EXTERN_MODE=TRUE

	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT,			pMission, __name__ + ".WeaponHit"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING,		pMission, __name__ + ".CloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING,		pMission, __name__ + ".DecloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, 	pMission, __name__ + ".TractorStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, 	pMission, __name__ + ".TractorEnded"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED, 		pMission, __name__ + ".TorpedoLose"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED,		pMission, __name__ + ".ShipCreated"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION,		pMission, __name__ + ".Collision"	)

	App.g_kEventManager.AddBroadcastPythonFuncHandler(ATP_WeaponsControl.GetOffEvent(),pMission,__name__+".CorboniteWentOff")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ATP_WeaponsControl.GetOnEvent(),pMission,__name__+".CorboniteWentOn")

	#The game didn't provide proper garbage collection
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME,App.Game_GetCurrentGame(), __name__ + ".Terminate")
	
	global pTimer
	pTimer = MissionLib.CreateTimer(ET_CYCLE_CHECK, __name__ + ".CycleHandle",App.g_kUtopiaModule.GetGameTime(), 1, -1)
	try:
		from Custom.NanoFX import NanoFX_Lib
		CT_NANOFX_MODE=TRUE
	except:
		CT_NANOFX_MODE=FALSE

	welcomeMessage()
	
	
def SetupEventHandlers():
	global CT_QUICKBATTLE_MODE
	global CT_MPMP_MODE
	global CT_EXTERN_MODE
	global CT_NANOFX_MODE

	CT_QUICKBATTLE_MODE=TRUE
	CT_MPMP_MODE=FALSE
	CT_EXTERN_MODE=FALSE
	
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, pMission, "QuickBattle.QuickBattle.ShipDestroyed")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission,"QuickBattle.QuickBattle.ShipExploding")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(QuickBattle.QuickBattle.ET_PRELOAD_DONE, pMission,"QuickBattle.QuickBattle.StartSimulation2")

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT,			pMission, __name__ + ".WeaponHit"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING,		pMission, __name__ + ".CloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING,		pMission, __name__ + ".DecloakStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, 	pMission, __name__ + ".TractorStarted"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, 	pMission, __name__ + ".TractorEnded"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED, 		pMission, __name__ + ".TorpedoLose"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED,		pMission, __name__ + ".ShipCreated"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED,		pMission, __name__ + ".LaunchUniverse"	)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION,		pMission, __name__ + ".Collision"	)
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ATP_WeaponsControl.GetOffEvent(),pMission,__name__+".CorboniteWentOff")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ATP_WeaponsControl.GetOnEvent(),pMission,__name__+".CorboniteWentOn")

	#The game didn't provide proper garbage collection
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_GAME,App.Game_GetCurrentGame(), __name__ + ".Terminate")

	global pTimer
	pTimer = MissionLib.CreateTimer(ET_CYCLE_CHECK, __name__ + ".CycleHandle",App.g_kUtopiaModule.GetGameTime(), 1, -1)	
	try:
		import Custom.NanoFX.NanoFX_Lib
		CT_NANOFX_MODE=TRUE
	except:
		CT_NANOFX_MODE=FALSE

	
	welcomeMessage()	
	

def PreResetATP():
	#Reset the globals
	ResetGlobals()

	#Initialise the Action & GUI & BridgeFX Module & Universe
	ATP_ActionDecoder.Initialise()
	ATP_GUIMain.Initialise()
	ATP_BridgeFX.Initialise()	

def PostResetATP():
	#Setup Up the Buttons
	ATP_GUIMain.Setup()	

def Terminate(pGame,pEvent):
	pass

def ResetGlobals():
	global g_StatusDict
	global g_fTractorStartFiringList
	global g_tIon
	global g_lifeList
	global g_cloakList
	global g_spreadHandleList
	global g_depleteHandleList
	global g_lifeSound
	global g_sneakerPlasmaCheck
	global g_sneakerPlasmaConstant
	global g_SpecialActive
	global g_FeedBackDict
	global g_RocketDict

	global TORPEDOES_FIRED
	global WEAPON_HITS
	global WEAPON_DAMAGE
	global TIMES_CLOAKED
	global TRACTORS_FIRED

	g_StatusDict = {}
	g_fTractorStartFiringList= []
	g_SpecialActive ={}
	g_tIon = {}
	g_lifeList=[]
	g_cloakList=[]
	g_spreadHandleList=[]
	g_depleteHandleList=[]
	g_lifeSound=0
	g_sneakerPlasmaCheck=0
	g_sneakerPlasmaConstant=0
	g_specialPowerDict={}
	g_FeedBackDict={}
	g_RocketDict = {}
	
	TORPEDOES_FIRED=0
	WEAPON_HITS=0
	WEAPON_DAMAGE=0.0
	TIMES_CLOAKED=0
	TRACTORS_FIRED=0
	

#########################################################################################################################
#	Advanced Technologies Main Event Decoder									#
#															#
#	Calls the various functions for each EventFunction								#
#															#
#															#
#########################################################################################################################

def LaunchUniverse(pMission,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return
	pPlayer=MissionLib.GetPlayer()
	if pPlayer:
		if pShip.GetObjID()==pPlayer.GetObjID():
			import Universe.ATP_UniverseGame
			Universe.ATP_UniverseGame.Launch()
	

def ShipCreated(pMission,pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle SHIP start")
	
	#if not pEvent.GetDestination():
	#	return

	pShip=App.ShipClass_Cast(pEvent.GetDestination())

	if not pShip or CT_MPMP_MODE:
		#debug("cycle SHIP leave")
		return

	if DEBUG_ERROR:
		debug("cycle SHIP A")
		pass

	pPlayer=MissionLib.GetPlayer()
	if pPlayer:
		if pShip.GetObjID()==pPlayer.GetObjID():
			PreResetATP()

	if DEBUG_ERROR:
		debug("cycle SHIP B")
	

	ATP_ActionDecoder.Decode(pMission,pEvent)

	if DEBUG_ERROR:
		debug("cycle SHIP start C")

	createNewEntryForSpecialPower(pShip)

	if DEBUG_ERROR:
		debug("cycle SHIP start D")

	ATP_SelfDecode(pMission,pEvent)

	if DEBUG_ERROR:
		debug("cycle SHIP start E")

	if DEBUG_ERROR:
		debug("cycle SHIP start F ")

	if pPlayer:
		if pShip.GetObjID()==pPlayer.GetObjID():
			PostResetATP()

	if DEBUG_ERROR:
		debug("cycle SHIP end")
	

def MPMPShipCreated(pMission,pEvent):
	return

	ID = pEvent.GetPlayerID ()
	if not ID:
		return

	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	pShip = pGame.GetShipFromPlayerID(ID)
	
	if not pShip:
		return

	createNewEntryForSpecialPower(pShip)	

	

def CycleHandle(TGObject,pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle main start")
	#Beam Effects
	inversionBeamMain(TGObject,pEvent)
	UCBMain(TGObject,pEvent)
	techAssimilationBeamMain(TGObject,pEvent)
	shipAssimilationBeamMain(TGObject,pEvent)
	
	#Critical Systems Listener
	lifeSupportCycle(TGObject,pEvent)
	
	#Torpedo Spread & Deplete Effect
	cycleSpreadType1(TGObject,pEvent)
	cycleSpreadType2(TGObject,pEvent)
	cycleRocket	(TGObject,pEvent)
	cycleDepleteType(TGObject,pEvent)
		
	#Disabled Subsystems Control
	if DEBUG_ERROR:
		debug("cycle ION start")
	cycleDisable(TGObject, pEvent)
	if DEBUG_ERROR:
		debug("cycle ION end")

	#Special Power Control
	# if not CT_MPMP_MODE:
	#	CycleAdjustSpecialPower(TGObject,pEvent)
	#	cycleSpecialPower(TGObject,pEvent)
	
	#Cycle GUI
	# if not CT_MPMP_MODE:
	#	ATP_GUIMain.CycleHandle(TGObject,pEvent)

	#Cycle Actions
	if not CT_MPMP_MODE:
		ATP_ActionDecoder.CycleHandle(TGObject,pEvent)
	
	TGObject.CallNextHandler(pEvent)
	if DEBUG_ERROR:
		debug("cycle main end")


def WeaponHit(pObject, pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle HIT start")

	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	#Defensive Actions
	multiVectralShields(pShip,pEvent)
	ablativeArmour(pShip)
	corboniteReflector(pObject,pEvent)

	PhaserHit(pObject,pEvent)
	
	#Critical Systems Listener
	lifeSupportHit(pObject,pEvent)

	#Offensive Actions
	YieldTypeDecoder(pObject,pEvent)
	ImpactTypeDecoder(pObject,pEvent)
	
	## Rockethit catch
	RocketHitWeapon(pObject,pEvent)
	
	pObject.CallNextHandler(pEvent)
	if DEBUG_ERROR:
		debug("cycle HIT end")

def Collision(pMission,pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle COLL start")

	## Delete a rocket that hit a target
	RocketHitCollision(pMission,pEvent)

	pMission.CallNextHandler(pEvent)

	if DEBUG_ERROR:
		debug("cycle COLL end")

def TorpedoLose(pObject, pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle TORP start")

	#Spread Initiator	
	SpreadTypeDecoder(pObject,pEvent)
	
	#Depletion Initiator
	DepleteTypeDecoder(pObject,pEvent)
	
	pObject.CallNextHandler(pEvent)

	if DEBUG_ERROR:
		debug("cycle TORP end")


def CloakStarted(pObject, pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle CLOAK start")

	# Called when a ship cloaks
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	phaseCloakOn(pShip)

	pObject.CallNextHandler(pEvent)
	if DEBUG_ERROR:
		debug("cycle CLOAK end")

def DecloakStarted(pObject,pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle DECLOAK start")

	# Called when a ship decloaks
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	phaseCloakOff(pShip)

	#MPMP forced 2 second cloakpause
	if CT_MPMP_MODE:
		enforceCloakPause(pObject,pEvent)
	

	pObject.CallNextHandler(pEvent)
	if DEBUG_ERROR:
		debug("cycle DECLOAK end")

def TractorStarted(pObject, pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle TRACT start")

	#Beam Initiated
	TractorStart(pObject,pEvent)

	pObject.CallNextHandler(pEvent)

	if DEBUG_ERROR:
		debug("cycle TRACT end")


def TractorEnded(pObject, pEvent):
	return

	if DEBUG_ERROR:
		debug("cycle TRACTE start")

	#Beam Ended
	TractorEnd(pObject,pEvent)
	
	pObject.CallNextHandler(pEvent)
	if DEBUG_ERROR:
		debug("cycle TRACTE end")

	
#########################################################################################################################
#	Advanced Technologies Functions											#
#															#
#	The various functions implementing each AT									#
#															#
#															#
#########################################################################################################################

def ATP_SelfDecode(pMission,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())

	found=FALSE
	pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Ablative Armour"):
			if(pSubsystem.GetCondition()>0.0):
				found=TRUE
			break
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)

	if found and positionSelectorShip(pShip,3)==0:
		pAff=pShip.GetAffiliation()
		pAff=pAff+100
		pShip.SetAffiliation(pAff)


	found=FALSE
	pIterator = pShip.StartGetSubsystemMatch(App.CT_CLOAKING_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Phase Cloak"):
			if(pSubsystem.GetCondition()>0.0):
				found=TRUE
			break
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)

	if found and positionSelectorShip(pShip,4)==0:
		pAff=pShip.GetAffiliation()
		pAff=pAff+1000
		pShip.SetAffiliation(pAff)


	found=FALSE
	pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Life Support"):
			if(pSubsystem.GetCondition()>0.0):
				found=TRUE
			break
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)

	if found and positionSelectorShip(pShip,7)==0:
		pAff=pShip.GetAffiliation()
		pAff=pAff+1000000
		pShip.SetAffiliation(pAff)

	## Create an entry in the status dict
	global g_StatusDict
	g_StatusDict[pShip.GetObjID()] = 0x00000000

	## Modify the flags
	if positionSelectorShipBoolean(pShip,1,1):
		SetFlag(pShip,MULTIVECTRAL_SHIELDS)
	elif positionSelectorShipBoolean(pShip,1,2):
		SetFlag(pShip,MULTIVECTRAL_SHIELDS_II)
	
	if positionSelectorShipBoolean(pShip,2,1):
		SetFlag(pShip,IMMUNE_TO_DRAINER_WEAPON)

	if positionSelectorShipBoolean(pShip,3,1):
		SetFlag(pShip,ABLATIVE_ARMOUR)
	
	if positionSelectorShipBoolean(pShip,4,1):
		SetFlag(pShip,PHASE_CLOAK)

	if positionSelectorShipBoolean(pShip,5,1):
		SetFlag(pShip,CORBONITE_REFLECT_STD)
	elif positionSelectorShipBoolean(pShip,5,2):
		SetFlag(pShip,CORBONITE_REFLECT_EXT)
	elif positionSelectorShipBoolean(pShip,5,3):
		SetFlag(pShip,CORBONITE_DEFLECT_STD)
	elif positionSelectorShipBoolean(pShip,5,4):
		SetFlag(pShip,CORBONITE_DEFLECT_EXT)

	if positionSelectorShipBoolean(pShip,7,1):
		SetFlag(pShip,LIFE_SUPPORT)	

def multiVectralShields(pShip,pEvent):
	if not (positionSelectorShipBoolean(pShip,1,1)):    #Check if the ship is scripted to have multivectral shields
		return

	pShields = pShip.GetShields()		
	if (pShields != None):
		pShieldTotal=0.0
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
			pShieldTotal=pShieldTotal+pShields.GetCurShields(ShieldDir)
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			pShields.SetCurShields(ShieldDir,pShieldTotal/6.0)  		#Redistribute shields equally



def ablativeArmour(pShip):
	return

	if(positionSelectorShip(pShip,3)==1):
		repair=FALSE			
		pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		while (pSubsystem != None):
			if(pSubsystem.GetName()=="Ablative Armour"):
				if(pSubsystem.GetCondition()>0.0):
					repair=TRUE
				break
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		pShip.EndGetSubsystemMatch(pIterator)

		if not repair:
			global g_ArmourBarDict
			if g_ArmourBarDict.keys().count(pShip.GetObjID())>0:
				#print "Armour Destroyed, Setting Normal Bar"
				
				pPane=g_ArmourBarDict[pShip.GetObjID()]
				kFillColor = App.TGColorA()
				kFillColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
				kEmptyColor = App.TGColorA()
				kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r,App.g_kSubsystemEmptyColor.g,App.g_kSubsystemEmptyColor.b,App.g_kSubsystemEmptyColor.a)

				pPane.SetFillColor(kFillColor)
				pPane.SetEmptyColor(kEmptyColor)
				pPane.SetObject(pShip.GetHull())
				
				del g_ArmourBarDict[pShip.GetObjID()]
	
		if repair:
			# Repair everything instantly except the ablative armour property

			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			while (pSubsystem != None):
				if(pSubsystem.GetName() != "Ablative Armour"):
					if(pSubsystem.GetCondition()>0.0):
						pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
						iChildren = pSubsystem.GetNumChildSubsystems()
						if (iChildren > 0):
							for iIndex in range(iChildren):
								pChild = pSubsystem.GetChildSubsystem(iIndex)
								pChild.SetCondition(pChild.GetMaxCondition())
					
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
			pShip.EndGetSubsystemMatch(pIterator)


def phaseCloakOn(pShip):
	global g_cloakList

	if CheckFlag(pShip,PHASE_CLOAK):
		pShip.RunDeathScript()

	if not(positionSelectorShip(pShip,4)>=1.0):
		g_cloakList.append(pShip.GetObjID())
		return

	App.DamageableObject_Cast(pShip).SetCollisionsOn(FALSE)	#Set collisions off, so simple !!!
	pCloakingSys = pShip.GetCloakingSubsystem()
	pSound = App.g_kSoundManager.GetSound("PhaseCloakOn")
	if pSound:
		pSound.Play()

	global g_SpecialActive
	g_SpecialActive[pShip.GetObjID(),PHASE_CLOAK]=60.0

			
def phaseCloakOff(pShip):
	global g_cloakList
	try:
		g_cloakList.remove(pShip.GetObjID())
	except:
		pass

	if(positionSelectorShip(pShip,4)>=1):
		App.DamageableObject_Cast(pShip).SetCollisionsOn(TRUE)		#Set collisions on, so simple !!!
		pCloakingSys = pShip.GetCloakingSubsystem()
		pSound = App.g_kSoundManager.GetSound("PhaseCloakOff")
		if pSound:
			pSound.Play()

	global g_SpecialActive
	if g_SpecialActive.has_key(pShip.GetObjID(),PHASE_CLOAK):
		del g_SpecialActive[pShip.GetObjID(),PHASE_CLOAK]

def SetPhaseCloakOff(pShip):
	IonSubSystem(pShip.GetCloakingSubsystem(),10.0)
	


def enforceCloakPause(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if pShip==None:
		return

	pCloak=pShip.GetCloakingSubsystem()
	if pCloak==None:
		return
	
	iChildren = pCloak.GetNumChildSubsystems()
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pCloak.GetChildSubsystem(i)
			IonSubSystem(pChild,4.0)
	else:
		IonSubSystem(pCloak,4.0)


def PhaserHit(pObject,pEvent):
	return

	global g_FeedBackDict
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	if pEvent.IsHullHit():
		return
	if not pEvent.GetWeaponType()==pEvent.PHASER:
		return
	
	pPhaserBank=App.PhaserBank_Cast(pEvent.GetSource())

	kVectNiWorldHitPoint=pEvent.GetWorldHitPoint()									
	kX=App.TGPoint3()			
	kX.SetXYZ(kVectNiWorldHitPoint.x,kVectNiWorldHitPoint.y,kVectNiWorldHitPoint.z)

	kY=pPhaserBank.GetWorldLocation()

	kY.Subtract(kX)
	kY.Unitize()

	pTorp=FireTorpFromPointWithVector(kX,kY,"Custom.AdvancedTechnologies.Projectiles.FeedBackTorpedo",pAttacker.GetObjID(),pShip,500.0,pPhaserBank.GetPositionTG())
	if not g_FeedBackDict.has_key(pPhaserBank.GetObjID()):
		pList=[]
		pList.append(pTorp.GetObjID())
		g_FeedBackDict[pPhaserBank.GetObjID()]=pList
	else:
		g_FeedBackDict[pPhaserBank.GetObjID()].append(pTorp.GetObjID())


def FeedBackRemoval(pObject,pEvent):
	return

	global g_FeedBackDict
	pPhaserBank=App.PhaserBank_Cast(pEvent.GetSource())
	if not pPhaserBank:
		return
	if not g_FeedBackDict.has_key(pPhaserBank.GetObjID()):
		return
	for ID in g_FeedBackDict[pPhaserBank.GetObjID()]:
		pTorp=App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(ID))
		if pTorp:
			pTorp.SetLifetime(0.0)
	del g_FeedBackDict[pPhaserBank.GetObjID()]
	
			



def corboniteReflector(pObject,pEvent):
	pTorp= App.Torpedo_Cast(pEvent.GetSource())
	if not pTorp:
		return
	
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	iAff=positionSelectorShip(pShip,5)

	
	if pEvent.IsHullHit():
		return

	if IsPhasedHit(pTorp):
		return

	if IsDrainerHit(pTorp):
		return	

	if not iAff>=1:
			return
	
	if iAff>=5:
		if not HasSufficientSpecialPower(pShip,80.0):
			return
	else:
		if not pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
			if HasSufficientSpecialPower(pShip,400.0):
				SetCorboniteOn(pShip)
			else:
				return
		else:
			return

	pTorpPath=pTorp.GetModuleName()
	life=pTorp.GetGuidanceLifeTime()

	iAff=positionSelectorShip(pShip,5)

	if (iAff==5 or iAff==7) and life==0.0:
			return

	pSet=pAttacker.GetContainingSet()			
					
	X=pAttacker.GetWorldLocation()
	
	kVectNiWorldHitPoint=pEvent.GetWorldHitPoint()
	Y=App.TGPoint3()			
	Y.SetX(kVectNiWorldHitPoint.x)
	Y.SetY(kVectNiWorldHitPoint.y)
	Y.SetZ(kVectNiWorldHitPoint.z)
	kVectNiWorldHitNormal=pEvent.GetWorldHitNormal()
	N=App.TGPoint3()			
	N.SetX(kVectNiWorldHitNormal.x)
	N.SetY(kVectNiWorldHitNormal.y)
	N.SetZ(kVectNiWorldHitNormal.z)

	if iAff==5 or iAff==6:
		FireTorpFromPoint(Y,None,pTorpPath,pAttacker.GetObjID(),pShip,pAttacker.GetHull().GetObjID())
	if iAff==7 or iAff==8:
		X.Subtract(Y)
		X.Unitize()
		U=X.Cross(N)
		V=N.Cross(U)
		V.Unitize()
		V.Scale(-2.0*X.Dot(V))
		X.Add(V)
		FireTorpFromPointWithVector(Y,X,pTorpPath,pAttacker.GetObjID(),pShip,pTorp.GetLaunchSpeed())	
								
	# Remove damage caused by the torpedo
	pTorp.SetLifetime(0.0)		
	fDamage=pEvent.GetDamage()#The power to reflect the weapon causes damage, 10% of the original damage
	shieldDistributePos(pShip,fDamage)


def TractorStart(pObject, pEvent):	
	global g_fTractorStartFiringList

	pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
	pAttacker = pProjector.GetParentShip()
	pShip=App.ShipClass_Cast(pEvent.GetDestination())

	pSound=pProjector.GetFireSound()
	pModule=__import__(pShip.GetScript())

	ID=0

	if pSound=="UCB":
		ID=1
		try:
			fVal=pModule.GetUCBStats()
		except:
			fVal=(100.0,100.0,100.0)
	elif pSound=="INV":
		ID=2
		try:
			fVal=pModule.GetInversionStats()
		except:
			fVal=(100.0,100.0,100.0)
	elif pSound=="TechAssimilationBeam":
		ID=3
		try:
			fVal=pModule.GetTechAssimilationStats()
		except:
			fVal=(15.0,80.0,80.0)
	elif pSound=="ShipAssimilationBeam":
		ID=4
		try:
			fVal=pModule.GetShipAssimilationStats()
		except:
			fVal=(1.0,80.0,80.0)
	else:
		return

	#Some Fx
	AID=pAttacker.GetObjID()
	sound=TRUE
	if AID==MissionLib.GetPlayer().GetObjID():
		for t in g_fTractorStartFiringList:
			if t[1]==AID:
				sound=FALSE
				break
		if sound:
			ATP_BridgeFX.MakeCharacterSay("Felix","SelfTractorsFire")

	#Add to the processing list
	tTuple=ID,AID,pShip.GetObjID(),App.g_kUtopiaModule.GetGameTime(),pProjector.GetObjID(),fVal
	g_fTractorStartFiringList.append(tTuple)
		
	
			
	
def TractorEnd(pObject, pEvent):
	global g_fTractorStartFiringList

	pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
	pAttacker = pProjector.GetParentShip()
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	
	pAttackerID=pAttacker.GetObjID()
	pShipID=pShip.GetObjID()
	pProjectorID=pProjector.GetObjID()
				
	for tTuple in g_fTractorStartFiringList[:]:
		i=tTuple[0]
		if tTuple[1]==pAttackerID  and tTuple[2]==pShipID and tTuple[4]==pProjectorID:
			if i==2:
				ATP_ShipDisplay.StopBeingINV(pShip)
				ATP_ShipDisplay.StopDoingINV(pAttacker)
			elif i==1:
				ATP_ShipDisplay.StopBeingUCB(pShip)
				ATP_ShipDisplay.StopDoingUCB(pAttacker)
			elif i==3 or i==4:
				ATP_ShipDisplay.StopBeingASS(pShip)
				ATP_ShipDisplay.StopDoingASS(pAttacker)
				
			g_fTractorStartFiringList.remove(tTuple)

	#Some Fx
	sound=TRUE
	if pAttackerID==MissionLib.GetPlayer().GetObjID():
		for t in g_fTractorStartFiringList:
			if t[1]==pAttackerID:
				sound=FALSE
				break
		if sound:
			ATP_BridgeFX.MakeCharacterSay("Felix","SelfTractorsStop")

	
				
			

def inversionBeamMain(pObject,pEvent):
	global g_fTractorStartFiringList
	j=0	
	
	for tTuple in g_fTractorStartFiringList[:]:
		if not tTuple[0]==2:
			continue

		try:
			pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
		except:
			g_fTractorStartFiringList.remove(tTuple)
			continue

		pAttacker=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		pShieldsShip=pShip.GetShields()
		pShieldsAttacker=pAttacker.GetShields()

		
		fStat=tTuple[5]


		if not CT_MPMP_MODE:
			if not HasSufficientSpecialPower(pAttacker,fStat[2]):
				pTractor = pAttacker.GetTractorBeamSystem()
				if (pTractor):
					pTractor.StopFiring()
				g_fTractorStartFiringList.remove(tTuple)
				continue

	
			AdjustSpecialPower(pAttacker,fStat[1])


		fRandom = App.g_kSystemWrapper.GetRandomNumber(470)
		if(fRandom==469):
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShieldsAttacker.SetCurShields(ShieldDir,0.0)
			return
			
		fDrain=fStat[0]

		shieldDistributeNeg(pShip,fDrain)	
		shieldDistributePos(pAttacker,fDrain)

		#Adjust the GUI
		ATP_ShipDisplay.IsBeingINV(pShip)
		ATP_ShipDisplay.IsDoingINV(pAttacker)				




def UCBMain(pObject,pEvent):
	global g_fTractorStartFiringList
		
	for tTuple in g_fTractorStartFiringList[:]:
		if not tTuple[0]==1:
			continue

		try:
			pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
			pAttacker=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		except:
			g_fTractorStartFiringList.remove(tTuple)
			continue

		fStat=tTuple[5]


		if not CT_MPMP_MODE:
			if not HasSufficientSpecialPower(pAttacker,fStat[2]):
				pTractor = pAttacker.GetTractorBeamSystem()
				if (pTractor):
					pTractor.StopFiring()
				g_fTractorStartFiringList.remove(tTuple)
				continue
		
			AdjustSpecialPower(pAttacker,fStat[1])
		

		fDrain=fStat[0]		
		
		pArmour=None

		if(positionSelectorShipBoolean(pShip,3,1)):
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	
			while (pSubsystem != None):
				if(pSubsystem.GetName()=="Ablative Armour"):
					if(pSubsystem.GetCondition()>0.0):
						pArmour=pSubsystem
					break
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				

			pShip.EndGetSubsystemMatch(pIterator)
	

		pHull=pShip.GetHull()
		fHull=pHull.GetCondition()

		if(pArmour):
			fArmour=pArmour.GetCondition()
			if(fArmour>fDrain):
				pArmour.SetCondition(fArmour-fDrain)
			else:
				pArmour.SetCondition(0)
			return			

		if(fDrain>=fHull):
			pShip.RunDeathScript()
		else:
			pHull.SetCondition(fHull-fDrain)


		#Adjust the GUI
		ATP_ShipDisplay.IsBeingUCB(pShip)
		ATP_ShipDisplay.IsDoingUCB(pAttacker)


def shipAssimilationBeamMain(pObject,pEvent):
	global g_fTractorStartFiringList

	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pFriendlies= pMission.GetFriendlyGroup()
	pEnemies= pMission.GetEnemyGroup()
	
	for tTuple in g_fTractorStartFiringList[:]:
				
		if not (tTuple[0]==4):
			continue
		
		pAttacker=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
		pPlayer=MissionLib.GetPlayer()

		fStat=tTuple[5]

		if not CT_MPMP_MODE:
			if not HasSufficientSpecialPower(pAttacker,fStat[2]):
				pTractor = pAttacker.GetTractorBeamSystem()
				if (pTractor):
					pTractor.StopFiring()
				g_fTractorStartFiringList.remove(tTuple)
				continue

			AdjustSpecialPower(pAttacker,fStat[1])

		time=fStat[0]*pShip.GetHull().GetCondition()/1000.0

		if (App.g_kUtopiaModule.GetGameTime()<tTuple[3]+time):
			continue

		pAttackerGroup=1
		pShipGroup=1

		pTractor = pAttacker.GetTractorBeamSystem()
		if (pTractor):
			pTractor.StopFiring()

		if not AreEnemies(pShip,pAttacker):
			continue

		#print "Ship Assimilation"

		if not CT_MPMP_MODE:
			if not IsEnemy(pShip):
				pFriendlies.RemoveName(pShip.GetName())
				pEnemies.AddName(pShip.GetName())
			else:
				pEnemies.RemoveName(pShip.GetName())
				pFriendlies.AddName(pShip.GetName())

		else:
			if pShip.GetObjID()==pPlayer.GetObjID():
				pFriendShips=makeFriendShipList()
				pEnemyShips=makeEnemyShipList()

				for pFriend in pFriendShips:
					if pFriend != pPlayer:
						pFriendlies.RemoveName(pFriend.GetName())
						pEnemies.AddName(pFriend.GetName())

				
				for pEnemy in pEnemyShips:
					if not AreEnemies(pEnemy,pAttacker):
						pEnemies.RemoveName(pEnemy.GetName())
						pFriendlies.AddName(pEnemy.GetName())
					
					

			elif IsFriend(pShip):
				pFriendlies.RemoveName(pShip.GetName())
				pEnemies.AddName(pShip.GetName())

			elif IsEnemy(pShip) and IsFriend(pAttacker):
				pEnemies.RemoveName(pShip.GetName())
				pFriendlies.AddName(pShip.GetName())

			
		pShields=pShip.GetShields()
		if pShields:
			ShieldGenerator=pShields.GetProperty()
			ShieldGeneratorShieldGlowColor = App.TGColorA()
			ShieldGeneratorShieldGlowColor.SetRGBA(31.0/255.0, 219.0/255.0, 26.0/255.0, 0.466667)
			ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				ShieldGenerator.SetShieldChargePerSecond(ShieldDir, 4.0*ShieldGenerator.GetShieldChargePerSecond(ShieldDir))
		
		pRepair=pShip.GetRepairSubsystem()
		if pRepair:
			Engineering=pRepair.GetProperty()
			Engineering.SetMaxRepairPoints(4.0*Engineering.GetMaxRepairPoints())
			Engineering.SetNumRepairTeams(2.0*Engineering.GetNumRepairTeams())		
		
			
		g_EnemyShipList=makeEnemyShipList(pAttacker.GetContainingSet())
		g_FriendShipList=makeFriendShipList(pAttacker.GetContainingSet())

		pPlayer=MissionLib.GetPlayer()
		pPlayerID=pPlayer.GetObjID()

		global CT_QUICKBATTLE_MODE

		if(len(g_EnemyShipList)==0 and CT_QUICKBATTLE_MODE):
			QuickBattle.QuickBattle.GenerateWinSequence()
			import BridgeHandlers
			BridgeHandlers.DropMenusTurnBack()
			g_pXO=QuickBattle.QuickBattle.g_pXO
			g_pXO.MenuUp ()
			for i in g_FriendShipList:
				pTemp=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
				pTemp.ClearAI()
				pTemp.CompleteStop()


		if(pShip.GetName()==pPlayer.GetName() and CT_QUICKBATTLE_MODE):
			bInSimulation=QuickBattle.QuickBattle.bInSimulation
			if bInSimulation:
				g_idTimer=QuickBattle.QuickBattle.g_idTimer
				g_pXO=QuickBattle.QuickBattle.g_pXO
				pEvent = App.TGIntEvent_Create()
				pEvent.SetInt(1)
				pEvent.SetEventType(QuickBattle.QuickBattle.ET_END_SIMULATION)
				pEvent.SetDestination(g_pXO)
				pTimer = App.TGTimer_Create()
				pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 1.0)
				pTimer.SetDelay(0)
				pTimer.SetDuration(0)
				pTimer.SetEvent(pEvent)
				g_idTimer = pTimer.GetObjID()
				App.g_kTimerManager.AddTimer(pTimer)
			else:
				RecreatePlayer()
				# Force back to the bridge
				pTopWindow = App.TopWindow_GetTopWindow()
				pTopWindow.ForceBridgeVisible()

				# Need to reset interactive mode, otherwise you'll get stuck if you go
				# to this mode.
				pCinematic = App.CinematicWindow_Cast(pTopWindow.FindMainWindow(App.MWT_CINEMATIC))
				if pCinematic:
					pCinematic.SetInteractive(1)

				if App.Game_GetCurrentGame().GetPlayer():
					App.Game_GetCurrentGame().GetPlayer().SetTarget(None)
		
		if not CT_MPMP_MODE:
			for i in g_EnemyShipList:
				ptempShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
				ptempShip.SetAI(CreateEnemyAI(ptempShip))

		
			for i in g_FriendShipList:
				if(i != pPlayerID):
					ptempShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
					ptempShip.SetAI(CreateFriendAI(ptempShip))


		pSound = App.g_kSoundManager.GetSound("ShipAssimilated")
		if(pSound):
			pSound.Play()

		#Adjust the GUI
		ATP_ShipDisplay.IsBeingASS(pShip)
		ATP_ShipDisplay.IsDoingASS(pAttacker)
						
		

def techAssimilationBeamMain(pObject,pEvent):
	global g_fTractorStartFiringList
		
	for tTuple in g_fTractorStartFiringList[:]:
		if not (tTuple[0]==3):
			continue


		try:
			pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
			pAttacker=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		except:
			g_fTractorStartFiringList.remove(tTuple)
			continue

		fStat=tTuple[5]
		
		if (App.g_kUtopiaModule.GetGameTime()<tTuple[3]+fStat[0]):
			continue

		if not CT_MPMP_MODE:
			if not HasSufficientSpecialPower(pAttacker,fStat[2]):
				pTractor = pAttacker.GetTractorBeamSystem()
				if (pTractor):
					pTractor.StopFiring()
				g_fTractorStartFiringList.remove(tTuple)
				continue

			AdjustSpecialPower(pAttacker,fStat[1])
	
		pAffAttacker=pAttacker.GetAffiliation()

		pTractor = pAttacker.GetTractorBeamSystem()
		if (pTractor):
			pTractor.StopFiring()
		succes=FALSE

		#print "Trying to assimilate tech"
		
		while(TRUE):

			fRandom = App.g_kSystemWrapper.GetRandomNumber(20)
			if(fRandom==0):
				break

			fRandom = App.g_kSystemWrapper.GetRandomNumber(3)
			
			if(fRandom==0):
				if(positionSelectorShipBoolean(pShip,1,0)):
					continue
				if not(positionSelectorShipBoolean(pAttacker,1,0)):
					continue
				pAffAttacker=pAffAttacker+1
				succes=TRUE
				break
				
				
			if(fRandom==1 ):

				if(positionSelectorShipBoolean(pShip,5,0)):
					continue
				if not(positionSelectorShipBoolean(pAttacker,5,0)):
					continue
				if(positionSelectorShip(pShip,5)>=1):
					pAffAttacker=pAffAttacker+10000			

				succes=TRUE
				break

			if(fRandom==2 or fRandom==3):
				pShipTractor=pShip.GetTractorBeamSystem()
				iChildren = pTractor.GetNumChildSubsystems()
				pName=None
				for iIndex in range(iChildren):
					pChild = pTractor.GetChildSubsystem(iIndex)
					pChildProp=pChild.GetProperty()
					if pChildProp.GetFireSound()=="UCB" or pChildProp.GetFireSound()=="INV":
						pName=pChildProp.GetFireSound()
						break
				if pName:
					pProjector=App.TractorBeamProjector_Cast(App.TGObject_GetTGObjectPtr(tTuple[4]))
					pProjector.GetProperty().SetFireSound(pName)
					succes=TRUE
				break

		#print "Tech Assimilated"

		pAttacker.SetAffiliation(pAffAttacker)		
		if(succes):
			pSound = App.g_kSoundManager.GetSound("AssimilationSucces")
			pSound.Play()

		#Adjust the GUI
		ATP_ShipDisplay.IsBeingASS(pShip)
		ATP_ShipDisplay.IsDoingASS(pAttacker)

		

def lifeSupportHit(pObject,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	
	if(positionSelectorShipBoolean(pShip,7,1)):
		found=0
		global g_lifeList
		ID =pShip.GetObjID()
			
		j=0
		for i in g_lifeList:
			tTuple=g_lifeList[j]
			j=j+1
			if(tTuple[0]==ID):
				found=1
				break

		if(found):
			return
		
		action=FALSE		
		pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

		while (pSubsystem != None):
			if(pSubsystem.GetName()=="Life Support"):			
				if(pSubsystem.IsDisabled()):
					action=TRUE
				pSys=pSubsystem
				break
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		pShip.EndGetSubsystemMatch(pIterator)
	
		if not (action):
			return
		if not (pSys):
			return

		tTuple=pShip.GetObjID(),pSys.GetObjID(),App.g_kUtopiaModule.GetGameTime()
		g_lifeList.append(tTuple)

		pPlayer = MissionLib.GetPlayer ()
		if(pPlayer.GetObjID()==pShip.GetObjID()):
			global g_lifeSound
			g_lifeSound=1
							
				
def lifeSupportCycle(pObject,pEvent):				
	global g_lifeList
	global g_lifeSound
	
	
	for tTuple in g_lifeList[:]:
		flush=FALSE
		pAlert=FALSE
		
		try:
			pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[0]))
		except:
			flush=TRUE

		if(flush or (pShip==None) ):
			g_lifeList.remove(tTuple)
			continue

		if pShip.IsDying():
			pPlayer = MissionLib.GetPlayer ()
			if(pPlayer.GetObjID()==pShip.GetObjID()):
				g_lifeSound=0	
			g_lifeList.remove(tTuple)
			continue
						

		pLife = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		T=App.g_kUtopiaModule.GetGameTime()
		t=tTuple[2]

		pPlayer = MissionLib.GetPlayer ()
		if(pPlayer.GetObjID()==pShip.GetObjID()):
			pAlert=TRUE
			
		
		if pAlert:		
			if((t+0<T) and (T<=t+10) and (g_lifeSound==1)):
				g_lifeSound=2
				ATP_BridgeFX.CreateLifeSupportEffect()
				ATP_BridgeFX.MakeCharacterSay("Miguel","SelfLifeSupportDisabled")
				

			elif((t+10<T) and (T<=t+20) and (g_lifeSound==2)):
				g_lifeSound=3
				pSound = App.g_kSoundManager.GetSound("LifeSupport30s")
				if(pSound):
					pSound.Play()
				
			elif((t+20<T) and (T<=t+30) and (g_lifeSound==3)):
				g_lifeSound=4
				pSound = App.g_kSoundManager.GetSound("LifeSupport20s")
				if(pSound):
					pSound.Play()
			
			elif((t+30<T) and (T<=t+40) and (g_lifeSound==4)):
				g_lifeSound=5
				pSound = App.g_kSoundManager.GetSound("LifeSupport10s")
				if(pSound):
					pSound.Play()

		if ((not pLife.IsDisabled()) or (T>t+120)):
			g_lifeList.remove(tTuple)
			if(pAlert):
				ATP_BridgeFX.EndLifeSupportEffect()
				ATP_BridgeFX.MakeCharacterSay("Miguel","SelfLifeSupportOnline")
				g_lifeSound=0				
			continue
		
		if(t+40<T):
			#pShip.RunDeathScript()
			if(pAlert):
				ATP_BridgeFX.CreateLifeSupportDeathEffect()
				print "Genocide..."
				g_lifeSound=6
				#g_lifeList.remove(tTuple)
				continue
		

def plasmaRuptureCheck(pObject,pEvent):
	import Custom.NanoFX.NanoFX_Lib

	pTargetShip = App.ShipClass_Cast(pEvent.GetTargetObject())
	pWarpSys = pTargetShip.GetWarpEngineSubsystem()
	if pWarpSys:
		# determine how many warp subsystems
		iNumWarp = pWarpSys.GetNumChildSubsystems()
		# go through every one of em.. make em smoke if they are damaged enough
		for iEng in range(iNumWarp):
			pWarpChild = pWarpSys.GetChildSubsystem(iEng)
			if pWarpChild:
				pWarpChildPos = pWarpChild.GetPosition()
				pWarpChildCondition = pWarpChild.GetCondition()
				pWarpChildMaxCondition = pWarpChild.GetMaxCondition()
				if (pWarpChildCondition <= pWarpChildMaxCondition / 2):
					global g_sneakerPlasmaCheck
					sneakerPlasmaRandom = App.g_kSystemWrapper.GetRandomNumber(4)
					if (g_sneakerPlasmaCheck == sneakerPlasmaRandom):
						sneakSize = pEvent.GetRadius()
						if sneakSize >= 0.5:
							sneakSize = sneakSize / 4
							if sneakSize < 0.4:
								sneakSize = 0.4
							elif sneakSize > 0.8:
								sneakSize = 0.8
							global g_sneakerPlasmaConstant
							if g_sneakerPlasmaConstant == 0:
								Custom.NanoFX.NanoFX_Lib.CreateSpecialFXSeq(pTargetShip,pEvent,"Plasma")								
								g_sneakerPlasmaConstant = 5
							else:
								g_sneakerPlasmaConstant = g_sneakerPlasmaConstant - 1

#########################################################################################################################
#	Torpedo Decoding												#
#															#
#	SpreadType:													#
#		0 - Normal Behaviour											#
#		1 - Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target	#
#		2 - Will scatter into a number of subtorpedoes specified in SpreadNumber, directed at different targets	#
#		3 - Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is set	#
#		    Friendly ships are aswell affected.									#
#		4 - Will convert into a rocket discribed by a shipscript						#
#		SpreadNumber: x - Number of subtorpedoes created							#
#		SpreadRadious: x - x range of the wavetorpedo								#
#		SpreadSplash: 0 - Allied ships not affected								#
#			      1 - Allied ships affected									#
#		SpreadPath: Defines the tactical/projectiles path of the subtorpedoes					#
#		eg "Tactical.Projectiles.subMyTorpedo"									#
#															#
#	ImpactType:													#
#		0 - Normal Behaviour											#
#		1 - Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
#		    that the torpedo isn't bounced									#
#		BounceYield:	x - torpedodamage is multiplied with this factor					#
#		BounceFail:	x - 1 on x chance that the weapon is absorbed						#
#															#
#															#
#	YieldType													#
#		0 - Normal Behaviour											#
#		1 - Special Behaviour:											#
#			DrainerWeapon:		0 - Not active								#
#						1 - Targets shields and powercore fails					#
#			SensorBlast:		0 - Not active								#
#						1 - Sensors disabled for SensorDisabledTime seconds			#
#			ShieldDisruptor:	0 - Not active								#
#						1 - Target shields are disrupted for ShieldDisabledTime seconds		#
#			EngineJammer:		0 - Not active								#
#						1 - Target Engines are disabled for EngineDisabledTime seconds		#
#			IonCannon:		0 - Not active								#
#						1 - Random Subtarget disabled for IonCannonDisabledTime seconds		#
#						    with a 1 on IonCannonMiss to have no effect				#
#			CloakBurn:		0 - Not active								#
#						1 - Target CloakingSys is disabled for CloakDisabledTime seconds	#
#########################################################################################################################


#########################################################################################################################
#	SpreadType Decoder:												#
#															#	
#	SpreadType:													#
#		0 - Normal Behaviour											#
#		1 - Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target	#
#		2 - Will scatter into a number of subtorpedoes specified in SpreadNumber, directed at different targets	#
#		3 - Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is set	#
#		    Friendly ships are aswell affected.									#
#		SpreadPath: Defines the tactical/projectiles path of the subtorpedoes					#
#		eg "Tactical.Projectiles.subMyTorpedo"									#															#
#########################################################################################################################

def SpreadTypeDecoder(pObject,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		SpreadType=pModule.SpreadType
	except:
		return

	try:
		SpreadDelay=pModule.SpreadDelay
	except:
		SpreadDelay=2.0


	global g_spreadHandleList

	if(SpreadType==0):
		return	

	if(SpreadType==1):
		tTuple=1,App.g_kUtopiaModule.GetGameTime()+SpreadDelay,pTorp.GetObjID(),pTorp.GetParentID()
		g_spreadHandleList.append(tTuple)
		return

	if(SpreadType==2):
		tTuple=2,App.g_kUtopiaModule.GetGameTime()+SpreadDelay,pTorp.GetObjID(),pTorp.GetParentID()
		g_spreadHandleList.append(tTuple)
		return
		
	
	if(SpreadType==3):
		cycleSpreadType3(pObject,pEvent)
		return
	
	if(SpreadType==4):
		MineHandler(pTorp)
		return

	if(SpreadType==5):
		RocketFired(pObject,pEvent)
		return
	
	#print "Error in SpreadTypeDecoder: Unknown SpreadType for Torpedo: ",pTorp.GetName()	

	
#########################################################################################################################
##	SpreadType Function 1												#
##															#
##		1 - Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target	#
#########################################################################################################################

def cycleSpreadType1(pObject,pEvent):
	global g_spreadHandleList

	j=0
	for i in g_spreadHandleList:
		tTuple=g_spreadHandleList[j] 
		
		if not tTuple[0]==1:
			j=j+1
			continue

		if not App.g_kUtopiaModule.GetGameTime()>=tTuple[1]:
			j=j+1
			continue
		
		pTorp=App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
		
		if pTorp==None:
			g_spreadHandleList.pop(j)
			continue			


		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[3]))

		pModuleName=pTorp.GetModuleName()
		pModule = __import__(pModuleName)
	
		try:
			SpreadNumber=pModule.SpreadNumber
		except:
			SpreadNumber=8
			
		try:
			SpreadDensity=pModule.SpreadDensity
		except:
			SpreadDensity=2.75


		try:
			pTorpPath=pModule.SecondPath
			if not pTorpPath:
				pTorpPath=pModuleName
		except:
			pTorpPath=pModuleName

		if(SpreadNumber<=1):
			g_spreadHandleList.pop(j)
			continue

		if App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetTargetID()))==None:
			TargetID=pShip.GetObjID()
		else:
			TargetID=pTorp.GetTargetID()

		try:
			SplitType=pModule.SplitType
		except:
			SplitType=1


		if(SplitType==0):
			g_spreadHandleList.pop(j)
			continue

		if(SplitType==1 or SplitType==3):
		
			kVectTorp=pTorp.GetWorldLocation()
			kVelocity = copyVector(pTorp.GetVelocityTG())
			fSpeed=kVelocity.Length()
			kVelocity.Unitize()
		
			kTest=App.TGPoint3()
			kTest.SetXYZ(1,0,0)
			if (kVelocity.GetY()==0.0):
				kTest.SetY(1.0)
			kX=kVelocity.Cross(kTest)
			kX.Unitize()
			kY=kX.Cross(kVelocity)

			theta=0.0
			delta=2.0*math.pi/SpreadNumber
	

			for k in range(SpreadNumber):
				ktX=copyVector(kX)
				ktX.Scale(math.cos(theta)/SpreadDensity)
			
				ktY=copyVector(kY)
				ktY.Scale(math.sin(theta)/SpreadDensity)
			
				kZ=copyVector(kVelocity)
				kZ.Add(ktX)
				kZ.Add(ktY)

				pTempTorp=FireTorpFromPointWithVector(kVectTorp,kZ,pTorpPath,TargetID,pShip,fSpeed)
				pTempTorp.SetLifetime(30.0)
				DepleteTypeDecoder(pObject,pEvent,pTempTorp)
				theta=theta+delta

		
		if(SplitType==2 or SplitType==3):		
			kVectTorp=pTorp.GetWorldLocation()
			kVelocity = copyVector(pTorp.GetVelocityTG())
			fSpeed=kVelocity.Length()
			kVelocity.Unitize()
		
			try:
				SpreadAngle=pModule.SpreadAngle
			except:
				SpreadAngle=25.0


			kX=pShip.GetWorldRightTG()
			theta=-SpreadAngle/180.0*math.pi
			delta=SpreadAngle/(SpreadNumber-1)/90.0*math.pi
	

			for k in range(SpreadNumber):
				ktX=copyVector(kX)
				ktX.Scale(math.sin(theta))
			
				kZ=copyVector(kVelocity)
				kZ.Add(ktX)
				
				pTempTorp=FireTorpFromPointWithVector(kVectTorp,kZ,pTorpPath,TargetID,pShip,fSpeed)
				pTempTorp.SetLifetime(30.0)
				DepleteTypeDecoder(pObject,pEvent,pTempTorp)
				theta=theta+delta

		try:
			ShellLive = pModule.ShellLive
		except:
			ShellLive = 0
		if not ShellLive:
			pTorp.SetLifetime(0.0)

		g_spreadHandleList.pop(j)



#########################################################################################################################
##	SpreadType Function 2												#
##															#
##		2 - Will scatter into a number of subtorpedoes specified in SpreadNumber, directed at different targets	#
#########################################################################################################################

def cycleSpreadType2(pObject,pEvent):
	j=0
	for i in g_spreadHandleList:
		tTuple=g_spreadHandleList[j] 
		
		if not tTuple[0]==2:
			j=j+1
			continue

		if not App.g_kUtopiaModule.GetGameTime()>=tTuple[1]:
			j=j+1
			continue

		pTorp=App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(tTuple[2]))
		if pTorp==None:
			g_spreadHandleList.pop(j)
			continue

		pModuleName=pTorp.GetModuleName()
		pModule = __import__(pModuleName)
	
		try:
			SpreadNumber=pModule.SpreadNumber
		except:
			SpreadNumber=5
		
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(tTuple[3]))
				
		if IsEnemy(pShip):
			ShipList=makeFriendShipList(pTorp.GetContainingSet())
		elif IsFriend(pShip):
			ShipList=makeEnemyShipList(pTorp.GetContainingSet())
		else:
			ShipList=makeEnemyShipList(pTorp.GetContainingSet())+makeFriendShipList(pTorp.GetContainingSet())

		if(SpreadNumber<=0):
			pTorp.SetLifetime(0.0)
			g_spreadHandleList.pop(j)
			continue

		
		kVect=pTorp.GetWorldLocation()
		
		ShipList=distanceSort(ShipList,kVect)
		
		if(len(ShipList)==0):
			g_spreadHandleList.pop(j)
			continue
	
		if(len(ShipList)==1):
			pTorp.SetTarget(ShipList[0])
			g_spreadHandleList.pop(j)
			continue
		
		length=len(ShipList)
		if(SpreadNumber<length):
			length=SpreadNumber

		try:
			pTorpPath=pModule.SecondPath
			if(pTorpPath==""):
				pTorpPath=pModuleName
		except:
			pTorpPath=pModuleName

		
		for k in range(length):
			pTempShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ShipList[k]))
			kTempShip=pTempShip.GetWorldLocation()
			kTempShip.Subtract(kVect)

			if(kTempShip.Length() >  500.0):
				break
			
			pTempTorp=FireTorpFromPoint(kVect,kVect,pTorpPath,ShipList[k],pShip,pTempShip.GetHull().GetObjID())
			DepleteTypeDecoder(pObject,pEvent,pTempTorp)

		try:
			ShellLive = pModule.ShellLive
		except:
			ShellLive = 0
		if not ShellLive:
			pTorp.SetLifetime(0.0)

		g_spreadHandleList.pop(j)


#########################################################################################################################
##	SpreadType Function 3												#
##															#
##		3 - Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is set	#
##		    Friendly ships are aswell affected.									#
#########################################################################################################################

def cycleSpreadType3(pObject,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
			
	pAttacker=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetParentID()))

	kVect0=pTorp.GetWorldLocation()
	
	try:
		ShellLive = pModule.ShellLive
	except:
		ShellLive = 0
	if not ShellLive:
		pTorp.SetLifetime(0.0)

	try:
		SpreadSplash=pModule.SpreadSplash
	except:
		SpreadSplash=0
				
	try:
		SpreadRadious=pModule.SpreadRadious
	except:
		SpreadRadious=150.0
				

	if not SpreadSplash:
		if IsEnemy(pAttacker):
			shipList=makeFriendShipList(pTorp.GetContainingSet())
		elif IsFriend(pAttacker):
			shipList=makeEnemyShipList(pTorp.GetContainingSet())
		else:
			shipList=makeFriendShipList(pTorp.GetContainingSet())+makeEnemyShipList(pTorp.GetContainingSet())
	else:
		shipList=makeNeutralShipList(pTorp.GetContainingSet())+makeFriendShipList(pTorp.GetContainingSet())+makeEnemyShipList(pTorp.GetContainingSet())
		shipList.remove(pAttacker.GetObjID())

	shipList=distanceSort(shipList,kVect0)

			
	for j in shipList:
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(j))
		
		kVect1=pShip.GetWorldLocation()
		kVect1.Subtract(kVect0)
		fDist=kVect1.Length()
		
		if(fDist>SpreadRadious):
			break

		YieldTypeDecoder(pObject,pEvent,pShip)


ROCKET	= 0
EFFECT	= 1
TIME	= 2

def RocketFired(pMission,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return 

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		sGfx = pModule.SpreadPath
		if not sGfx:
			sGfx = "ATP_Rocket"
		if sGfx == "":
			sGfx = "ATP_Rocket"
	except:
		sGfx = "ATP_Rocket"
	
	kThis = App.Waypoint_Create("Rocket_POS_"+str(pTorp.GetObjID()),pTorp.GetContainingSet().GetName(), None)
	kThis.SetStatic(FALSE)
	kThis.SetNavPoint(FALSE)
	kThis.SetTranslateXYZ(0.0,0.0,0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0,1.0,0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0,0.0,1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.0)
	kThis.Update(0)
	
	import loadspacehelper
	print sGfx
	pRocket = loadspacehelper.CreateShip(sGfx,pTorp.GetContainingSet(),"__Rocket__"+str(pTorp.GetObjID()),kThis.GetName())	
	pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetParentID()))
	pShip.EnableCollisionsWith(pRocket,FALSE)
	pRocket.EnableCollisionsWith(pShip,FALSE)

	kThis.Destroy()

	pTorp.AttachObject(pRocket)
	pRocket.SetTranslateXYZ(0.0,0.0,0.0)
	pRocket.SetHurtable(FALSE)
	pRocket.SetTargetable(FALSE)

	U = pTorp.GetWorldLocation()
	if pTorp.GetTargetID() != App.NULL_ID:
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetTargetID()))
		if pTarget:
			V = pTarget.GetWorldLocation()
			V.Subtract(U)
			Z = pTorp.GetWorldUpTG()
			Y = Z.Cross(V)
			Z = Y.Cross(V)
			pTorp.AlignToVectors(V,Z)
	
	## Attach smoke to it
	Emittor = findEmittor(pRocket,"Smoke")
	assert Emittor
	
	vEmitPos = Emittor.GetPosition()
	kEmitPos = App.NiPoint3(vEmitPos.x,vEmitPos.y,vEmitPos.z)
	vEmitDir = Emittor.GetForward()
	kEmitDir = App.NiPoint3(vEmitDir.x,vEmitDir.y,vEmitDir.z)

	pSet 	      = pRocket.GetContainingSet()
	pAttachTo     = pSet.GetEffectRoot()
	pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pRocket.GetNode())
	sFile         = "scripts/Custom/NanoFX/SpecialFX/Gfx/Plasma/Plasma.tga"

	import Custom.NanoFX.NanoFX_ScriptActions
	pSequence = App.TGSequence_Create()
	pPlasma = Custom.NanoFX.NanoFX_ScriptActions.CreateControllerFX(sFile, 
									pEmitFrom, 
									pAttachTo, 
									pRocket.GetRadius(), 
									kEmitPos, 
									kEmitDir,
									bDetach = 0,
									fFrequency = 0.01, 
									fLifeTime = 99.0, 
									fVariance = 15.0,
									iTiming = 64,
									fRed   = 200, 
									fGreen = 200, 
									fBlue  = 200,
									fBrightness = 1.00)
	pSequence.AddAction(pPlasma)
	pSequence.Play()

	global g_RocketDict
	g_RocketDict[pTorp.GetObjID()]  = pRocket.GetObjID(), pSequence, App.g_kUtopiaModule.GetGameTime() + 0.90*pTorp.GetLifetime()


def RocketHitCollision(pMission,pEvent):
	pA = App.ShipClass_Cast(pEvent.GetSource())
	pB = App.ShipClass_Cast(pEvent.GetDestination())
	if not pA or not pB:
		return
	
	global g_RocketDict
	AID = pA.GetObjID()
	bA  = FALSE
	BID = pB.GetObjID()
	bB  = FALSE
	for TID in g_RocketDict.keys():
		RID = g_RocketDict[TID][ROCKET]
		if RID == AID or RID == BID:
			if RID == AID:
				bA = TRUE
			if RID == BID:
				bB = TRUE
			g_RocketDict[TID][EFFECT].Abort()
			del g_RocketDict[TID]

	import string
	sNameA = pA.GetName()
	if string.rfind(sNameA,"__Rocket__") != -1 and bA:
		#debug("RocketHitCollisionA: trying to delete "+sNameA)
		pA.SetDeleteMe(TRUE)
		#debug("RocketHitCollisionA: deleted "+sNameA)
	sNameB = pB.GetName()
	if string.rfind(sNameB,"__Rocket__") != -1 and bB:
		#debug("RocketHitCollisionB: trying to delete "+sNameB)
		pB.SetDeleteMe(TRUE)
		#debug("RocketHitCollisionB: deleted "+sNameB)

def RocketHitWeapon(pMission,pEvent):
	global g_RocketDict

	## Find the torpedo entry and the matching rocket
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	TID = pTorp.GetObjID()
	if not g_RocketDict.has_key(TID):
		return
	pRocket = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(g_RocketDict[TID][ROCKET]))
	if not pRocket:
		return
	
	## Delete the rocket and stop the effect
	#debug("RocketHitWeapon: trying to delete "+pRocket.GetName())
	pRocket.SetDeleteMe(TRUE)
	#debug("RocketHitWeapon: deletong "+pRocket.GetName())
	g_RocketDict[TID][EFFECT].Abort()
	
	## Remove the entry
	del g_RocketDict[TID]

def cycleRocket(pMission,pEvent):
	global g_RocketDict
	T = App.g_kUtopiaModule.GetGameTime()

	## Check if the lifetime of the rocket is over
	for TID in g_RocketDict.keys():
		pRocket = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(g_RocketDict[TID][ROCKET]))
		if not pRocket:
			continue
		
		pTorp	= App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(TID))
		if not pTorp:
			continue
		if pTorp.GetTargetID() != App.NULL_ID:
			pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetTargetID()))
			if pTarget:
				## Orient the rocket well
				pass
				#debug("trying to turn "+pRocket.GetName())
				#TurnToward(pRocket,pTarget.GetWorldLocation(),pTarget.GetWorldUpTG())

		if T >= g_RocketDict[TID][TIME]:
			## Lifetime exceeded, remove it
			
			## Delete the rocket and stop the effect
			#debug("cycleRocket: trying to delete "+pRocket.GetName())
			pRocket.SetDeleteMe(TRUE)
			#debug("cycleRocket: deletong "+pRocket.GetName())
			g_RocketDict[TID][EFFECT].Abort()
	
			## Remove the entry
			del g_RocketDict[TID]


#####################
# Mines
#####################

## New style for ATP
import ATP_Handler
class MineHandler(ATP_Handler.ATP_Handler):
	FRIEND = 0
	ENEMY  = 1

	def __init__(self,pTorp):
		## Base class
		ATP_Handler.ATP_Handler.__init__(self)

		## Stop the torpedo
		pTorp.SetLifetime(0.0)

		## Create the mine model
		
		### find the Gfx
		pModuleName=pTorp.GetModuleName()
		pModule = __import__(pModuleName)
		try:
			sGfx = pModule.SpreadPath
			if not sGfx:
				sGfx = "ATP_Mine"				
		except:
			sGfx = "ATP_Mine"		

		### create a waypoint
		kThis = App.Waypoint_Create("Mine_POS_"+str(pTorp.GetObjID()),pTorp.GetContainingSet().GetName(), None)
		kThis.SetStatic(FALSE)
		kThis.SetNavPoint(FALSE)
		kThis.SetTranslateXYZ(0.0,0.0,0.0)
		kForward = App.TGPoint3()
		kForward.SetXYZ(0.0,1.0,0.0)
		kUp = App.TGPoint3()
		kUp.SetXYZ(0.0,0.0,1.0)
		kThis.AlignToVectors(kForward, kUp)
		kThis.SetSpeed(0.0)
		kThis.Update(0)
	
		### the mothership
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetParentID()))
		assert pShip

		### create the actual model
		import loadspacehelper
		i=0
		pMine = None
		while(i<100):
			i=i+1
			pMine = loadspacehelper.CreateShip(sGfx,pTorp.GetContainingSet(),pShip.GetName()+" Mine "+str(i),kThis.GetName())
			if pMine:
				break
		assert pMine
		self.Mine = pMine
		kThis.Destroy()

		## Reposition
		pMine.SetTranslate(pTorp.GetWorldLocation())
		pMine.AlignToVectors(pTorp.GetWorldForwardTG(),pTorp.GetWorldUpTG())

		## Friend or foe?
		if IsFriend(pShip):
			MissionLib.GetMission().GetFriendlyGroup().AddName(pMine.GetName())
			self.Aff = MineHandler.FRIEND
		elif IsEnemy(pShip):
			MissionLib.GetMission().GetEnemyGroup().AddName(pMine.GetName())
			self.Aff = MineHandler.ENEMY
		else:
			debug("error 811")		

		## Disable collisions		
		pMine.SetCollisionsOn(FALSE)
		
		## Set the impulse at max
		V = pTorp.GetVelocityTG()
		V.Unitize()
		V.Scale(1.0+pShip.GetVelocityTG().Length())
		pMine.SetVelocity(V)
		pMine.SetSpeed(0.0,App.TGPoint3_GetModelForward(),App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
					
		## Some stats
		try:
			self.fRadius	= pModule.SpreadRadius * km
		except:
			self.fRadius	= 15.0 * km
		self.fRadius	= 0.0
		try:
			self.fStop	= pModule.SpreadDelay
		except:
			self.fStop	= 5.0
		try:
			self.bSplash	= pModule.SpreadSplash
		except:
			self.bSplash	= FALSE
		try:
			self.fStrength  = pModule.GetDamage()
		except:
			self.fStrength  = 100.0

		## Give it low explosion strength for now
		pPower = pMine.GetPowerSubsystem().GetProperty()
		pPower.SetPowerOutput(self.fStrength / 10.0)
		
		## Add a clock
		self.AddClock("StopMine",self.fStop*GetRandom(0.5,2.0))

		debug("B")

	def StopMine(self,pEvent):
		debug("C")

		## Remove the clock
		self.RemoveClock("StopMine")

		## Stop the torpedo
		# self.Mine.SetSpeed(0.0,App.TGPoint3_GetModelForward(),App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		## Triggerlist of objects
		if not self.bSplash:
			if self.Aff == MineHandler.FRIEND:
				lObjectIDs = makeEnemyShipList(self.Mine.GetContainingSet())
			elif self.Aff == MineHandler.ENEMY:
				lObjectIDs = makeFriendShipList(self.Mine.GetContainingSet())
		else:
			lObjectIDs = makeEnemyShipList(self.Mine.GetContainingSet()) + makeFriendShipList(self.Mine.GetContainingSet())		

		debug("CA")

		## Convert the list from an ID list to a pointer list
		lObjects = ()
		for ID in lObjectIDs:
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ID))
			if pShip and not pShip.GetObjID()==self.Mine.GetObjID():
				lObjects = lObjects + (pShip,)

		## Setup a proximity manager
		self.e = App.Mission_GetNextEventType()
		self.AddHandler(self.e,"ExplodeMe")
		self.Proxy = MissionLib.ProximityCheck(self.Mine,self.fRadius,lObjects,TOOL_PATH+".Dummy",eEventType = self.e)

		debug("CB")

		## Give it a high explosion strength for now
		pPower = self.Mine.GetPowerSubsystem().GetProperty()
		pPower.SetPowerOutput(self.fStrength * 100.0)

		## Reenable collisions
		self.Mine.SetCollisionsOn(TRUE)

		debug("D")

	def ExplodeMe(self,pEvent):
		debug("E")
		
		## A ship came too close, explode
		self.Mine.RunDeathScript()
		self.delete()

		debug("F")		



#########################################################################################################################
##	ImpactType Decoder												#
##															#
##		0 - Normal Behaviour											#
##		1 - Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
##		    that the torpedo isn't bounced									#
##		BounceYield:	x - torpedodamage is multiplied with this factor					#
##		BounceFail:	x - 1 on x chance that the weapon is absorbed						#
##															#
#########################################################################################################################

def ImpactTypeDecoder(pObject,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
		
	if pTorp==None:
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		ImpactType=pModule.ImpactType
	except:
		return


	if(ImpactType==0):
		return	

	if(ImpactType==1):
		bounceTorpedo(pObject,pEvent)
		return

	if(ImpactType==2):
		phasedTorpedo(pObject,pEvent)
		return

	if ImpactType==3:
		enveloppingTorpedo(pObject,pEvent)
		return

	#print "Error in ImpactTypeDecoder: Unknown ImpactType for Torpedo: ", pTorp.GetName()	


#########################################################################################################################
###	Bounce Torpedo													#
###															#
###		Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
###		that the torpedo isn't bounced										#
###			BounceYield:	x - torpedodamage is multiplied with this factor				#
###			BounceFail:	x - 1 on x chance that the weapon is absorbed					#
###															#
#########################################################################################################################

def bounceTorpedo(pObject,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return

	if pEvent.IsHullHit():
		return
	
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		BounceYield=pModule.BounceYield
	except:
		BounceYield=1.0

	try:
		BounceFail=pModule.BounceFail
	except:
		BounceFail=10


	fRandom = App.g_kSystemWrapper.GetRandomNumber(BounceFail)

	if fRandom==0:
		return

	friend=TRUE
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	if IsEnemy(pShip):
		friend=FALSE

	if friend:
		ShipList=makeFriendShipList(pTorp.GetContainingSet())
	else:
		ShipList=makeEnemyShipList(pTorp.GetContainingSet())

	kVect=pTorp.GetWorldLocation()
		
	ShipList=distanceSort(ShipList,kVect)
	
	if(len(ShipList)<=1):
		return
	

	pTarget=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ShipList[1]))

	pTorp2=FireTorpFromPoint(kVect,kVect,pTorp.GetModuleName(),ShipList[1],pShip,pTarget.GetHull().GetObjID())	
	
	pTorp2.SetDamage(BounceYield*pTorp.GetDamage())



def IsPhasedHit(pTorp):
	if not pTorp:
		return FALSE

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		ImpactType=pModule.ImpactType
	except:
		return FALSE

	if ImpactType==2:
		return TRUE
	return FALSE



def phasedTorpedo(pObject,pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())
	
	pTorp= App.Torpedo_Cast(pEvent.GetSource())

	if not pTorp:
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		pTorpPath=pModule.SecondPath
		if(pTorpPath==""):
			return
	except:
		return
	
	
	kVectNiWorldHitNormal=pEvent.GetWorldHitNormal()		
										
	V=App.TGPoint3()
	V.SetX(kVectNiWorldHitNormal.x)
	V.SetY(kVectNiWorldHitNormal.y)
	V.SetZ(kVectNiWorldHitNormal.z)
	V.Unitize()

	#We try to push the torpedo inside the shields
	X=pTorp.GetWorldLocation()
	V.Scale(55.0/10000.0*(-1.0))
	if pEvent.IsHullHit():
		V.Scale(-1.0)
	X.Add(V)

	FireTorpFromPointWithVector(X,pTorp.GetVelocityTG(),pTorpPath,pShip.GetObjID(),pAttacker,pTorp.GetVelocityTG().Length(),pAttacker.GetTargetOffsetTG())
	pTorp.SetLifetime(0.0)


def enveloppingTorpedo(pObject,pEvent):

	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())
	
	pTorp= App.Torpedo_Cast(pEvent.GetSource())

	if not pTorp:
		return

	kVectNiWorldHitNormal=pEvent.GetWorldHitNormal()		
										
	kN=App.TGPoint3()
	kN.SetX(kVectNiWorldHitNormal.x)
	kN.SetY(kVectNiWorldHitNormal.y)
	kN.SetZ(kVectNiWorldHitNormal.z)
	kN.Unitize()
	kX=pTorp.GetVelocityTG()
	kX.Unitize()
	kN.Scale((-1.0)*kX.Dot(kN))
	kX.Add(kN)
	kN.Unitize()
	kY=kX.Cross(kN)
	
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)

	try:
		SpreadNumber=pModule.EnveloppingNumber
		if EnveloppingNumber==0:
			return
	except:
		SpreadNumber=6
	
	try:
		IsShell=pModule.IsShell
	except:
		IsShell=FALSE

	if not IsShell:
		SpreadNumber=1
		pTorpPath=pModuleName
	else:
		try:
			pTorpPath=pModule.SecondPath
			if(pTorpPath==""):
				return
		except:
			return

	

	theta=0.0
	delta=2.0*math.pi/(SpreadNumber*1.0)
	fSpeed=pTorp.GetVelocityTG().Length()
	
	for k in range(SpreadNumber):
		kZ=pTorp.GetWorldLocation()
		ktN=copyVector(kN)
		ktN.Scale(1.5*55.0/1000.0*(-1.0))
				
		ktX=copyVector(kX)
		ktX.Scale(math.cos(theta))
		ktX.Scale(55.0/100.0*(+1.0))
			
		ktY=copyVector(kY)
		ktY.Scale(math.sin(theta))
		ktY.Scale(55.0/100.0*(+1.0))
			
		ktY.Add(ktX)
		kZ.Add(ktY)

		ktY.Add(ktN)
		
		pTempTorp=FireTorpFromPointWithVector(kZ,ktY,pTorpPath,pShip.GetObjID(),pAttacker,fSpeed,pAttacker.GetTargetOffsetTG())
		pTempTorp.SetLifetime(2.0)
		theta=theta+delta

	pTorp.SetLifetime(0.0)
						
	

#########################################################################################################################
##	Yield Type Decoder												#
##															#
##	YieldType:													#
##		0 - Normal Behaviour											#
##		1 - Special Behaviour:											#
##			DrainerWeapon:		0 - Not active								#
##						1 - Targets shields and powercore fails					#
##			SensorBlast:		0 - Not active								#
##						1 - Sensors disabled for SensorDisabledTime seconds			#
##			ShieldDisruptor:	0 - Not active								#
##						1 - Target shields are disrupted for ShieldDisabledTime seconds		#
##			EngineJammer:		0 - Not active								#
##						1 - Target Engines are disabled for EngineDisabledTime seconds		#
##			Ion Cannon:		0 - Not active								#
##						1 - Random Subtarget disabled for IonCannonDisabledTime seconds		#
##						    with a 1 on IonCannonMiss to have no effect				#
##			CloakBurn:		0 - Not active								#
##						1 - Target CloakingSys is disabled for CloakDisabledTime seconds	#
#########################################################################################################################

def YieldTypeDecoder(pObject,pEvent,pShip=None):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
		
	if pTorp==None:
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)

	try:
		YieldType=pModule.YieldType
	except:
		return

	if YieldType==0:
		return
	
	if YieldType>1:
		#print "Error in YieldTypeDecoder: Unknown YieldType for Torpedo: ", pTorp.GetModuleName()
		return

	try:
		DrainerWeapon=pModule.DrainerWeapon
	except:
		DrainerWeapon=0
	
	try:
		SensorBlast=pModule.SensorBlast
	except:
		SensorBlast=0
	try:
		ShieldDisruptor=pModule.ShieldDisruptor
	except:
		ShieldDisruptor=0

	try:
		EngineJammer=pModule.EngineJammer
	except:
		EngineJammer=0

	try:
		IonCannon=pModule.IonCannon
	except:
		IonCannon=0

	try:
		CloakBurn=pModule.CloakBurn
	except:
		CloakBurn=0

	

	if not DrainerWeapon==0:
		drainerWeapon(pObject,pEvent,pShip)
	if not SensorBlast==0:
		sensorBlast(pObject,pEvent,)
	if not ShieldDisruptor==0:
		shieldDisruptor(pObject,pEvent,pShip)
	if not EngineJammer==0:
		engineJammer(pObject,pEvent,pShip)
	if not IonCannon==0:
		try:
			IonFrequency=pModule.IonFrequency
		except:
			IonFrequency=1
		if not IonFrequency<=0:
			for m in range(IonFrequency):
				ionCannon(pObject,pEvent,pShip)
	if not CloakBurn==0:
		cloakBurn(pObject,pEvent,pShip)

	if not CT_NANOFX_MODE:
		return
	try:
		PhalantiumWave=pModule.PhalantiumWave
	except:
		PhalantiumWave=0

	try:
		SpatialCharges=pModule.SpatialCharges
	except:
		SpatialCharges=0

	if not PhalantiumWave==0:
		phalantiumWave(pObject,pEvent,pShip)
	if not SpatialCharges==0:
		spatialCharges(pObject,pEvent,pShip)

	

#########################################################################################################################
###	Drainer Weapon													#
###															#
###		0 - Not active												#
###		1 - Targets shields and powercore fails									#
###															#
#########################################################################################################################

def drainerWeapon(pObject,pEvent,pShip=None):
	global DrainerDict
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())	
									
	if not positionSelectorShip(pShip,2)==0:
		#Check if the tartget is immune to the drainerweapon (Klingon, Breen, Coalition (new shipline))
		return

	pPlayer = MissionLib.GetPlayer ()
	if not pPlayer:
		return

	## Check the flag
	if CheckFlag(pShip,HIT_BY_DRAINER_WEAPON):
		return
	SetFlag(pShip,HIT_BY_DRAINER_WEAPON)

	if(pPlayer.GetObjID()==pShip.GetObjID()):
		ATP_BridgeFX.CreateDrainEffect()

	if CT_NANOFX_MODE:
		from Custom.NanoFX import NanoFX_Lib
		pSequence = NanoFX_Lib.CreateFlickerSeq(pShip,10, fFlickerSpeed = 0.2, sStatus = "Off")
		pSequence.Play()

	#Warp Core doesn't produce a single Watt anymore		
	pPower = pShip.GetPowerSubsystem()
	IonSubSystem(pPower,99999)
	pProp = pPower.GetProperty()
	pProp.SetPowerOutput(0.0)
	powerTest(pShip,0.0)				

	#Bye shields
	pShields = pShip.GetShields()
	if pShields:
		IonSubSystem(pShields,99999)

	#No more special power
	AdjustSpecialPower(pShip,9999999)

	#No more speed
	StopShip(pShip)

	#Fry the cloak
	pCloak=pShip.GetCloakingSubsystem()
	if pCloak:
		IonSubSystem(pCloak,99999)

	#Prevent warp out
	pWarp=pShip.GetWarpEngineSubsystem()
	if not pWarp:
		return
	
	iChildren = pWarp.GetNumChildSubsystems()
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pWarp.GetChildSubsystem(i)
			IonSubSystem(pChild,99999)
	else:
		IonSubSystem(pWarp,99999)

	ATP_ActionDecoder.NotifyDrainerWeapon(pShip)



def IsDrainerHit(pTorp):	
	if not pTorp:
		return FALSE

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	try:
		YieldType=pModule.YieldType
	except:
		return FALSE

	if not YieldType==1:
		return FALSE
		
	try:
		DrainerWeapon=pModule.DrainerWeapon
	except:
		return FALSE

	if DrainerWeapon:
		return TRUE
	return FALSE


		
#########################################################################################################################
###	Sensor Blast													#
###															#
###		0 - Not active												#
###		1 - Sensors disabled for SensorDisabledTime seconds							#
###															#
#########################################################################################################################

def sensorBlast(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
		
	#print "sensorBlast on ship: ",pShip.GetName()
								
	pSensor = pShip.GetSensorSubsystem()
	if not pSensor:
		#print "No sensorSystem in ship ",pShip.GetName()
		return

	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		#print "Torpedo Already Dead"
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		SensorDisabledTime=pModule.SensorDisabledTime
	except:
		SensorDisabledTime=30.0
	
	iChildren = pSensor.GetNumChildSubsystems()
			
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pSensor.GetChildSubsystem(i)
			IonSubSystem(pChild,SensorDisabledTime)
	else:
		IonSubSystem(pSensor,SensorDisabledTime)

	PID=MissionLib.GetPlayer().GetObjID()
	AID=pTorp.GetParentID()
	SID=pShip.GetObjID()
	if pSensor.IsDisabled():
		if PID==SID:
			ATP_BridgeFX.MakeCharacterSay("Miguel","SelfSensorsDisabled")
		elif PID==AID:
			ATP_BridgeFX.MakeCharacterSay("Miguel","TargetSensorsDisabled")

	
#########################################################################################################################
###	Shield Disruptor												#
###															#
###		0 - Not active												#
###		1 - Target shields are disrupted for ShieldDisabledTime seconds						#
###															#
#########################################################################################################################

def shieldDisruptor(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
								
   	pShieldSys = pShip.GetShields()
	if not pShieldSys:
		return

	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		ShieldDisabledTime=pModule.ShieldDisabledTime
	except:
		ShieldDisabledTime=30.0

	
	iChildren = pShieldSys.GetNumChildSubsystems()
			
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pShieldSys.GetChildSubsystem(i)
			IonSubSystem(pChild,ShieldDisabledTime)
	else:
		IonSubSystem(pShieldSys,ShieldDisabledTime,1)

	PID=MissionLib.GetPlayer().GetObjID()
	AID=pTorp.GetParentID()
	SID=pShip.GetObjID()
	if IsDisabled(pShieldSys):
		if PID==SID:
			ATP_BridgeFX.MakeCharacterSay("Brex","SelfShieldsDisabled")
		elif PID==AID:
			ATP_BridgeFX.MakeCharacterSay("Miguel","TargetShieldsDisabled")
	
	
#########################################################################################################################
###	EngineJammer:													#
###		0 - Not active												#
###		1 - Target Engines are disabled for EngineDisabledTime seconds						#
###															#
#########################################################################################################################

def engineJammer(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())

	pWarp=pShip.GetWarpEngineSubsystem()
	pImpulse=pShip.GetImpulseEngineSubsystem()
								
	if not pWarp or not pImpulse:
		return

	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		EngineDisabledTime=pModule.EngineDisabledTime
	except:
		EngineDisabledTime=30.0
	
	iChildren = pWarp.GetNumChildSubsystems()
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pWarp.GetChildSubsystem(i)
			IonSubSystem(pChild,EngineDisabledTime)
	else:
		IonSubSystem(pWarp,EngineDisabledTime)

	iChildren = pImpulse.GetNumChildSubsystems()
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pImpulse.GetChildSubsystem(i)
			IonSubSystem(pChild,EngineDisabledTime)
	else:
		IonSubSystem(pImpulse,EngineDisabledTime)

	PID=MissionLib.GetPlayer().GetObjID()
	AID=pTorp.GetParentID()
	SID=pShip.GetObjID()
	if IsDisabled(pImpulse):
		if PID==SID:
			ATP_BridgeFX.MakeCharacterSay("Brex","SelfImpulseDisabled")
		elif PID==AID:
			ATP_BridgeFX.MakeCharacterSay("Miguel","TargetImpulseDisabled")


#########################################################################################################################
###	CloakBurn:													#
###		0 - Not active												#
###		1 - Target CloakingSys is disabled for CloakDisabledTime seconds					#
###															#
#########################################################################################################################

def cloakBurn(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
	
	pCloak=pShip.GetCloakingSubsystem()
	if pCloak==None:
		return

	if not pShip.IsCloaked():
		return
	
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		CloakDisabledTime=pModule.CloakDisabledTime
	except:
		CloakDisabledTime=30.0
	
	iChildren = pCloak.GetNumChildSubsystems()
	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pCloak.GetChildSubsystem(i)
			IonSubSystem(pChild,CloakDisabledTime)
	else:
		IonSubSystem(pCloak,CloakDisabledTime)


#########################################################################################################################
###	IonCannon:													#
###		0 - Not active												#
###		1 - Random Subtarget disabled for IonCannonDisabledTime seconds	with a 1 on IonCannonMiss		#
###		    to have no effect											#
###															#
#########################################################################################################################

def ionCannon(pObject,pEvent,pShip=None):
	if not pEvent.IsHullHit():
		return

	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	pPlayer=MissionLib.GetPlayer()
	if not pPlayer or not pAttacker:
		return

	AID=pAttacker.GetObjID()
	SID=pShip.GetObjID()
	PID=pPlayer.GetObjID()

	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	if pTorp==None:
		return
	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		IonCannonDisabledTime=pModule.IonCannonDisabledTime
	except:
		IonCannonDisabledTime=30.0

	try:
		IonCannonMiss=pModule.IonCannonMiss
	except:
		IonCannonMiss=20
	
	fRandom = App.g_kSystemWrapper.GetRandomNumber(IonCannonMiss)

	if fRandom==0:
		return


	fRandom = App.g_kSystemWrapper.GetRandomNumber(100)
	pSubSystem=0
	bShield=FALSE
	
	if(0<=fRandom<3):
		pSubSystem=pShip.GetShields()
		bShield=TRUE
		if pSubSystem:
			if not pSubSystem.IsDisabled():
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfShieldsDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetShieldsDisabled")
	elif(3<=fRandom<12):
		pSubSystem=pShip.GetPowerSubsystem()
		if pSubSystem:
			if not pSubSystem.IsDisabled():
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfPowerDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetPowerDisabled")
	elif(12<=fRandom<15):
		pSubSystem=pShip.GetSensorSubsystem()
		if pSubSystem:
			if not pSubSystem.IsDisabled():
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","SelfSensorsDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetSensorsDisabled")
	elif(15<=fRandom<30):
		pSubSystem=pShip.GetWarpEngineSubsystem()
	elif(30<=fRandom<45):
		pSubSystem=pShip.GetTorpedoSystem()
		bChild=1
	elif(45<=fRandom<65):
		pSubSystem=pShip.GetPhaserSystem()
		bChild=1
	elif(65<=fRandom<80):
		pSubSystem=pShip.GetPulseWeaponSystem()
		bChild=1
	elif(80<=fRandom<90):
		pSubSystem=pShip.GetTractorBeamSystem()
		bChild=1
	elif(90<=fRandom<100):
		pSubSystem=pShip.GetImpulseEngineSubsystem()
		bChild=1
	else:
		return

	if pSubSystem==None:
		return	

	iChildren = pSubSystem.GetNumChildSubsystems()
		
	if (iChildren > 0):
		fRandom2 = App.g_kSystemWrapper.GetRandomNumber(iChildren)
		pChild = pSubSystem.GetChildSubsystem(fRandom2)
		IonSubSystem(pChild,IonCannonDisabledTime)
	else:
		if not bShield:
			IonSubSystem(pSubSystem,IonCannonDisabledTime)
		else:
			IonSubSystem(pSubSystem,IonCannonDisabledTime,1)
	

	if(15<=fRandom<30):
		pSubSystem=pShip.GetWarpEngineSubsystem()
		if pSubSystem:
			if IsDisabled(pSubSystem):
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfWarpDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetWarpDisabled")
	elif(30<=fRandom<45):
		pSubSystem=pShip.GetTorpedoSystem()
		if pSubSystem:
			if IsDisabled(pSubSystem):
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfTorpedoesDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetTorpedoesDisabled")
	elif(45<=fRandom<65):
		pSubSystem=pShip.GetPhaserSystem()
		if pSubSystem:
			if IsDisabled(pSubSystem):
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfPhasersDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetPhasersDisabled")
	elif(80<=fRandom<90):
		pSubSystem=pShip.GetTractorBeamSystem()
		if pSubSystem:
			if IsDisabled(pSubSystem):
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfTractorDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetTractorDisabled")
	elif(90<=fRandom<100):
		pSubSystem=pShip.GetImpulseEngineSubsystem()
		if pSubSystem:
			if IsDisabled(pSubSystem):
				if PID==SID:
					ATP_BridgeFX.MakeCharacterSay("Brex","SelfImpulseDisabled")
				elif PID==AID:
					ATP_BridgeFX.MakeCharacterSay("Miguel","TargetImpulseDisabled")
	
	if CT_NANOFX_MODE:
		from Custom.NanoFX import NanoFX_Lib
		pSequence = NanoFX_Lib.CreateFlickerSeq(pShip,0.76, fFlickerSpeed = 0.25, sStatus = "On")
		pSequence.Play()


def IsDisabled(pSubSystem):
	if not pSubSystem:
		return FALSE

	iNum=pSubSystem.GetNumChildSubsystems()
	if iNum==0:
		if pSubSystem.IsDisabled():
			return TRUE
		else:
			return FALSE

	for i in range(iNum):
		pChild = pSubSystem.GetChildSubsystem(i)
		if pChild:
			if not pChild.IsDisabled():
				return FALSE
	return TRUE
		

#########################################################################################################################
###	PhalantiumWave:													#
###		0 - Not active												#
###		1 - The effect designed by DreamYard, modified to work with NanoFX aswell				#											#
###	Phalantium Wave and NanoFX are now compatible ;-)								#
#########################################################################################################################

def phalantiumWave(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())

	if pShip==None:
		return

	pExplosion=None

	# phalantium explosion
	
	pTorp= App.Torpedo_Cast(pEvent.GetSource())
	if (TRUE):
		if pShip:
			# hull
			iHDamageMax = pShip.GetHull().GetCondition()
			iHDamage = App.g_kSystemWrapper.GetRandomNumber(iHDamageMax * 0.4)
			# minimal 50% hull damage, ~70% mean, 90% maximal damage to remaining integrity
			pShip.DamageSystem(pShip.GetHull(), (iHDamageMax * 0.5) + iHDamage)
		
			# shields
			pShields = pShip.GetShields()
			if pShields:
				iShDamageMax = pShip.GetShields().GetCondition()
				if iShDamageMax > 1:
					# ~20% chance that this launch will completely destroy the shield system
					iShDamage = App.g_kSystemWrapper.GetRandomNumber(iShDamageMax * 0.25)
					# minimal 80% shield damage, ~90% mean damage to remaining integrity
					pShip.DamageSystem(pShields, (iShDamageMax * 0.8) + iShDamage)

			# sensors
			pSensors = pShip.GetSensorSubsystem()
			if pSensors:
				iSeDamageMax = pSensors.GetCondition()
				if iSeDamageMax > 1:
					# ~10% chance that this launch will completely destroy the shield system
					iSeDamage = App.g_kSystemWrapper.GetRandomNumber(iSeDamageMax * 0.45)
					# minimal 60% sensor damage, ~80% mean damage to remaining integrity
	 				pShip.DamageSystem(pSensors, (iSeDamageMax * 0.6) + iSeDamage)
	
			# many ways of querying subsystems; this is just one of them

			#torpedo tubes
			pTorpSys = pShip.GetTorpedoSystem()

			if pTorpSys:
				# iterate through torpedo launchers
				iNumTubes = pTorpSys.GetNumChildSubsystems()
				for jTube in range(iNumTubes):
					pTorpChild = pTorpSys.GetChildSubsystem(jTube)
					if pTorpChild:
						fToDamageMax = pTorpChild.GetConditionPercentage()
						if fToDamageMax > 0.0:
							# ~30% chance that this launch will completely destroy the launcher system
							fToDamage = App.g_kSystemWrapper.GetRandomNumber(fToDamageMax * 60.0)
	
							# not sure if method clamps, so just to be safe
							if (fToDamage > 40.0):
								fToDamage = 40.0						

							# minimal 60% torpedo tube damage, ~90% mean damage to remaining integrity
							pTorpChild.SetConditionPercentage((fToDamageMax * 0.4) - (fToDamage * 0.01))

			# impulse drive
			pImpSys = pShip.GetImpulseEngineSubsystem()
	
			if pImpSys:
				# iterate through impulse drive units
				iNumImp = pImpSys.GetNumChildSubsystems()
				for iEng in range(iNumImp):
					pImpChild = pImpSys.GetChildSubsystem(iEng)
					if pImpChild:
						fImDamageMax = pImpChild.GetConditionPercentage()
						if fImDamageMax > 0.0:
							# ~17% chance that this launch will completely destroy the engine
							fImDamage = App.g_kSystemWrapper.GetRandomNumber(fImDamageMax * 70.0)

							# not sure if method clamps, so just to be safe
							if (fImDamage > 50.0):
								fImDamage = 50.0

							# minimal 50% impulse powerplant damage, ~80% mean damage to remaining integrity
							pImpChild.SetConditionPercentage ((fImDamageMax * 0.5) - (fImDamage * 0.01))

			# Spin our new hulk
			fRot = App.g_kSystemWrapper.GetRandomNumber(70)
			SetLBRandRotation(pShip, (fRot + 1.0))


		import Custom.NanoFX.NanoFX_Lib
		Custom.NanoFX.NanoFX_Lib.CreateSpecialFXSeq(pObject,pEvent,"Phalantium")


#########################################################################################################################
###	Spatial Charges:												#
###		0 - Not active												#
###		1 - The effect designed by Sneaker, modified to work with NanoFX aswell					#
###	Sneaker and NanoFX are now compatible ;-)									#
#########################################################################################################################

def spatialCharges(pObject,pEvent,pShip=None):
	if pShip==None:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
	
	if pShip==None:
		return

	import Custom.NanoFX.NanoFX_Lib
	Custom.NanoFX.NanoFX_Lib.CreateSpecialFXSeq(pShip,pEvent,"Spatial")

		
#########################################################################################################################
###	IonSubSystem:													#
###		Disables the system and add it the cycleprocessList							#
###															#
#########################################################################################################################			

def IonSubSystem(pSubSystem,tTime,Special=0):
	global g_tIon
	#print "Ionizing Subsystem: ",pSubSystem.GetName()
	if not pSubSystem:
		return

	ID=pSubSystem.GetObjID()

	pSubSystemProp=pSubSystem.GetProperty()

	if g_tIon.has_key(ID):
		t=g_tIon[ID]
		tTime=App.g_kUtopiaModule.GetGameTime()+tTime
		fDisabledAt=t[3]
		fRepairComplex=t[4]
		if not Special==1:
			tTuple=0,tTime,pSubSystem,fDisabledAt,fRepairComplex
		else:
			tTuple=1,tTime,pSubSystem,fDisabledAt,fRepairComplex,t[5],t[6],t[7],t[8],t[9],t[10]
		
		g_tIon[ID]=tTuple
		return
			
	else:
		pSubSystem.SetCondition(0.999*pSubSystem.GetCondition())
		fDisabledAt=pSubSystemProp.GetDisabledPercentage()
		fRepairComplex=pSubSystemProp.GetRepairComplexity()
		pSubSystemProp.SetDisabledPercentage(1.0)
		pSubSystemProp.SetRepairComplexity(10000000)

		if not Special:
			tTime=App.g_kUtopiaModule.GetGameTime()+tTime
			tTuple=0,tTime,pSubSystem,fDisabledAt,fRepairComplex
			g_tIon[ID]=tTuple
			return
	
		if Special==1:
			pShields = pSubSystem.GetParentShip().GetShields()		
			tTime=App.g_kUtopiaModule.GetGameTime()+tTime
			tTuple=1,tTime,pSubSystem,fDisabledAt,fRepairComplex,pShields.GetCurShields(pShields.FRONT_SHIELDS),pShields.GetCurShields(pShields.REAR_SHIELDS),pShields.GetCurShields(pShields.TOP_SHIELDS),pShields.GetCurShields(pShields.BOTTOM_SHIELDS),pShields.GetCurShields(pShields.LEFT_SHIELDS),pShields.GetCurShields(pShields.RIGHT_SHIELDS)
		g_tIon[ID]=tTuple
		return


#########################################################################################################################
###	cycleDisable:													#
###		Corefunction of all the Disable Weapons									#
###		Each second, it iterates of the disabled, list and reenable the sybsystems if necessary			#
###															#
#########################################################################################################################
		
def cycleDisable(pObject,pEvent):
	global g_tIon
		
	for ID in g_tIon.keys():
		tTuple=g_tIon[ID]
		Special=tTuple[0]
		pTime=tTuple[1]

		if(pTime>App.g_kUtopiaModule.GetGameTime()):
			continue
		
		pSubSystem=tTuple[2]
		if not pSubSystem:
			del g_tIon[ID]
			continue

		if pSubSystem.GetCondition()<=0.0 or pSubSystem.GetParentShip().GetHull().GetCondition()<=0:
			del g_tIon[ID]
			continue
				
		pSubSystemProp=pSubSystem.GetProperty()
		pSubSystemProp.SetDisabledPercentage(tTuple[3])
		pSubSystemProp.SetRepairComplexity(tTuple[4])
		pSubSystem.SetCondition(1.0001*pSubSystem.GetCondition())
		

		if Special==1:
			pShields = pSubSystem.GetParentShip().GetShields()
			pShields.SetCurShields(pShields.FRONT_SHIELDS,tTuple[5])
			pShields.SetCurShields(pShields.REAR_SHIELDS,tTuple[6])
			pShields.SetCurShields(pShields.TOP_SHIELDS,tTuple[7])
			pShields.SetCurShields(pShields.BOTTOM_SHIELDS,tTuple[8])
			pShields.SetCurShields(pShields.LEFT_SHIELDS,tTuple[9])
			pShields.SetCurShields(pShields.RIGHT_SHIELDS,tTuple[10])

		pShip=pSubSystem.GetParentShip()
		SID=pShip.GetObjID()
		pPlayer=MissionLib.GetPlayer()
		PID=pPlayer.GetObjID()

		pTest=pSubSystem.GetParentSubsystem()
		if pTest:
			pSubSystem=pTest
		
		if PID==SID and not pSubSystem.IsDisabled():
			if pSubSystem.IsTypeOf(App.CT_SENSOR_SUBSYSTEM):
				ATP_BridgeFX.MakeCharacterSay("Brex","SelfSensorsOnline")
			elif pSubSystem.IsTypeOf(App.CT_WARP_ENGINE_SUBSYSTEM):
				ATP_BridgeFX.MakeCharacterSay("Brex","SelfWarpOnline")
			elif pSubSystem.IsTypeOf(App.CT_IMPULSE_ENGINE_SUBSYSTEM):
				ATP_BridgeFX.MakeCharacterSay("Brex","SelfImpulseOnline")
			elif pSubSystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
				ATP_BridgeFX.MakeCharacterSay("Brex","SelfShieldsOnline")

		del g_tIon[ID]

	

#########################################################################################################################
#	DepleteType Decoder:												#
#															#
#	DepleteType:													#
#		0 - Normal Behaviour											#
#		1 - Will deplete the torpedo with a 100-DepletionPerSecond(%) factor.					#
#		    When DepleteAtPercentage(%) of the original damage is reached, the torpedo is lost			#
#########################################################################################################################

def DepleteTypeDecoder(pObject,pEvent,pTorp=None):
	if pTorp==None:
		pTorp=App.Torpedo_Cast(pEvent.GetSource())
		
	if pTorp==None:
		return

	pModuleName=pTorp.GetModuleName()
	pModule = __import__(pModuleName)
	
	try:
		DepleteType=pModule.DepleteType
	except:
		return

	global g_depleteHandleList

	if(DepleteType==0):
		return	

	try:
		DepleteAtPercentage=pModule.DepleteAtPercentage
	except:
		DepleteAtPercentage=15

	try:
		DepletionPerSecond=pModule.DepletionPerSecond
	except:
		DepletionPerSecond=10
	
	if not DepleteType==1:
		#print "Error in depleteTypeDecoder: Unknown DepleteType for Torpedo: ", pTorp.GetModuleName()
		pass
		
	try:
		DepleteColour=pModule.DepleteColour
	except:
		DepleteColour=0
	
	try:
		DepleteShrink=pModule.DepleteShrink
	except:
		DepleteShrink=0
	
	try:
		statsTuple=pModule.GraphicsTuple
	except:
		#print "Error in depleteTypeDecoder: GraphicsTuple not specified for Torpedo: ", pTorp.GetModuleName()	
		return

	#DepletionPerSecond=(1.0-math.pow((1.0-DepletionPerSecond/100.0),0.25))*100.0
	
	if(DepleteColour!=0 and DepleteShrink!=0):
		tTuple=4,pTorp.GetObjID(),1.0-DepletionPerSecond/100.0,DepleteAtPercentage/100.0*pTorp.GetDamage(),pTorp.GetDamage(),statsTuple
		g_depleteHandleList.append(tTuple)
		return
	
	if(DepleteColour!=0):
		tTuple=2,pTorp.GetObjID(),DepletionPerSecond,DepleteAtPercentage/100.0*pTorp.GetDamage(),pTorp.GetDamage(),statsTuple
		g_depleteHandleList.append(tTuple)
		return
		
	if(DepleteShrink!=0):
		DepletionPerSecond=(1.0-math.pow((1.0-DepletionPerSecond/100.0),0.25))
		tTuple=3,pTorp.GetObjID(),DepletionPerSecond,DepleteAtPercentage/100.0*pTorp.GetDamage(),pTorp.GetDamage(),statsTuple
		g_depleteHandleList.append(tTuple)
		return
	
	if (TRUE):
		tTuple=1,pTorp.GetObjID(),DepletionPerSecond,DepleteAtPercentage/100.0*pTorp.GetDamage()
		g_depleteHandleList.append(tTuple)
	
	
#########################################################################################################################
##	DepleteType Cyclic Function											#
##															#
#########################################################################################################################

def cycleDepleteType(pObject,pEvent):
	global g_depleteHandleList
	
	j=0
	for i in g_depleteHandleList:
		tTuple=g_depleteHandleList[j]
		j=j+1

		flag=tTuple[0]
		pTorp=App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(tTuple[1]))
		
		if pTorp==None:
			j=j-1
			g_depleteHandleList.pop(j)
			continue

		damage=pTorp.GetDamage()

		if damage<tTuple[3]:
			j=j-1
			pTorp.SetLifetime(0.0)
			g_depleteHandleList.pop(j)
			continue

		if(flag==1):
			continue

		
		fRatio=0.2+(damage-tTuple[3])/(tTuple[4]-tTuple[3])*0.8

		statsTuple=tTuple[5]

		if(flag==3):
			kCoreColor = App.TGColorA()
			kCoreColor.SetRGBA(statsTuple[1][0], statsTuple[1][1],statsTuple[1][2], statsTuple[1][3])
			kGlowColor = App.TGColorA()
			kGlowColor.SetRGBA(statsTuple[5][0],statsTuple[5][1], statsTuple[5][2], statsTuple[5][3])
			kFlareColor = App.TGColorA()
			kFlareColor.SetRGBA(statsTuple[10][0],statsTuple[10][1], statsTuple[10][2], statsTuple[10][3])
		if(flag==2 or flag==4):
			kCoreColor = App.TGColorA()
			kCoreColor.SetRGBA((2-fRatio)*statsTuple[1][0], fRatio*statsTuple[1][1], 0, fRatio*statsTuple[1][3])
			kGlowColor = App.TGColorA()
			kGlowColor.SetRGBA((2-fRatio)*statsTuple[5][0], fRatio*statsTuple[5][1], 0, fRatio*statsTuple[5][3])
			kFlareColor = App.TGColorA()
			kFlareColor.SetRGBA((2-fRatio)*statsTuple[10][0], fRatio*statsTuple[10][1], 0, fRatio*statsTuple[10][3])

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetParentID()))
		## Create a new torpedo
		pNewTorp = FireTorpFromPointWithVector(	pTorp.GetWorldLocation(),
							pTorp.GetWorldForwardTG(),
							pTorp.GetModuleName(),
							pTorp.GetTargetID(),
							pShip,
							pTorp.GetVelocityTG().Length(),
							pShip.GetTargetOffsetTG()
						      )

		if flag==3 or flag==4:
			pNewTorp.CreateTorpedoModel(statsTuple[0],kCoreColor,fRatio*statsTuple[2],statsTuple[3],statsTuple[4],kGlowColor,statsTuple[6],fRatio*statsTuple[7],fRatio*statsTuple[8],statsTuple[9],kFlareColor,statsTuple[11],fRatio*statsTuple[12],statsTuple[13])			
		if flag==2:
			pNewTorp.CreateTorpedoModel(statsTuple[0],kCoreColor,statsTuple[2],statsTuple[3],statsTuple[4],kGlowColor,statsTuple[6],statsTuple[7],statsTuple[8],statsTuple[9],kFlareColor,statsTuple[11],statsTuple[12],statsTuple[13])			

		pNewTorp.SetDamage(tTuple[2]*damage)

		## The old torpedo is gone
		pTorp.SetLifetime(0.0)








#########################################################################################################################
#	Advanced Technologies GUI											#
#															#
#	The great experiment!!!!! 	All turning out good for now ;-)						#
#															#
#															#
#########################################################################################################################

def CycleAdjustSpecialPower(pObject,pEvent):
	for ID,I in g_SpecialActive.keys():
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ID))
		if not pShip:
			del g_SpecialActive[ID,I]
			continue

		if I==CORBONITE_REFLECTOR:
			if not HasSufficientSpecialPower(pShip,g_SpecialActive[ID,I]):
				SetCorboniteOff(pShip)
				if pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
					ATP_WeaponsControl.CorboniteSetOffNoArg()
					continue
			AdjustSpecialPower(pShip,g_SpecialActive[ID,I])

		elif I==PHASE_CLOAK:
			if not HasSufficientSpecialPower(pShip,g_SpecialActive[ID,I]):
				SetPhaseCloakOff(pShip)
			AdjustSpecialPower(pShip,g_SpecialActive[ID,I])
				
		


def HasSufficientSpecialPower(pShip,fDrain):
	global g_specialPowerDict
	
	ID=pShip.GetObjID()

	if not g_specialPowerDict.has_key(ID):
		return FALSE

	if g_specialPowerDict[ID][0]-fDrain>0:
		return TRUE
	else:
		return FALSE


def createNewEntryForSpecialPower(pShip):
	global g_specialPowerDict
		
	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
	except:
		return

	try:
		SpecialPowerCapacity=pModule.SpecialPowerCapacity()
		if SpecialPowerCapacity<=0:
			SpecialPowerCapacity=0.0
	except:
		SpecialPowerCapacity=2250.0
		
	try:
		SpecialPowerRecharge=pModule.GetSpecialPowerRecharge()
	except:
		SpecialPowerRecharge=40.0
			
	g_specialPowerDict[pShip.GetObjID()]=SpecialPowerCapacity*1.0,SpecialPowerCapacity*1.0,SpecialPowerRecharge*1.0



def AdjustSpecialPower(pShip,fDrain):
	global g_specialPowerDict
	
	ID=pShip.GetObjID()

	if not g_specialPowerDict.has_key(ID):
		return

	fCur=g_specialPowerDict[ID][0]
	fMax=g_specialPowerDict[ID][1]
	fRec=g_specialPowerDict[ID][2]
	fVal=fCur-fDrain
	

	if fVal>=0.0 and fVal<=fMax:
		g_specialPowerDict[ID]=fVal,fMax,fRec
	elif fVal<0.0:
		g_specialPowerDict[ID]=0.0,fMax,fRec
	else:
		g_specialPowerDict[ID]=fMax,fMax,fRec

	

def cycleSpecialPower(pObject,pEvent):
	global g_specialPowerDict

	pPlayer=MissionLib.GetPlayer()
	if not pPlayer:
		return

	PID=pPlayer.GetObjID()
	
	for ID in g_specialPowerDict.keys():
		pShip=App.TGObject_GetTGObjectPtr(ID)
		if not pShip:
			del g_specialPowerDict[ID]
			continue
		pShip=App.ShipClass_Cast(pShip)
		if not pShip:
			del g_specialPowerDict[ID]
			continue

		fCur=g_specialPowerDict[ID][0]
		fMax=g_specialPowerDict[ID][1]
		fRec=g_specialPowerDict[ID][2]
		fRatio=pShip.GetPowerSubsystem().GetConditionPercentage()

		fCur=fCur+fRatio*fRec
		if fCur>fMax*fRatio:
			fCur=fMax*fRatio

		g_specialPowerDict[ID]=fCur,fMax,fRec
	
		if fMax*fRatio!=0.0:
			fVal=fCur/(fMax*fRatio)
		else:
			fVal=0.0

		if ID==PID:
			#continue
			ATP_PowerDisplay.UpdateSpecialPowerWindow(fVal,fRatio)
		
		
		
		 

	

#########################################################################################################################
#	Advanced Technologies Tools											#
#															#
#	The explicit codes for the the Tools used by Functions								#
#															#
#															#
#########################################################################################################################

def CheckFlag(pShip,iVal):
	global g_StatusDict

	ID = pShip.GetObjID()
	if not g_StatusDict.has_key(ID):
		return FALSE

	i = g_StatusDict[ID]
	j = 1 << iVal

	return i & j

def SetFlag(pShip,iVal):
	global g_StatusDict

	ID = pShip.GetObjID()
	if not g_StatusDict.has_key(ID):
		return

	i = g_StatusDict[ID]
	g_StatusDict[ID] = i | (1 << iVal)

def ResetFlag(pShip,iVal):
	global g_StatusDict

	ID = pShip.GetObjID()
	if not g_StatusDict.has_key(ID):
		return

	i = g_StatusDict[ID]
	g_StatusDict[ID] = i & ( 0xFFFFFFFF ^ (1 << iVal) )
	
	
def positionSelectorShip(pShip,p):	
	a=pShip.GetAffiliation()
	return positionSelector(a,p)

def positionSelector(a,p):
	P=pow(10,p)
	n=(a-(a/P)*P)/(P/10)
	return n

def positionSelectorShipBoolean(pShip,p,n):
	bFlag=0
	if(positionSelectorShip(pShip,p)==n):
		bFlag=1
	return bFlag
		

def pow(x,y):	
	#BC Python lacks the pow so I need to declare it explicitely  ---> I was wrong (cfr. import math) ... but I like my old solution
	n=x
	i=1
	if(y<0):
		n=0
	if(y==0):
		n=1
	if(y==1):
		n=x
	while((y-i)>0):
		n=n*x
		i=i+1
	return n


def powerTest(pShip,a):
	#Just for debugging, to see how far a def goes without errors
	if(a<0 or a>1):
		a=0.5
	pPower = pShip.GetPowerSubsystem()
	if (pPower != None):
		pPower.SetMainBatteryPower(a*pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(a*pPower.GetBackupBatteryLimit())


def FireTorpFromPoint(kPoint,kNormal,pcTorpScriptName, idTarget ,pShip,idTargetSubsystem = App.NULL_ID,fSpeed = 0.0,pcSetName = None):

	# This is an slightly altered version of the original definition (MissionLib.py) , to suit specific needs

	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet == None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	
	pTorp.SetParent(pShip.GetObjID())

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()
	
	kVelocity = pTorp.GetWorldForwardTG()

	# Give the torpedo an appropriate speed.
	if (fSpeed == 0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)
	
	return pTorp


def FireTorpFromPointWithVector(kPoint,kVector,pcTorpScriptName, idTarget ,pShip,fSpeed,TGOffset=None):

	# This is an slightly altered version of the original definition (MissionLib.py) , to suit specific needs

	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
	pSet = pTarget.GetContainingSet()
	if not pSet:
		return None
	
	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)
	if not TGOffset:
		pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
	else:
		pTorp.SetTargetOffset(TGOffset)
	pTorp.SetParent(pShip.GetObjID())

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)
	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	kTorpLocation = pTorp.GetWorldLocation()
	kTargetLocation = pTarget.GetWorldLocation()

	kTargetLocation.Subtract(kTorpLocation)
	kFwd = kTargetLocation
	kFwd.Unitize()
	kPerp = kFwd.Perpendicular()
	kPerp2 = App.TGPoint3()
	kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
	pTorp.AlignToVectors(kFwd, kPerp2)
	pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kSpeed=copyVector(kVector)
	kSpeed.Unitize()
	kSpeed.Scale(fSpeed)
	pTorp.SetVelocity(kSpeed)

	return pTorp

def shieldDistributePos(pShip,fDamage):
	i=0
	L=[0.0,0.0,0.0,0.0,0.0,0.0]
	iNumber=6.0
	fYield=fDamage

	pShields=pShip.GetShields()

	if ((pShields != None) and (fYield>0) ):
		while((iNumber>0) and (fYield>0)):
			i=0
			fSum=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fAdd=fYield/iNumber+pShields.GetCurShields(ShieldDir)
				fMax=pShields.GetMaxShields(ShieldDir)
				fExcess=0

				if (L[i]<=0.0):
					if(fAdd<fMax):
						pShields.SetCurShields(ShieldDir,fAdd)
					else:
						pShields.SetCurShields(ShieldDir,fMax)					
						fExcess=fAdd-fMax
						fSum=fSum+fExcess
						L[i]=fExcess
				i=i+1

			fYield=fSum
			
			iNumber=L.count(0.0)
			

def shieldDistributeNeg(pShip,fDamage):
	i=0
	L=[0.0,0.0,0.0,0.0,0.0,0.0]
	iNumber=6.0
	fYield=fDamage

	pShields=pShip.GetShields()

	if ((pShields != None) and (fYield>0) ):
		while((iNumber>0) and (fYield>0)):
			i=0
			fSum=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fSus=pShields.GetCurShields(ShieldDir)-fYield/iNumber
				fExcess=0

				if (L[i]<=0.0):
					if(fSus>0):
						pShields.SetCurShields(ShieldDir,fSus)
					else:
						pShields.SetCurShields(ShieldDir,0.0)					
						fExcess=(-1.0)*fSus
						fSum=fSum+fExcess
						L[i]=fExcess
				i=i+1

			fYield=fSum
			
			iNumber=L.count(0.0)



def AreEnemies(pShip1,pShip2):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pFriendlies= pMission.GetFriendlyGroup()
	pEnemies= pMission.GetEnemyGroup()
	
	pAttackerGroup=0
	pShipGroup=0
	
	if IsEnemy(pShip1):
		pShipGroup=1
	elif IsFriend(pShip1):
		pShipGroup=2
	
	if IsEnemy(pShip2):
		pAttackerGroup=1
	elif IsFriend(pShip2):
		pAttackerGroup=2

	if pAttackerGroup==0 or pShipGroup==0:
		return FALSE

	return(pAttackerGroup!=pShipGroup)

def IsEnemy(pShip):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies= pMission.GetEnemyGroup()
	return(pEnemies.IsNameInGroup(pShip.GetName()))

def IsFriend(pShip):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pFriendlies= pMission.GetFriendlyGroup()
	return(pFriendlies.IsNameInGroup(pShip.GetName()))


def makeFriendShipList(pSet=None):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pFriendlies= pMission.GetFriendlyGroup()
	
	pPlayer = MissionLib.GetPlayer ()
	pPlayerID=pPlayer.GetObjID()
	
	g_FriendShipList=[]

	if pFriendlies!=None:
		if(pSet==None):
			ObjTuple = pFriendlies.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pFriendlies.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					g_FriendShipList.append(pObj.GetObjID())

	return g_FriendShipList[:]

def makeEnemyShipList(pSet=None):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies= pMission.GetEnemyGroup()
	pPlayer = MissionLib.GetPlayer ()
	pPlayerID=pPlayer.GetObjID()
	
	g_EnemyShipList=[]

	if pEnemies!=None:
		if(pSet==None):
			ObjTuple = pEnemies.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pEnemies.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					g_EnemyShipList.append(pObj.GetObjID())

	return g_EnemyShipList[:]

def makeNeutralShipList(pSet=None):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pNeutral= pMission.GetNeutralGroup()
	pPlayer = MissionLib.GetPlayer ()
	pPlayerID=pPlayer.GetObjID()
	
	g_NeutralShipList=[]

	if pNeutral!=None:
		if(pSet==None):
			ObjTuple = pNeutral.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pNeutral.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					g_NeutralShipList.append(pObj.GetObjID())
	
	return g_NeutralShipList[:]
	

def distanceSort(List,kPoint,fMax=0):
	distanceDict={}

	for i in List:
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
		kTemp=App.TGPoint3()
		kTemp=pShip.GetWorldLocation()
		kTemp.Subtract(kPoint)
		fKey=kTemp.Length()
		if fMax==0:
			distanceDict[fKey]=i
		elif fKey<=fMax:
			distanceDict[fKey]=i

	keylist=distanceDict.keys()
	keylist.sort()
	
	RetList=[]

	for i in keylist:
		RetList.append(distanceDict[i])

	return RetList[:]

def GetDebrisListInSet(pSet=None):
	if pSet==None:
		pPlayer = MissionLib.GetPlayer()
		pSet=pPlayer.GetContainingSet()
	
	RetList=[]

	pFirst=pSet.GetFirstObject()
	pObject=pSet.GetNextObject(pFirst.GetObjID())

	i=0
	while pObject:
		i=i+1
		if pObject.IsTypeOf(App.CT_BASE_OBJECT):
			RetList.append(pObject)

		pObject=pSet.GetNextObject(pObject.GetObjID())

		if pObject.GetObjID()==pFirst.GetObjID():	
			break
		if i>1000:
			print "OVERFLOW"
			break

	return (RetList[:])
	
def CreateEnemyAI(pShip):
	ATP_QuickBattleAI.CreateAI(pShip)

def CreateFriendAI(pShip):
	ATP_QuickBattleFriendlyAI.CreateAI(pShip)

		
def copyVector(kVect):
	kCopy=App.TGPoint3()		
	kCopy.SetXYZ(kVect.GetX(),kVect.GetY(),kVect.GetZ())
	return kCopy

def toDegree(a):
	return a*180.0/math.pi	
 	
def callFloatEvent(eventType,fFloat):
	pEvent = App.TGEvent_Create()
	pEvent.SetFloat(fFloat)
	pEvent.SetEventType(eventType)
	MissionLib.GetMission().ProcessEvent(pEvent)


def StopShip(pShip):
	pPlayer=MissionLib.GetPlayer()
	
	if not pShip or not pPlayer:
		return

	if pShip.GetObjID()==pPlayer.GetObjID():
		if MissionLib.GetPlayerShipController() == "Tactical":
			import Bridge.TacticalMenuHandlers
			Bridge.TacticalMenuHandlers.g_iOrderState = Bridge.TacticalMenuHandlers.EST_ORDER_STOP
			Bridge.TacticalMenuHandlers.UpdateOrders(0)	# No acknowledgement.
			return

	S=App.TGPoint3()
	S.SetXYZ(0.0,0.0,0.0)

	pShip.SetVelocity(S)
	pShip.SetAngularVelocity(S, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
	pShip.SetAcceleration(S)
	pShip.SetAngularAcceleration(S)
	pShip.SetUsePhysics(FALSE)


def HasOffensiveTractors(pShip):
	if not pShip:
		return FALSE
	pTractorSys=pShip.GetTractorBeamSystem()
	if not pTractorSys:
		return FALSE
	iChildren = pTractorSys.GetNumChildSubsystems()

	for i in range(iChildren):
		pProjector = App.EnergyWeapon_Cast(pTractorSys.GetChildSubsystem(i))
		pSound=pProjector.GetFireSound()
				
		if pSound=="UCB":
			return TRUE
		elif pSound=="INV":
			return TRUE	
		elif pSound=="TechAssimilationBeam":
			return TRUE
		elif pSound=="ShipAssimilationBeam":
			return TRUE
	return FALSE
		


#################################################################################
#	Various Corbonite Functions						#
#	Args: the names speak for themselves					#
#	Return: TRUE it is a valid Corbonite Hit else FALSE			#
#################################################################################

def IsCorboniteHitEvent(pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	res=FALSE
	while(TRUE):
		if(positionSelectorShip(pShip,5)>=1.0):
			if  not (pEvent.IsHullHit()):
				try:
					pTorp= App.Torpedo_Cast(pEvent.GetSource())
					pTorpPath=pTorp.GetModuleName()
				except:
					break

				life=pTorp.GetGuidanceLifeTime()

				if(positionSelectorShipBoolean(pShip,5,1) and life==0.0):
					break

				res=TRUE
		break
	return res

def IsPlayerCorbonite():
	pPlayer=MissionLib.GetPlayer()
	if not positionSelectorShip(pPlayer,5)>0:
		return FALSE
	return TRUE

def SetCorboniteOff(pShip):
	global g_SpecialActive
	if g_SpecialActive.has_key(pShip.GetObjID(),CORBONITE_REFLECTOR):
		del g_SpecialActive[pShip.GetObjID(),CORBONITE_REFLECTOR]
	pAff=pShip.GetAffiliation()
	pAff=pAff-40000
	pShip.SetAffiliation(pAff)

def CorboniteWentOn(pObject,pEvent):
	SetCorboniteOn(MissionLib.GetPlayer())

def CorboniteWentOff(pObject,pEvent):
	SetCorboniteOff(MissionLib.GetPlayer())

def SetCorboniteOn(pShip):
	global g_SpecialActive
	g_SpecialActive[pShip.GetObjID(),CORBONITE_REFLECTOR]=80.0
	pAff=pShip.GetAffiliation()
	pAff=pAff+40000
	pShip.SetAffiliation(pAff)



#################################################################################
#	Various Ablative Armour	Functions					#
#	Args: the names speak for themselves					#
#										#
#################################################################################

def HasAblativeArmour(pShip):
	return (positionSelectorShip(pShip,3))

def GetAblativeArmour(pShip):
	succes=FALSE
	pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Ablative Armour"):
			succes=TRUE
			break
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)

	if succes:
		return pSubsystem
	else:
		return None


def RegisterShipForArmourBar(ID,pHealthGauge):
	g_ArmourBarDict[ID]=pHealthGauge
	
	