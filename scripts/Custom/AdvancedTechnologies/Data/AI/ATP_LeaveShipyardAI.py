import App

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def CreateAI(lArgs):
	pShip			= lArgs.pop(0)
	pYard			= lArgs.pop(0)
	e			= lArgs.pop(0)
	
	VAR_ATP_SHIP  		= pShip
	VAR_ATP_YARD  		= pYard
	VAR_DISTANCE  		= pYard.GetRadius()*2.0
	VAR_SHIP_NAME 		= pShip.GetNode().GetName()
	VAR_YARD_NAME 		= pYard.GetNode().GetName()
		
	#########################################
	# Creating PlainAI MoveOut at (369, 32)
	pMoveOut = App.PlainAI_Create(pShip.GetNode(), "MoveOut")
	pMoveOut.SetScriptModule("GoForward")
	pMoveOut.SetInterruptable(1)
	pScript = pMoveOut.GetScriptInstance()
	pScript.SetImpulse(1.0)
	# Done creating PlainAI MoveOut
	#########################################
	#########################################
	# Creating ConditionalAI NearShipyard at (310, 87)
	## Conditions:
	#### Condition RangeCondition
	pRangeCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", VAR_DISTANCE, VAR_SHIP_NAME, VAR_YARD_NAME)
	## Evaluation function:
	def EvalFunc(bRangeCondition):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bRangeCondition:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pNearShipyard = App.ConditionalAI_Create(pShip.GetNode(), "NearShipyard")
	pNearShipyard.SetInterruptable(1)
	pNearShipyard.SetContainedAI(pMoveOut)
	pNearShipyard.AddCondition(pRangeCondition)
	pNearShipyard.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI NearShipyard
	#########################################
	#########################################
	# Creating PlainAI EndMoveOut at (440, 114)
	pEndMoveOut = App.PlainAI_Create(pShip.GetNode(), "EndMoveOut")
	pEndMoveOut.SetScriptModule("RunScript")
	pEndMoveOut.SetInterruptable(1)
	pScript = pEndMoveOut.GetScriptInstance()
	pScript.SetScriptModule(TOOL_PATH)
	pScript.SetFunction("RaiseConceptualEvent")
	pScript.SetArguments(e,pYard,pShip)	
	# Done creating PlainAI EndMoveOut
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (277, 173)
	pPriorityList = App.PriorityListAI_Create(pShip.GetNode(), "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (384, 143)
	pPriorityList.AddAI(pNearShipyard, 1)
	pPriorityList.AddAI(pEndMoveOut, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList
