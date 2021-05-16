import App

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def CreateAI(lArgs):
	pShip		= lArgs.pop(0)
	VAR_ALERT_LEVEL = App.ShipClass.GREEN_ALERT
	if lArgs:
		VAR_ALERT_LEVEL = lArgs.pop(0)
	pShip		= pShip.GetNode()
	
	
	#########################################
	# Creating PlainAI Stay at (174, 94)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(0)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PreprocessingAI AlertLevel at (91, 162)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AlertLevel(VAR_ALERT_LEVEL)
	## The PreprocessingAI:
	pAlertLevel = App.PreprocessingAI_Create(pShip, "AlertLevel")
	pAlertLevel.SetInterruptable(1)
	pAlertLevel.SetPreprocessingMethod(pScript, "Update")
	pAlertLevel.SetContainedAI(pStay)
	# Done creating PreprocessingAI AlertLevel
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (22, 222)
	## Setup:
	import ATP_Preprocessors
	pScript = ATP_Preprocessors.ATP_AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pAlertLevel)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
