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
	kCoreColor.SetRGBA(1.0, 0.8, 0.7, 1.0)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.9, 0.7, 0.4, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.35,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					2.2,			# Pulse rate
					0.65,			# Minimum size
					0.95,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					12,				# Number of flares
					0.32,			# Length
					0.1)			# Creation interval


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("Antimatter Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Antimatter")

def GetDamage():
	return 880.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.7

def GetLifetime():
	return 15.0