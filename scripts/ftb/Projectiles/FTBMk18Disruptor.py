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
	kOuterShellColor.SetRGBA(0.272549, 1.000000, 0.272549, 1.000000)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.839216, 1.000000, 0.939216, 1.000000)
	# pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.15)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.6, 0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.12)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("FTB Klingon Disruptor")

def GetPowerCost():
	return(45.0)

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
