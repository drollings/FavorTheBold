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
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(124.0 / 255.0, 178.0 / 255.0, 234.0 / 255.0, 0.700000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.06,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					2.2,			# Pulse rate
					0.10,			# Minimum size
					0.15,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					12,				# Number of flares
					0.06,			# Length
					0.3)			# Creation interval


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
	return(25.0)

def GetLaunchSound():
	return("FTB Polaron Torp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Micro Polaron")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.10

def GetLifetime():
	return 10.0
