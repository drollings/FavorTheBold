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
	kGlowColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 0.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 0.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					10.0,			# Pulse rate
					0.4,			# Minimum size
					0.75,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBTorpedoFlares.tga",
					kGlowColor,
					1,				# Number of flares
					0.01,			# Length
					1.0)			# Creation interval

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.08)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("FTB Spatial Torp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Spatial")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 4.5

def GetMaxAngularAccel():
	return 0.09

def GetLifetime():
	return 20.0



##################################################################################
# Foundation Technologies, copyright 2004 by Daniel Rollings AKA Dasher42
#
# This string is used to set a yield type using Foundation Technology plugins.
# If you wish extra functionality, subclassing an existing plugin here is acceptable,
# but the easiest way to set a special yield is to set this string to the name of an
# existing technology.
sYieldName = None
sFireName = ''

import FoundationTech
import ftb.Tech.SolidProjectiles

oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Torpedo', {
	'sEmit': 		'Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga',
	'sModel':		'FTB_FerengiShuttle',
})
FoundationTech.dOnFires[__name__] = oFire

try:
	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	pass
