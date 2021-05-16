import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		# "FilenameHigh": "data/Models/Ships/Galaxy/Galaxy.NIF",
		# "FilenameMed": "data/Models/Ships/Galaxy/GalaxyMed.NIF",
		# "FilenameLow": "data/Models/Ships/Galaxy/GalaxyLow.NIF",
		"FilenameHigh": "Custom/FTB/Ships/FTBGalaxy/FTB_Stardrive.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBGalaxy/FTB_StardriveMed.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBGalaxy/FTB_StardriveLow.NIF",
		"Name": "FTB_GalaxyDrive",
		"HardpointFile": "ftb_galaxydrive",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_GALAXY_DRIVE,
		"SpecularCoef": 0.55
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 700, "_glow", None, '_specular')
		pLODModel.SetTextureSharePath("Custom/FTB/Ships/SharedTextures/FedShips")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
