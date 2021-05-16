import App
import ATP_Turret
import ATP_Nacelle
import ATP_Rotation
import ATP_Rocket
import MissionLib

TRUE=1
FALSE=0

DEBUG=FALSE

INITIALISED=FALSE
TIME_GRANULATION=1.0

def Initialise():
	ATP_Turret.Initialise()
	ATP_Nacelle.Initialise()
	ATP_Rotation.Initialise()
	ATP_Rocket.Initialise()

def Terminate(pMission,pObject):
	pass


def CycleHandle(pMission,pObject):
	ATP_Nacelle.CycleHandle(pMission,pObject)
	ATP_Rotation.CycleHandle(pMission,pObject)		
	ATP_Turret.CycleHandle(pMission,pObject)
	ATP_Rocket.CycleHandle(pMission,pObject)

def NotifyDrainerWeapon(pShip):
	ATP_Nacelle.NotifyDrainerWeapon(pShip)

def IsActionShip(pShip):
	b1=ATP_Turret.IsActionShip(pShip)
	b2=ATP_Nacelle.IsActionShip(pShip)
	b3=ATP_Rotation.IsActionShip(pShip)
	b4=ATP_Rocket.IsActionShip(pShip)
	return (b1 + b2 + b3 + b4)

def HasTurrets(pShip):
	if not pShip:
		return FALSE

	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
	except:
		return FALSE

	try:
		return pModule.HasTurrets()
	except:
		return FALSE

def IsMotherShip(pShip):
	if not pShip:
		return FALSE
	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
	except:
		return FALSE

	try:
		b1=pModule.HasTurrets()
	except:
		b1=FALSE
	try:
		b2=pModule.HasNacelles()
	except:
		b2=FALSE
	try:
		b3=pModule.HasRotatingParts()
	except:
		b3=FALSE
	try:
		b4=pModule.HasRockets()
	except:
		b4=FALSE

	return b1 or b2 or b3 or b4

def GiveTurretList(pShip):
	return ATP_Turret.GiveTurretList(pShip)

	

def Decode(pMission,pEvent,pShip=None):
	if not pShip:
		pShip=App.ShipClass_Cast(pEvent.GetDestination())

	if DEBUG:
		print "Ship Created, Checking for special features"

	if not pShip:
		return

	try:
		s=pShip.GetScript()
		pModule=__import__ (s)
	except:
		return

	try:
		HasTurrets=pModule.HasTurrets()
	except:
		HasTurrets=FALSE

	try:
		HasNacelles=pModule.HasNacelles()
	except:
		HasNacelles=FALSE

	try:
		HasRotatingParts=pModule.HasRotatingParts()
	except:
		HasRotatingParts=FALSE

	try:
		HasRockets=pModule.HasRockets()
	except:
		HasRockets=FALSE


	if not (HasRotatingParts or HasRockets or HasTurrets or HasNacelles):
		return

	j=len(s)-1
	while(TRUE):
		if j==0:
			break
		if s[j]==".":
			break
		j=j-1

	sScriptName=s[j+1:]
			
	pSet=pShip.GetContainingSet()
	if not pSet:
		return

	sSetName=pSet.GetName()
	sShipName=pShip.GetName()
	sLocation=sShipName+"__POS__"

	kThis = App.Waypoint_Create(sLocation, sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0,0.0,0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0,1.0,0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0,0.0,1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.0)
	kThis.Update(0)
	
	if HasTurrets:
		if DEBUG:
			print "Turret feature detected"
		ATP_Turret.CreateShipWithTurrets(pShip,sScriptName,pSet,sShipName,sLocation)	
	if HasNacelles:
		if DEBUG:
			print "Nacelle feature detected"
		ATP_Nacelle.CreateShipWithMovingNacelles(pShip,sScriptName,pSet,sShipName,sLocation)	
	if HasRotatingParts:
		if DEBUG:
			print "Rotating Parts feature detected"
		ATP_Rotation.CreateShipWithRotatingParts(pShip,sScriptName,pSet,sShipName,sLocation)
	if HasRockets:
		if DEBUG:
			print "Rocket Parts feature detected"
		ATP_Rocket.CreateShipWithRockets(pShip,sScriptName,pSet,sShipName,sLocation)

	kThis.SetDeleteMe(TRUE)

