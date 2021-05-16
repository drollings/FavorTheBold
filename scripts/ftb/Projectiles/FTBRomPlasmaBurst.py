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
	kGlowColor.SetRGBA(49.0 / 255.0, 190.0 / 255.0, 68.0 / 255.0, 0.300000)
	kPlumeColor = App.TGColorA()
	kPlumeColor.SetRGBA(49.0 / 255.0, 190.0 / 255.0, 68.0 / 255.0, 0.400000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(202.0 / 255.0, 250.0 / 255.0, 218.0 / 255.0, 0.200000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.15,			# Size
					2.8,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/GreenPlasmaTorpGlow.tga",
					kGlowColor,
					3.6,			# Pulse rate
					0.45,			# Minimum size
					0.6,			# Maximum size
					"data/Textures/Tactical/TractorBeam.tga",
					kPlumeColor,
					24,				# Number of flares
					0.225,			# Length
					0.15)			# Creation interval

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("FTB Plasma")

def GetPowerCost():
	return(1000.0)

def GetName():
	return("Plasma")

def GetDamage():
	return 4000.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 25.0
