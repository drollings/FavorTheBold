import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBFerengiShuttle/FTBFerengiShuttle.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBFerengiShuttle/FTBFerengiShuttlelow.NIF",
		"Name": "FerengiShuttle",
		"HardpointFile": "ftb_type9",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_FERENGISHUTTLE,
		# "SpecularCoef": 1.5,
		"DamageRadMod" : 0.1,
		"DamageStrMod" : 0.001
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameLow'] ), 50, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
