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
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					3.5,
					0.6,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					1.8,	 
					3.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					12,		
					1.7,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.30)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("Plasma")

def GetPowerCost():
	return(10.0)

def GetName():
	return("DEPL Torpedo")

def GetDamage():
	return 1400.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.4


#########################################################################################################################
#	Torpedo Decoding Version 3											#
#															#
#	SpreadType:													#
#		0 - Normal Behaviour											#
#		1 - Will scatter into a number of subtorpedoes specified in SpreadNumber, all directed to one target.	#
#		    The type of splitting is defined by SplitType							#
#		2 - Will scatter into a number of subtorpedoes specified in SpreadNumber, directed at different targets	#
#		3 - Will scatter into wave explosion affecting all enemy ships in SpreadRadious, if SpreadSplash is set	#
#		    Friendly ships are aswell affected.									#
#															#
#		SpreadNumber: x - Number of subtorpedoes created							#
#		SpreadPath: Defines the tactical/projectiles path of the subtorpedoes					#
#		eg "Tactical.Projectiles.subMyTorpedo"									#
#															#
#		SplitType: 	0 - Nothing										#
#				1 - Conical Spread, with SpreadDensity determining the inverse conical aperture		#							#
#				2 - Circular Spread, with SpreadAngle determining the angle of the circlesector		#							#
#															#
#		SpreadRadious: x - x range of the wavetorpedo								#
#		SpreadSplash: 0 - Allied ships not affected								#
#			      1 - Allied ships affected									#
#															#
#	ImpactType:													#
#		0 - Normal Behaviour											#
#		1 - Will bounce off to the nearest enemy, with damage multiplied with BounceYield. One on BounceFail 	#
#		    that the torpedo isn't bounced									#
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
#						    with a 1 on IonCannonMiss to have no effect				#
#			CloakBurn:		0 - Not active								#
#						1 - Target CloakingSys is disabled for CloakDisabledTime seconds	#
#			PhalaniumWave:		0 - Not ACtive								#
#						1 - The Effect designed by DreamYards, now compatible with NanoFX	#
#			SpatialCharges:		0 - Not ACtive								#
#						1 - The Effect designed by Sneaker, now compatible with NanoFX		#															#
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

SpreadType=0

#Spread Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
SpreadPath = ""

##for SpreadType 1 & 2
SpreadNumber=5

##for SpreadType 1 
SplitType=2

##for SpreadType 1 with SplitType 1
SpreadDensity=2

##for SpreadType 1 with SplitType 2
SpreadAngle=75.0

##for SpreadType 3
SpreadRadious=0
SpreadSplash=0


#########################
#ImpactType		#
#########################

ImpactType=0

#Impact Options	#
#################
BounceYield=1.5
BounceFail=10

SecondPath="Custom.AdvancedTechnologies.Projectiles.PhasedReal"


#########################
#YieldType		#
#########################

YieldType=0


#Yield Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
DrainerWeapon=0

SensorBlast=1
SensorDisabledTime=25

ShieldDisruptor=1
ShieldDisabledTime=15

EngineJammer=1
EngineDisabledTime=20

IonCannon=0
IonCannonDisabledTime=0
IonCannonMiss=0
IonFrequency=1

# Thirth Party Options #
########################

PhalantiumWave=0

SpatialCharges=0


#########################
#DepleteType		#
#########################

DepleteType = 1
GraphicsTuple="data/Textures/Tactical/TorpedoCore.tga",(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000),3.5,0.6,"data/Textures/Tactical/TorpedoGlow.tga",(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000),4.0,1.8,3.3,"data/Textures/Tactical/TorpedoFlares.tga",(48.0 / 255.0, 190.0 / 255.0, 29.0 / 255.0, 1.000000),12,1.7,0.4


#Deplete Options - all parameters are optional and if not defined take default values	#
#########################################################################################
DepletedAtPercentage = 10
DepletionPerSecond = 15
DepleteColour=1
DepleteShrink=1