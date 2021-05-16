import App
import MissionLib
import loadspacehelper
import math

from Actions import ShipScriptActions
from Custom.AdvancedTechnologies.Data.GUI import ATP_GUIUtils

from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

FALSE=0
TRUE=1

DEBUG=TRUE

ET_MOVE_NACELLES=App.Mission_GetNextEventType()
ET_MOVE_NACELLES_END=App.Mission_GetNextEventType()
ET_REVERSE_NACELLES=App.Mission_GetNextEventType()
ET_DUMMY=App.Mission_GetNextEventType()

DOWN=0
GOING_UP=1
UP=2
GOING_DOWN=3
STALLED=4
PARENT=0
SYS=1
TIME_TO_SET=3
THETA=2

DEFAULT_TIME_TO_SET=3.0
DEFAULT_ANGLE=math.pi/4.0

WingsUp={}
pCountDownTimer={}
NacelleNode={}
Register={}

def Initialise():
	global WingsUp
	global pCountDownTimer
	global NacelleNode
	global Register
		
	WingsUp={}
	pCountDownTimer={}
	NacelleNode={}
	Register={}
	
	
def Terminate():
	pass

	
def CreateShipWithMovingNacelles(pShip,sScriptName,pSet,sShipName,sLocation):
	global NacelleNode

	if not pShip:
		return

	pWarp=pShip.GetWarpEngineSubsystem()
	if not pWarp:
		print "Error in CreateShipWithMovingNacelles: No warp system defined"
		pSet.RemoveObjectFromSet(pShip.GetName())
		return

	iChildren = pWarp.GetNumChildSubsystems()
	nacellesbasic=[]

	if (iChildren > 0):
		for i in range(iChildren):
			pChild = pWarp.GetChildSubsystem(i)
			if pChild:
				nacellesbasic.append(pChild.GetObjID())

	if len(nacellesbasic)==0:
		print "Error in CreateShipWithMovingNacelles: No warp system children defined"
		pSet.RemoveObjectFromSet(pShip.GetName())
		return

	nacelles=[]
	j=0
	M=App.TGMatrix3()

	#Set the nacelle status DOWN
	global WingsUp
	if not WingsUp.has_key(pShip.GetObjID()):
		WingsUp[pShip.GetObjID()]=DOWN

	

	for i in nacellesbasic:
		j=j+1
		if DEBUG:
			print "Creating ship :",sShipName+"_Nacelle_"+str(j)
		pNacelle=loadspacehelper.CreateShip(sScriptName+"_Nacelle_"+str(j),pSet,sShipName+"_Nacelle_"+str(j),sLocation)
				
		if not pNacelle:
			try:
				pSet.RemoveObjectFromSet(sShipName+"_Nacelle_"+str(j))
			except:
				print "Error in CreateShipWithMovingNacelles: Couldn't create Nacelle ",pSysName,"; The ship script: ",sScriptName+"_Nacelle_"+str(j)," doesn't exist."
				return pShip
			pNacelle=loadspacehelper.CreateShip(sScriptName+"_Nacelle_"+str(j),pSet,sShipName+"_Nacelle_"+str(j),sLocation)
			
			if not pNacelle:
				print "Error in CreateShipWithMovingNacelles: Couldn't create Nacelle ",pSysName,": Undefined Error"
				return pShip

		pShip.AttachObject(pNacelle)
		pWarpSubsys=App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(nacellesbasic[j-1]))
		pNacelle.SetTranslate(pWarpSubsys.GetPositionTG())
		pNacelle.EnableCollisionsWith(pShip,FALSE)

		pNacelle.GetShipProperty().SetMass(1.0e+25)
		pNacelle.GetShipProperty().SetRotationalInertia(1.0e+25)
		pNacelle.GetShipProperty().SetStationary(TRUE)
		pNacelle.SetTargetable(TRUE)
	
		nacelles.append(pNacelle)
		
		s=pShip.GetScript()+"_Nacelle_"+str(j)
		pModule=__import__ (s)

		try:
			theta=pModule.GetAngle()/180.0*math.pi
		except:
			theta=DEFAULT_ANGLE
		try:
			timetoset=pModule.GetTimeToSet()
		except:
			timetoset=DEFAULT_TIME_TO_SET

		if WingsUp[pShip.GetObjID()]==DOWN:
			pass
		elif WingsUp[pShip.GetObjID()]==UP:
			M.MakeIdentity()
			M.MakeYRotation(theta)
			pNacelle.SetMatrixRotation(M)

		NacelleNode[pNacelle.GetObjID()]=pShip.GetObjID(),i,theta,timetoset

	#Disable collisions
	for i in nacelles:
		for j in nacelles:
			i.EnableCollisionsWith(j,0)	
	
	#Add listeners for mutual explosions
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET,MissionLib.GetMission(),__name__ + ".EnterSet")
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXITED_SET,MissionLib.GetMission(),__name__ + ".ExitSet")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET,MissionLib.GetMission(),__name__ + ".EnterSet")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_SET,MissionLib.GetMission(),__name__ + ".ExitSet")	
		
	#Create the GUI if necessary
	if pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
		ATP_GUIUtils.CreateStandardButton(ET_MOVE_NACELLES,__name__+".MoveNacellesEvent","Helm","Move Nacelles",pShip)

	if DEBUG:
		print "Done setting up ship with nacelles"

	return pShip

def ExitSet(pMission,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return

	if pShip.GetContainingSet():
		debug("Ship "+pShip.GetName()+" about to enter set "+pShip.GetContainingSet().GetName())

	SID = pShip.GetObjID()
	
	## Did the ship leave the system first?
	for NID in NacelleNode.keys():
		PID = NacelleNode[NID][PARENT]
		if SID == PID:
			pNacelle = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if not pNacelle:
				pWarp=App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(NacelleNode[SID][SYS]))
				if pWarp:
					pWarp.SetCondition(0.0)
				del NacelleNode[SID]
				continue
			pNacelle.UpdateNodeOnly()

			pShip.DetachObject(pNacelle)
			debug ("Detaching "+pNacelle.GetName()+ " from "+pShip.GetName())

		
	
def EnterSet(pMission,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return

	if pShip.GetContainingSet():
		debug("Ship "+pShip.GetName()+" has entered set "+pShip.GetContainingSet().GetName())

	SID = pShip.GetObjID()
	for NID in NacelleNode.keys():
		PID = NacelleNode[NID][PARENT]
		if SID == PID:
			pNacelle = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if pNacelle.GetContainingSet().GetObjID() != pShip.GetContainingSet().GetObjID():
				
				#pNacelle.UpdateNodeOnly()
				
				debug(pNacelle.GetName()+" was in "+pNacelle.GetContainingSet().GetName())
				ShipScriptActions.MoveBetweenSetsAction(None,NID,pShip.GetContainingSet().GetName())
				debug(pNacelle.GetName()+" is now in "+pNacelle.GetContainingSet().GetName())
			
				#When checking the nacelles it seemed they deattached after transferring from set, so I reattach them
				pShip.AttachObject(pNacelle)
				pWarp=App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(NacelleNode[NID][SYS]))
				pNacelle.SetTranslate(pWarp.GetPositionTG())

				debug(pNacelle.GetName()+" is reattached to "+pShip.GetName())


def ForceNacelles(pShip,sState):
	if not pShip:
		return
	ID=pShip.GetObjID()

	global WingsUp
	if not WingsUp.has_key(ID):
		return
	
	
	STATE=WingsUp[ID]
	if sState=="Up" or sState=="up":
		if STATE==UP or STATE==GOING_UP:
			pass
		elif STATE==DOWN:
			MoveNacelles(pShip)
		elif STATE==GOING_DOWN:
			ReverseMovingNacelles(pShip)
		elif STATE==STALLED:
			pass
	elif sState=="Down" or sState=="down":
		if STATE==UP:
			MoveNacelles(pShip)
		elif STATE==DOWN or STATE==GOING_DOWN:
			pass
		elif STATE==GOING_UP:
			ReverseMovingNacelles(pShip)
		elif STATE==STALLED:
			pass
	else:
		print "ATP_Nacelles: ForceNacelles: Unknow string indicating state"
		pass


def GetNacellesSetTime(pShip,sState):
	timetoset=0.0
	
	if not pShip:
		return 0.0
	ID=pShip.GetObjID()

	global WingsUp
	if not WingsUp.has_key(ID):
		return 0.0

	for NID in NacelleNode.keys():
		if NacelleNode[NID][PARENT]==ID:
			timetoset=NacelleNode[NID][TIME_TO_SET]
			break

	if timetoset==0.0:
		return 0.0	
		
	if sState=="Up" or sState=="up":
		if WingsUp[ID]==UP:
			return 0.0
		elif WingsUp[ID]==GOING_UP:
			return pCountDownTimer[ID].GetTimerStart()-App.g_kUtopiaModule.GetGameTime()
		elif WingsUp[ID]==DOWN:
			return timetoset
		elif WingsUp[ID]==GOING_DOWN:
			return timetoset-(pCountDownTimer[ID].GetTimerStart()-App.g_kUtopiaModule.GetGameTime())
		elif WingsUp[ID]==STALLED:
			return 1.0e+20

	elif sState=="Down" or sState=="down":
		if WingsUp[ID]==UP:
			return timetoset
		elif WingsUp[ID]==GOING_UP:
			return timetoset-(pCountDownTimer[ID].GetTimerStart()-App.g_kUtopiaModule.GetGameTime())
		elif WingsUp[ID]==DOWN:
			return 0.0
		elif WingsUp[ID]==GOING_DOWN:
			return pCountDownTimer[ID].GetTimerStart()-App.g_kUtopiaModule.GetGameTime()
		elif WingsUp[ID]==STALLED:
			return 1.0e+20
	else:
		print "ATP_Nacelles: GetNacellesSetTime: Unknown string indicating state"
		pass


def IsActionShip(pShip):
	global NacelleNode
	if NacelleNode.has_key(pShip.GetObjID()):
		return TRUE
	return FALSE


def CycleHandle(pMission,pEvent):
	global NacelleNode, WingsUp

	for ID in NacelleNode.keys():
		pNacelle=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ID))
		pWarp=App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(NacelleNode[ID][SYS]))
		pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NacelleNode[ID][PARENT]))
		
		if not pWarp:
			continue
		if pNacelle:
			if pNacelle.GetHull():
				pWarp.SetConditionPercentage(pNacelle.GetHull().GetConditionPercentage())
			else:
				pWarp.SetCondition(0.0)
		else:
			pWarp.SetCondition(0.0)
			
		if pNacelle:
			pNacelle.SetTranslate(pWarp.GetPositionTG())
			V=App.TGPoint3()
			V.SetXYZ(0.0,0.0,0.0)
			pNacelleFys=App.PhysicsObjectClass_Cast(pNacelle)
			pNacelleFys.SetVelocity(V)
		

def NotifyDrainerWeapon(pShip):
	from Custom.AdvancedTechnologies.Data import QuickBattleAddon

	global WingsUp

	if not pShip:
		return
	ID=pShip.GetObjID()

	if not WingsUp.has_key(ID):
		return

	#Check if it is the player, if so modify the GUI
	pPlayer=MissionLib.GetPlayer()
	if pPlayer:
		if pPlayer.GetObjID()==ID:
			if WingsUp[MissionLib.GetPlayer().GetObjID()]==UP:
				ATP_GUIUtils.RemoveStandardButton("Helm","Reset Nacelles")
			elif WingsUp[MissionLib.GetPlayer().GetObjID()]==DOWN:
				ATP_GUIUtils.RemoveStandardButton("Helm","Move Nacelles")
			
			ATP_GUIUtils.CreateStandardButton(ET_DUMMY,__name__+".Dummy","Helm","Nacelles Blocked",MissionLib.GetPlayer())
	
	for NID in NacelleNode.keys():
		if NacelleNode[NID][PARENT]==ID:
			pNacelleShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if pNacelleShip:
				if QuickBattleAddon.CT_NANOFX_MODE:
					from Custom.NanoFX import NanoFX_Lib
					pSequence = NanoFX_Lib.CreateFlickerSeq(pNacelleShip,10, fFlickerSpeed = 0.2, sStatus = "Off")
					pSequence.Play()

	WingsUp[ID]=STALLED

def Dummy(pMission,pEvent):
	pass
	

def Explosion(pMission,pEvent):
	global WingsUp
	global NacelleNode

	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return
	SID=pShip.GetObjID()
	
	if WingsUp.has_key(SID):
		#A ship with Nacelles was destroyed, kill its nacelles too.
		for NID in NacelleNode.keys():
			if NacelleNode[NID][PARENT]==SID:
				pNacelleShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
				if pNacelleShip:
					pNacelleShip.RunDeathScript()
		del WingsUp[SID]

	if NacelleNode.has_key(SID):
		pWarp=App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(NacelleNode[SID][SYS]))
		if pWarp:
			pWarp.SetCondition(0.0)
		del NacelleNode[SID]

	

	
	
def MoveNacellesEvent(pMission,pEvent):
	MoveNacelles(MissionLib.GetPlayer())

def GetNacellePositions(pShip):
	global NacelleNode, WingsUp

	#Absolute checking
	if not pShip:
		return []
	ID=pShip.GetObjID()

	#Vars
	
	retList=[]
	M=App.TGMatrix3()

	#Main loop
	if WingsUp.has_key(ID):
		for NID in NacelleNode.keys():
			if NacelleNode[NID][PARENT]==ID:
				pNacelle=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
				if not pNacelle:
					continue

				theta=NacelleNode[NID][THETA]
				
				pPos=pNacelle.GetWarpEngineSubsystem()
				if not pPos:
					continue

				vPos=pPos.GetPositionTG()
				vLoc=pNacelle.GetTranslate()
				
				M.MakeIdentity()
				M.MakeYRotation(theta)
				
				vPos.MultMatrixLeft(M)
				vLoc.Add(vPos)
	
				retPos=App.NiPoint3(vLoc.GetX(),vLoc.GetY(),vLoc.GetZ())	
				retList.append(vLoc)

		return retList[:]

	else:
		pWarp=pShip.GetWarpEngineSubsystem()
		if not pWarp:
			return retList[:]

		iChildren = pWarp.GetNumChildSubsystems()
		if iChildren > 0:
			for i in range(iChildren):
				pChild = pWarp.GetChildSubsystem(i)
				if pChild:
					vLoc=pChild.GetPosition()
					retList.append(vLoc)

		return retList[:]

		
				

def MoveNacelles(pShip):
	global WingsUp, NacelleNode, pCountDownTimer

	#Absolute checking
	if not pShip:
		print "ATP_Nacelle: MoveNacelles: None argument given !!!!"
		return
	ID=pShip.GetObjID()

	#Vars
	v=App.TGPoint3()
	
	if WingsUp[ID]==STALLED:
		return
	
	#Main loop
	for NID in NacelleNode.keys():
		if NacelleNode[NID][PARENT]==ID:
			pNacelle=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if not pNacelle:
				print "ATP_Nacelle: MoveNacelles: pNacelle doesn't exist for Ship ",pShip.GetName()
				continue			
	
			#Get the stats
			theta=NacelleNode[NID][THETA]
			timetoset=NacelleNode[NID][TIME_TO_SET]
			
			#Opposite theta when moving down
			if WingsUp[ID]==UP:
				theta=theta*(-1.0)
		
			#Set the angular velocity of the nacelle
			v.SetXYZ(0.0,theta/timetoset,0.0)
			pNacelle.SetAngularVelocity(v,App.PhysicsObjectClass_Cast(pShip).DIRECTION_MODEL_SPACE)

	
	#Create an event in timetoset seconds to stop the movement of the nacelles
	pCountDownTimer[ID]=CreateIntTimer(ET_MOVE_NACELLES_END,__name__ +".MoveNacellesEndEvent",App.g_kUtopiaModule.GetGameTime()+timetoset,1.0,-1.0,0,pShip)

	#Modify the state of Nacelle movement
	if WingsUp[ID]==UP:
		WingsUp[ID]=GOING_DOWN
	elif WingsUp[ID]==DOWN:
		WingsUp[ID]=GOING_UP
	

	#Check if it is the player, if so modify the GUI
	pPlayer=MissionLib.GetPlayer()
	if pPlayer:
		if pPlayer.GetObjID()==ID:
			if WingsUp[MissionLib.GetPlayer().GetObjID()]==GOING_DOWN:
				ATP_GUIUtils.RemoveStandardButton("Helm","Reset Nacelles")
			elif WingsUp[MissionLib.GetPlayer().GetObjID()]==GOING_UP:
				ATP_GUIUtils.RemoveStandardButton("Helm","Move Nacelles")
			else:
				print "ATP_MoveNacelles: MoveNacellesEvent: STATE of Nacelles is invalid for action."
				return
			ATP_GUIUtils.CreateStandardButton(ET_REVERSE_NACELLES,__name__+".ReverseMovingNacellesEvent","Helm","Moving Nacelles",MissionLib.GetPlayer())



def ReverseMovingNacellesEvent(pMission,pEvent):
	ReverseMovingNacelles(MissionLib.GetPlayer())
	
def ReverseMovingNacelles(pShip):
	global WingsUp, NacelleNode, pCountDownTimer

	#Absolute checking
	if not pShip:
		return
	ID=pShip.GetObjID()

	#Can we move?
	if WingsUp[ID]==STALLED:
		return
	
	#Main loop
	for NID in NacelleNode.keys():
		if NacelleNode[NID][PARENT]==ID:
			pNacelle=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if not pNacelle:
				continue
	
			#Check if the mothership and the nacelle are still in the same set, if not move the nacelle
			#if not pShip.GetContainingSet().GetObjID()==pNacelle.GetContainingSet().GetObjID():
			#	ShipScriptActions.MoveBetweenSetsAction(None,NID,pShip.GetContainingSet().GetName())
			#	
			#	#When checking the nacelles seemed, they deattached after transferring from set, so I reattach them
			#	pShip.AttachObject(pNacelle)
			#	pNacelle.Update(TRUE)
			#	pShip.Update(TRUE)
			
			#Get the stats
			timetoset=NacelleNode[NID][TIME_TO_SET]
			
			#Set the angular velocity of the nacelle
			v=pNacelle.GetAngularVelocityTG()
			v.SetY((-1.0)*v.GetY())
			pNacelle.SetAngularVelocity(v,App.PhysicsObjectClass_Cast(pShip).DIRECTION_MODEL_SPACE)
			
	
	#Delete the current timer and recreate one with a new timetoset
	if not pCountDownTimer.has_key(ID):
		return
	timetoset=timetoset-(pCountDownTimer[ID].GetTimerStart()-App.g_kUtopiaModule.GetGameTime())
	App.g_kTimerManager.DeleteTimer(pCountDownTimer[ID].GetObjID())
	pCountDownTimer[ID]=CreateIntTimer(ET_MOVE_NACELLES_END,__name__ +".MoveNacellesEndEvent",App.g_kUtopiaModule.GetGameTime()+timetoset,1.0,-1.0,0,pShip)


	#Modify the state of Nacelle movement
	if WingsUp[ID]==GOING_DOWN:
		WingsUp[ID]=GOING_UP
	elif WingsUp[ID]==GOING_UP:
		WingsUp[ID]=GOING_DOWN
	
	#No GUI changes here
	pass

	
def MoveNacellesEndEvent(pMission,pEvent):
	global WingsUp, NacelleNode, pCountDownTimer

	try:
		ID=pEvent.GetInt()
	except:
		print "ATP_Nacelles: MoveNacellesEndEvent: Event is not of type IntEvent"
		return
	#Local vars
	v=App.TGPoint3()
	v.SetXYZ(0,0,0)

	#Absolute checking
	pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(ID))
	if not pShip:
		return
		
	#Main loop
	for NID in NacelleNode.keys():
		if NacelleNode[NID][PARENT]==ID:
			pNacelle=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(NID))
			if not pNacelle:
				continue
	
			#Check if the mothership and the nacelle are still in the same set, if not move the nacelle
			#if not pShip.GetContainingSet().GetObjID()==pNacelle.GetContainingSet().GetObjID():
			#	ShipScriptActions.MoveBetweenSetsAction(None,NID,pShip.GetContainingSet().GetName())
			#	
			#	#When checking the nacelles seemed, they deattached after transferring from set, so I reattach them
			#	pShip.AttachObject(pNacelle)
			#	pNacelle.Update(TRUE)
			#	pShip.Update(TRUE)

			#Set the angular velocity of the nacelle
			pNacelle.SetAngularVelocity(v,App.PhysicsObjectClass_Cast(pShip).DIRECTION_MODEL_SPACE)
	
	#Delete the timer
	if not pCountDownTimer.has_key(ID):
		return	
	App.g_kTimerManager.DeleteTimer(pCountDownTimer[ID].GetObjID())
	del pCountDownTimer[ID]

	#Modify the state of the nacelle movement
	if WingsUp[ID]==GOING_DOWN:
		WingsUp[ID]=DOWN
	elif WingsUp[ID]==GOING_UP:
		WingsUp[ID]=UP
	
		
	#Check if it is the player, if so modify the GUI
	if pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
		ATP_GUIUtils.RemoveStandardButton("Helm","Moving Nacelles")
		if WingsUp[ID]==DOWN:
			ATP_GUIUtils.CreateStandardButton(ET_MOVE_NACELLES,__name__+".MoveNacellesEvent","Helm","Move Nacelles",pShip)
		elif WingsUp[ID]==UP:
			ATP_GUIUtils.CreateStandardButton(ET_MOVE_NACELLES,__name__+".MoveNacellesEvent","Helm","Reset Nacelles",pShip)


def CreateIntTimer(eType, sFunctionHandler, fStart, fDelay, fDuration,bRealTime = 0,pShip=None):
	#"A simplified function for creating a script-based timer event."

	# Setup the handler function.
	pMission=MissionLib.GetMission()
	pMission.AddPythonFuncHandlerForInstance( eType, sFunctionHandler )

	# Create the event and the event timer.
	pEvent = App.TGIntEvent_Create()
	if pShip:
		pEvent.SetInt(pShip.GetObjID())
	else:
		pEvent.SetInt(App.NULL_ID)

	pEvent.SetEventType(eType)
	pEvent.SetDestination(pMission)
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(fStart)
	pTimer.SetDelay(fDelay)
	pTimer.SetDuration(fDuration)
	pTimer.SetEvent(pEvent)

	if (bRealTime):
		App.g_kRealtimeTimerManager.AddTimer(pTimer)
	else:
		App.g_kTimerManager.AddTimer(pTimer)

	MissionLib.g_lMissionTimers.append(pTimer.GetObjID())
	
	return pTimer

	
	
	