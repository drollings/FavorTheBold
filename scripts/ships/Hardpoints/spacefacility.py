# C:\Utopia\Current\Build\scripts\ships\Hardpoints\spacefacility.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShuttleBay1 = App.ObjectEmitterProperty_Create("Shuttle Bay 1")

ShuttleBay1Forward = App.TGPoint3()
ShuttleBay1Forward.SetXYZ(-1.000000, 0.000000, 0.000000)
ShuttleBay1Up = App.TGPoint3()
ShuttleBay1Up.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay1Right = App.TGPoint3()
ShuttleBay1Right.SetXYZ(0.000000, -1.000000, 0.000000)
ShuttleBay1.SetOrientation(ShuttleBay1Forward, ShuttleBay1Up, ShuttleBay1Right)
ShuttleBay1Position = App.TGPoint3()
ShuttleBay1Position.SetXYZ(-4.700000, -0.090000, 1.500000)
ShuttleBay1.SetPosition(ShuttleBay1Position)
ShuttleBay1.SetEmittedObjectType(ShuttleBay1.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1)
#################################################
ShuttleBay2 = App.ObjectEmitterProperty_Create("Shuttle Bay 2")

ShuttleBay2Forward = App.TGPoint3()
ShuttleBay2Forward.SetXYZ(1.000000, 0.000000, 0.000000)
ShuttleBay2Up = App.TGPoint3()
ShuttleBay2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay2Right = App.TGPoint3()
ShuttleBay2Right.SetXYZ(0.000000, 1.000000, 0.000000)
ShuttleBay2.SetOrientation(ShuttleBay2Forward, ShuttleBay2Up, ShuttleBay2Right)
ShuttleBay2Position = App.TGPoint3()
ShuttleBay2Position.SetXYZ(4.700000, -0.120000, 1.500000)
ShuttleBay2.SetPosition(ShuttleBay2Position)
ShuttleBay2.SetEmittedObjectType(ShuttleBay2.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay2)

# Property load function.
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(32934.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, -0.200000)
ShieldGenerator.SetPosition2D(64.0, 64.0771905186)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(2.000000)
ShieldGenerator.SetNormalPowerPerSecond(6666.66666667)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 33333.3333333)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 33333.3333333)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 33333.3333333)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 33333.3333333)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 33333.3333333)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 33333.3333333)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 68.1558441558)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 68.1558441558)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 68.1558441558)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 68.1558441558)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 68.1558441558)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 68.1558441558)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")
PowerPlant.SetMaxCondition(29562.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, -7.000000)
PowerPlant.SetPosition2D(64.0, 158.558385345)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(1.700000)
PowerPlant.SetMainBatteryLimit(2250000.0)
PowerPlant.SetBackupBatteryLimit(720000.0)
PowerPlant.SetMainConduitCapacity(10800.0)
PowerPlant.SetBackupConduitCapacity(3600.0)
PowerPlant.SetPowerOutput(9000.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(546324.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.500000)
Hull.SetPosition2D(64.0, 64.4824407416)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(11.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Spacefacility = App.ShipProperty_Create("Spacefacility")
Spacefacility.SetGenus(2)
Spacefacility.SetSpecies(707)
Spacefacility.SetMass(440.0)
Spacefacility.SetRotationalInertia(225001.0)
Spacefacility.SetShipName("Space Facility")
Spacefacility.SetModelFilename("data/Models/Bases/SpaceFacility/SpaceFacility.nif")
Spacefacility.SetDamageResolution(15.000000)
Spacefacility.SetAffiliation(0)
Spacefacility.SetStationary(0)
Spacefacility.SetAIString("StarbaseAttack")
Spacefacility.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Spacefacility)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(15224.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 4.000000)
Engineering.SetPosition2D(64.0, 94.8762074595)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(1.000000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(150.9125)
Engineering.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(52662.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, 5.700000)
SensorArray.SetPosition2D(64.0, 126.697998772)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(2.700000)
SensorArray.SetNormalPowerPerSecond(1200.0)
SensorArray.SetBaseSensorRange(3000.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
def LoadPropertySet(pObj):

	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Spacefacility", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
