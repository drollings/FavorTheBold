
import App

def Create(pTorp):

	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(210.0 / 255.0, 105.0 / 255.0, 30.0 / 255., 1.000000)	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(210.0 / 255.0, 105.0 / 255.0, 30.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 193.0 / 255.0, 37.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.09,
					1.1,	 
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga", 
					kGlowColor,
					1.0,
					0.35,
					0.55,
					"Custom/FTB/Textures/Tactical/FTBTorpedoFlares.tga",
					kFlareColor,										
					8,		
					0.15,		
					0.125)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTONIC)

	return(0)

def GetLaunchSpeed():
	return(28.0)

def GetLaunchSound():
	return("ENTNXTorp2")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photonic")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.15
