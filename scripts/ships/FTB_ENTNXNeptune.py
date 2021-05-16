import App
import ftb.Multiplayer.SpeciesToShip
import FTB_Support

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "Custom/FTB/Ships/FTBEIntrepid/FTB_EIntrepid.NIF",
		"FilenameMed": "Custom/FTB/Ships/FTBEIntrepid/FTB_EIntrepidmed.NIF",
		"FilenameLow": "Custom/FTB/Ships/FTBEIntrepid/FTB_EIntrepidlow.NIF",
		"Name": "FTB_NXNeptune",
		"HardpointFile": "ftb_entneptune",
		"Species": ftb.Multiplayer.SpeciesToShip.FTB_NEPTUNE,
		# "SpecularCoef": 1.5,
		"DamageRadMod" : 0.4,
		# "DamageStrMod" : 0.3
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

		FTB_Support.AddLODs(pLODModel, (pStats['FilenameHigh'], pStats['FilenameMed'], pStats['FilenameLow']), 200, "_glow", None, "_specular")
		pLODModel.SetTextureSharePath("Custom/FTB/Ships/SharedTextures/HumanShips")

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
	return 'Custom/FTB/Ships/FTBEIntrepid/'

def OnLoad(sName, pPlayer, pSet, sPath = GetPath(), pShipDef = None):
	if pShipDef:
		sName = pShipDef.name
	FTB_Support.ReplaceShipTextures(pPlayer, sName, sPath)
