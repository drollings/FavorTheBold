import App
import MissionLib

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def CreateAI(lArgs):
	
	pConceptualShip	= lArgs.pop(0)	# Ship
	pHolder		= lArgs.pop(0)  # Holder
	e		= lArgs.pop(0)  # Eventtype to call when the action is done
	pShip 		= pConceptualShip.Node

	sname = pHolder.Node.GetName()  # VARS
		
	#########################################
	# Creating PlainAI Guidance at (205, 182)
	pGuidance = App.PlainAI_Create(pShip, "Guidance")
	pGuidance.SetScriptModule("Intercept_Dasher")
	pGuidance.SetInterruptable(1)
	pScript = pGuidance.GetScriptInstance()
	pScript.SetTargetObjectName(sname)
	pScript.SetInterceptDistance(fDistance = 60.0)
	pScript.SetAddObjectRadius(bUseRadius = 1)
	# Done creating PlainAI Guidance
	#########################################
	#########################################
	# Creating PlainAI RaiseDoneEvent at (290, 263)
	pRaiseDoneEvent = App.PlainAI_Create(pShip, "RaiseDoneEvent")
	pRaiseDoneEvent.SetScriptModule("RunScript")
	pRaiseDoneEvent.SetInterruptable(1)
	pScript = pRaiseDoneEvent.GetScriptInstance()
	pScript.SetScriptModule(ATP_OBJECT_PATH)
	pScript.SetFunction("Raise")
	pScript.SetArguments(e,pConceptualShip,pHolder)
	# Done creating PlainAI RaiseDoneEvent
	#########################################
	#########################################
	# Creating SequenceAI GuidedMove at (101, 334)
	pGuidedMove = App.SequenceAI_Create(pShip, "GuidedMove")
	pGuidedMove.SetInterruptable(1)
	pGuidedMove.SetLoopCount(1)
	pGuidedMove.SetResetIfInterrupted(1)
	pGuidedMove.SetDoubleCheckAllDone(0)
	pGuidedMove.SetSkipDormant(0)
	# SeqBlock is at (215, 341)
	pGuidedMove.AddAI(pGuidance)
	pGuidedMove.AddAI(pRaiseDoneEvent)
	# Done creating SequenceAI GuidedMove
	#########################################
	return pGuidedMove
