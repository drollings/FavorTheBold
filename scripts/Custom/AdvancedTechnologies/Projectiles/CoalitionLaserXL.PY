import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0, 1.0, 0.0, 1.0)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.0, 1.0, 0.001, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 60.0, 1.22) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(150.0)

def GetLaunchSound():
	return("CoalitionLaserXL")

def GetPowerCost():
	return(5.0)

def GetName():
	return("CoalitionLaserXL")

def GetDamage():
	return 20000.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 8.0



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

##for SpreadType 1 & 2
SpreadNumber=0
SpreadPath=""

##for SpreadType 1 
SplitType=0

##for SpreadType 1 with SplitType 1
SpreadDensity=0

##for SpreadType 1 with SplitType 2
SpreadAngle=0

##for SpreadType 3
SpreadRadious=0
SpreadSplash=0


#########################
#ImpactType		#
#########################

ImpactType=0

#Impact Options	#
#################
BounceYield=0
BounceFail=0


#########################
#YieldType		#
#########################

YieldType=0


#Yield Options	- all parameters are optional and if not defined take default values	#
#########################################################################################
DrainerWeapon=0

SensorBlast=0
SensorDisabledTime=0

ShieldDisruptor=0
ShieldDisabledTime=0

EngineJammer=1
EngineDisabledTime=50

IonCannon=0
IonCannonDisabledTime=0
IonCannonMiss=0

# Thirth Party Options #
########################

PhalantiumWave=0

SpatialCharges=0


#########################
#DepleteType		#
#########################

DepleteType = 0
GraphicsTuple=""

#Deplete Options - all parameters are optional and if not defined take default values	#
#########################################################################################
DepletedAtPercentage = 0
DepletionPerSecond = 0
DepleteColour=0
DepleteShrink=0