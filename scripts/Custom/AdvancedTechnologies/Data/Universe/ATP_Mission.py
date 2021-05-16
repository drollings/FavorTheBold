import App

from ATP_Object import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

class Mission(UniverseElement):
	def __init__(self):
		UniverseElement.__init__(self)


class DefenseMission(Mission):

	def __init__(self,pObject):
		Mission.__init__(self)

		## Already a defense mission on it?
		if FALSE:
			raise RuntimerError
	
		## Is the object a system?
		if not pSolar.IsTypeOf(SOLAR):
			raise RuntimeError

		## Register the defended system
		self.DefendedID = pObject.ID

		

	def Update(self,involved = None):

		## What system is attacked?
		assert lEnemyFleets
		pSolar 	= lEnemyFleets[0].GetSolar()
		RID	= self.GetRace().ID

		## Asses the power of the enemies
		iEnemy = 0
		for pEnemy in lEnemyFleets:
			iEnemy = iEnemy + pEnemy.Strength()

		## Match the enemy with 1.5 times their strength
		iEnemy = int(iEnemy * 1.5)

		## Now iterate over the ownFleets to match the strength() if possible
		iSelf = 0
		for pFleet in self.GetFleets():
			iSelf = iSelf + pFleet.Strength()

		keys,dOwnFleets = StrengthDict (lOwnFleets[:])
				
		## Define the priority for this mission
		iPriority = DEFENSE + CRITICAL

		for iStrength in keys:
			pFriend = dOwnFleets[iStrength]

			## Try to assign the mission to the fleet
			reply = pFriend.AssignMission(self,iPriority)
			if reply == ACK:
				iSelf = iSelf + iStrength

				## Check if we have already enough power
				if iSelf >= iEnemy:
					## Decrease the priority for the other fleets
					iPriority = DEFENSE + OVERRUN

		## How long can we survive?
		fTime 	= LifeTime(iSelf,iTime)
		iTrials = 0
		bbAllies  = TRUE
		bbFellows = TRUE

		while(TRUE):
			## Do we have enough strength()?
			if iSelf >= iEnemy:
				break

			## Decrement a counter
			iTrials = iTrials + 1

			if iTrials > ARMAGEDDON_THRESHOLD:
				## Cannot find enough help, we are probably doomed...
				break

			elif iTrials == ARMAGEDDON_THRESHOLD:
				## We are in huge trouble, this might be well the end of our race....
				## Increase our priority and range
				iPriority = DEFENSE + ARMAGEDDON
				fTime     = - 1.0				

			## Panic!!! Ask for reinforcements...
			lNearSolars = pSolar.GetSortedSpace(DistanceWarpXinTime(9,fTime),bFellows=bbFellows,bAllies=bbAlies)
			for pNearSolar in lNearSolars:
				for pFleet in pNearSolar.GetAlliedFleets(self.GetRace()):
					if pFleet.GetRace().ID == RID:
						## Try to assign the mission to the fleet
						reply = pFriend.AssignMission(self,iPriority)
						if reply == ACK:
							iSelf = iSelf + iStrength
						
						## Check if we have already enough power
						if iSelf >= iEnemy:
							break

			## Increase our priority and range
			iPriority = DEFENSE + OVERWRITE
			fTime	  = fTime * 2.0


		## The instructions should be given now...
		return				
			
			
			
						


			

		

		