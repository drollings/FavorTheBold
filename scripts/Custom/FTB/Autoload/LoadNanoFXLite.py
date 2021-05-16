###############################################################################
##	Filename:	LoadNanoFXv2.py
##
##	Nano's Special Effects Enhancements Mutator Plugin Version 2.0
##
##	Updated:	10/07/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import Foundation
import Custom.NanoFXv2Lite.NanoFX_Config
import Custom.NanoFXv2Lite.NanoFX_Setup
import Custom.NanoFXv2Lite.NanoFX_ScriptActions

import App

intCount = 0

###############################################################################
## Create Mutator Menu
###############################################################################
mode = Foundation.MutatorDef.FTB
# Foundation.MutatorDef.NanoFX = mode
dMode = { 'modes': [ mode ] }
# mode.bBase = 1


class NanoFXTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):

		pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

		### Fix Lights ###
		if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_LightFlickerFX == "On"):
			Custom.NanoFXv2Lite.NanoFX_ScriptActions.TurnOnLights(None)
		###
		### Setup WarpFX Warp Speed Buttons for QB###
		if pMission.GetScript() == "QuickBattle.QuickBattle":

			from Custom.NanoFXv2Lite.WarpFX import WarpFX_GUI
			WarpFX_GUI.SetupWarpSpeedButtons()

			import Systems.Starbase12.Starbase
			Systems.Starbase12.Starbase.CreateMenus()

			import Systems.Belaruz.Belaruz
			Systems.Belaruz.Belaruz.CreateMenus()

			import Systems.Vesuvi.Vesuvi
			Systems.Vesuvi.Vesuvi.CreateMenus()

		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_FIRED, pMission, "Custom.NanoFXv2Lite.SpecialFX.WeaponFlashFX.CreateWeaponFlashFX")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_FIRED, pMission, "Custom.NanoFXv2Lite.SpecialFX.WeaponFlashFX.CreateWeaponFlashFX")

class NanoFXBlinkers(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)

	def __call__(self, pObject, pEvent, dict = {}):

		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		import Custom.NanoFXv2Lite.SpecialFX.BlinkerFX
		Custom.NanoFXv2Lite.SpecialFX.BlinkerFX.CreateBlinkerFX(pShip)


# Foundation.FolderDef('ship', 'ships.', dMode)



def Initialize():
	###############################################################################
	## Setup BridgeFX
	###############################################################################
	Custom.NanoFXv2Lite.NanoFX_Setup.SetupBridgeFX(mode)

	###############################################################################
	## Setup CameraFX
	###############################################################################
	Custom.NanoFXv2Lite.NanoFX_Setup.SetupCameraFX(mode)

	###############################################################################
	## Setup ExplosionFX
	###############################################################################
	Custom.NanoFXv2Lite.NanoFX_Setup.SetupExplosionFX(mode)

	###############################################################################
	## Setup SpecialFX
	###############################################################################
	Custom.NanoFXv2Lite.NanoFX_Setup.SetupSpecialFX(mode)

	###############################################################################
	## Setup WarpFX
	###############################################################################
	Custom.NanoFXv2Lite.NanoFX_Setup.SetupWarpFX(mode)

	NanoFXTrigger('NanoFXTrigger', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = dMode )
	NanoFXBlinkers('NanoFXBlinkers', Foundation.TriggerDef.ET_FND_CREATE_SHIP, dict = dMode )

	Foundation.OverrideDef('FixSetPosition', 'Bridge.Characters.CommonAnimations.SetPosition', 'Fixes20030217.SetPosition', dict = dMode )
	Foundation.OverrideDef('FixLoadBridge', 'LoadBridge.Load', 'Fixes20030217.LoadBridge_Load', dict = dMode )
	###############################################################################
	## End of Loading NanoFX
	###############################################################################



# If Regular NanoFX is already installed, leave it alone.
if not Foundation.MutatorDef.__dict__.has_key('NanoFX'):
	Initialize()