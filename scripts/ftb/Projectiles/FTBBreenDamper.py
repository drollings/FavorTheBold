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

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(50.0 / 255.0, 72.0 / 255.0, 253.0 / 255.0, 1.000000)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(64.0 / 255.0, 128.0 / 255.0, 234.0 / 255.0, 1.000000)

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
	return(30.0)

def GetLaunchSound():
	return("FTB Breen Damper")

def GetPowerCost():
	return(100.0)

def GetName():
	return("Damper Weapon")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 20.0


##################################################################################
# Foundation Technologies, copyright 2004 by Daniel Rollings AKA Dasher42
#
# This string is used to set a yield type using Foundation Technology plugins.
# If you wish extra functionality, subclassing an existing plugin here is acceptable,
# but the easiest way to set a special yield is to set this string to the name of an
# existing technology.
sYieldName = 'Damper Weapon'
sFireName = None


##################################################
# Do not edit below.
import FoundationTech

try:
	import FoundationTech

	try:
		oFire = FoundationTech.oTechs[sFireName]
		FoundationTech.dOnFires[__name__] = oFire
	except:
		pass

	try:
		oYield = FoundationTech.oTechs[sYieldName]
		FoundationTech.dYields[__name__] = oYield
	except:
		pass

except:
	pass
