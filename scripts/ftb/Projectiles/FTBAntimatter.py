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
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.5, 0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.04)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(10.0)

def GetLaunchSound():
	return("FTB Antimatter")

def GetPowerCost():
	return(300.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 800.0

def GetGuidanceLifetime():
	return 0.5

def GetMaxAngularAccel():
	return 0.02

def GetLifetime():
	return 4.0
