###############################################################################
#	Filename:	QuantumTorpedo.py
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
	kGlowColor.SetRGBA(104.0 / 255.0, 158.0 / 255.0, 234.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.2,
					0.9,
					"Custom/FTB/Textures/Tactical/QuantumTorpCore.tga",
					kGlowColor,
					4.0,
					1.0,
					1.2,
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,
					12,
					0.5,
					0.38)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(22.0)

def GetLaunchSound():
	return("FTB Quantum Torp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 2500.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.12

def GetLifetime():
	return 20.0
