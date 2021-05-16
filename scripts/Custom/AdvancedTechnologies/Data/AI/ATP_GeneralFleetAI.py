import App

AI_LOW					= 0.0
AI_MEDIUM				= 0.5
AI_HIGH					= 1.0

def CreateAI(pShip):
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pEnemies= pMission.GetEnemyGroup()
	pFriends= pMission.GetFriendlyGroup()
	
	#Tricky, I got it from QB.py
	if not pEnemies.GetNameTuple():
		pEnemies.AddName("Hello from Apollo")

	#########################################
	# Creating CompoundAI FollowThroughWarp at (143, 199)
	import AI.Compound.FollowThroughWarp
	import MissionLib
	pPlayer = MissionLib.GetPlayer()
	pFollowThroughWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName(), FollowToSB12 = 1, FollowThroughMissions = 1)
	# Done creating CompoundAI FollowThroughWarp
	#########################################

	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import ATP_BasicAttack
	pAttack = ATP_BasicAttack.CreateAI(pShip,pEnemies,Difficulty = AI_HIGH,FollowTargetThroughWarp = 0, UseCloaking = 1)
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
	pScript = ATP_Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWait)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles