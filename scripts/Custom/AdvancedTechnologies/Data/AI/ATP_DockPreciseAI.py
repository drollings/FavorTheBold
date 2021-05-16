import App
import MissionLib

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def StopRealShip(pShip):
	# Hard stop, so the ship doesn't drift while being repaired.
	vZero = App.TGPoint3()
	vZero.SetXYZ(0, 0, 0)
	pShip.SetVelocity(vZero)
	pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

def CreateAI(lArgs):
	
	pShip 		= lArgs.pop(0)	#Ship to Dock
	pWaypoint	= lArgs.pop(0)  #Waypoint to invoke "ATP_Dock_Start_A" , "ATP_Undock_Start_A"
	pYard		= lArgs.pop(0)	#The Starbase involved
	e		= lArgs.pop(0)  #Eventtype to call when the action is done
	pLast           = None
	if lArgs:
		pLast   = lArgs.pop(0)
		pLast   = pLast.Node.GetName()
	
	pWaypointName	= pWaypoint.Node.GetName()
	pRealShip	= pShip.Node
	
	#########################################
	# Creating PlainAI Guidance at (248, 216)
	pGuidance = App.PlainAI_Create(pRealShip, "Guidance")
	pGuidance.SetScriptModule("ATP_FollowWaypoints")
	pGuidance.SetInterruptable(1)
	pScript = pGuidance.GetScriptInstance()
	pScript.SetTargetWaypointName(pWaypointName,pLast)
	# Done creating PlainAI Guidance
	#########################################
	#########################################
	# Creating PlainAI StopRealShip at (270, 263)
	pStopRealShip = App.PlainAI_Create(pRealShip, "StopRealShip")
	pStopRealShip.SetScriptModule("RunScript")
	pStopRealShip.SetInterruptable(1)
	pScript = pStopRealShip.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StopRealShip")
	pScript.SetArguments(pRealShip)
	# Done creating PlainAI StopRealShip
	#########################################
	#########################################
	# Creating PlainAI RaiseDoneEvent at (290, 263)
	pRaiseDoneEvent = App.PlainAI_Create(pRealShip, "RaiseDoneEvent")
	pRaiseDoneEvent.SetScriptModule("RunScript")
	pRaiseDoneEvent.SetInterruptable(1)
	pScript = pRaiseDoneEvent.GetScriptInstance()
	pScript.SetScriptModule(ATP_OBJECT_PATH)
	pScript.SetFunction("Raise")
	pScript.SetArguments(e,pShip,pYard)
	# Done creating PlainAI RaiseDoneEvent
	#########################################
	#########################################
	# Creating SequenceAI GuidedMove at (101, 334)
	pGuidedMove = App.SequenceAI_Create(pRealShip, "GuidedMove")
	pGuidedMove.SetInterruptable(0)
	pGuidedMove.SetLoopCount(1)
	pGuidedMove.SetResetIfInterrupted(0)
	pGuidedMove.SetDoubleCheckAllDone(0)
	pGuidedMove.SetSkipDormant(0)
	# SeqBlock is at (215, 341)
	pGuidedMove.AddAI(pGuidance)
	pGuidedMove.AddAI(pStopRealShip)
	pGuidedMove.AddAI(pRaiseDoneEvent)
	# Done creating SequenceAI GuidedMove
	#########################################
	return pGuidedMove
