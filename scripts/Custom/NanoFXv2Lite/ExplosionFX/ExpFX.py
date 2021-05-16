 ###############################################################################
##	Filename:	ExpFX.py
##
##	Nano's Explosion Effects Enhancements Version 2.0
##
##	Created:	03/11/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################

import App
import Foundation
import ExpSfx
import Custom.NanoFXv2Lite.NanoFX_Lib
import Custom.NanoFXv2Lite.NanoFX_Config
import Custom.NanoFXv2Lite.NanoFX_ScriptActions

import FoundationTech

g_GfxSet		= { "DebrisGfx"  : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/Debris", 'tga'),
					"ExpFlashGfx" : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash", 'tga'),
				    "ExplosionGfx" : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/Explosions", 'tga'),
					"NovaFlashGfx"   : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/NovaFlash", 'tga'),
					"NovaSphereGfx"   : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/NovaSphere", 'tga'),
					"NovaRingGfx"   : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/NovaRing", 'tga'),
					"ParticleGfx"  : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/Particles", 'tga')
				  }

g_SfxSet		= { "ExpShieldSfx"		: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpShield"),
					"ExpSmallSfx"		: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpSmall"),
					"ExpMedSfx"			: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpMed"),
					"ExpLargeSfx"		: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpLarge"),
					"ExpNovaSfx"		: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpNova"),
					"ExpCollisionSfx"	: Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetSfxList("ExpCollision")
				  }

g_ParticleControl = 0
g_SimultaneousControl = 0
CONST_MAXPARTICLES = Custom.NanoFXv2Lite.NanoFX_Config.eFX_ParticleControl
CONST_MAXSIMULTANEOUS = 200

###############################################################################
## Get Explosion File,  Random pick of Explosions
###############################################################################
def GetNanoGfxFile(sGfxSet, sFolderPath):
	
	### Random File ###
		
	#if (sGfxSet == "ExplosionGfx"):
		#global g_RandomExp
		#g_RandomExp = g_RandomExp + 1
		#if (g_RandomExp >= len(g_GfxSet[sGfxSet])):
			#g_RandomExp = 0
		#iRandom = g_RandomExp
	#else:
	iRandom = App.g_kSystemWrapper.GetRandomNumber(len(g_GfxSet[sGfxSet]))

	strFile = sFolderPath + g_GfxSet[sGfxSet][iRandom]

	return strFile

###############################################################################
## Control the Number of Particles being displayed at once so BC doesn't get
## bogged down or even CRASH!
###############################################################################	
def ControlParticles(pAction, iNum):
	
	global g_ParticleControl
	g_ParticleControl = g_ParticleControl + iNum
	#if g_ParticleControl >= CONST_MAXPARTICLES:
		#print "I have reached the Maximum of " + str(g_ParticleControl) + " Particles!"
		
	return 0
	
###############################################################################
## Control the Number of Particles being Played at once so BC doesn't bog down
###############################################################################	
def ControlSimultaneous(pAction, iNum):
	
	global g_SimultaneousControl
	g_SimultaneousControl = g_SimultaneousControl + iNum
	#if g_SimultaneousControl >= CONST_MAXSIMULTANEOUS:
		#print "I have exceeded the Maximum of " + str(g_SimultaneousControl) + " Simultaneous Particles!"
		
	return 0

###############################################################################
## New Sequences...
###############################################################################
###############################################################################
###############################################################################
## Weapon Explosion Sequence
###############################################################################
def CreateNanoWeaponExpSeq(pEvent, sType):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	
	### Setup ###
	pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
	if not pShip:
		return pSequence
	pSet = pShip.GetContainingSet()
	pAttachTo = pShip.GetNode()
	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	vEmitPos = pEvent.GetObjectHitPoint()
	vEmitDir = pEvent.GetObjectHitNormal()
	fSize  = pEvent.GetDamage() * (App.g_kSystemWrapper.GetRandomNumber(10) + 30) * 0.000035
	
	if sType == "TorpShieldHit":
		fSize = fSize / 2.0
		pAttachTo = pSet.GetEffectRoot()
	if sType == "PhaserHullHit":
		fSize = fSize * 2.0
	###
	if sType == "TorpHullHit":
		if (pEvent.GetDamage() >= 500 and sType == "TorpHullHit"):
			pSparks = CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
			pDebris = CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.4)
			if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
				pSparks = CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
			pSound = CreateNanoSoundSeq(pShip, "ExpMedSfx")
			pSequence.AddAction(pSound, App.TGAction_CreateNull(), 0.4)
		###	
		### Add Rotational Spin to Ship From Torp Explosion 25% Chance##
		if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
			if (pEvent.GetDamage() >= 200):
				if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_RotationFX == "On"):
					pSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateRotationSeq(pShip, pEvent.GetDamage()), App.TGAction_CreateNull(), 0.4)
				if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_LightFlickerFX == "On"):
					pSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5), App.TGAction_CreateNull(), 0.4)
			else:
				###
				if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_LightFlickerFX == "On"):
					if (App.g_kSystemWrapper.GetRandomNumber(100) < 10):
						pSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateFlickerSeq(pShip, 0.6))
				###
		if (Custom.NanoFXv2Lite.NanoFX_Config.sFX_PlasmaFX == "On"):
			pPlasma = Custom.NanoFXv2Lite.NanoFX_Lib.CreateSpecialFXSeq(pShip, pEvent, "PlasmaFX")
			if pPlasma != None:
				pSequence.AddAction(pPlasma)
		###
	### Create Nano's Large Explosion ###
	sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
	pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fBrightness = 0.6)
	pSequence.AddAction(pExplosion)
	sFile = GetNanoGfxFile("ExpFlashGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
	pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
	pSequence.AddAction(pFlash)
	### Create Nano's Small Explosion Sound ###
	if sType == "TorpShieldHit":
		pSound = CreateNanoSoundSeq(pShip, "ExpShieldSfx")
		pSequence.AddAction(pSound)
	else:
		pSound = CreateNanoSoundSeq(pShip, "ExpSmallSfx")
		pSequence.AddAction(pSound)
	###
	iNumPlume = 3
	for iPoint in range( iNumPlume ):
		sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 20, sType = "Plume")
		pSequence.AddAction(pExplosion)
		sFile = GetNanoGfxFile("ExpFlashGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
		pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
		pSequence.AddAction(pFlash)
	###
	return pSequence

###############################################################################
## ExpSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir = None):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	###
	vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.eFX_ExpSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES and g_SimultaneousControl < CONST_MAXSIMULTANEOUS:
			sFile = GetNanoGfxFile("ParticleGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(10)
			fVelocity = 0.5 + fSize + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01
			pSparks = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, bInheritVel = 0, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 1.0, sType = "ExpSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), 4.0)			
			ControlSimultaneous(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlSimultaneous", -1), App.TGAction_CreateNull(), 1.0)			
	###	
	return pSequence
	
###############################################################################
## DamageSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	fDuration = Custom.NanoFXv2Lite.NanoFX_Config.eFX_DamageSparkFXDuration
	###
	vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.eFX_DamageSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES and g_SimultaneousControl < CONST_MAXSIMULTANEOUS:
			sFile = GetNanoGfxFile("ParticleGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			fVelocity = (App.g_kSystemWrapper.GetRandomNumber(5) + 1) * 0.1
			pSparks = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fLifeTime = fDuration, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 1.5, sType = "DamageSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)
			ControlSimultaneous(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlSimultaneous", -1), App.TGAction_CreateNull(), 1.0)
	###
	return pSequence
	
###############################################################################
## Debris Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateNanoDebrisSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	fDuration = Custom.NanoFXv2Lite.NanoFX_Config.eFX_DebrisFXDuration
	###
	vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.eFX_DebrisFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES and g_SimultaneousControl < CONST_MAXSIMULTANEOUS:
			sFile = GetNanoGfxFile("DebrisGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Debris/")
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(5) + 5
			fVelocity = 1.0 + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01
			pDebris = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, bInheritVel = 1, fEmitVel = fVelocity, fLifeTime = fDuration, fVariance = 150.0, fDamping = 0.1, sType = "Debris")
			pSequence.AddAction(pDebris)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)
			ControlSimultaneous(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlSimultaneous", -1), App.TGAction_CreateNull(), 1.0)
	###
	return pSequence

###############################################################################
##  Create Nova WarpCore Nano Explosion Sequence
###############################################################################
def CreateNanoExpNovaSeq(pShip, fSize):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	pSet = pShip.GetContainingSet()
	###
	### Setup for Effect ###
	pAttachTo 	 = pSet.GetEffectRoot()
	pEmitFrom 	 = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	pWarpcore 	 = pShip.GetPowerSubsystem()
	pWarpcoreEmitPos = pWarpcore.GetPosition()
	vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
	fFlashColor   = Custom.NanoFXv2Lite.NanoFX_Lib.GetOverrideColor(pShip, "ExpFX")
	iShow = 0.0
	if pShip.GetName() == "Player" or pShip.GetName() == "player":
		iShow = 2.0
	if (fFlashColor == None):
		sRace 			= Custom.NanoFXv2Lite.NanoFX_Lib.GetSpeciesName(pShip)
		fFlashColor 	= Custom.NanoFXv2Lite.NanoFX_Lib.GetRaceTextureColor(sRace)
	###
	if fSize != 1:
		# sFile = GetNanoGfxFile("NovaRingGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/NovaRing/")
		# pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (5.0 + iShow), pWarpcoreEmitPos, iTiming = 64, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.5)
		# pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.4)
		sFile = GetNanoGfxFile("NovaSphereGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/NovaSphere/")
		pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 28)
		pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.5)
		sFile = GetNanoGfxFile("NovaFlashGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/NovaFlash/")
		pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 20)
		pSequence.AddAction(pExplosion)
		### Create Nano's Nova Explosion Sound ###
		pSound = CreateNanoSoundSeq(pShip, "ExpNovaSfx")
		pSequence.AddAction(pSound)
		###
		### Damage the model with Warp Core Explosion ###
		pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, pShip.GetRadius(), 600.0), App.TGAction_CreateNull(), 0.7)
	else:
		fSize = pShip.GetRadius() / 1.2
		### Create Nano's Nova Explosion Sound ###
		pSound = CreateNanoSoundSeq(pShip, "ExpLargeSfx")
		pSequence.AddAction(pSound)
		###
	iNovaSparks = Custom.NanoFXv2Lite.NanoFX_Config.eFX_ExpSparkFXLevel * 7.0
	for iPoint in range( iNovaSparks ):
		fRand = App.g_kSystemWrapper.GetRandomNumber(100) *  0.01
		pSparks = CreateExpSparkSeq(fSize * (0.8 + fRand), pEmitFrom, pAttachTo, pWarpcoreEmitPos, vEmitDir)
		pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.50)
	###
	return pSequence

###############################################################################
##  Create Large Nano Explosion Sequence
###############################################################################
def CreateNanoExpLargeSeq(pShip, iNumPlume):
	
	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	###
	### Setup for Effect ###
	pSet = pShip.GetContainingSet()
	pEmitFrom = pShip.GetRandomPointOnModel()
	pAttachTo = pShip.GetNode()
	vEmitPos = App.NiPoint3(0, 0, 0)
	vEmitDir = App.NiPoint3(1, 1, 1)
	fSize     = pShip.GetRadius() * 0.50
	sFile     = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
	###
	pSound = CreateNanoSoundSeq(pShip, "ExpMedSfx")
	pSequence.AddAction(pSound)
	pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
	pSequence.AddAction(pExplosion)
	pSparks = CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
	pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
	pDebris = CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
	pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
	for iPoint in range( iNumPlume ):
		sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume", fBrightness = 0.3)
		pSequence.AddAction(pExplosion)
		pSparks =CreateExpSparkSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
		pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
		pDebris = CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
		pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
	###
	return pSequence

###############################################################################
##  Create Small Nano Explosions Sequence (Crack the Ship Like an EGG!)
###############################################################################
def CreateNanoExpSmallSeq(pShip, fTime):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	###
	### Setup for Effect ###
	iNumPlume = 1
	pSet = pShip.GetContainingSet()
	pAttachTo = pShip.GetNode()
	vEmitPos = App.NiPoint3(0, 0, 0)
	vEmitDir = App.NiPoint3(1, 1, 1)
	###
	### Create Nano's Explosion Sound ###
	pSound = CreateNanoSoundSeq(pShip, "ExpLargeSfx")
	pSequence.AddAction(pSound)
	fExplosionTime = 0.0
	while (fExplosionTime < fTime):
		###
		### Create Nano's Visual Smaller Explosions ###
		pEmitFrom = pShip.GetRandomPointOnModel()
		fSize  = pShip.GetRadius() * (App.g_kSystemWrapper.GetRandomNumber(40) + 20) * 0.01
		sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
		pSequence.AddAction(pExplosion)
		pSparks = CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
		pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
		pDebris = CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
		pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
		for iPoint in range( iNumPlume ):
			sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume")
			pSequence.AddAction(pExplosion)
			pSparks = CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
			pDebris = CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
		###
		### Damage the model with these explosions ###
		pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, pShip.GetRadius() / 2.0, 1200.0), App.TGAction_CreateNull(), 0.3)
		fExtraDamage = 0.1
		while (fExtraDamage < fTime):
			pEmitFrom = pShip.GetRandomPointOnModel()
			pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, pShip.GetRadius() / 3.0, 1200.0), App.TGAction_CreateNull(), 0.3)
			fExtraDamage = fExtraDamage + 0.04
		###
		fExplosionTime = fExplosionTime + 0.5
		
	return pSequence

###############################################################################
## Create Sound Sequence
###############################################################################
def CreateNanoSoundSeq(pShip, sSoundSet):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	pSet = pShip.GetContainingSet()
	###
	### Get a random sound from that group ###
	#lSoundGroup = g_SfxSet[ sSoundSet ]
	#sSound = Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetRandomSound( lSoundGroup )
	sSound = Custom.NanoFXv2Lite.ExplosionFX.ExpSfx.GetRandomSound( sSoundSet[:-3] )
	###
	### Add an action to play the sound. ###
	pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
	pSound.SetNode(pShip.GetNode())
	pSequence.AddAction(pSound)
	###
	return pSequence

###############################################################################
## New Death Sequence by Nano
###############################################################################
def NanoDeathSeq(pShip):
	
	### Holds the Entire Death Sequence ###
	pFullSequence = App.TGSequence_Create()
	###
	### Setup Sequence Timing ###
	fTotalSequenceTime = 14
	fExplosionShift = -8.0
	###
	### Set up Exploding Ship Properties ###
	pExplodingShip = App.ShipClass_Cast(pShip)

	bBreach = 0		# Dasher42's addition; no violent explosion if the ship doesn't have a core

	# Dasher42's change:  FTB has a consistent standard, we don't *want* this.
	# pExplodingShip.SetMass(50000)
	# pExplodingShip.SetRotationalInertia(11000)

	pPower = pExplodingShip.GetPowerSubsystem()
	if pPower and not pPower.IsDisabled():
		bBreach = 1

	if (pExplodingShip.GetName() == "Player") or (pExplodingShip.GetName() == "player"):
		pExplodingShip.SetLifeTime (fTotalSequenceTime)
		pWarpPower = pExplodingShip.GetPowerSubsystem()
		if pWarpPower.GetPowerOutput() > 0:
			pWarpPower = pExplodingShip.GetRadius() * 15
		else:
			pWarpPower = 15
		fRadius = pWarpPower
	else:
		pExplodingShip.SetLifeTime (fTotalSequenceTime / 2 + 1)
		pWarpPower = pExplodingShip.GetPowerSubsystem()
		pWarpPower = (pWarpPower.GetAvailablePower() * 0.025) + (pWarpPower.GetPowerOutput() * 0.075)
		pWarpPower = pWarpPower * Custom.NanoFXv2Lite.NanoFX_Config.eFX_SplashRadius
		fRadius = pWarpPower / 150.0
		if pWarpPower:
			pExplodingShip.SetSplashDamage(pWarpPower, fRadius)
			print("Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
	###
	### Begin Death Sequence ###
	############################
	###
	### Flicker some lights ###
	if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_LightFlickerFX == "On"):
		pFullSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateFlickerSeq(pExplodingShip, 3.0, sStatus = "Off"), App.TGAction_CreateNull(), 1.0)
	###
	### Create Nano's Initial Large explosions ###
	pFullSequence.AddAction(CreateNanoExpSmallSeq(pExplodingShip, 0.01), App.TGAction_CreateNull(), 0.2)
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 3.2 + fExplosionShift)
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 3.05 + fExplosionShift)
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 2.85 + fExplosionShift)
	###
	### Destroy Model into Debris Parts ###
	if bBreach:
		pFullSequence.AddAction(CreateNanoExpSmallSeq(pExplodingShip, 2.0), App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)

	pFullSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "TurnOffLights", pExplodingShip), App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)

	###
	### Add Random Spin to Model ###
	if (Custom.NanoFXv2Lite.NanoFX_Config.eFX_RotationFX == "On"):
		pFullSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 700), App.TGAction_CreateNull(), 0.3)
		pFullSequence.AddAction(Custom.NanoFXv2Lite.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 1000, 0.5), App.TGAction_CreateNull(), fTotalSequenceTime - 1.6 + fExplosionShift)
	###
	### Create Nano's Warp Core Explosion ###
	if bBreach:
		pFullSequence.AddAction(CreateNanoExpNovaSeq(pExplodingShip, fRadius / 15), App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
	#pFullSequence.AddAction(ShakeSequence(1.5), App.TGAction_CreateNull(), fTotalSequenceTime - 1.3 + fExplosionShift)
	###
	### Create Nano's Final Explosions ###
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.95 + fExplosionShift)
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.85 + fExplosionShift)
	pFullSequence.AddAction(CreateNanoExpLargeSeq(pExplodingShip, 2), App.TGAction_CreateNull(), fTotalSequenceTime - 1.65 + fExplosionShift)
	###
	#pFullSequence.SetUseRealTime(1)
	pFullSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pFullSequence), fTotalSequenceTime)
	pFullSequence.Play()
	###
	bFound = 0
	for sName in Custom.NanoFXv2Lite.NanoFX_Lib.g_LightsOff:
		if pShip.GetName() == sName:
			bFound = 1
		if bFound == 1:
			Custom.NanoFXv2Lite.NanoFX_Lib.g_LightsOff.remove(pShip.GetName())
			
	return

###############################################################################
## New Event Handling...
###############################################################################
###############################################################################
###############################################################################
## Torpedo Hitting Shield Event
###############################################################################
def NanoTorpedoShieldHit(pShip, pEvent):

	### Set up ###
	### Create Explosion Seq ###
	pSequence = CreateNanoWeaponExpSeq(pEvent, "TorpShieldHit")
	###
	if pSequence:
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
		pSequence.Play()
		###
		#pShip.CallNextHandler(pEvent)

###############################################################################
## Torpedo Hitting Hull Event
###############################################################################
def NanoTorpedoHullHit(pShip, pEvent):

	### Set up ###
	### Create Explosion Seq ###
	pSequence = CreateNanoWeaponExpSeq(pEvent, "TorpHullHit")
	###
	if pSequence:
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
		pSequence.Play()
		###
		#pShip.CallNextHandler(pEvent)

###############################################################################
## Phaser Hitting Hull Event
###############################################################################
def NanoPhaserHullHit(pShip, pEvent):
	
	### Set up ###
	### Create an Explosion 50% Chance ###
	if (App.g_kSystemWrapper.GetRandomNumber(100) < 50):
		pSequence = CreateNanoWeaponExpSeq(pEvent, "PhaserHullHit")
		###
		if pSequence:
			pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
			pSequence.Play()
		###
		#pShip.CallNextHandler(pEvent)
	

###############################################################################
## Collision Event
###############################################################################
def NanoCollisionEffect(pShip, pEvent):

	### Setup ###
	pSet = pShip.GetContainingSet()
	fSize     = pShip.GetRadius()
	pAttachTo = pSet.GetEffectRoot()
	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	pSequence = App.TGSequence_Create()
	###
	### Get the collision points ###
	for iPoint in range( pEvent.GetNumPoints() ):
		vEmitPos = pEvent.GetPoint(iPoint)
		vEmitDir = App.TGPoint3_GetRandomUnitVector()

		### Add an explosion at this point ###
		sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pCollision = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, None, pAttachTo, fSize, vEmitPos, vEmitDir)
		pSequence.AddAction(pCollision)
		pSound = CreateNanoSoundSeq(pShip, "ExpCollisionSfx")
		pSequence.AddAction(pSound)
	###
	pSequence.Play()
	###
	pShip.CallNextHandler(pEvent)

###############################################################################
## End of ExplosionFX
###############################################################################
