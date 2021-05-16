
import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.99, 0.001, 0.001, 0.2500000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.1, 0.03) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("NX01Pulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("nx01pulse")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 8.0
