import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		# CHANGE ME!  I need real LODs!
		"FilenameHigh": "Custom/FTB/Ships/FTBKvort/FTB_Kvort.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBKvort/FTB_Kvort.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBKvort/FTB_Kvort.NIF",
		"Name": "Kvort",
		"HardpointFile": "ftb_kvort",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_KVORT,
		"SpecularCoef": 1.2,
 		# "DamageRadMod" : 0.5,
 		# "Rescale": 3.0,
 		"DamageStrMod" : 0.6,
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameHigh'], pStats['FilenameHigh']), 400, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
