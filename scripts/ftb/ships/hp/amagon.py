# C:\Utopia\Current\Build\scripts\ships\Hardpoints\amagon.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Asteroid = App.HullProperty_Create("Asteroid")
Asteroid.SetMaxCondition(181440.0)
Asteroid.SetCritical(1)
Asteroid.SetTargetable(1)
Asteroid.SetPrimary(1)
Asteroid.SetPosition(0.000000, 0.000000, 0.000000)
Asteroid.SetPosition2D(64.0, 64.0)
Asteroid.SetRepairComplexity(3.0)
Asteroid.SetDisabledPercentage(0.0)
Asteroid.SetRadius(5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Asteroid)
#################################################
AsteroidMass = App.ShipProperty_Create("Asteroid Mass")
AsteroidMass.SetGenus(3)
AsteroidMass.SetSpecies(712)
AsteroidMass.SetMass(299.0)
AsteroidMass.SetRotationalInertia(152751.0)
AsteroidMass.SetShipName("Asteroid")
AsteroidMass.SetModelFilename("data/Models/Misc/asteroid.nif")
AsteroidMass.SetDamageResolution(10.000000)
AsteroidMass.SetAffiliation(0)
AsteroidMass.SetStationary(0)
AsteroidMass.SetAIString("NonFedAttack")
AsteroidMass.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(AsteroidMass)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1526.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(64.0, 64.0)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.250000)
ShieldGenerator.SetNormalPowerPerSecond(1737.5)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")
PowerPlant.SetMaxCondition(2126.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.100000, 0.100000, 0.100000)
PowerPlant.SetPosition2D(190.732673267, 213.318694246)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(0.250000)
PowerPlant.SetMainBatteryLimit(875000.0)
PowerPlant.SetBackupBatteryLimit(280000.0)
PowerPlant.SetMainConduitCapacity(4200.0)
PowerPlant.SetBackupConduitCapacity(1400.0)
PowerPlant.SetPowerOutput(3500.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
# Property load function.
def LoadPropertySet(pObj):

	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Asteroid", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Asteroid Mass", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
