# C:\Utopia\Current\Build\scripts\ships\Hardpoints\commlight.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Impulse = App.EngineProperty_Create("Impulse")
Impulse.SetMaxCondition(2356.0)
Impulse.SetCritical(0)
Impulse.SetTargetable(1)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, 0.000000, 0.150000)
Impulse.SetPosition2D(64.0, 64.9783687061)
Impulse.SetRepairComplexity(3.0)
Impulse.SetDisabledPercentage(0.5)
Impulse.SetRadius(0.500000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
# Property load function.
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1780.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(64.0, 64.0)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(1691.37073171)
ImpulseEngines.SetMaxAccel(0.67575)
ImpulseEngines.SetMaxAngularAccel(0.0001)
ImpulseEngines.SetMaxAngularVelocity(0.00025)
ImpulseEngines.SetMaxSpeed(3.0)
ImpulseEngines.SetEngineSound('Federation Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(3875.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.100000)
ShieldGenerator.SetPosition2D(64.0, 64.434830536)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(1.000000)
ShieldGenerator.SetNormalPowerPerSecond(30000.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 150000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 150000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 150000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 150000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 150000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 150000.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 153.350649351)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 153.350649351)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 153.350649351)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 153.350649351)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 153.350649351)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 153.350649351)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")
PowerPlant.SetMaxCondition(3056.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, -0.900000)
PowerPlant.SetPosition2D(64.0, 99.2212734184)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(0.500000)
PowerPlant.SetMainBatteryLimit(5875000.0)
PowerPlant.SetBackupBatteryLimit(1880000.0)
PowerPlant.SetMainConduitCapacity(28200.0)
PowerPlant.SetBackupConduitCapacity(9400.0)
PowerPlant.SetPowerOutput(23500.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(9284.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.150000)
Hull.SetPosition2D(64.0, 64.9783687061)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Transmitter = App.HullProperty_Create("Transmitter")
Transmitter.SetMaxCondition(2111.0)
Transmitter.SetCritical(0)
Transmitter.SetTargetable(0)
Transmitter.SetPrimary(0)
Transmitter.SetPosition(0.000000, 0.000000, 0.800000)
Transmitter.SetPosition2D(64.0, 91.8291543059)
Transmitter.SetRepairComplexity(3.0)
Transmitter.SetDisabledPercentage(0.5)
Transmitter.SetRadius(0.400000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Transmitter)
#################################################
Receiver1 = App.HullProperty_Create("Receiver 1")
Receiver1.SetMaxCondition(3875.0)
Receiver1.SetCritical(0)
Receiver1.SetTargetable(0)
Receiver1.SetPrimary(0)
Receiver1.SetPosition(1.200000, 0.010000, 0.150000)
Receiver1.SetPosition2D(191.893422148, 65.0715466781)
Receiver1.SetRepairComplexity(3.0)
Receiver1.SetDisabledPercentage(0.5)
Receiver1.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Receiver1)
#################################################
Receiver2 = App.HullProperty_Create("Receiver 2")
Receiver2.SetMaxCondition(3875.0)
Receiver2.SetCritical(0)
Receiver2.SetTargetable(0)
Receiver2.SetPrimary(0)
Receiver2.SetPosition(-1.200000, 0.010000, 0.150000)
Receiver2.SetPosition2D(-63.8934221482, 65.0715466781)
Receiver2.SetRepairComplexity(3.0)
Receiver2.SetDisabledPercentage(0.5)
Receiver2.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Receiver2)
#################################################
CommArray = App.ShipProperty_Create("Comm Array")
CommArray.SetGenus(2)
CommArray.SetSpecies(708)
CommArray.SetMass(440.0)
CommArray.SetRotationalInertia(225001.0)
CommArray.SetShipName("Comm Array")
CommArray.SetModelFilename("data/Models/Bases/SpaceFacility/SpaceFacility.nif")
CommArray.SetDamageResolution(15.000000)
CommArray.SetAffiliation(0)
CommArray.SetStationary(0)
CommArray.SetAIString("StarbaseAttack")
CommArray.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(CommArray)
#################################################
def LoadPropertySet(pObj):

	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Comm Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Transmitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Receiver 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Receiver 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
