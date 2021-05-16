###############################################################################
##	Filename:	ExpSfx.py
##
##	Explosion Sound Effects Module for Loading Sounds Dynamically
##
##	Created:	03/09/2003 - NanoByte a.k.a Michael T. Braams
##	Modified:	04/17/2004 - Dasher42 a.k.a Daniel Rollings
###############################################################################
import App
import Foundation


# By setting this up as an object with a __call__ method, we can encapsulate its data along with it.
# The main thing was to stop using GetFileNames() for GetRandomSound, for efficiency.
GetRandomSound = Foundation.MediaListDef('ExpSfx')

def LoadNanoExpSfx(mode):
	dSoundFolders = {
		'ExpNova': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpNova',
		'ExpLarge': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpLarge',
		'ExpMed': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpMed',
		'ExpSmall': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpSmall',
		'ExpShield': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpShield',
		'ExpCollision': 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpCollision',
	}

	for i in dSoundFolders.items():
		GetRandomSound.LoadFolder(i[0], i[1], 'wav')

	import StaticDefs
	for i in range(1, 11):
		sKey = 'Death Explosion ' + str(i)
		oSound = Foundation.soundList._keyList[sKey]
		GetRandomSound.AddSoundDef('ExpSmall', oSound)

	for i in range(1, 20):
		sKey = 'Explosion ' + str(i)
		oSound = Foundation.soundList._keyList[sKey]
		GetRandomSound.AddSoundDef('ExpMed', oSound)

	for i in range(1, 9):
		sKey = 'Big Death Explosion ' + str(i)
		oSound = Foundation.soundList._keyList[sKey]
		GetRandomSound.AddSoundDef('ExpLarge', oSound)

	for i in range(1, 9):
		sKey = 'Collision ' + str(i)
		oSound = Foundation.soundList._keyList[sKey]
		GetRandomSound.AddSoundDef('ExpCollision', oSound)

def GetSfxList(sSoundSet):
	return GetRandomSound.dFiles[sSoundSet]


# ###############################################################################
# ## Get Sfx List for Game use
# ###############################################################################
# def GetSfxList(sSoundSet):
#
# 	sFileNames = Foundation.GetFileNames('Custom/NanoFXv2/ExplosionFX/Sfx/' + sSoundSet, 'wav')
# 	sSfxList = []
#
# 	for fileIndex in range(len(sFileNames)):
# 		sSfxList.append(sSoundSet + str(fileIndex))
#
# 	return sSfxList
#
# ###############################################################################
# ## Setup Sound Defs for Explosion Sounds
# ###############################################################################
# def LoadNanoExpSfx(mode):
#
# 	### Collision Explosion Sfx ###
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpCollision'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpCollision" + str(loadIndex), 1.0, { 'modes': [ mode ] })
# 	###
# 	### Shield Explosion Sfx (Weapon Hit Sheild) ###
# 	sIndex = "1"
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpShield'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpShield" + str(loadIndex), 1.0), { 'modes': [ mode ] }
# 	###
# 	### Small Explosion Sfx (Weapon Hit Hull) ###
# 	sIndex = "1"
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpSmall'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpSmall" + str(loadIndex), 1.0), { 'modes': [ mode ] }
# 	###
# 	### Medium Explosion Sfx (Debris and Sparks) ###
# 	sIndex = "1"
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpMed'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpMed" + str(loadIndex), 1.0), { 'modes': [ mode ] }
# 	###
# 	### Large Explosion Sfx (Ship Destroyed) ###
# 	sIndex = "1"
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpLarge'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpLarge" + str(loadIndex), 1.0, { 'modes': [ mode ] })
# 	###
# 	### Nova Explosion Sfx (Warpcore Explosion!)###
# 	sIndex = "1"
# 	sFolder = 'Custom/NanoFXv2/ExplosionFX/Sfx/ExpNova'
# 	sFileNames = Foundation.GetFileNames(sFolder, 'wav')
# 	for loadIndex in range(len(sFileNames)):
# 		strFile = sFolder + '/' + sFileNames[loadIndex]
# 		Foundation.SoundDef(strFile, "ExpNova" + str(loadIndex), 1.0, { 'modes': [ mode ] })
#
# ###############################################################################
# ## Get a Random Sfx, try not to repeat last 3 sounds in Recent List
# ###############################################################################
# def GetRandomSound(sSfxList):
#
# 	sSound = sSfxList[ App.g_kSystemWrapper.GetRandomNumber( len(sSfxList) ) ]
# 	return sSound
#
# ###############################################################################
# ## End of Exp Sfx
# ###############################################################################
