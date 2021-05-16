###############################################################################
#	Filename:	PhotonTorpedo.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of photon torpedoes.
#
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#
#	Creates a photon torpedo.
#
#	Args:	pTorp - the torpedo, ready to be filled-in
#
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					1.2,			# Pulse rate
					0.9,			# Minimum size
					1.2,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBTorpedoFlares.tga",
					kGlowColor,
					12,				# Number of flares
					0.7,			# Length
					0.3)			# Creation interval

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("FTB Photon Torp")

def GetPowerCost():
	return(200.0)

def GetName():
	return("Mk3 MultiTarget")

def GetDamage():
	return 900.0

def GetGuidanceLifetime():
	return 4.5

def GetMaxAngularAccel():
	return 0.18

def GetLifetime():
	return 15.0


##################################################################################
# Foundation Technologies, copyright 2004 by Daniel Rollings AKA Dasher42
#
# This string is used to set a yield type using Foundation Technology plugins.
# If you wish extra functionality, subclassing an existing plugin here is acceptable,
# but the easiest way to set a special yield is to set this string to the name of an
# existing technology.
sYieldName = None
sFireName = ''


##################################################
# Do not edit below.


import FoundationTech
import ftb.Tech.TimedTorpedoes

oFire = ftb.Tech.TimedTorpedoes.MIRVMultiTargetTorpedo('Mk3 Multi Target', {
	'spreadNumber':		3,
	'spreadDensity': 	7.0,
	'warheadModule': 	'ftb.Projectiles.FTBMk3PhotonTorpedo',
	'shellLive':		0,
})
FoundationTech.dOnFires[__name__] = oFire

try:
	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	pass

