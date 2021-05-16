import App
import MissionLib

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def StopRealShip(pRealShip):
	return

	# Hard stop, so the ship doesn't drift while being repaired.
	vZero = App.TGPoint3()
	vZero.SetXYZ(0, 0, 0)
	pRealShip.SetVelocity(vZero)
	pRealShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

def CreateAI(lArgs):
	
	pConShip 	= lArgs.pop(0)	#Ship to Dock
	pWaypoint	= lArgs.pop(0)  #Waypoint to invoke "ATP_Dock_Start_A" , "ATP_Undock_Start_A"
	pSignalTo	= lArgs.pop(0)	#The object to call when done
	e		= lArgs.pop(0)  #Eventtype to call when the action is done
	pLast=None
	if lArgs:
		pLast   = lArgs.pop(0)
		pLast   = pLast.Node.GetName()

	pWaypointName	= pWaypoint.Node.GetName()
	pShip		= pConShip.Node

	VAR_SWAP_DISTANCE  = 150.0
	
	#########################################
	# Creating PlainAI ATP_FollowIt at (327, 213)
	pATP_FollowIt = App.PlainAI_Create(pShip, "ATP_FollowIt")
	pATP_FollowIt.SetScriptModule("ATP_FollowWaypointsBis")
	pScript = pATP_FollowIt.GetScriptInstance()
	pScript.SetTargetWaypointName(pWaypointName,pLast)
	pATP_FollowIt.SetInterruptable(1)
	# Done creating PlainAI ATP_FollowIt
	#########################################
	#########################################
	# Creating PlainAI StopRealShip at (356, 262)
	pStopRealShip = App.PlainAI_Create(pShip, "StopRealShip")
	pStopRealShip.SetScriptModule("RunScript")
	pStopRealShip.SetInterruptable(1)
	pScript = pStopRealShip.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StopRealShip")
	pScript.SetArguments(pShip)
	# Done creating PlainAI StopRealShip
	#########################################
	#########################################
	# Creating PlainAI RaiseDoneEvent at (290, 263)
	pRaiseDoneEvent = App.PlainAI_Create(pShip, "RaiseDoneEvent")
	pRaiseDoneEvent.SetScriptModule("RunScript")
	pRaiseDoneEvent.SetInterruptable(1)
	pScript = pRaiseDoneEvent.GetScriptInstance()
	pScript.SetScriptModule(ATP_OBJECT_PATH)
	pScript.SetFunction("Raise")
	pScript.SetArguments(e,pConShip,pSignalTo)
	# Done creating PlainAI RaiseDoneEvent
	#########################################
	#########################################
	# Creating SequenceAI GuidedMove at (168, 391)
	pGuidedMove = App.SequenceAI_Create(pShip, "GuidedMove")
	pGuidedMove.SetInterruptable(1)
	pGuidedMove.SetLoopCount(1)
	pGuidedMove.SetResetIfInterrupted(1)
	pGuidedMove.SetDoubleCheckAllDone(0)
	pGuidedMove.SetSkipDormant(0)
	# SeqBlock is at (275, 351)
	pGuidedMove.AddAI(pATP_FollowIt)
	pGuidedMove.AddAI(pStopRealShip)
	pGuidedMove.AddAI(pRaiseDoneEvent)
	# Done creating SequenceAI GuidedMove
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (59, 587)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (177, 569)
	pPriorityList.AddAI(pGuidedMove, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (25, 700)
	## Setup:
	import ATP_Preprocessors
	pScript = ATP_Preprocessors.ATP_AvoidObstacles()
	pScript.AddObjectsToIngoreList(pSignalTo.GetNode())
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
