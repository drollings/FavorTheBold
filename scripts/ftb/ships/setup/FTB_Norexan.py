import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

g_dSavedCameraModeInfo = {}

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBNorexan/FTB_Valdore.nif",
		"FilenameMed": "Custom/FTB/Ships/FTBNorexan/FTB_Valdoremed.nif",
		"FilenameLow": "Custom/FTB/Ships/FTBNorexan/FTB_Valdorelow.nif",
		"Name": "FTB_Norexan",
		"HardpointFile": "ftb_norexan",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_NOREXAN,
		"SpecularCoef": 1.5,
		"Rescale": 0.8476,
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 1500, "_glow", None, "_specular")
		pLODModel.SetTextureSharePath("Custom/FTB/Ships/SharedTextures/RomulanShips")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
