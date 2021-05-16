import App
from QuickBattle import QuickBattle
def CreateAI(pShip):
	#########################################
	# Creating CompoundAI Attack at (194, 57)
	import ATP_BasicAttack
	pAttack = ATP_BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("QuickBattle.QuickBattle", "pEnemies"), Difficulty = QuickBattle.GetCurrentAILevel(), FollowTargetThroughWarp=1, UseCloaking=1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	from Custom.AdvancedTechnologies.Data.Actions import ATP_ActionDecoder
	if ATP_ActionDecoder.IsMotherShip(pShip):
		#print "QuickBattleFriendlyAI: The Ship ",pShip.GetName()," was given specific AI."
		return pWait
	else:
		pass
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (41, 304)
	## Setup:
	import ATP_Preprocessors
	pScript = ATP_Preprocessors.ATP_AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "ATP_AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
