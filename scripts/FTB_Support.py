NonSerializedObjects = ('AddLODS')

def AddLODs(pLODModel, filenames, sizeMod, sSearchGlow, sSearchSpec, sSuffixSpec, sShipDef = None):
	# surfaceDR = max(12.0, 20.0 * sizeMod / 1000.0)
	# internalDR = max(12.0, 15.0 * sizeMod / 1000.0)
	surfaceDR = max(12.0, 20.0 * sizeMod / 1000.0)
	internalDR = max(12.0, 15.0 * sizeMod / 1000.0)
	burnValue = 200
	holeValue = 1400
	# startLOD = 50 + (200.0 * sizeMod / 1000.0)
	startLOD = 40 + (80.0 * sizeMod / 1000.0)
	count = 1

	if sShipDef:
		try:
			import Foundation
			s = Foundation.shipList[sShipDef]
			holeValue = s.dTechs['Ablative Armour'] + holeValue
		except:
			pass

		try:
			holeValue = holeValue + s.stats['hullIndex']
		except:
			pass

	lastFile = filenames[-1]

	for i in filenames:
		if i is lastFile:
			startLOD = sizeMod * 10.0
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel.AddLOD(i, 10, startLOD, surfaceDR, internalDR, burnValue, holeValue, sSearchGlow, sSearchSpec, sSuffixSpec)
		startLOD = startLOD * (count + 2.0)
		count = count + 1
		if (count > 1):
			internalDR = internalDR * 1.5
			
		if (count > 2):
			surfaceDR = surfaceDR * 1.5		# Experimental addition


def Register(sShipFile, dict, bCustomFolder = 0):
	pModule = None
	if bCustomFolder:
		pModule = __import__(sShipFile)
	else:
		pModule = __import__('ships.' + sShipFile)
	pModule.__dict__.update(dict)


def ReplaceShipTextures(pPlayer, sShipName, sPath, sTexturePath = None):
	import nt
	import string
	
	if not sTexturePath:
		sTexturePath = sPath + '/High'

	# pShipProperty = pPlayer.GetShipProperty()
	# if pShipProperty:
	# 	sShipName = pShipProperty.GetShipName()

	sName = string.lower(sShipName)
	sName = string.replace(sName, ' ', '_')
	lFiles = nt.listdir(sTexturePath)

	if sPath[-1] != '/':
		sPath = sPath + '/'

	print 'Replacing textures for', sName, sPath

	for sTexture in lFiles:
		if string.find(sTexture, sName) >= 0:
			sID = string.split(sTexture, '_')[0]
			pPlayer.ReplaceTexture(sPath + sTexture, sID)
			print sTexture, sName, ':', '(%s) %s' % (sPath + sTexture, sID)
