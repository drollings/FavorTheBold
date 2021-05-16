import App
import MissionLib
import loadspacehelper
import math
import time
import TacticalInterfaceHandlers

from Custom.AdvancedTechnologies.Data.GUI import ATP_GUIUtils

from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

FALSE=0
TRUE=1

STATS=0
CHILDREN=1
PARENT=2

SYS=0
ARMED=0
MIN=1
MAX=2
DIFF=3
FIRST_SHOT=4
CROSSHAIR=4
SPEED=5

DEBUG=TRUE
METHOD=2

TIME_GRANULATION=2.0  
#----> Very important. Controls the frequency at which the turrets are positioned 
#      Complexity lineair with this factor. I will play with it to optimize performance...

ITERATION_GRANULATION=0.1
ITERATION_NUMBER=20
ITERATION_LIM=ITERATION_NUMBER*ITERATION_GRANULATION*TIME_GRANULATION
MIN_ANGLE=0.0

ET_CYCLE=App.Mission_GetNextEventType()
ET_ACTIVATE_TURRETS=App.Mission_GetNextEventType()
ET_DEACTIVATE_TURRETS=App.Mission_GetNextEventType()
TIMER=None

MotherNode={}
TurretNode={}
CannonNode={}
ShipListDict={}


def Initialise():
	global TIMER
	global TurretNode
	global CannonNode
	global MotherNode
	global ShipListDict
	
	if TIMER:
		App.g_kTimerManager.DeleteTimer(TIMER.GetObjID())
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")	
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_FIRED,MissionLib.GetMission(),__name__ + ".ResetFiringObject")
	
	TIMER=None
	MotherNode={}
	TurretNode={}
	CannonNode={}
	ShipListDict={}
	

def Terminate():
	pass


def CreateShipWithTurrets(pShip,sScriptName,pSet,sShipName,sLocation):
	global TurretNode
	global CannonNode
	global MotherNode
		
	P=MissionLib.GetPlayer()
	if P:
		PID=P.GetObjID()
	else:
		PID=0	

	if not pShip:
		print "Error in CreateShipWithTurrets: Couldn't create ship"
		return None
	
	cannons=[]
	turrets=[]

	#Import the Turretpaths
	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
		pList=pModule.GetTurretNames()
	except:
		print "Error in CreateShipWithTurrets: Couldn't find Shippath for Ship "+pShip.GetName()
		return pShip
	
	ShipChildList=[]
	
	j=0
	for pIt in pList:
		pTurretSysName=pIt[0]
		pTurretSysPath=pIt[1]

		j=j+1

		#Find the OPE's and create a turret for each of them
		pTurretSys = findEmittor(pShip,pTurretSysName)
		if not pTurretSys:
			print "Error in CreateShipWithTurrets: Turret with name: ",pTurretSysName," doesn't exist in ",pShip.GetName()
			return pShip
		if not App.PositionOrientationProperty_Cast(pTurretSys):
			print "Error in CreateShipWithTurrets: Turret with name: ",pTurretSysName," isn't linked to a Position Orientation Property"
			return pShip

		
		#Create a TURRET	
		pTurretShip=loadspacehelper.CreateShip(pTurretSysPath,pSet,sShipName+"_"+pTurretSysName,sLocation)
		
		if not pTurretShip:
			try:
				pSet.RemoveObjectFromSet(sShipName+"_"+pTurretSysName)
			except:
				print "Error in CreateShipWithTurrets: Couldn't create Turret ",pTurretSysName,": There is an error in the name of the script ",pTurretSysPath
				return pShip

			pTurretShip=loadspacehelper.CreateShip(pTurretSysPath,pSet,sShipName+"_"+pTurretSysName,sLocation)
			
			if not pTurretShip:
				print "Error in CreateShipWithTurrets: Couldn't create Turret ",pTurretSysName,": Unknown Error."
				return pShip

		#Attach the TURRET and register
		pShip.AttachObject(pTurretShip)
		pTurretShip.SetTranslate(pTurretSys.GetPosition())
		pTurretShip.EnableCollisionsWith(pShip, 0)
		pTurretShip.AlignToVectors(pTurretSys.GetForward(),pTurretSys.GetUp())
		turrets.append(pTurretShip)
		
		#Set some properties 
		#pTurretShip.SetTargetable(FALSE)
		#pTurretShip.SetInvincible(TRUE)
		
							
		#Load some parameters
		try:
			s=pTurretShip.GetScript()
			pModule=__import__ (s)
		except:
			print "Error in CreateShipWithTurrets: Couldn't find Turretpath for Turret "+pTurretSysName
			return pShip
			
		Min=-math.pi/4
		Max=-Min
		Diff=math.pi/8
			
		try:
			Min=pModule.GetMinAngle()/180.0*math.pi
		except:
			print "Error in loading GetMinAngle()"

		try:
			Max=pModule.GetMaxAngle()/180.0*math.pi
		except:
			print "Error in loading GetMaxAngle()"


		try:
			Diff=pModule.GetMaxDiffAngle()/180.0*math.pi
		except:
			print "Error in loading GetMaxDiffAngle()"


		#Import the Cannonpaths

		try:
			pSList=pModule.GetCannonNames()
		except:
			print "Error in CreateShipWithTurrets: Couldn't find CannonNames for Turret "+pTurretSysName
			return pShip

		TurretChildList=[]

			
		i=0
		for pIt in pSList:
			i=i+1
			pCannonSysName=pIt[0]
			pCannonSysPath=pIt[1]

			#Make a cannon for each subsripted OPE
			pCannonSys=findEmittor(pTurretShip,pCannonSysName)
			if pCannonSys==None:
				print "Error in CreateShipWithTurrets: Cannon with name: ",pCannonSysName," doesn't exist in ",pTurretShip.GetName()
				return pShip
			if not App.PositionOrientationProperty_Cast(pCannonSys):
				print "Error in CreateShipWithTurrets: Cannon with name: ",pCannonSysName," isn't linked to a PositionOrientationProperty"
				return pShip

		
			#Create a CANNON	
			pCannonShip=loadspacehelper.CreateShip(pCannonSysPath,pSet,sShipName+"_"+pTurretSysName+"_"+pCannonSysName,sLocation)
		
			if not pCannonShip:
				try:
					pSet.RemoveObjectFromSet(sShipName+"_"+pTurretSysName+"_"+pCannonSysName)
				except:
					print "Error in CreateShipWithTurrets: Couldn't create Cannon ",pCannonSysName,": There is an error in the name of the script: ",pCannonSysPath
					return pShip

				pCannonShip=loadspacehelper.CreateShip(pCannonSysPath,pSet,sShipName+"_"+pTurretSysName+"_"+pCannonSysName,sLocation)
				
				if not pCannonShip:
					print "Error in CreateShipWithTurrets: Couldn't create Cannon ",pCannonSysName,": Unknown Error"
					return pShip

			#Attach the CANNON and register
			pTurretShip.AttachObject(pCannonShip)
			pCannonShip.SetTranslate(pCannonSys.GetPosition())
			pCannonShip.EnableCollisionsWith(pShip, 0)	
			pCannonShip.AlignToVectors(pCannonSys.GetForward(),pCannonSys.GetUp())
			cannons.append(pCannonShip)

			#Set some properties 
			pCannonShip.SetTargetable(FALSE)
								
			#Load some parameters
			try:
				s=pCannonShip.GetScript()
				pModule=__import__ (s)
			except:
				print "Error in CreateShipWithTurrets: Couldn't find Cannonpath for Cannon "+pCannonSysName
				return pShip
			
			Min2=-math.pi/4
			Max2=-Min
			Diff2=math.pi/8
			
			try:
				Min2=pModule.GetMinAngle()/180.0*math.pi
			except:
				print "Error in loading GetMinAngle()"

			try:
				Max2=pModule.GetMaxAngle()/180.0*math.pi
			except:
				print "Error in loading GetMaxAngle()"

			try:
				Diff2=pModule.GetMaxDiffAngle()/180.0*math.pi
			except:
				print "Error in loading GetMaxDiffAngle()"
		
										
			#Register parameters for later use
			CannonNode[pCannonShip.GetObjID()]=[[pCannonSys,Min2,Max2,Diff2*TIME_GRANULATION,TRUE],None,pTurretShip.GetObjID()]
			
			TurretChildList.append(pCannonShip.GetObjID())


		#pSysC is used to display the damage to the different parties
		pSysC=MissionLib.GetSubsystemByName(pShip,pTurretSysName+' ')
		if not pSysC:
			print "Error in CreateShipWithTurrets: the ship ",pShip.GetName()," hasn't a hull subsystem called: \"",pTurretSysName," \" ,mind the extra space at the end of the name!!"
			return pShip
		pSysC.GetProperty().SetMaxCondition(1.0e+25)
		pSysC.GetProperty().SetRepairComplexity(1.0e+15)

		#We need the torpedoes speed to fire
		try:
			vWeapon=pCannonShip.GetTorpedoSystem().GetCurrentAmmoType().GetLaunchSpeed()
			vWeapon=vWeapon*vWeapon
		except:
			print "Error in CreateShipWithTurrets: Ship ",pShip.GetName(),"; Turret ",pTurretSysName,"; The Cannon ",pCannonSysName," has a not properly setup torpedosystem."	
			return pShip
						
		#Register parameters for later use
		TurretNode[pTurretShip.GetObjID()]=[[pTurretSys,Min,Max,Diff*TIME_GRANULATION,pSysC,vWeapon],TurretChildList,pShip.GetObjID()]
		ShipChildList.append(pTurretShip.GetObjID())

	#Register parameters for later use
	MotherNode[pShip.GetObjID()]=[[FALSE,FALSE],ShipChildList,None]
	group=turrets+cannons
		
	#Fully disable collisions with eachother
	for i in group:
		for j in group:
			i.EnableCollisionsWith(j, 0)
	


	#Add listeners for mutual explosions and create the positionTimer
	global TIMER
	if not TIMER:
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")	
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORPEDO_FIRED,MissionLib.GetMission(),__name__ + ".ResetFiringObject")
		TIMER=MissionLib.CreateTimer(ET_CYCLE,__name__ +".Cycle",App.g_kUtopiaModule.GetGameTime()+TIME_GRANULATION,TIME_GRANULATION,-1.0,0)
	

	#Create an activation button for the player
	if pShip.GetObjID()==MissionLib.GetPlayer().GetObjID():
		ATP_GUIUtils.CreateStandardButton(ET_ACTIVATE_TURRETS,__name__+".ActivateTurrets","Tactical","Arm Turrets",pShip)
	
	return pShip


def ResetFiringObject(pMission,pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	
	if not pTorp:
		return

	if not CannonNode.has_key(pTorp.GetParentID()):
		return
	pShipID=TurretNode[CannonNode[pTorp.GetParentID()][PARENT]][PARENT]

	TorpVel=pTorp.GetVelocityTG()
	pShipFys=App.PhysicsObjectClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
	if not pShipFys:
		return
	TorpVel.Add(pShipFys.GetVelocityTG())

	FireTorpFromPointWithVector(pTorp.GetWorldLocation(),TorpVel,pTorp.GetModuleName(),pTorp.GetTargetID(),pShipID)
	pTorp.SetLifetime(0.0)			


def ActivateTurrets(pMission,pEvent):
	pPlayer=MissionLib.GetPlayer()
	PID=pPlayer.GetObjID()
	
	ATP_GUIUtils.RemoveStandardButton("Tactical","Arm Turrets")
	ATP_GUIUtils.CreateStandardButton(ET_DEACTIVATE_TURRETS,__name__+".DeActivateTurrets","Tactical","Turrets Armed",pPlayer)
	
	global MotherNode
	MotherNode[PID][STATS][ARMED]=TRUE
	
		
def DeActivateTurrets(pMission,pEvent):	
	pPlayer=MissionLib.GetPlayer()
	PID=pPlayer.GetObjID()
	
	ATP_GUIUtils.RemoveStandardButton("Tactical","Turrets Armed")
	ATP_GUIUtils.CreateStandardButton(ET_ACTIVATE_TURRETS,__name__+".ActivateTurrets","Tactical","Arm Turrets",pPlayer)
	
	global MotherNode
	MotherNode[PID][STATS][ARMED]=FALSE


def IsActionShip(pShip):
	global CannonNode
	if CannonNode.has_key(pShip.GetObjID()):
		return TRUE
	global TurretNode
	if TurretNode.has_key(pShip.GetObjID()):
		return TRUE
	return FALSE


def GiveTurretList(pShip):
	global TurretNode
	
	retList=[]
	if not pShip:
		return retList

	SID=pShip.GetObjID()
	SortedTurretNodeKeys=TurretNode.keys()
	SortedTurretNodeKeys.sort()

	for TID in SortedTurretNodeKeys:
		if TurretNode[TID][PARENT]==SID:
			retList.append(TurretNode[TID][STATS][CROSSHAIR])
	return retList


def CycleHandle(pMission,pEvent):
	for TID in TurretNode.keys():
		pCrossHair=TurretNode[TID][STATS][CROSSHAIR]
		pTurretShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(TID))
		if not pCrossHair:
			continue
		if pTurretShip:
			if pTurretShip.GetHull():
				pCrossHair.SetConditionPercentage(pTurretShip.GetHull().GetConditionPercentage())
			else:
				pCrossHair.SetCondition(0.0)
		else:
			pCrossHair.SetCondition(0.0)

	
def Cycle(pMission,pEvent):
	#debug("cyvle TURRET start")
	
	global TurretNode
	global CannonNode
	global MotherNode

	pPlayer=MissionLib.GetPlayer()
	if not pPlayer:
		return
	PID=pPlayer.GetObjID()
	Axe=App.TGPoint3()
	
	prepareFindShipToAttack()

	for MID in MotherNode.keys():
		pMotherShip=App.PhysicsObjectClass_Cast(App.TGObject_GetTGObjectPtr(MID))
		if not pMotherShip:
			continue

		#Gather some information about the host ship
		pMotherShipFys=App.PhysicsObjectClass_Cast(pMotherShip)
		MotherVel=pMotherShipFys.GetVelocityTG()
		MotherPos=pMotherShipFys.GetPredictedPosition(pMotherShipFys.GetWorldLocation(),pMotherShipFys.GetVelocityTG(),pMotherShipFys.GetAccelerationTG(),TIME_GRANULATION)
		MotherRot=pMotherShipFys.GetPredictedRotationTG(TIME_GRANULATION)

		#Check if we need to reset all turrets of the ship
		sReset=FALSE
		if not MotherNode[MID][STATS][ARMED]:
			if PID==MID:
				sReset=TRUE
			else:
				MotherNode[MID][STATS][ARMED]=TRUE
	
		for TID in MotherNode[MID][CHILDREN]:
			pTurretShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(TID))
			if not TurretNode.has_key(TID):
				continue

			#Determine the worldlocation  and worldrotation of the turret
			pTurretOr=TurretNode[TID][STATS][SYS]
			TurretPos=pTurretOr.GetPosition()
			TurretPos.MultMatrixLeft(MotherRot)
			TurretPos.Add(MotherPos)
			TurretRot=pTurretShip.GetRotation()
			TurretRot=TurretRot.MultMatrixLeft(MotherRot)
			pTurretShipFys=App.PhysicsObjectClass_Cast(pTurretShip)
		
			#Hold the turrets to the correct position
			Axe.SetXYZ(0.0,0.0,0.0)
			pTurretShip.SetVelocity(Axe)
			pTurretShip.SetTranslate(pTurretOr.GetPosition())
					
			#Calcaulate the realangle of turret
			Axe.SetXYZ(0.0,1.0,0.0)
			Axe.MultMatrixLeft(pTurretShip.GetRotation())
			realangle=getTrueAngleS(Axe,pTurretOr.GetRight(),pTurretOr.GetForward())

			#Find a target, we only have on target for each turret
			tReset=FALSE
			if not sReset:
				pTargetShip=App.PhysicsObjectClass_Cast(findShipToAttack(pMotherShip,TurretPos,pTurretOr.GetForward()))
				#If we didn't found a target, reset the turret
				if not pTargetShip:
					tReset=TRUE
			
			#Now if we have the target, interpolate its position
			if not sReset and not tReset:
				pTargetShipFys=App.PhysicsObjectClass_Cast(pTargetShip)

				#We iterate untill the weapons and target predicted pos are close enough, or stop if too long
				fTime=0.0
				vWeapon=TurretNode[TID][STATS][SPEED]
								
				while(TRUE):
					TargetPos=pTargetShipFys.GetPredictedPosition(pTargetShipFys.GetWorldLocation(),pTargetShipFys.GetVelocityTG(),pTargetShipFys.GetAccelerationTG(),TIME_GRANULATION+fTime)
					MotherVelTemp=copyVector(MotherVel)
					MotherVelTemp.Scale(fTime)
					DiffTemp=copyVector(MotherVelTemp)
					DiffTemp.Add(TurretPos)
					DiffTemp.Subtract(TargetPos)
											
					if DiffTemp.SqrLength()<=fTime*fTime*vWeapon:
						#Refine our targetposition
						TargetPos.Subtract(MotherVelTemp)
						break

					if fTime>ITERATION_LIM:
						tReset=TRUE
						break
					fTime=fTime+ITERATION_GRANULATION*TIME_GRANULATION
			
			#Now that we have interpolated the position, lets' calculate the angle to orient the turret to the target
			if not sReset and not tReset:
				DiffTemp=copyVector(TargetPos)
				DiffTemp.Subtract(TurretPos)
				R=pTurretOr.GetRight()
				R.MultMatrixLeft(MotherRot)
				F=pTurretOr.GetForward()
				F.MultMatrixLeft(MotherRot)
				U=R.Cross(F)
				U.Unitize()
				U.Scale(U.Dot(DiffTemp))
				DiffTemp.Subtract(U)
				setangle=getTrueAngleS(DiffTemp,R,F)
				if setangle > TurretNode[TID][STATS][MAX] or setangle < TurretNode[TID][STATS][MIN]:
					tReset=TRUE
			
				
			#Now that we have the angle,let's move it !!!
			if sReset or tReset:
				diff=0.0-realangle
			else:
				diff=setangle-realangle
			if diff < MIN_ANGLE and diff > -MIN_ANGLE:
				diff=0.0
		
			Axe.SetXYZ(0.0,0.0,-diff/TIME_GRANULATION)
			pTurretShip.SetAngularVelocity(Axe,pTurretShipFys.DIRECTION_MODEL_SPACE)

			#Update TurretRot
			M=App.TGMatrix3()
			M.MakeIdentity()
			M.MakeZRotation(-diff)
			TurretRot=M.MultMatrixLeft(TurretRot)
			
			
			for CID in TurretNode[TID][CHILDREN]:
				pCannonShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(CID))
				pCannonShipFys=App.PhysicsObjectClass_Cast(pCannonShip)
				if not CannonNode.has_key(CID) or not pCannonShip:
					continue
									
				#Determine the worldlocation  and worldrotation of the Cannon --> Difficulty: turret will have turned in one TIME_GRANULATION
				pCannonOr=CannonNode[CID][STATS][SYS]
				CannonPos=pCannonOr.GetPosition()
				CannonPos.MultMatrixLeft(TurretRot) 
				CannonPos.Add(TurretPos) 
				
				#Hold the cannon to the correct position
				Axe.SetXYZ(0.0,0.0,0.0)
				pCannonShip.SetVelocity(Axe)
				pCannonShip.SetTranslate(pCannonOr.GetPosition())
						
				#Calcaulate the realangle of Cannon
				Axe.SetXYZ(0.0,1.0,0.0)
				Axe.MultMatrixLeft(pCannonShip.GetRotation())
				realangle=getTrueAngleF(Axe,pCannonOr.GetForward(),pCannonOr.GetUp())

				cReset=FALSE
				#We already have a target, lets' calculate the angle to orient the turret to the target
				if not sReset and not tReset:
					DiffTemp=copyVector(TargetPos)
					DiffTemp.Subtract(CannonPos)
					U=pCannonOr.GetUp()
					U.MultMatrixLeft(TurretRot)
					F=pCannonOr.GetForward()
					F.MultMatrixLeft(TurretRot)
					R=U.Cross(F)
					R.Unitize()
					R.Scale(R.Dot(DiffTemp))
					DiffTemp.Subtract(R)
					setangle=getTrueAngleF(DiffTemp,F,U)
					if setangle >= CannonNode[CID][STATS][MAX] or setangle <= CannonNode[CID][STATS][MIN]:
						cReset=TRUE
				
				#Now that we have the angle,let's move it !!!
				if sReset or tReset or cReset:
					diff=0.0-realangle
				else:
					diff=setangle-realangle
				if diff <= MIN_ANGLE and diff >= -MIN_ANGLE:
					diff=0.0
		
				Axe.SetXYZ(-diff/TIME_GRANULATION,0.0,0.0)
				pCannonShip.SetAngularVelocity(Axe,pCannonShipFys.DIRECTION_MODEL_SPACE)

				#Fire the weapons, but not the first time because we were idle and aren't positioned well
				if not sReset and not tReset and not cReset:
					if not CannonNode[CID][STATS][FIRST_SHOT]:
						pCannonShip.SetTarget(pTargetShip.GetName())
						StartFireWeapons(pCannonShip)
					CannonNode[CID][STATS][FIRST_SHOT]=FALSE
					
				else:
					CannonNode[CID][STATS][FIRST_SHOT]=TRUE
					StopFireWeapons(pCannonShip)


	#debug("cyvle TURRET end")
			
					
						
def Explosion(pMission,pEvent,pShip=None):
	global TurretNode
	global CannonNode
	global MotherNode

	if not pShip:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return
	ID=pShip.GetObjID()

	if MotherNode.has_key(ID):
		for TID in MotherNode[ID][CHILDREN]:
			pTurretShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(TID))
			if pTurretShip:
				pTurretShip.RunDeathScript()
				Explosion(pMission,pEvent,pTurretShip)
		del MotherNode[ID]

	if TurretNode.has_key(ID):
		pCrossHair=TurretNode[ID][STATS][CROSSHAIR]
		if pCrossHair:
			pCrossHair.SetCondition(0.0)

		for CID in TurretNode[ID][CHILDREN]:
			pCannonShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(CID))
			if pCannonShip:
				pCannonShip.RunDeathScript()
				Explosion(pMission,pEvent,pCannonShip)
		del TurretNode[ID]

	if CannonNode.has_key(ID):
		del CannonNode[ID]
	
	
def printVector(v):
	return "[ "+str(v.GetX())+" , "+str(v.GetY())+" , "+str(v.GetZ())+" ]"


def copyVector(v):
	X=App.TGPoint3()
	X.SetXYZ(v.GetX(),v.GetY(),v.GetZ())
	return X


def getTrueAngleS(w,x,y):
	w.Unitize()
	y.Unitize()

	f=w.Dot(y)
	
	if f>1.0:
		f=1.0
	elif f<-1.0:
		f=-1.0

	a=math.acos(f)

	if w.Dot(x)>0.0:
		a=(-1.0)*a
	return a

def getTrueAngleF(w,x,y):
	w.Unitize()
	x.Unitize()
	
	f=w.Dot(x)
	
	if f>1.0:
		f=1.0
	elif f<-1.0:
		f=-1.0

	a=math.acos(f)

	if w.Dot(y)<0.0:
		a=(-1.0)*a
	return a


def toDegree(a):
	return a*180.0/math.pi


def findEmittor(pShip,pName):
	# Find any object emitter properties on the ship.
	pPropSet = pShip.GetPropertySet()
	pEmitterInstanceList = pPropSet.GetPropertiesByType(App.CT_POSITION_ORIENTATION_PROPERTY)

	pEmitterInstanceList.TGBeginIteration()
	iNumItems = pEmitterInstanceList.TGGetNumItems()

	pLaunchProperty = None

	for i in range(iNumItems):
		pInstance = pEmitterInstanceList.TGGetNext()

		# Check to see if the property for this instance is a shuttle
		# emitter point.
		pProperty = App.PositionOrientationProperty_Cast(pInstance.GetProperty())

		pString=pProperty.GetName()
		pString2=App.TGString()
		pString2.SetString(pName[:])
		
		if (pProperty != None):
			if not pString.Compare(pString2):
				pLaunchProperty = pProperty
				break

	pEmitterInstanceList.TGDoneIterating()
	pEmitterInstanceList.TGDestroy()
	
	return pLaunchProperty


def prepareFindShipToAttack():
	from Custom.AdvancedTechnologies.Data import ATP_Lib
	P=MissionLib.GetPlayer()
	if not P:
		return

	ShipListID=ATP_Lib.GetShipListInSet(P.GetContainingSet())
	global ShipListDict
	ShipListDict={}

	for pTargetID in ShipListID:
		pTarget=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTargetID))
		Aff=0
		if ATP_Lib.IsEnemy(pTarget):
			Aff=1
		if ATP_Lib.IsFriend(pTarget):
			Aff=2

		v=pTarget.GetWorldLocation()
		
		if Aff!=0:
			ShipListDict[pTargetID,Aff]=pTarget
			
	
def findShipToAttack(pShip,kLocation,kFwd):
	from Custom.AdvancedTechnologies.Data import ATP_Lib

	mAff=0
	if ATP_Lib.IsEnemy(pShip):
		mAff=2
	if ATP_Lib.IsFriend(pShip):
		mAff=1

	if mAff==0:
		return None
	
	u=copyVector(kFwd)
	u.Unitize()
	
	v=App.TGPoint3()
	pTargetDict={}
	
	for key in ShipListDict.keys():
		if not mAff==key[1]:
			continue

		pTarget=ShipListDict[key]
		v=pTarget.GetWorldLocation()
		v.Subtract(kLocation)

		
		#10km is 55.0 in their units
		if not v.Length() <275.0:
			continue

		v.Unitize()
		fKey=u.Dot(v)
		
		pTargetDict[fKey]=pTarget

	
	if len(pTargetDict.keys())==0:
		return None

	TargetKeys=pTargetDict.keys()
	TargetKeys.sort()
	TargetKeys.reverse()
	
	pTarget=pTargetDict[TargetKeys[0]]

	return pTarget

	
		

def FireTorpFromPointWithVector(kPoint,kVector,pcTorpScriptName, idTarget ,pShipID):
	# This is an slightly altered version of the original definition (MissionLib.py) , to suit specific needs

	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
	pShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))	
	if not pTarget:
		return

	pSet = pTarget.GetContainingSet()
	if not pSet or not pShip:
		return None
	
	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()
	
	

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)
	pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
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
	kVelocity = kVector
	pTorp.SetVelocity(kVelocity)

	return pTorp

def Integrate(pSys):
	pSys.SetInvincible(1)
	pSysProp=pSys.GetProperty()
	pSysProp.SetMaxCondition(100000000)
	pSysProp.SetCritical(0)
	pSysProp.SetTargetable(1)
	pSysProp.SetPrimary(0)
	pSysProp.SetRepairComplexity(999999.000000)
	pSysProp.SetDisabledPercentage(0.000000)
	pSysProp.SetRadius(0.0)

def StartFireWeapons(pShip):
	TacticalInterfaceHandlers.FireWeapons(pShip,TRUE,App.ShipClass.WG_PRIMARY)
	TacticalInterfaceHandlers.FireWeapons(pShip,TRUE,App.ShipClass.WG_SECONDARY)
	TacticalInterfaceHandlers.FireWeapons(pShip,TRUE,App.ShipClass.WG_TERTIARY)

def StopFireWeapons(pShip):
	TacticalInterfaceHandlers.FireWeapons(pShip,FALSE,App.ShipClass.WG_PRIMARY)
	TacticalInterfaceHandlers.FireWeapons(pShip,FALSE,App.ShipClass.WG_SECONDARY)
	TacticalInterfaceHandlers.FireWeapons(pShip,FALSE,App.ShipClass.WG_TERTIARY)
	