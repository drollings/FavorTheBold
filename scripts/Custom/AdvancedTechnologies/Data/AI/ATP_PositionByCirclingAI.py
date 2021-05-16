import App
from Custom.AdvancedTechnologies.Data.Universe.ATP_Object import *

def StopShip(pShip):
	## Hard stop, so the ship doesn't drift while being repaired.
	vZero = App.TGPoint3()
	vZero.SetXYZ(0, 0, 0)
	pShip.SetVelocity(vZero)
	pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)


def CreateAI(lArgs):
	
	## Arguments
	pConShip 	= lArgs.pop(0)	# Ship to Dock
	pWaypoint	= lArgs.pop(0)  # Destination
	pYard		= lArgs.pop(0)	# The base involved
	e		= lArgs.pop(0)  # Eventtype to call when the action is done
	fCloseEnough	= lArgs.pop(0)	# Precision
	
	pShip		= pConShip.Node
	
	#########################################
	# Creating PlainAI Guidance at (248, 216)
	pGuidance = App.PlainAI_Create(pShip, 'Guidance')
	pGuidance.SetScriptModule('ATP_PositionByCircle')
	pGuidance.SetInterruptable(1)
	pScript = pGuidance.GetScriptInstance()
	pScript.SetOrbitted(pYard.Node)
	pScript.SetDestination(pWaypoint.Node)	
	pScript.SetPrecision(fCloseEnough)
	# Done creating PlainAI Guidance
	#########################################
	#########################################
	# Creating PlainAI StopShip at (270, 263)
	pStopShip = App.PlainAI_Create(pShip, 'StopShip')
	pStopShip.SetScriptModule('RunScript')
	pStopShip.SetInterruptable(1)
	pScript = pStopShip.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction('StopShip')
	pScript.SetArguments(pShip)
	# Done creating PlainAI StopShip
	#########################################
	#########################################
	# Creating PlainAI RaiseDoneEvent at (290, 263)
	pRaiseDoneEvent = App.PlainAI_Create(pShip, 'RaiseDoneEvent')
	pRaiseDoneEvent.SetScriptModule('RunScript')
	pRaiseDoneEvent.SetInterruptable(1)
	pScript = pRaiseDoneEvent.GetScriptInstance()
	pScript.SetScriptModule(ATP_OBJECT_PATH)
	pScript.SetFunction('Raise')
	pScript.SetArguments(e,pConShip,pYard)
	# Done creating PlainAI RaiseDoneEvent
	#########################################
	#########################################
	# Creating SequenceAI GuidedMove at (101, 334)
	pGuidedMove = App.SequenceAI_Create(pShip, 'GuidedMove')
	pGuidedMove.SetInterruptable(1)
	pGuidedMove.SetLoopCount(1)
	pGuidedMove.SetResetIfInterrupted(1)
	pGuidedMove.SetDoubleCheckAllDone(0)
	pGuidedMove.SetSkipDormant(0)
	# SeqBlock is at (215, 341)
	pGuidedMove.AddAI(pGuidance)
	pGuidedMove.AddAI(pStopShip)
	pGuidedMove.AddAI(pRaiseDoneEvent)
	# Done creating SequenceAI GuidedMove
	#########################################
	return pGuidedMove
	#########################################
	# Creating PriorityListAI PriorityList at (59, 587)
	pPriorityList = App.PriorityListAI_Create(pShip, 'PriorityList')
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
	pScript.AddObjectsToIngoreList(pYard.Node)
	pScript.SetPersonalSpace(1.0)
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip,'AvoidObstacles')
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript,'Update')
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles	
