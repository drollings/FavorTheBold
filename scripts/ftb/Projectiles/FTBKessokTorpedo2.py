###############################################################################
#	Filename:	PositronTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of positron torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a positron torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(240.0 / 255.0, 192.0 / 255.0, 49.0 / 255.0, 0.600000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 192.0 / 255.0, 152.0 / 255.0, 0.400000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(236.0 / 255.0, 192.0 / 255.0, 17.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.15,			# Size
					2.8,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/PlasmaTorpGlow.tga",
					kGlowColor,
					3.6,			# Pulse rate
					0.65,			# Minimum size
					0.76,			# Maximum size
					"data/Textures/Tactical/TractorBeam.tga",
					kFlareColor,
					12,				# Number of flares
					0.425,			# Length
					0.15)			# Creation interval

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(15.0)

def GetLaunchSound():
	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Positron")

def GetDamage():
	return 2200.0

def GetGuidanceLifetime():
	return 40.0

def GetMaxAngularAccel():
	return 1.5

def GetLifetime():
	return 15.0