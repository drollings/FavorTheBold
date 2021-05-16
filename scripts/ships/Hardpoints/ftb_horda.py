# D:\Games\FTB\scripts\Custom\FTB\ships\hp\ftb_peregrine.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ImpulseEngine = App.EngineProperty_Create("Impulse Engine")
ImpulseEngine.SetMaxCondition(1084.0)
ImpulseEngine.SetCritical(0)
ImpulseEngine.SetTargetable(1)
ImpulseEngine.SetPrimary(1)
ImpulseEngine.SetPosition(0.000000, -0.420000, 0.120742)
ImpulseEngine.SetPosition2D(64.0, 46.1564730015)
ImpulseEngine.SetRepairComplexity(3.0)
ImpulseEngine.SetDisabledPercentage(0.5)
ImpulseEngine.SetRadius(0.100000)
ImpulseEngine.SetEngineType(ImpulseEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngine)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")
PortWarp.SetMaxCondition(964.0)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(0.000000, 0.000000, 0.000000)
PortWarp.SetPosition2D(64.0, 64.0)
PortWarp.SetRepairComplexity(3.0)
PortWarp.SetDisabledPercentage(0.5)
PortWarp.SetRadius(0.001000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")
StarWarp.SetMaxCondition(964.0)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.000000, 0.000000, 0.000000)
StarWarp.SetPosition2D(64.0, 64.0)
StarWarp.SetRepairComplexity(3.0)
StarWarp.SetDisabledPercentage(0.5)
StarWarp.SetRadius(0.001000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1109.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -0.218531, 0.050000)
ImpulseEngines.SetPosition2D(64.0, 59.9576458326)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.120000)
ImpulseEngines.SetNormalPowerPerSecond(3300.09658537)
ImpulseEngines.SetMaxAccel(12.675)
ImpulseEngines.SetMaxAngularAccel(0.4)
ImpulseEngines.SetMaxAngularVelocity(0.666666666667)
ImpulseEngines.SetMaxSpeed(13.2)
ImpulseEngines.SetEngineSound('Federation Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")
PortCannon.SetMaxCondition(1149.0)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-0.024417, 0.055692, 0.004839)
PortCannon.SetPosition2D(57.0701197339, 64.1259348383)
PortCannon.SetRepairComplexity(4.0)
PortCannon.SetDisabledPercentage(0.75)
PortCannon.SetRadius(0.150000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.12)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(73)
PortCannon.SetIconPositionY(38)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound('FTB Polaron Pulse')
PortCannon.SetMaxCharge(2.0)
PortCannon.SetMaxDamage(600.0)
PortCannon.SetMaxDamageDistance(80.0)
PortCannon.SetMinFiringCharge(1.0)
PortCannon.SetNormalDischargeRate(1.0)
PortCannon.SetRechargeRate(0.039)
PortCannon.SetIndicatorIconNum(512)
PortCannon.SetIndicatorIconPositionX(55)
PortCannon.SetIndicatorIconPositionY(35)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.436332, 0.436332)
PortCannon.SetArcHeightAngles(-0.436332, 0.436332)
PortCannon.SetCooldownTime(0.25)
PortCannon.SetModuleName('ftb.Projectiles.FTBPulsePolaron')
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")
StarCannon.SetMaxCondition(1149.0)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(1)
StarCannon.SetPosition(0.024417, 0.055692, 0.004839)
StarCannon.SetPosition2D(70.9298802661, 64.1259348383)
StarCannon.SetRepairComplexity(4.0)
StarCannon.SetDisabledPercentage(0.75)
StarCannon.SetRadius(0.150000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(2)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(0.12)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(82)
StarCannon.SetIconPositionY(38)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound('FTB Polaron Pulse')
StarCannon.SetMaxCharge(2.0)
StarCannon.SetMaxDamage(600.0)
StarCannon.SetMaxDamageDistance(80.0)
StarCannon.SetMinFiringCharge(1.0)
StarCannon.SetNormalDischargeRate(1.0)
StarCannon.SetRechargeRate(0.039)
StarCannon.SetIndicatorIconNum(513)
StarCannon.SetIndicatorIconPositionX(64)
StarCannon.SetIndicatorIconPositionY(35)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.436332, 0.436332)
StarCannon.SetArcHeightAngles(-0.436332, 0.436332)
StarCannon.SetCooldownTime(0.25)
StarCannon.SetModuleName('ftb.Projectiles.FTBPulsePolaron')
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(964.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(64.0, 64.0)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.001000)
ShieldGenerator.SetNormalPowerPerSecond(22.5)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.109804, 0.549020, 0.137255, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 225.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 112.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 112.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 112.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 112.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 112.5)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.215993678234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.215993678234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.215993678234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.215993678234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.215993678234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.215993678234)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(1472.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, 0.000000, 0.000000)
WarpCore.SetPosition2D(64.0, 64.0)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.001000)
WarpCore.SetMainBatteryLimit(600000.0)
WarpCore.SetBackupBatteryLimit(192000.0)
WarpCore.SetMainConduitCapacity(2880.0)
WarpCore.SetBackupConduitCapacity(960.0)
WarpCore.SetPowerOutput(2400.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(4125.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.020000, 0.000000)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.120000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000408, 0.048185, 0.014485)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, 0.007257, 0.015994)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(-0.007885, 0.046525, 0.013208)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.007885, 0.046525, 0.013208)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000297, 0.020838, 0.017276)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000297, 0.020838, 0.017276)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, 0.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
DisruptorCannons = App.WeaponSystemProperty_Create("Disruptor Cannons")
DisruptorCannons.SetMaxCondition(1046.0)
DisruptorCannons.SetCritical(0)
DisruptorCannons.SetTargetable(0)
DisruptorCannons.SetPrimary(1)
DisruptorCannons.SetPosition(0.000000, 0.450000, 0.060000)
DisruptorCannons.SetPosition2D(64.0, 77.003829873)
DisruptorCannons.SetRepairComplexity(3.0)
DisruptorCannons.SetDisabledPercentage(0.5)
DisruptorCannons.SetRadius(0.070000)
DisruptorCannons.SetNormalPowerPerSecond(287.0)
DisruptorCannons.SetWeaponSystemType(DisruptorCannons.WST_PULSE)
DisruptorCannons.SetSingleFire(1)
DisruptorCannons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorCannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
#################################################
Peregrine = App.ShipProperty_Create("Peregrine")
Peregrine.SetGenus(1)
Peregrine.SetSpecies(401)
Peregrine.SetMass(1.0)
Peregrine.SetRotationalInertia(8.0)
Peregrine.SetShipName("FTB_Peregrine")
Peregrine.SetModelFilename("Custom/FTB/Ships/FTBPeregrine/FTB_Peregrine.nif")
Peregrine.SetDamageResolution(10.000000)
Peregrine.SetAffiliation(0)
Peregrine.SetStationary(0)
Peregrine.SetAIString("NonFedAttack")
Peregrine.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Peregrine)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(964.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(64.0, 64.0)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(0.001000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(0.0)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(1476.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.040000, 0.009331)
SensorArray.SetPosition2D(64.0, 64.1912634718)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.005000)
SensorArray.SetNormalPowerPerSecond(880.0)
SensorArray.SetBaseSensorRange(600.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
WarpEngines.SetMaxCondition(1084.0)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.237953, -0.306927, 0.053082)
WarpEngines.SetPosition2D(131.534332594, 57.6919487727)
WarpEngines.SetRepairComplexity(3.0)
WarpEngines.SetDisabledPercentage(0.5)
WarpEngines.SetRadius(0.100000)
WarpEngines.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
# Property load function.
def LoadPropertySet(pObj):







	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Peregrine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
