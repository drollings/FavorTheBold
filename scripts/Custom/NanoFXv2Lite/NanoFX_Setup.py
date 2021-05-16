###############################################################################
##	Filename:	NanoFXv2.py
##	
##	Nano's Special Effects Enhancements Version 2.0
##	
##	Updated:	09/30/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation
import Custom.NanoFXv2Lite.NanoFX_Config
import Custom.NanoFXv2Lite.BridgeFX.BrdgGfx
import Custom.NanoFXv2Lite.ExplosionFX.ExpGfx
import Custom.NanoFXv2Lite.ExplosionFX.ExpSfx
import Custom.NanoFXv2Lite.SpecialFX.SpecialGfx
import Custom.NanoFXv2Lite.SpecialFX.SpecialSfx
import Custom.NanoFXv2Lite.WarpFX.WarpSfx

TRUE = 1
FALSE = 0

###############################################################################
## Setup BridgeFX (Optimizations for BC Performance, Small Preview)
###############################################################################
def SetupBridgeFX(mode):
	
	### Override Stock Definitions ###
	Foundation.OverrideDef('NanoBridgeHit', 'Bridge.bridgeeffects.DoHullDamage', 'Custom.NanoFXv2Lite.BridgeFX.BrdgFX.NanoBridgeHit', dict = { 'modes': [ mode ] } )
	Custom.NanoFXv2Lite.BridgeFX.BrdgGfx.LoadNanoBrdgGfx()
	###
	if Custom.NanoFXv2Lite.NanoFX_Config.bFX_Enabled == TRUE:
		print "BridgeFX Enabled..."
		###
###############################################################################
## Setup CameraFX (Preview of Upcoming Camera Mod)
###############################################################################
def SetupCameraFX(mode):
	
	if Custom.NanoFXv2Lite.NanoFX_Config.cFX_Enabled == TRUE:
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoFlyByCamera', 'CameraModes.DropAndWatch', 'Custom.NanoFXv2Lite.CameraFX.CamFX.NanoFlyByCamera', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoViewScreenZoom', 'CameraModes.ViewscreenZoomTarget', 'Custom.NanoFXv2Lite.CameraFX.CamFX.NanoViewScreenZoom', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoFixWarpCam', 'WarpSequence.FixCamera', 'Custom.NanoFXv2Lite.CameraFX.CamFX.NanoFixWarpCam', dict = { 'modes': [ mode ] } )
		###
		print "CameraFX Enabled..."
		###
###############################################################################
## Setup ExplosionFX
###############################################################################
def SetupExplosionFX(mode):

	if Custom.NanoFXv2Lite.NanoFX_Config.eFX_Enabled == TRUE:
		### Load Explosion Gfx ###
		Custom.NanoFXv2Lite.ExplosionFX.ExpGfx.LoadNanoExpGfx()
		App.g_kIconManager.RegisterIconGroup("DamageTextures", "Custom.NanoFXv2Lite.ExplosionFX.ExpGfx", "LoadNanoDamageGfx")
		###
		### Load Explosion Sfx ###
		Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.LoadNanoExpSfx(mode)
		###
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoTorpedoShieldHit', 'Effects.TorpedoShieldHit', 'Custom.NanoFXv2Lite.ExplosionFX.ExpFX.NanoTorpedoShieldHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoTorpedoHullHit', 'Effects.TorpedoHullHit', 'Custom.NanoFXv2Lite.ExplosionFX.ExpFX.NanoTorpedoHullHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoPhaserHullHit', 'Effects.PhaserHullHit', 'Custom.NanoFXv2Lite.ExplosionFX.ExpFX.NanoPhaserHullHit', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoCollisionEffect', 'Effects.CollisionEffect', 'Custom.NanoFXv2Lite.ExplosionFX.ExpFX.NanoCollisionEffect', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoDeathSeq', 'Effects.ObjectExploding', 'Custom.NanoFXv2Lite.ExplosionFX.ExpFX.NanoDeathSeq', dict = { 'modes': [ mode ] } )
		###
		### Override Definitions for GlowFX ###
		Foundation.OverrideDef('RepairShipFullyGlowFix', 'Actions.ShipScriptActions.RepairShipFully', 'Custom.NanoFXv2Lite.ExplosionFX.GlowFX.RepairShipFullyGlowFix', dict = { 'modes': [ mode ] } )
		###
		print "ExplosionFX Enabled..."
		###
###############################################################################
## Setup SpecialFX
###############################################################################
def SetupSpecialFX(mode):
	
	import Custom.NanoFXv2Lite.SpecialFX.AtmosphereFX
	
	if Custom.NanoFXv2Lite.NanoFX_Config.sFX_Enabled == TRUE:
		### Load SpecialFX Gfx ###
		Custom.NanoFXv2Lite.SpecialFX.SpecialGfx.LoadNanoSpecialGfx()
		###
		### Load Explosion Sfx ###
		Custom.NanoFXv2Lite.SpecialFX.SpecialSfx.LoadNanoSpecialSfx(mode)
		###
		### Add Atmospheres to Planets
		Custom.NanoFXv2Lite.SpecialFX.AtmosphereFX.OverrideStockPlanets(mode)
		###
		print "SpecialFX Enabled..."
		###

###############################################################################
## Setup WarpFX
###############################################################################
def SetupWarpFX(mode):
	
	if Custom.NanoFXv2Lite.NanoFX_Config.wFX_Enabled == TRUE:
		### Load Warp Gfx ###
		App.g_kIconManager.RegisterIconGroup("EffectTextures", "Custom.NanoFXv2Lite.WarpFX.WarpGfx", "LoadNanoWarpNacelleGfx")
		App.g_kIconManager.RegisterIconGroup("WarpFlashTextures", "Custom.NanoFXv2Lite.WarpFX.WarpGfx", "LoadNanoWarpFlashGfx")
		###
		### Load Warp Sfx ###
		Custom.NanoFXv2Lite.WarpFX.WarpSfx.LoadNanoWarpSfx(mode)
		###
		### Override Stock Definitions ###
		Foundation.OverrideDef('NanoWarpSeq', 'WarpSequence.SetupSequence', 'Custom.NanoFXv2Lite.WarpFX.WarpFX.NanoWarpSeq', dict = { 'modes': [ mode ] } )
		###
		### Setup New AI
		#Foundation.OverrideDef.NanoIntercept = Foundation.OverrideDef('NanoIntercept', 'AI.PlainAI.Intercept.Intercept', 'Custom.NanoFXv2Lite.WarpFX.AI.NanoIntercept.NanoIntercept', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoWarp', 'AI.PlainAI.Warp.Warp', 'Custom.NanoFXv2Lite.WarpFX.AI.NanoWarp.NanoWarp', dict = { 'modes': [ mode ] } )
		Foundation.OverrideDef('NanoFollowThroughWarp', 'AI.PlainAI.FollowThroughWarp.FollowThroughWarp', 'Custom.NanoFXv2Lite.WarpFX.AI.NanoFollowThroughWarp.NanoFollowThroughWarp', dict = { 'modes': [ mode ] } )
		###
		print "WarpFX Enabled..."
		###
###############################################################################
## End of Loading NanoFX
###############################################################################
