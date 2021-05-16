###############################################################################
##	Filename:	BrdgFX.py
##	
##	Nano's Bridge Effects Enhancements Version 0.1 (No real Changes, just Optimized Game Performance)
##	
##	Created:	03/14/2003 - NanoByte a.k.a Michael T. Braams
###############################################################################
import App
import Foundation
import Custom.NanoFXv2Lite.NanoFX_Lib
import Custom.NanoFXv2Lite.NanoFX_Config
import Custom.NanoFXv2Lite.NanoFX_ScriptActions

g_GfxSet		= { "DebrisGfx"  : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/Debris", 'tga'),
					"ExpFlashGfx" : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash", 'tga'),
				    "ExplosionGfx" : Foundation.GetFileNames("Custom/NanoFXv2/BridgeFX/Gfx/Explosions", 'tga'),
					"ParticleGfx"  : Foundation.GetFileNames("Custom/NanoFXv2/ExplosionFX/Gfx/Particles", 'tga')
				  }

g_ParticleControl = 0
CONST_MAXPARTICLES = Custom.NanoFXv2Lite.NanoFX_Config.bFX_ParticleControl

###############################################################################
## Get Explosion File,  Random pick of Explosions
###############################################################################
def GetNanoGfxFile(sGfxSet, sFolderPath):
	
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
	#print g_ParticleControl
		
	return 0
	
###############################################################################
## ExpSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	###
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.bFX_ExpSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("ParticleGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(10)
			fVelocity = 1.0 + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01 - 0.2
			fVelocity = fVelocity * fSpeed
			pSparks = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 0.4, vGravity = vGravity, sType = "ExpSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), 4.0)			
	###
	return pSequence
	
###############################################################################
## DamageSpark Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	fDuration = Custom.NanoFXv2Lite.NanoFX_Config.bFX_DamageSparkFXDuration
	###
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.bFX_DamageSparkFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("ParticleGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Particles/")
			fVelocity = (App.g_kSystemWrapper.GetRandomNumber(5) + 1) * 0.1
			fVelocity = fVelocity * fSpeed
			pSparks = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fLifeTime = fDuration, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 1.5, vGravity = vGravity, sType = "DamageSparks")
			pSequence.AddAction(pSparks)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)			
	###
	return pSequence
	
###############################################################################
## Debris Sequence (Produce Effect Level based on NanoFX_Config)
###############################################################################
def CreateNanoDebrisSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed = 1, vGravity = None):

	### Create Sequence Object ###
	pSequence = App.TGSequence_Create()
	fDuration = 3.0
	###
	for iNum in range(Custom.NanoFXv2Lite.NanoFX_Config.eFX_DebrisFXLevel):
		if g_ParticleControl < CONST_MAXPARTICLES:
			sFile = GetNanoGfxFile("DebrisGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/Debris/")
			fRandomSize = App.g_kSystemWrapper.GetRandomNumber(5) + 5
			fVelocity = 1.0 + App.g_kSystemWrapper.GetRandomNumber(fSize * 100 + fRandomSize) * 0.01
			fVelocity = fVelocity * fSpeed
			pDebris = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, bInheritVel = 1, fLifeTime = fDuration, fEmitVel = fVelocity, fVariance = 150.0, fDamping = 0.1, vGravity = vGravity, sType = "Debris")
			pSequence.AddAction(pDebris)
			ControlParticles(None, 1)
			pSequence.AddAction(App.TGScriptAction_Create(__name__, "ControlParticles", -1), App.TGAction_CreateNull(), fDuration)
	###
	return pSequence


def CreateSmoke (fDuration):
	# create smoke
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")
	if (pBridgeObject):
		pSequence = App.TGSequence_Create()
		pAction = App.BridgeEffectAction_CreateSmoke (fDuration, 1.5, 0.01, pBridgeObject, None, "data/sphere.tga")
		pController = pAction.GetController ()

		# Setup some default values for velocity, colors and alpha
		# Time zero.
		pController.AddColorKey (0.0, 0.8, 0.8, 0.8)
		pController.AddAlphaKey (0.0, 0.75)
		pController.AddSizeKey (0.0, 2.5)

		# End of life.
		pController.AddAlphaKey (1.0, 0.0)
		pController.AddSizeKey (1.0, 20.0)
		pController.SetEmitVelocity (40)
		pController.SetAngleVariance (60)
		
		pcHardpointName = pAction.GetHardpointName ()

		pBridgeObject.DoCrewReactions (pcHardpointName)
		pBridgeObject.FlickerLCARs(1.0)

		###

		pSequence.AddAction(pAction)
		#pSequence.Play()

def CreateSpark (fDuration):
	# create spark
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")

	if (pBridgeObject):
		pSequence = App.TGSequence_Create()
		pAction = App.BridgeEffectAction_CreateSparks (fDuration, fDuration - 0.005 * 40, 0.005, pBridgeObject, None, "data/spark.tga")
		pController = pAction.GetSparkController ()

		# Setup some default values for velocity, colors and alpha
		pController.AddColorKey (0.0, 1.0, 1.0, 1.0)
		pController.AddColorKey (0.5, 1.0, 1.0, 0.6)
		pController.AddColorKey (1.0, 1.0, 0.7, 0.7)
		
		pController.AddAlphaKey (0.0, 1.0)
		pController.AddAlphaKey (0.5, 1.0)
		pController.AddAlphaKey (1.0, 0.0)

		pController.AddSizeKey (0.0, 0.35)

		pController.SetEmitVelocity (150.0)
		pController.SetGravity (0.0, 0.0, -150.0)
		pController.SetTailLength (10.0)

		###

		pSequence.AddAction(pAction)
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence))
		pSequence.SetUseRealTime(1)
		pSequence.Play()
		
		pcHardpointName = pAction.GetHardpointName ()

		pBridgeObject.DoCrewReactions (pcHardpointName)
		pBridgeObject.FlickerLCARs(1.0)

	return

def CreateExplosion (fDuration):
	# Create explosion
	pSet = App.g_kSetManager.GetSet("bridge")
	pBridgeObject = App.BridgeObjectClass_GetObject (pSet, "bridge")

	if (pBridgeObject):
		# Create sequence
		pAttachTo = pBridgeObject.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(0, 0, 150)
		vGravity = App.TGPoint3()
		vGravity.SetXYZ(0, 0, -150)
		fSize     = pBridgeObject.GetRadius() * 0.05

		pSequence = App.TGSequence_Create()
		
		iFun = 3
		for iPoint in range( iFun ):
			pEmitFrom = pBridgeObject.GetRandomPointOnModel()
			fSpeed = 5.0
			pSparks = CreateExpSparkSeq(fSize * 2.0, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
			fSpeed = 100.0
			pSparks = CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pSparks)
			fSpeed = 10.0
			pDebris = CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir, fSpeed, vGravity)
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			
			#pSequence.AddAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "NanoDamageShip", pBridgeObject, pEmitFrom, fSize / 3.0, 1200.0), App.TGAction_CreateNull(), 0.3)
			
			sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/BridgeFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 24.0, fBrightness = 0.6)
			pSequence.AddAction(pExplosion)
			sFile = GetNanoGfxFile("ExpFlashGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
			pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
			pSequence.AddAction(pFlash)
			iNumPlume = 3
			for iPoint in range( iNumPlume ):
				sFile = GetNanoGfxFile("ExplosionGfx", "Custom/NanoFXv2/BridgeFX/Gfx/Explosions/")
				pExplosion = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 16.0, sType = "Plume")
				pSequence.AddAction(pExplosion)
				sFile = GetNanoGfxFile("ExpFlashGfx", "Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
				pFlash = Custom.NanoFXv2Lite.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
				pSequence.AddAction(pFlash)
				fSpeed = 5.0
				pSparks = CreateExpSparkSeq(fSize * 2.0, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				fSpeed = 100.0
				pSparks = CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pSparks)
				fSpeed = 10.0
				pDebris = CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir, fSpeed, vGravity)
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			###	
		
		#pSequence.SetUseRealTime(1)
		pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2Lite.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
		pSequence.Play ()

	return


def NanoBridgeHit (fCurHullPercent):
	
	if Custom.NanoFXv2Lite.NanoFX_Config.bFX_Enabled == 0:
		return
		
	pSet = App.g_kSetManager.GetSet ("bridge")
	if not pSet:
		return

	pCamera = App.ZoomCameraObjectClass_GetObject (pSet, "maincamera")
	if not pCamera:
		return
		
	if (fCurHullPercent > 0.85):
		# Light damage.  Do sparks most of the time, occasionally steam
		r = App.g_kSystemWrapper.GetRandomNumber (100)
		#if (r < 20):
			#CreateSmoke (5)		# 5 seconds of smoke
		#else:
	#CreateSpark (1.0)
		CreateExplosion (15)
		SparkSound()
		# Shake the camera also.
		pCamera.SetShake (1.0, 1.0)
	elif (fCurHullPercent > 0.70):
		# Moderate damage
		#r = App.g_kSystemWrapper.GetRandomNumber (100)
#		if (r < 50):
#			CreateSmoke (10)

		# always create sparks
		#CreateSpark (1.5)
		CreateExplosion (15)
		SparkSound()

		# Shake the camera also.
		pCamera.SetShake (2.0, 1.0)
	else:
		# Heavy damage
		# Do explosions, steam, and sparks.
		#CreateSmoke (10)
		#CreateSpark (2.00)
		CreateExplosion (15)
		SparkSound()

		# Shake the camera also.
		pCamera.SetShake (3.0, 3.0)

	###

	return

def SparkSound():
	# Don't do anything if the rendered set isn't the bridge.
	try:
		if App.g_kSetManager.GetRenderedSet().GetName() != "bridge":
			return
	except AttributeError:
		return

	# How long has it been since the last spark sound?  These sounds
	# are very distinctive, and we don't want them constantly playing
	# whenever the bridge shows damage.
	global g_fNextSpark
	fCurrentTime = App.g_kUtopiaModule.GetRealTime()
	try:
		if g_fNextSpark > fCurrentTime:
			return
	except NameError:
		pass

	g_fNextSpark = fCurrentTime + (App.g_kSystemWrapper.GetRandomNumber(2000) / 1000.0)

	import LoadTacticalSounds
	sSound = LoadTacticalSounds.GetRandomSound(g_lsSparks)
	pSound = App.g_kSoundManager.GetSound(sSound)
	if pSound:
		pSound.Play()
	
	###

g_lsSparks = ( "ConsoleExplosion1", "ConsoleExplosion2",
			   "ConsoleExplosion3", "ConsoleExplosion4",
			   "ConsoleExplosion5", "ConsoleExplosion6",
			   "ConsoleExplosion7", "ConsoleExplosion8" )
