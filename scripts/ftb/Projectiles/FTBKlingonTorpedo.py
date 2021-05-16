###############################################################################
#	Filename:	KlingonTorpedo.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of klingon torpedoes.
#
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#
#	Creates a klingon torpedo.
#
#	Args:	pTorp - the torpedo, ready to be filled-in
#
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(190.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 218.0 / 255.0, 202.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					1.2,			# Pulse rate
					0.8,			# Minimum size
					1.0,			# Maximum size
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
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("FTB Klingon Torp")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 1200.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 15.0
