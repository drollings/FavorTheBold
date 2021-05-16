import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBSovereignMK2/FTBSovereignmk2.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBSovereignMK2/FTBSovereignmk2med.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBSovereignMK2/FTBSovereignmk2low.NIF",
		"Name": "Sovereign Mk2",
		"HardpointFile": "ftb_sovereignmk2",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_SOVEREIGNMK2,
		"DamageRadMod" : 0.6,
		"SpecularCoef": 1.5,
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
		pLODModel.SetTextureSharePath("Custom/FTB/Ships/SharedTextures/FedShips")

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 1200, "_glow", None, "_specular", 'FTB_Sovereign')

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
