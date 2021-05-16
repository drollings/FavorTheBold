###############################################################################
#	Filename:	PolaronTorpedo.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of quantum torpedoes.
#
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#
#	Creates a quantum torpedo.
#
#	Args:	pTorp - the torpedo, ready to be filled-in
#
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(160.0 / 255.0, 192.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(16.0 / 255.0, 32.0 / 255.0, 64.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					1.0,			# Pulse rate
					1.0,			# Minimum size
					2.0,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					40,				# Number of flares
					50.0,			# Length
					0.2)			# Creation interval


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
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
	return("FTB Cloak Disruptor")

def GetPowerCost():
	return(300.0)

def GetName():
	return("Cloak Disruptor")

def GetDamage():
	return 20.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.10

def GetLifetime():
	return 10.0

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
import ftb.Tech.CloakDisruptor

oFire = ftb.Tech.CloakDisruptor.CloakDisruptor('Cloak Disruptor', {})
FoundationTech.dOnFires[__name__] = oFire
