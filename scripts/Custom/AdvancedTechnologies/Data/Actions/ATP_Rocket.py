import App
import MissionLib
import loadspacehelper
import math

from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

DEBUG=FALSE
MIN_ANGLE = 45.0 / 180.0 * math.pi

RocketNode={}
FlyingRocketNode={}

ET_PLAYER_FIRES_ROCKET = App.Mission_GetNextEventType()

def Initialise():
	global RocketNode, FlyingRocketNode
	RocketNode={}
	FlyingRocketNode={}

	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")	
			
def Terminate():
	pass
	
def CreateShipWithRockets(pShip,sScriptName,pSet,sShipName,sLocation):
	global RocketNode
	
	#Import the paths
	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
		pList=pModule.GetRocketNames()
	except:
		debug("Error in CreateShipWithRocket: Couldn't find Shippath for Ship "+pShip.GetName())
		return pShip

	j=0
	V=App.TGPoint3()
	Rockets=[]

	for pIt in pList:
		pSysName=pIt[0]
		pSysPath=pIt[1]

		j=j+1

		#Find the OPE's and create a Rocket for each of them
		pSys = findEmittor(pShip,"POP_"+pSysName)
		if pSys==None:
			debug("Error in CreateShipWithRocket: Part with name: "+pSysName+" doesn't exist in ",pShip.GetName())
			return pShip
		if not App.PositionOrientationProperty_Cast(pSys):
			debug("Error in CreateShipWithRockets: Part with name: "+pSysName+" isn't linked to a PositionOrientationProperty with name "+"POP_"+pSysName)
			return pShip
		
		#Create a Part	
		pRocketShip=loadspacehelper.CreateShip(pSysPath,pSet,sShipName+"_"+pSysName,sLocation)
		
		if not pRocketShip:
			try:
				pSet.RemoveObjectFromSet(sShipName+"_"+pSysName)
			except:
				pass

			pRocketShip=loadspacehelper.CreateShip(pSysPath,pSet,sShipName+"_"+pSysName,sLocation)
			
			if not pRocketShip:
				debug("Error in CreateShipWithRocket: Couldn't create Part "+pSysName+": It already exists or there is a patherror")
				return pShip

		#Attach the Rocket and register
		pShip.AttachObject(pRocketShip)
		Rockets.append(pRocketShip)

		#Set some properties 
		pRocketShip.GetShipProperty().SetStationary(TRUE)
		pRocketShip.SetTargetable(TRUE)
		pRocketShip.SetCollisionsOn(TRUE)
		pRocketShip.SetInvincible(TRUE)
					
		#Load some parameters
		try:
			s=pRocketShip.GetScript()
			pModule=__import__ (s)
		except:
			debug("Error in CreateShipWithRocket: Couldn't find Rocketpath for Rocket "+pSysName)
			return pShip
			
		Damage=1000.0			
		try:
			Damage=pModule.GetDamage()
		except:
			debug("Error in loading GetDamage")

		
		#Set up the movement
		pRocketShip.SetTranslate(pSys.GetPosition())
		pRocketShip.AlignToVectors(pSys.GetForward(),pSys.GetUp())		

		#Get the crosshair:
		pCrosshair=MissionLib.GetSubsystemByName(pShip,pSysName)
		if not pCrosshair:
			debug("Error in CreateShipWithRocketParts: the ship hasn't a hull subsystem called: \""+pSysName+"\"")
			return pShip
		
		#Register parameters for later use
		RocketNode[pRocketShip.GetObjID()]=pShip,pSys,Damage,pCrosshair
		
	Rockets.append(pShip)
	
	#Fully disable collision with eachother
	for i in Rockets:
		for j in Rockets:
			i.EnableCollisionsWith(j, 0)
			j.EnableCollisionsWith(i, 0)	


	#Add listeners for mutual explosions
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")

	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_COLLISION,MissionLib.GetMission(),__name__ + ".Collision")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION,MissionLib.GetMission(),__name__ + ".Collision")	
	
	debug("Done setting up ship with Rocket parts "+pShip.GetName())

	# For now only the player can fire a rocket
	if pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
		num = len(pList)
		from Custom.AdvancedTechnologies.Data.GUI import ATP_GUIUtils
		ATP_GUIUtils.CreateStandardButton(ET_PLAYER_FIRES_ROCKET,__name__+".PlayerFiresRocket","Tactical","Fire Torpedo")
		ATP_GUIUtils.SetDisplayName("Tactical","Fire Torpedo","Fire Torpedo: "+str(num))

	return pShip

CHILD=0
PARENT=0
SYS=1
DAMAGE=2
CROSSHAIR=3

def PlayerFiresRocket(pMission,pEvent):
	global RocketNode, FlyingRocketNode
	from Custom.AdvancedTechnologies.Data.GUI import ATP_GUIUtils

	pPlayer = MissionLib.GetPlayer()
	
	## Get the rockets of the player
	lRockets = []
	PID = pPlayer.GetObjID()
	for RID in RocketNode.keys():
		if RocketNode[RID][PARENT].GetObjID() == PID:
			lRockets.append(App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(RID)))
	num = len(lRockets)
	if num==0:
		debug("No rockets present")
		return
	
	## Target?
	pTarget = pPlayer.GetTarget()
	if not pTarget:
		debug("No target for rocket...")
		return

	## Choose the best positioned rocket
	dInfo = {}
	for pRocket in lRockets:
		Void,Void,Void,fAngle = pRocket.GetRelativePositionInfo(pTarget.GetWorldLocation())
		if fAngle < MIN_ANGLE:
			dInfo [fAngle] = pRocket	
	keys = dInfo.keys()
	if not keys:
		debug("None of the rockets was positioned well")
		return
	keys.sort()
	pRocket = dInfo[keys[0]]

	## Ok we have got our rocket

	## Release and reposition the rocket
	V = pRocket.GetWorldLocation()
	M = pRocket.GetWorldRotation()
	pPlayer.DetachObject(pRocket)
	pRocket.SetMatrixRotation(M)
	pRocket.SetTranslate(V)

	## Give it some initial velocity
	P = pPlayer.GetVelocityTG()
	P.Scale(1.0)
	pRocket.SetVelocity(P)

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
									pRocket.GetRadius()*0.25, 
									kEmitPos, 
									kEmitDir,
									bDetach = 0,
									fFrequency = 0.05, 
									fLifeTime = 99.0, 
									fVariance = 75.0,
									iTiming = 64,
									fRed   = 200, 
									fGreen = 200, 
									fBlue  = 200,
									fBrightness = 0.10)
	pSequence.AddAction(pPlasma)
	pSequence.Play()

	## Assign specifcally made AI
	AI = __import__(AI_PATH + ".ATP_RocketAI")
	pRocket.SetAI(AI.CreateAI(pRocket,pTarget))

	## Play a sound
	#pSound = App.g_kSoundManager.GetSound("FireRocket")
	#if pSound:
	#	pSound.Play()

	## Decrement the counterstatus
	if num-1==0:
		ATP_GUIUtils.SetDisplayName("Tactical","Fire Torpedo","Out of rockets")
	else:
		ATP_GUIUtils.SetDisplayName("Tactical","Fire Torpedo","Fire Torpedo: "+str(num-1))

	## Swap containers
	RID 			= pRocket.GetObjID()
	FlyingRocketNode[RID]	= RocketNode[RID][:]
	del RocketNode[RID]




def Collision(pMission,pEvent):
	global FlyingRocketNode

	pA = App.ShipClass_Cast(pEvent.GetSource())
	pB = App.ShipClass_Cast(pEvent.GetDestination())
	if not pA or not pB:
		return

	bA = FlyingRocketNode.has_key(pA.GetObjID())
	bB = FlyingRocketNode.has_key(pB.GetObjID())
	if bA or bB:
		if bA:
			DamageShip(pB,FlyingRocketNode[pA.GetObjID()][DAMAGE])
			del FlyingRocketNode[pA.GetObjID()]
			pA.RunDeathScript()			
		if bB:
			DamageShip(pA,FlyingRocketNode[pB.GetObjID()][DAMAGE])
			del FlyingRocketNode[pB.GetObjID()]
			pB.RunDeathScript()

def DamageShip(pShip,fDamage):
	fHull =pShip.GetHull().GetCondition()
	fHull = fHull - fDamage
	if fHull<0.0:
		pShip.RunDeathScript()
		return
	pShip.GetHull().SetCondition(fHull)

def IsActionShip(pShip):
	global RocketNode
	if RocketNode.has_key(pShip.GetObjID()):
		return TRUE
	return FALSE

def CycleHandle(pMission,pEvent):
	global RocketNode
	V=App.TGPoint3()
		
	for RID in RocketNode.keys():
		pRocketShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(RID))
		
		#Maintain the crosshair system
		pCrosshair=RocketNode[RID][CROSSHAIR]		

		if pCrosshair:
			pRocketShip.GetHull().SetConditionPercentage(pCrosshair.GetConditionPercentage())
			if pCrosshair.GetCondition()<=0.0 and pRocketShip:
				pRocketShip.RunDeathScript()
				del RocketNode[RID]
				continue

		elif pRocketShip:
			pRocketShip.RunDeathScript()
			del RocketNode[RID]
			continue

		#Maintain the stop
		V.SetXYZ(0.0,0.0,0.0)
		pRocketShip.SetVelocity(V)
		pRocketShip.SetTranslate(RocketNode[RID][SYS].GetPosition())
		pRocketShipFys=App.PhysicsObjectClass_Cast(pRocketShip)
		pRocketShip.SetAngularVelocity(V,pRocketShipFys.DIRECTION_MODEL_SPACE)

def Explosion(pMission,pEvent):
	global RocketNode
	
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return
	SID=pShip.GetObjID()

	for RID in RocketNode.keys():
		if RocketNode[RID][PARENT]==SID:
			pRocketShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(RID))
			if pRocketShip:
				pRocketShip.RunDeathScript()

	if RocketNode.has_key(SID):
		del RocketNode[SID]	

