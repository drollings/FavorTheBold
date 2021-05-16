import Foundation


# NonSerializedObjects = ('mode', 'version', 'MotionBlurOverrider', 'mbOverrider')

mode = Foundation.MutatorDef('Favor The Bold')
Foundation.MutatorDef.FTB = mode

mode.bBase = 1
bDebug = 1

__version__ = 20040318


# import App
# Foundation.bfEra = App.g_kConfigMapping.GetIntValue("QuickBattle", "Ships Unlocked1")

Foundation.FolderDef('ship', 'ships.', { 'modes': [ mode ] })
Foundation.FolderDef('hp', 'ships.Hardpoints.', { 'modes': [ mode ] })
# Foundation.FolderDef('ship', 'ftb.ships.setup.', { 'modes': [ mode ] })
# Foundation.FolderDef('hp', 'ftb.ships.hp.', { 'modes': [ mode ] })

try:
	Foundation.OverrideDef.Intercept_Dasher.AddToMutator(mode)
	Foundation.OverrideDef.Orbit_Dasher.AddToMutator(mode)
except:
	print "Warning:  Dasher42's intercept not detected!"

# class EraFlag(Foundation.OverrideDef):
# 	def __init__(self, name, bitval, dict = {}):
# 		self.bitval = bitval
# 		Foundation.OverrideDef.__init__(self, name, self, self)
# 
# 	#def AddToMutator(self, toMode):
# 	#	self.Activate()
# 
# 	def Activate(self):
# 		Foundation.bfEra = Foundation.bfEra | self.bitval
# 		print 'Activating era', self.name, self.bitval, Foundation.bfEra
# 
# 	def Deactivate(self):
# 		App.g_kConfigMapping.SetIntValue("QuickBattle", "Ships Unlocked1", Foundation.bfEra)

Foundation.ERA_ENT = 1
Foundation.ERA_TOS = 2
Foundation.ERA_TMP = 4
Foundation.ERA_PRETNG = 8
Foundation.ERA_TNG = 16
Foundation.ERA_DS9 = 32
Foundation.ERA_NEMESIS = 64

# import Custom.FTB.ships.FTB_ENTNX01
# import Custom.FTB.ships.FTB_TOSConstitution
# import Custom.FTB.ships.FTB_ConstitutionMk2
# import Custom.FTB.ships.FTB_Excelsior
# import Custom.FTB.ships.FTB_Galaxy
# import Custom.FTB.ships.FTB_Sovereign
# import Custom.FTB.ships.FTB_SovereignMk2

import FoundationTech
import ftb.Tech
import ftb.Tech.AblativeArmour
import ftb.Tech.Shields
import ftb.Tech.DamperWeapon

Foundation.LoadExtraPlugins('scripts\\Custom\\FTB\\Autoload')
Foundation.LoadExtraPlugins('scripts\\Custom\\FTB\\ships')

# era1 = Foundation.MutatorDef('Era:  Enterprise')
# era1.startShipDef = Foundation.ShipDef.FTBNX01
# era2 = Foundation.MutatorDef('Era:  TOS')
# era2.startShipDef = Foundation.ShipDef.FTBConstitution
# era3 = Foundation.MutatorDef('Era:  TMP')
# era3.startShipDef = Foundation.ShipDef.FTBConstitutionMk2
# era4 = Foundation.MutatorDef('Era:  Pre-TNG')
# era4.startShipDef = Foundation.ShipDef.FTBExcelsior
# era5 = Foundation.MutatorDef('Era:  TNG')
# era5.startShipDef = Foundation.ShipDef.FTBGalaxy
# era6 = Foundation.MutatorDef('Era:  DS9')
# era6.startShipDef = Foundation.ShipDef.FTBSovereign
# era7 = Foundation.MutatorDef('Era:  Nemesis')
# era7.startShipDef = Foundation.ShipDef.FTBSovereignMk2

# # EraFlag('Reset', 0, { 'modes': [ mode ] } )
# EraFlag('Era:  Enterprise', 1, { 'modes': [ era1 ] })
# Foundation.FolderDef('ship', 'ftb.ships.ent.setup.', { 'modes': [ era1 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.ent.hp.', { 'modes': [ era1 ] })
# EraFlag('Era:  TOS', 2, { 'modes': [ era2 ] })
# Foundation.FolderDef('ship', 'ftb.ships.tos.setup.', { 'modes': [ era2 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.tos.hp.', { 'modes': [ era2 ] })
# EraFlag('Era:  TMP', 4, { 'modes': [ era3 ] })
# Foundation.FolderDef('ship', 'ftb.ships.tmp.setup.', { 'modes': [ era3 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.tmp.hp.', { 'modes': [ era3 ] })
# EraFlag('Era:  Pre-TNG', 8, { 'modes': [ era4 ] })
# Foundation.FolderDef('ship', 'ftb.ships.pretng.setup.', { 'modes': [ era4 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.pretng.hp.', { 'modes': [ era4 ] })
# EraFlag('Era:  TNG', 16, { 'modes': [ era5 ] })
# Foundation.FolderDef('ship', 'ftb.ships.tng.setup.', { 'modes': [ era5 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.tng.hp.', { 'modes': [ era5 ] })
# EraFlag('Era:  DS9', 32, { 'modes': [ era6 ] })
# Foundation.FolderDef('ship', 'ftb.ships.ds9.setup.', { 'modes': [ era6 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.ds9.hp.', { 'modes': [ era6 ] })
# EraFlag('Era:  Nemesis', 64, { 'modes': [ era7 ] })
# Foundation.FolderDef('ship', 'ftb.ships.nemesis.setup.', { 'modes': [ era7 ] })
# # Foundation.FolderDef('hp', 'ftb.ships.nemesis.hp.', { 'modes': [ era7 ] })
			

if bDebug:
	Foundation.SystemDef('Blackness', 0, dict = { 'modes': [ mode ] } )


class MotionBlurOverrider(Foundation.OverrideDef):
	def __init__(self, name, dict):
		self.overridden = 0
		Foundation.MutatorElementDef.__init__(self, name, dict)

	def Activate(self):
		import App
		if App.g_kLODModelManager.IsMotionBlurEnabled() == 1:
			App.g_kLODModelManager.SetMotionBlurEnabled(0)
			self.overridden = 1

	def Deactivate(self):
		import App
		if self.overridden:
			App.g_kLODModelManager.SetMotionBlurEnabled(1)
			self.overridden = 0

MotionBlurOverrider('FTB Motion Blur Override', { 'modes': [ mode ] })

Foundation.SoundDef('Custom/FTB/Sfx/Weapons/RomPlasmaBurst.wav', 'FTB Plasma', 1.0, { 'modes': [ mode ] })

oIPhasers = Foundation.OverrideDef('Inaccurate Phasers', 'TacticalControlHandlers.FireWeapons', 'FoundationTech.FireWeapons', { 'modes': [ mode ] } )

