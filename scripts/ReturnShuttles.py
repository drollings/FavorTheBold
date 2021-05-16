#!/usr/bin/python1.5
## This Mod was created by Defiant <mail@defiant.homedns.org>
## and is under the GNU GPL License (see README)!
## 
## Basic TractorTargetDocked() and TractorBeamOn() are from the SDK and
## some parts of GetShuttlesInBay(), IncreaseShuttleCount() and ShuttlesInBayOfThisType()
## are copied from sleight42 Shuttle Launching Framework.
##
## SetMaxShuttlesInBay() & GetOEPs() by Sim Rex
## Quote by Sim Rex: "btw, I have no idea what the ftb guys were smoking when they came up
## with this very convoluted way of launching stuff...."
##
# Functions:
# GetShuttlesInBay()	-	Returns the count of _all_ Shuttles in all bays
#	Arguments: sFiringShipName (The Name of the Carrer Ship)
# IncreaseShuttleCount()	-	Add a Ship to the Carrier
#	Arguments: Shuttle (The name of the Ship we want to add)
# GetShuttleBaySize()	-	Returns the Shuttle bay size
#	Arguments: pShip (Shipclass)
# ShuttlesInBayOfThisType()	-	Returns the count of Shuttles in the bay.
#	Arguments: Type (Ship Type)
# FindAShuttleBay()	-	Returns the first Shuttle bay Hull Property
#	Arguments: pShip (Shipclass)
# SetMaxShuttlesInBay()	-	Returns how much Shuttles a Ship can carry
#	Arguments: OurShipName (The Name of the Carrer Ship)
# GetOEPs()		-	Returns the whole OEP list.
# GetFirstShuttleBayName()	-	Returns the name of the first Shuttle Bay
# GetIgnoredTractors()	-	Tractors not to use for docking
#	Arguments: OurShipName (The Name of the Carrer Ship)
# Transport()		-	Changes the Players Ship with a Sequence
# TractorTargetDocked()	-	Event handler called when tractor target has docked with ship.
#	Arguments: pObject, pEvent
# TractorBeamOn()		-	Event handler called when tractor beam starts hitting a target.
#	Arguments: pObject, pEvent
# ReturnWithoutTractor()	-	Same as TractorTargetDocked() but without Tractors. Maybe called by a button
#	Arguments: pObject, pEvent, NotHost (If the Player's Ship is not the Host set to 1, standard 0)
##
## Have Fun!

import App
import MissionLib
import string
import ftb.ShipManager
import ftb.LaunchShipHandlers
import AI.Compound.ReturnShuttle

# Global Vars
verbose                 = 0 # Be verbose
g_pMissionDatabase      = None

# dics
EventToShip_dic         = {}
ShuttleBayInUse_dic     = {}

# Events - we set them up later.
SHUTTLE_COUNT_TIMER     = None


# Here we Count the Shuttles in our Bay
# Basicly copied from the Shuttle Launching Framework by sleight42 (ftb.LaunchShipHandlers.AddLaunchButtons() )
def GetShuttlesInBay(sFiringShipName = None):
        global verbose
        
        if not sFiringShipName:
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
            
        pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
        pLaunchers = pCarrier.GetLaunchers()
        numTypes = len( pLaunchers)
        for index in range( numTypes):
                launchType = pLaunchers[index].GetLaunchType()
                if (string.find(str(launchType), 'Mine') == "-1"):
                        numLaunches = pLaunchers[index].GetNumLaunches( launchType)
                else:
                        numLaunches = 0

                launchType = pLaunchers[index].NextLaunchType()
                firstlaunchType = None
        
                i = 0
                while (launchType != firstlaunchType):
                        if (launchType != firstlaunchType): #and string.find(str(launchType), 'Mine') == "-1"):
                                numLaunches =  numLaunches + pLaunchers[index].GetNumLaunches(launchType)
                        if (i == 0):
                                firstlaunchType = launchType
                        launchType = pLaunchers[index].NextLaunchType()
                        if ( i > 10 ):
                        # This makes sure the Game is not crashing if we have 0 Shuttles in Bay.
                                return 0
                        i = i + 1

	return numLaunches


# Returns the Shiptype
def GetShipType(ShipName):
        return string.split(MissionLib.GetShip(ShipName).GetScript(), '.')[1]


# Start the Timer
def IncreaseShuttleCountStartTimer(Shuttle, sFiringShipName = None):
        global SHUTTLE_COUNT_TIMER, EventToShip_dic, ShuttleBayInUse_dic

	# Small test if the Tractor Firing Ship is not the Players Ships
	if (Shuttle == App.Game_GetCurrentGame().GetPlayer().GetName()):
		# then Beam
		Transport(sFiringShipName)

        ShuttleType = GetShipType(Shuttle)

        if (ShuttleType == "EscapePod"):
            # Pods won't be addded to the Launcher
            return

        # If verbose add them without timer - faster for working on it.
        if verbose:
            IncreaseShuttleCount(ShuttleType, sFiringShipName)
            return
	
        # Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(SHUTTLE_COUNT_TIMER)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

        # Save the Ships into the dic here
        EventToShip_dic[str(pTimerEvent)] = [ShuttleType, sFiringShipName]
        # Lock the bay
        ShuttleBayInUse_dic[sFiringShipName] = 1

	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 10 + App.g_kSystemWrapper.GetRandomNumber(10))
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)


# Timer finished, find the Ships and pass it to IncreaseShuttleCount()
def IncreaseShuttleCountStartInit(pObject, pEvent):
    global EventToShip_dic, verbose, ShuttleBayInUse_dic
    # Now get the Event in our dic and grep the Ships out.
    if not EventToShip_dic.has_key(str(pEvent)):
        print("ReturnShuttles: IncreaseShuttleCountStartInit called by nothing?", EventToShip_dic.keys())
        return
    ShuttleType = EventToShip_dic[str(pEvent)][0]
    sFiringShipName = EventToShip_dic[str(pEvent)][1]
    if verbose: print("Ships from Timer are: ", ShuttleType, sFiringShipName)
    # finally delete the dic.
    del EventToShip_dic[str(pEvent)]
    del ShuttleBayInUse_dic[sFiringShipName]
    # yeehah we are done with the timer.
    IncreaseShuttleCount(ShuttleType, sFiringShipName)
    ReturnShuttlesSay("ShipAdded", "Science")


# Now the hard Work with the ftb begins!
def IncreaseShuttleCount(ShipType, sFiringShipName = None):
        global verbose
        if verbose: print("Trying to increase Shuttle Count")

        if (sFiringShipName == None):
                if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
                sFiringShipName = App.Game_GetCurrentPlayer().GetName()
        
        ShuttleCount = ShuttlesInBayOfThisType(ShipType, sFiringShipName)
        if verbose: print("ShipType:", ShipType, "ShipCount1: ", ShuttleCount)
        pShip = MissionLib.GetShip(sFiringShipName)

	# Thats from the Carrier System config by Sleight42
	launcher = ftb.LauncherManager.GetLauncher(GetFirstShuttleBayName(sFiringShipName), pShip)
	launcher.AddLaunchable(ShipType, "QuickBattle.QuickBattleFriendlyAI", 1)

        # There maybe a Problem with some Carrier configurations, correct those
        if (ShuttleCount >= ShuttlesInBayOfThisType(ShipType, sFiringShipName)):
                if verbose: print("ShipCount Problem: ", ShuttlesInBayOfThisType(ShipType, sFiringShipName))
                launcher.AddLaunchable(ShipType, "QuickBattle.QuickBattleFriendlyAI", ShuttleCount + 1)

	# and finally reload the Button - yeah we fixed the damm Problem!
	ftb.LaunchShipHandlers.SetToggleLaunchButton()
	if verbose: print("ShipCount2: ", ShuttlesInBayOfThisType(ShipType, sFiringShipName))
		

# just a split of the old GetShuttleBay()
def GetShuttleBaySize(OurShipName, pShip):
        ShuttleBaySize = FindAShuttleBay(pShip)
        if ShuttleBaySize:
                return ShuttleBaySize.GetRadius()
        return 0


# This make sure we don't destroy the other Shuttles in this Bay
# Its mostly the same like GetShuttlesInBay(), so also from the Shuttle Launching Framework by sleight42.
def ShuttlesInBayOfThisType(Type, sFiringShipName = None):
        global verbose
        
        if (sFiringShipName == None):
                if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
                sFiringShipName = App.Game_GetCurrentPlayer().GetName()
            
        pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
        pLaunchers = pCarrier.GetLaunchers()
        numTypes = len( pLaunchers)
        for index in range( numTypes):
                launchType = None
                i = 0
                while (launchType != Type):
                        if verbose: print(Type, launchType)
                        launchType = pLaunchers[index].NextLaunchType()
                        numLaunches =  pLaunchers[index].GetNumLaunches( launchType)
                        if ( i > 10 ):
                        # Stop crashing Stupid Game
                                return 0
                        i = i + 1

	return numLaunches
	

# Actually based on MissionLib().FindShuttleBay()
def FindAShuttleBay(pShip):
	iShipID = pShip.GetObjID()

	pPropSet = pShip.GetPropertySet()
	pHullPropInstanceList = pPropSet.GetPropertiesByType(App.CT_HULL_PROPERTY)
	
	pHullPropInstanceList.TGBeginIteration()
	iNumItems = pHullPropInstanceList.TGGetNumItems()
	
	pLaunchProperty = None

	for i in range(iNumItems):
		pInstance = pHullPropInstanceList.TGGetNext()

		# Check to see if the property for this instance is a Hull Property
		pProperty = App.HullProperty_Cast(pInstance.GetProperty())

		if (pProperty != None):
			if ( pProperty.GetName().CompareC("Shuttle", 1) != -1 ):
				pHullPropInstanceList.TGDoneIterating()
				pHullPropInstanceList.TGDestroy()
				return(pProperty)


#How much Shuttles can we get in our Bay?
# Created by Sim Rex
def SetMaxShuttlesInBay(OurShipName):
    pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(OurShipName))
    if hasattr(pCarrier, "GetMaxShuttles"):
        iMaxShuttles = pCarrier.GetMaxShuttles()
    else:
        iMaxShuttles = 10
    return iMaxShuttles


# Created by Sim Rex
# Quote: Took far too long to work that out.. 
# It's a shame that the BC Python version doesn't have the very useful help() function...
# Would've saved me a lot of opening and closing of BC...
def GetOEPs(sFiringShipName = None):
        global verbose
        
        if not sFiringShipName:
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
            
	pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
	if not hasattr(pCarrier, "GetLaunchers"):
            return
        pFTBLaunchers = pCarrier.GetLaunchers() 
	OEPList = [] 
	for launcher in pFTBLaunchers: 
		OEPs = launcher.GetLaunchers() 
		OEPList = OEPList + OEPs 
	return OEPList


# Just give me the name of our first Shuttle Bay plz:
def GetFirstShuttleBayName(sFiringShipName = None):
        global verbose
        
        if not sFiringShipName:
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()

	ShuttleBayName = GetOEPs(sFiringShipName) #calling Sim Rex's Function
        if not ShuttleBayName:
            return
	return ShuttleBayName[0] # yes, thats the easy Version ;)


# next Shuttle Bay:
def GetNextShuttleBayName(sFiringShipName, LastBay):
	ShuttleBayNames = GetOEPs(sFiringShipName) #calling Sim Rex's Function
        if not ShuttleBayNames:
            return
        i = 0
        for i in range (len(ShuttleBayNames)):
                if (ShuttleBayNames[i] == LastBay):
                    if (i + 1 < len(ShuttleBayNames)):
                        return ShuttleBayNames[i + 1]
                    else:
                        return ShuttleBayNames[0]


# Modified Version of  Sim Rex's SetMaxShuttlesInBay()
def GetIgnoredTractors(OurShipName):
	global sFiringShipName, verbose
        
        if not sFiringShipName:
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
            
	pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
	if hasattr(pCarrier, "IgnoreTractors"):
		return pCarrier.IgnoreTractors()
	else:
		return []


def Transport(sFiringShipName = None):
	global verbose
        
        if (sFiringShipName == None):
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
	
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.Game_GetCurrentPlayer()

	pSequence = App.TGSequence_Create()
	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
	pSequence.AppendAction (pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
	pSequence.AppendAction(pAction)
	pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName ())
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pSet.GetName(), sFiringShipName)
	pSequence.AppendAction(pAction)
	pSequence.AppendAction(pGame.SetPlayer(MissionLib.GetShip(sFiringShipName)))
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet().GetName ())
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
	pSequence.AppendAction(pAction)
	pSequence.Play()

        # clear AI
        pPlayer = pGame.GetPlayer()
        MissionLib.SetPlayerAI("Captain", None)
        pPlayer.ClearAI()


def ReturnShuttlesSay(SayString, Person = "Felix"):
        global g_pMissionDatabase
        pBridge = App.g_kSetManager.GetSet('bridge')
        g_pScience = App.CharacterClass_GetObject(pBridge, "Science")
        g_pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
        g_pBrex	= App.CharacterClass_GetObject(pBridge, "Engineer")

        if (Person == "Science"):
            Person = g_pScience
        elif (Person == "Brex"):
            Person = g_pBrex
        else:
            Person = g_pFelix

        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(Person, App.CharacterAction.AT_SAY_LINE, SayString, None, 0, g_pMissionDatabase))
        pSequence.Play()  


################################################################################
##	TractorTargetDocked()
##
##	Event handler called when tractor target has docked with ship.
##
##	Args:	pTGObject	- The TGObject object
##			pEvent		- The event that was sent to the object
##
##	Return:	None
################################################################################
def TractorTargetDocked(pTGObject, pEvent):
        global verbose, g_pMissionDatabase, ShuttleBayInUse_dic
	if verbose: print("Calling TractorTargetDocked()")

	# Get the object that was docked and it's name
	pObject	= App.ShipClass_Cast(pEvent.GetObjPtr())
        sFiringShipName = App.ShipClass_Cast(pEvent.GetDestination()).GetName()
        
	if (pObject == None):
		return
	pShip	= App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip == None):
		return
	
	# sShipName is not used here
	sShipName	= pShip.GetName()
        ShipType = GetShipType(sShipName)

        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return

	# Remove the Object from the set
	pObject.SetDeleteMe(1)
	
	if (ShipType == "EscapePod"):
		if verbose: print("Play the audio line that will let the player know pod is docked")
		FelixLineIs = "E6M2PodDocked"
	else:
		# and the Audio Line is:
		FelixLineIs = "ShipDocked"
        
        # Increase the captured count
        IncreaseShuttleCountStartTimer(pObject.GetName(), sFiringShipName)
        
	ReturnShuttlesSay(FelixLineIs)

	if verbose: print("Tractor Target Docked is finished and done")


################################################################################
##	TractorBeamOn()
##
##	Event handler called when tractor beam starts hitting a target.  Checks to
##	see if the target is a pod and starts docking behavior if it is.
##
##	Args:	TGObject	- The TGObject object.
##			pEvent		- The event that was sent.
##
##	Return:	None
################################################################################
def TractorBeamOn(TGObject, pEvent):
        global verbose, sFiringShipName, sTargetName, ShuttleBayInUse_dic
	# Get the event destination (the thing hit by tractor beam)
	if verbose: print("Tractor Beam on")
	
	ShuttleBaySize		= None
	MaxShuttlesInBay	= None
	pDocking			= None
	
	# Do we have a Ship?
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip == None):
		if verbose: print("failed - no Ship")
		return
	
	# Get the tractor beam system that fired so we
	# can set it's behavior.
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem		= App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	# Get the name of the ship that fired
	pShip = pTractorSystem.GetParentShip()
	if (pShip == None):
		return
	sFiringShipName = pShip.GetName()
	
	# Get Target Ship Name
        if not hasattr(MissionLib.GetShip(sFiringShipName), "GetTarget"):
            return
        
	if not MissionLib.GetShip(sFiringShipName).GetTarget():
		return
		
	sTargetName = MissionLib.GetShip(sFiringShipName).GetTarget().GetName()
	
        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return
        
	#Lets try to get the size of our Target ship
	TargetHullSize = MissionLib.GetShip(sTargetName).GetHull().GetRadius()
	if verbose: print("Size of the Target:", TargetHullSize)
	
	if not FindAShuttleBay(pShip):
		if verbose: print("No Shuttle Bay - return")
		return
	
	# Test if this Tractor can be used to Dock:
	if ( GetIgnoredTractors(sFiringShipName).count(pTractorProjector.GetName()) != 0 ):
		return
	
	#and the size of our Shuttle Bay
	ShuttleBaySize=GetShuttleBaySize(sFiringShipName, pShip)
	if (ShuttleBaySize == None):
		if verbose: print("ShuttleBaySize not set")
		return
	if verbose: print("Size of our Shuttle Bay:", ShuttleBaySize)
	
	MaxShuttlesInBay=SetMaxShuttlesInBay(sFiringShipName)
	if (MaxShuttlesInBay == None):
		MaxShuttlesInBay = 10
		if verbose: print("Setting default MaxShuttlesInBay")
	if verbose: print("Max Shuttles we can carry:", MaxShuttlesInBay)
	
	ShuttlesInBay=GetShuttlesInBay(sFiringShipName)
	if verbose: print("Shuttles currently in Bay:", ShuttlesInBay)
	
	# See if the ship is small enough to fit into out Bay
	if (TargetHullSize < ShuttleBaySize):

                ShipType = GetShipType(sTargetName)
		if (ShipType == "EscapePod"):
			# It's a pod
			if verbose: print("Playing Brex's .attempting to dock pod. line")	
			ReturnShuttlesSay("E6M2FelixDockPod", "Brex")
			
			# set the tractor beam to pull in and dock the pod
			pTractorSystem.SetMode(pTractorSystem.TBS_DOCK_STAGE_1)
		else:
			# It's not a Pod
			# Test if we got enough space in our Bay left
			if ( MaxShuttlesInBay > ShuttlesInBay ):
				if verbose: print("There is enough space left in our Bay")
				if verbose: print("Target will be docked")
				
				if verbose: print("Playing Brex's attempting to dock line")	
				ReturnShuttlesSay("FelixDockShip", "Brex")

				# set the tractor beam to pull in and dock the pod
				pTractorSystem.SetMode(pTractorSystem.TBS_DOCK_STAGE_1)
			else:
				ReturnShuttlesSay("NoSpaceLeft", "Science")
				return
	else:
                print("Target is NOT small enough to get in our Bay")
		print("Size of the Shuttle Bay: ", ShuttleBaySize)
		print("Size of the Target: ", TargetHullSize)


	# We're done.  Let any other handlers for this event handle it.
	if verbose: print("Tractor beam on finished")
	TGObject.CallNextHandler(pEvent)
	

# This is a copy of TractorBeamOn() but without using the Tractor
def ReturnWithoutTractor(pObject, pEvent, NotHost = 0):
        global verbose, sFiringShipName, sTargetName, ShuttleBayInUse_dic

	# Get the event destination (the thing hit by tractor beam)
	if verbose: print("Returning without Tractor")

        pGame                   = App.Game_GetCurrentGame()
        pEpisode	        = pGame.GetCurrentEpisode()
        pMission	        = pEpisode.GetCurrentMission()
        pBridge 		= App.g_kSetManager.GetSet("bridge")
        pPlayer                 = MissionLib.GetPlayer()
        pTarget                 = pPlayer.GetTarget()
        pFriendlies             = pMission.GetFriendlyGroup()
        ShuttleBaySize		= None
        MaxShuttlesInBay	= None
        pDocking		= None

        # Check the Target
        if not pTarget:
                if verbose: print("No Target")
                return
        if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                if verbose: print("Target is not friendly - failed.")
                return

	# Get the name of the ship that fired
	if (NotHost == 0):
		#pShip = pPlayer # currently it is only the Player
		pShip = MissionLib.GetShip(ftb.LaunchShipHandlers.ShuttleLaunchShip)
		sTarget = App.ShipClass_Cast(pTarget)
	else:
		pShip = App.ShipClass_Cast(pTarget)
		sTarget = pPlayer
	sFiringShipName = pShip.GetName()
	sTargetName = sTarget.GetName()

        # Same Ship?
        if (sFiringShipName == sTargetName):
            return

        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return
        if not sTarget.GetImpulseEngineSubsystem():
                ReturnShuttlesSay("UseTractor", "Science") 
                return

	if verbose: print("Target Ship in Tractor is: " + sTargetName)
	
	#Lets try to get the size of our Target ship
	TargetHullSize = MissionLib.GetShip(sTargetName).GetHull().GetRadius()
	if verbose: print("Size of the Target:", TargetHullSize)
	
	#and the size of our Shuttle Bay
	ShuttleBaySize=GetShuttleBaySize(sFiringShipName, pShip)
	if (ShuttleBaySize == None):
		if verbose: print("ShuttleBaySize not set")
		return
	if verbose: print("Size of our Shuttle Bay:", ShuttleBaySize)
	
	MaxShuttlesInBay=SetMaxShuttlesInBay(sFiringShipName)
	if (MaxShuttlesInBay == None):
		MaxShuttlesInBay = 10
		if verbose: print("Setting default MaxShuttlesInBay")
	if verbose: print("Max Shuttles we can carry:", MaxShuttlesInBay)
	
	ShuttlesInBay=GetShuttlesInBay(sFiringShipName)
	if verbose: print("Shuttles currently in Bay:", ShuttlesInBay)
	
	# See if the ship is small enough to fit into out Bay
	if (TargetHullSize < ShuttleBaySize):
            # Test if we got enough space in our Bay left
            if ( MaxShuttlesInBay > ShuttlesInBay ):
                if verbose: print("There is enough space left in our Bay")
                if verbose: print("Target will be docked")

                sTarget.SetAI(AI.Compound.ReturnShuttle.CreateAI(sTarget, sFiringShipName))
            else:
                ReturnShuttlesSay("NoSpaceLeft", "Science")
                return
        else:
                ReturnShuttlesSay("TargetTooBig", "Science")
                print("Target is NOT small enough to get in our Bay")
                print("Size of the Shuttle Bay: ", ShuttleBaySize)
                print("Size of the Target: ", TargetHullSize)

def MissionStart(SHUTTLE_COUNT_TIMER_CALLER):
    global SHUTTLE_COUNT_TIMER, g_pMissionDatabase
    pGame                   = App.Game_GetCurrentGame()
    pEpisode                = pGame.GetCurrentEpisode()
    pMission                = pEpisode.GetCurrentMission()
    SHUTTLE_COUNT_TIMER     = SHUTTLE_COUNT_TIMER_CALLER
    g_pMissionDatabase      = pMission.SetDatabase("data/TGL/QuickBattle/ReturnShuttles.tgl")
    # Tractor beam target docked event
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_TARGET_DOCKED, pMission, __name__+".TractorTargetDocked")
    # Tractor beam starts hitting event
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__+".TractorBeamOn")
    # Shuttle add timer
    App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(SHUTTLE_COUNT_TIMER, __name__ + ".IncreaseShuttleCountStartInit")


if verbose: print("Loading Defiants event Handlers to get the Shuttles back")