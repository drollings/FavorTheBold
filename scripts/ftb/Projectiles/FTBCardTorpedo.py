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
	kGlowColor.SetRGBA(210.0 / 255.0, 105.0 / 255.0, 30.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

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
	pTorp.SetDamageRadiusFactor(0.12)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON2)

	return(0)

def GetLaunchSpeed():
	return(32.0)

def GetLaunchSound():
	return("FTB Cardassian Torp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon Mk 5")

def GetDamage():
	return 1200.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.18
