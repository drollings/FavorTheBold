###############################################################################
#	Filename:	PhotonTorpedo2.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of photon torpedoes.
#
#	Created:	10/29/01 -	Evan Birkby
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
	kGlowColor.SetRGBA(34.0 / 255.0, 139.0 / 255.0, 34.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(152.0 / 255.0, 251.0 / 255.0, 152.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					1.2,
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					2.0,
					0.6,
					0.8,
					"Custom/FTB/Textures/Tactical/FTBTorpedoFlares.tga",
					kGlowColor,
					10,
					0.3,
					0.25)


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.

	import Multiplayer.SpeciesToTorp

	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON2)
	return(0)

def GetLaunchSpeed():
	return(38.0)

def GetLaunchSound():
	return("FTB Romulan Torp")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 5000.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
 	return 12.0


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
	'sModel':		'Custom/FTB/Ships/FTBFerengiShuttle/',
})
FoundationTech.dOnFires[__name__] = oFire

try:
	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	pass
