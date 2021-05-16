import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBBreenFighter/FTB_BreenFighter.NIF",
		# "FilenameMed": "Custom/FTB/Ships/FTBBreenFighter/FTB_BreenFighterlow.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBBreenFighter/FTB_BreenFighterlow.NIF",
		"Name": "BreenFighter",
		"HardpointFile": "ftb_breenfighter",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_BREENFIGHTER,
		"SpecularCoef": 0.5,
 		"DamageRadMod" : 0.1,
		 }
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameLow']), 500, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
