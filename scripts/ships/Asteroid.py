import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Misc/Asteroids/asteroid.NIF",
		"Name": "Asteroid",
		"HardpointFile": "asteroid",
		"Species": Multiplayer.SpeciesToShip.ASTEROID
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"], 10000)
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 1000.0, 4.50, 4.50, 499, 500, None, None, None)
		pLODModel.SetTextureSharePath("data/Models/Misc/Asteroids")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
