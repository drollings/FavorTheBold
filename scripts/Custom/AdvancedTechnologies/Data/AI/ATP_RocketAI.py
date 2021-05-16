import App

def CreateAI(pShip,pTarget):

	VAR_TARGET_NAME	= pTarget.GetName()
	VAR_RAM_SPEED	= App.PhysicsObjectClass_Cast(pTarget).GetVelocityTG().Length()*5.0

	#########################################
	# Creating PlainAI Ram at (284, 97)
	pRam = App.PlainAI_Create(pShip, "Ram")
	pRam.SetScriptModule("Ram")
	pRam.SetInterruptable(1)
	pScript = pRam.GetScriptInstance()
	pScript.SetTargetObjectName(VAR_TARGET_NAME)
	pScript.SetMaximumSpeed(VAR_RAM_SPEED)
	# Done creating PlainAI Ram
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (142, 97)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (243, 104)
	pPriorityList.AddAI(pRam, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (55, 146)
	## Setup:
	import ATP_Preprocessors
	pScript = ATP_Preprocessors.ATP_AvoidObstacles()
	pScript.AddObjectsToIngoreList(pShip,pTarget)
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
