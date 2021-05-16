import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBNebula/FTB_Nebula.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBNebula/FTB_NebulaMed.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBNebula/FTB_NebulaLow.NIF",
		# "FilenameHigh": "data/Models/Ships/Nebula/Nebula.NIF",
		# "FilenameMed": "data/Models/Ships/Nebula/NebulaMed.NIF",
		# "FilenameLow": "data/Models/Ships/Nebula/NebulaLow.NIF",
		"Name": "Peregrine",
		"HardpointFile": "ftb_nebula",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_NEBULA,
		"SpecularCoef": 0.55,
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 800, "_glow", None, "_specular")
		# pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedShips")
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

def GetPath():
	return 'Custom/FTB/Ships/FTBNebula/'

def OnLoad(sName, pPlayer, pSet, sPath = GetPath(), pShipDef = None):
	if pShipDef:
		sName = pShipDef.name
	FTB_Support.ReplaceShipTextures(pPlayer, sName, sPath)
	
	
