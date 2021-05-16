###############################################################################
#	Filename:	PhotonTorpedo.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	Script for filling in the attributes of photon torpedoes.
#
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#
#	Creates a photon torpedo.
#
#	Args:	pTorp - the torpedo, ready to be filled-in
#
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,			# Size
					1.2,			# Rotation of flares
					"Custom/FTB/Textures/Tactical/FTBpoltorp02.tga",
					kGlowColor,
					1.2,			# Pulse rate
					0.9,			# Minimum size
					1.2,			# Maximum size
					"Custom/FTB/Textures/Tactical/FTBTorpedoFlares.tga",
					kGlowColor,
					12,				# Number of flares
					0.7,			# Length
					0.3)			# Creation interval

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.16)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("FTB Photon Torp")

def GetPowerCost():
	return(400.0)

def GetName():
	return("Spread Mk5 Burst")

def GetDamage():
	return 1875.0

def GetGuidanceLifetime():
	return 4.5

def GetMaxAngularAccel():
	return 0.18

def GetLifetime():
	return 20.0



#########################################################################################################################
#	Torpedo Decoding Version 5											#
#															#
#	SpreadType:													#
#		0 - Normal Behaviour											#
#		1 - Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target.	#
#		    The type of splitting is defined by SplitType							#
#		2 - Will scatter into a number of subtorpedoes specified in SpreadNumber, directed at different targets	#
#		3 - Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is set	#
#		    Friendly ships are aswell affected. No damage is applied, yet a yield is simulated and executed	#
#		    e.g. an ion effect											#
#															#
#		ShellLive:	0 - The shell torpedo is removed after spreading					#
#				1 - The shell torpedo continues moving							#
#		SpreadNumber: x - Number of subtorpedoes created							#
#		SpreadPath: Defines the tactical/projectiles path of the subtorpedoes					#
#		eg "Tactical.Projectiles.subMyTorpedo"									#
#		SpreadDelay	x - Time(sec) before the torpedoes starts spreading 					#
#															#
#		SplitType: 	0 - Nothing										#
#				1 - Conical Spread, with SpreadDensity determining the inverse conical aperture		#
#				2 - Circular Spread, with SpreadAngle(°) determining the angle of the circlesector	#
#															#
#		SpreadRadious: x - x range of the wavetorpedo								#
#		SpreadSplash: 0 - Allied ships not affected								#
#			      1 - Allied ships affected									#
#		ShellPersist:	0 - The Shell Torpedo is removed after splitting					#
#				1 - The Shell Torpedo remains and continues						#
#															#
#	ImpactType:													#
#		0 - Normal Behaviour											#
#		1 - Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
#		    that the torpedo isn't bounced									#
#		2 - Phased Torpedo - You need to create a shelltorpedo script with little damage (like 0.001) and	#
#		    ImpactType 2 set. Define a string SecondPath indicating the real torpedo script with the actual	#
#		    damage. That torpedo must NOT be set at ImpactType=2 or you might create on infinite loop(=crash). 	#
#		BounceYield:	x - torpedodamage is multiplied with this factor					#
#		BounceFail:	x - 1 on x chance that the weapon is absorbed						#
#															#
#															#
#	YieldType:													#
#		0 - Normal Behaviour											#
#		1 - Special Behaviour:											#
#			DrainerWeapon:		0 - Not active								#
#						1 - Targets shields and powercore fails					#
#			SensorBlast:		0 - Not active								#
#						1 - Sensors disabled for SensorDisabledTime seconds			#
#			ShieldDisruptor:	0 - Not active								#
#						1 - Target shields are disrupted for ShieldDisabledTime seconds		#
#			EngineJammer:		0 - Not active								#
#						1 - Target Engines are disabled for EngineDisabledTime seconds		#
#			IonCannon:		0 - Not active								#
#						1 - Random Subtarget disabled for IonCannonDisabledTime seconds		#
#						    with a 1 on IonCannonMiss to have no effect. The effect is executed #
#						    IonFrequency times.				 			#
#			CloakBurn:		0 - Not active								#
#						1 - Target CloakingSys is disabled for CloakDisabledTime seconds	#
#			PhalaniumWave:		0 - Not ACtive								#
#						1 - The Effect designed by DreamYards, now compatible with NanoFX	#
#			SpatialCharges:		0 - Not ACtive								#
#						1 - The Effect designed by Sneaker, now compatible with NanoFX		#
#															#
#	DepleteType:													#
#		0 - Normal Behaviour											#
#		1 - Torpedo will lose damage each second with a factor (100-DepletionPerSecond(in %))%, untill the	#
#		    damage is reduced to DepletedAtPercentage of the original damage.					#
#		GraphicsTuple: Set containing the grahical info about the torpedo					#
#		DepleteColour: 	0 - Not active										#
#			 	1 - The colour changes from green to red, while flying					#
#		DepleteShrink: 	0 - Not active										#
#			 	1 - The torpedo shrinks, while flying							#
#															#
#########################################################################################################################

#########################
#SpreadType		#
#########################

SpreadType=3

#Spread Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
SpreadPath = "ftb.Projectiles.FTBMk5PhotonTorpedo"

##for SpreadType 1 & 2
SpreadNumber 	= 4
ShellLive 	= 0
SpreadDelay	= 1.0

##for SpreadType 1
SplitType=1

##for SpreadType 1 with SplitType 1
SpreadDensity=2

##for SpreadType 1 with SplitType 2
SpreadAngle=75.0

##for SpreadType 3
SpreadRadious=20.0
SpreadSplash=1


#########################
#ImpactType		#
#########################

ImpactType=0

#Impact Options	#
#################
BounceYield=1.0
BounceFail=15
SecondPath=""


#########################
#YieldType		#
#########################

YieldType=0


#Yield Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
DrainerWeapon=1

SensorBlast=1.0
SensorDisabledTime=20.0

ShieldDisruptor=0
ShieldDisabledTime=0

EngineJammer=0
EngineDisabledTime=0

IonCannon=0
IonCannonDisabledTime=15
IonCannonMiss=4
IonFrequency=1

# Thirth Party Options #
########################

PhalantiumWave=0

SpatialCharges=0


#########################
#DepleteType		#
#########################

DepleteType = 0
GraphicsTuple="data/Textures/Tactical/TorpedoCore.tga",(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000),3.5,0.6,"data/Textures/Tactical/TorpedoGlow.tga",(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000),4.0,1.8,3.3,"data/Textures/Tactical/TorpedoFlares.tga",(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000),12,1.7,0.4


#Deplete Options - all parameters are optional and if not defined take default values	#
#########################################################################################
DepletedAtPercentage = 10
DepletionPerSecond = 15
DepleteColour=1
DepleteShrink=1

