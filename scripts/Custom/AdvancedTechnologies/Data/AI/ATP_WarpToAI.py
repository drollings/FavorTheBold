import App

from Custom.AdvancedTechnologies.Data.ATP_Tools  import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def CreateAI(lArgs):
	
	pShip		= lArgs[0]
	pSolar		= lArgs[1]
	pWay		= lArgs[2]

	#########################################
	# Creating PlainAI WarptoSB12 at (213, 75)
	pWarptoSB12 = App.PlainAI_Create(pShip.GetNode(),"Warpto"+pWay.Node.GetName())
	pWarptoSB12.SetScriptModule("Warp")
	pWarptoSB12.SetInterruptable(1)
	pScript = pWarptoSB12.GetScriptInstance()
	pScript.EnableTowingThroughWarp(TRUE)
	pScript.SetDestinationSetName(pSolar.GetNode().GetRegionModule())
	pScript.SetDestinationPlacementName(pWay.Node.GetName())
	pScript.SetWarpDuration(12.0)
	# Done creating PlainAI WarptoSB12
	#########################################
	return pWarptoSB12

