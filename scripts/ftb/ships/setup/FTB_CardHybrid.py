import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBCardHybrid/FTB_BARKUS.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBCardHybrid/FTB_BARKUSmed.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBCardHybrid/FTB_BARKUSlow.NIF",
		"Name": "CardHybrid",
		"HardpointFile": "ftb_cardhybrid",
		"Species": ftb.Multiplayer.SpeciesToShip.CARDHYBRID,
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 600, "_glow", None, "_specular")
		pLODModel.SetTextureSharePath("Custom/FTB/Ships/SharedTextures/CardShips")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

