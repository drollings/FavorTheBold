###############################################################################
#	Filename:	nxtorp.py
#	
#	Created by Darren Napper for Jimmy Obriens nx01 Enterprise
#	
#	This file was created to emulate the torpedoes fo the nx01 enterprise.
#	
#	Created:	05/07/02 -	Darren Napper
###############################################################################
import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(255.0 / 255.0, 210.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(100.0 / 255.0, 100.0 /255.0, 100.0 /255.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.2, 0.035) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ENTSPATIAL)

	return(0)

def GetLaunchSpeed():
	return(23.0)

def GetLaunchSound():
	return("ENTNXTorp")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Spatial")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.10

def GetLifetime():
	return 8.0