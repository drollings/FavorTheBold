###############################################################################
#	Filename:	PulseDisruptor.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of disruptor blasts.
#
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#
#	Creates a disruptor blast.
#
#	Args:	pTorp - the "torpedo", ready to be filled-in
#
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.65, 0.81, 0.95, 0.900000)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.9, 0.96, 1.000000, 1.000000)
	# pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.15)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 3.0, 0.25)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

# 	pTorp.CreateTorpedoModel(
# 					"data/Textures/Tactical/TorpedoCore.tga",
# 					kCoreColor,
# 					10.3,			# Size
# 					11.2,			# Rotation of flares
# 					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
# 					kGlowColor,
# 					2.2,			# Pulse rate
# 					10.6,			# Minimum size
# 					10.9,			# Maximum size
# 					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
# 					kGlowColor,
# 					12,				# Number of flares
# 					0.3,			# Length
# 					0.3)			# Creation interval
#
#
# 	pTorp.SetDamage( 0.0 )
# 	pTorp.SetDamageRadiusFactor(0.0)
# 	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
# 	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
# 	pTorp.SetLifetime( GetLifetime() )

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("FTB Heavy Polaron")

def GetPowerCost():
	return(100.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 3000.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.025

def GetLifetime():
	return 6.0
