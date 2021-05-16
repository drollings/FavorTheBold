import App

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Objects/Wormholes/LC_Wormhole/wormhole-helix2.NIF",
		"FilenameMed": 	"scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Objects/Wormholes/LC_Wormhole/wormhole-helix2.NIF",
		"FilenameLow":	"scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Objects/Wormholes/LC_Wormhole/wormhole-helix2.NIF",
		"Name": 	"Wormhole_Helix2",
		"HardpointFile":"Dummy",
		"Species": 0
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  40.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 100.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 500.0, 15.0, 30.0, 400, 900, "_glow", None, None)
		
		if (bPreLoad == 0):
			pLODModel.Load()
		else:
			pLODModel.LoadIncremental()


def PreLoadModel():
	LoadModel(1)
