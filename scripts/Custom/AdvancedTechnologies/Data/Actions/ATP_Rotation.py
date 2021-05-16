import App
import MissionLib
import loadspacehelper
import math

FALSE=0
TRUE=1
DEBUG=FALSE
RotatorNode={}


def Initialise():
	global RotatorNode
	RotatorNode={}	
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")	
	
		
def Terminate():
	pass

	
def CreateShipWithRotatingParts(pShip,sScriptName,pSet,sShipName,sLocation):
	global RotatorNode

	if not pShip:
		return	

	#Import the paths
	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
		pList=pModule.GetRotationPartsNames()
	except:
		print "Error in CreateShipWithRotatingParts: Couldn't find Shippath for Ship "+pShip.GetName()
		return pShip


	j=0
	V=App.TGPoint3()
	Rotators=[]

	for pIt in pList:
		pSysName=pIt[0]
		pSysPath=pIt[1]

		j=j+1

		#Find the OPE's and create a Rotator for each of them
		pSys = findEmittor(pShip,pSysName)
		if pSys==None:
			print "Error in CreateShipWithRotatingParts: Part with name: ",pSysName," doesn't exist in ",pShip.GetName()
			return pShip
		if not App.PositionOrientationProperty_Cast(pSys):
			print "Error in CreateShipWithRotators: Part with name: ",pSysName," isn't linked to a PositionOrientationProperty"
			return pShip

		
		#Create a Part	
		pRotatorShip=loadspacehelper.CreateShip(pSysPath,pSet,sShipName+"_"+pSysName,sLocation)
		
		if not pRotatorShip:
			try:
				pSet.RemoveObjectFromSet(sShipName+"_"+pSysName)
			except:
				pass

			pRotatorShip=loadspacehelper.CreateShip(pSysPath,pSet,sShipName+"_"+pSysName,sLocation)
			
			if not pRotatorShip:
				print "Error in CreateShipWithRotatingParts: Couldn't create Part ",pSysName,": It already exists or there is a patherror"
				return pShip

		#Attach the Rotator and register
		pShip.AttachObject(pRotatorShip)
		Rotators.append(pRotatorShip)


		#Set some properties 
		pRotatorShip.GetShipProperty().SetStationary(TRUE)
		pRotatorShip.SetTargetable(FALSE)
		pRotatorShip.SetCollisionsOn(TRUE)
		pRotatorShip.SetInvincible(TRUE)
					
		#Load some parameters
		try:
			s=pRotatorShip.GetScript()
			pModule=__import__ (s)
		except:
			print "Error in CreateShipWithRotatingParts: Couldn't find Rotatorpath for Rotator "+pSysName
			return pShip
			
		Speed=0.25/180.0*math.pi
			
		try:
			Speed=pModule.GetRotationSpeed()/180.0*math.pi
		except:
			print "Error in loading GetRotationSpeed"

		
		#Set up the movement
		pRotatorShip.SetTranslate(pSys.GetPosition())
		pRotatorShip.AlignToVectors(pSys.GetForward(),pSys.GetUp())

		V.SetXYZ(0.0,Speed,0.0)
		pRotatorShipFys=App.PhysicsObjectClass_Cast(pRotatorShip).DIRECTION_MODEL_SPACE
		pRotatorShip.SetAngularVelocity(V,pRotatorShipFys)

		#Get the crosshair:
		pCrossHair=MissionLib.GetSubsystemByName(pShip,pSysName+' ')
		if not pCrossHair:
			print "Error in CreateShipWithRotatingParts: the ship hasn't a hull subsystem called: \"",pSysName," \" ,mind the extra space at the end of the name!!"
			return pShip
		
		#Register parameters for later use
		RotatorNode[pRotatorShip.GetObjID()]=pShip,pSys,Speed,pCrossHair
		
	Rotators.append(pShip)
	
	#Fully disable collision with eachother
	for i in Rotators:
		for j in Rotators:
			i.EnableCollisionsWith(j, 0)
			j.EnableCollisionsWith(i, 0)
	


	#Add listeners for mutual explosions and create the positionTimer
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING,MissionLib.GetMission(),__name__ + ".Explosion")	
	
	if DEBUG:
		print "Done setting up ship with rotating parts ",pShip.GetName()
	return pShip

PARENT=0
SYS=1
SPEED=2
CROSSHAIR=3


def IsActionShip(pShip):
	global RotatorNode
	if RotatorNode.has_key(pShip.GetObjID()):
		return TRUE
	return FALSE


def CycleHandle(pMission,pEvent):
	global RotatorNode
	V=App.TGPoint3()
		
	for RID in RotatorNode.keys():
		pRotatorShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(RID))
		
		#Maintain the crosshair system
		pCrossHair=RotatorNode[RID][CROSSHAIR]
		if pCrossHair:
			if pCrossHair.GetCondition()<=0.0 and pRotatorShip:
				pRotatorShip.RunDeathScript()
				del RotatorNode[RID]
				continue
		elif pRotatorShip:
			pRotatorShip.RunDeathScript()
			del RotatorNode[RID]
			continue

		#Maintain the movement
		V.SetXYZ(0.0,0.0,0.0)
		pRotatorShip.SetVelocity(V)
		pRotatorShip.SetTranslate(RotatorNode[RID][SYS].GetPosition())
		V.SetXYZ(0.0,RotatorNode[RID][SPEED],0.0)
		pRotatorShipFys=App.PhysicsObjectClass_Cast(pRotatorShip)
		pRotatorShip.SetAngularVelocity(V,pRotatorShipFys.DIRECTION_MODEL_SPACE)


def Explosion(pMission,pEvent):
	global RotatorNode
	
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip:
		return
	SID=pShip.GetObjID()

	for RID in RotatorNode.keys():
		if RotatorNode[RID][PARENT]==SID:
			pRotatorShip=App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(RID))
			if pRotatorShip:
				pRotatorShip.RunDeathScript()

	if RotatorNode.has_key(SID):
		del RotatorNode[SID]
	

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