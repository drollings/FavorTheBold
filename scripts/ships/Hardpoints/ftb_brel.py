# F:\Activision\Favour The Bold\scripts\Custom\FTB\ships\hp\ftb_brel.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ProbeLauncher = App.ObjectEmitterProperty_Create("Probe Launcher")

ProbeLauncherForward = App.TGPoint3()
ProbeLauncherForward.SetXYZ(0.000000, 1.000000, 0.000000)
ProbeLauncherUp = App.TGPoint3()
ProbeLauncherUp.SetXYZ(0.000000, 0.000000, 1.000000)
ProbeLauncherRight = App.TGPoint3()
ProbeLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
ProbeLauncher.SetOrientation(ProbeLauncherForward, ProbeLauncherUp, ProbeLauncherRight)
ProbeLauncherPosition = App.TGPoint3()
ProbeLauncherPosition.SetXYZ(0.000000, -0.029764, -0.182428)
ProbeLauncher.SetPosition(ProbeLauncherPosition)
ProbeLauncher.SetEmittedObjectType(ProbeLauncher.OEP_PROBE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ProbeLauncher)
#################################################
ImpulseEngine = App.EngineProperty_Create("Impulse Engine")
ImpulseEngine.SetMaxCondition(1600.0)
ImpulseEngine.SetCritical(0)
ImpulseEngine.SetTargetable(1)
ImpulseEngine.SetPrimary(1)
ImpulseEngine.SetPosition(0.000000, -0.450000, 0.153299)
ImpulseEngine.SetPosition2D(64.0, 53.6774493928)
ImpulseEngine.SetRepairComplexity(3.0)
ImpulseEngine.SetDisabledPercentage(0.5)
ImpulseEngine.SetRadius(0.100000)
ImpulseEngine.SetEngineType(ImpulseEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngine)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")
PortWarp.SetMaxCondition(1600.0)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.095615, -0.225000, 0.225867)
PortWarp.SetPosition2D(45.8759736759, 61.0312099452)
PortWarp.SetRepairComplexity(3.0)
PortWarp.SetDisabledPercentage(0.5)
PortWarp.SetRadius(0.100000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")
StarWarp.SetMaxCondition(1600.0)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.095615, -0.225000, 0.225867)
StarWarp.SetPosition2D(82.1240263241, 61.0312099452)
StarWarp.SetRepairComplexity(3.0)
StarWarp.SetDisabledPercentage(0.5)
StarWarp.SetRadius(0.100000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1638.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -0.218531, 0.050000)
ImpulseEngines.SetPosition2D(64.0, 62.1968792322)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.120000)
ImpulseEngines.SetNormalPowerPerSecond(3417.38780488)
ImpulseEngines.SetMaxAccel(14.175)
ImpulseEngines.SetMaxAngularAccel(0.41625)
ImpulseEngines.SetMaxAngularVelocity(0.69375)
ImpulseEngines.SetMaxSpeed(12.5578125)
ImpulseEngines.SetEngineSound('Klingon Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")
PortCannon.SetMaxCondition(1697.0)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-0.674276, 0.290836, -0.201266)
PortCannon.SetPosition2D(-63.8104478761, 58.0699045129)
PortCannon.SetRepairComplexity(3.2)
PortCannon.SetDisabledPercentage(0.75)
PortCannon.SetRadius(0.150000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(1)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.12)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(15)
PortCannon.SetIconPositionY(55)
PortCannon.SetIconAboveShip(0)
PortCannon.SetFireSound('FTB Klingon Pulse')
PortCannon.SetMaxCharge(5.0)
PortCannon.SetMaxDamage(200.0)
PortCannon.SetMaxDamageDistance(50.0)
PortCannon.SetMinFiringCharge(1.0)
PortCannon.SetNormalDischargeRate(1.0)
PortCannon.SetRechargeRate(0.167)
PortCannon.SetIndicatorIconNum(512)
PortCannon.SetIndicatorIconPositionX(-3)
PortCannon.SetIndicatorIconPositionY(62)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.436332, 0.436332)
PortCannon.SetArcHeightAngles(-0.436332, 0.436332)
PortCannon.SetCooldownTime(0.2)
PortCannon.SetModuleName('ftb.Projectiles.FTBMk6PulseDisruptor')
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")
StarCannon.SetMaxCondition(1697.0)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(1)
StarCannon.SetPosition(0.674276, 0.290836, -0.201266)
StarCannon.SetPosition2D(191.810447876, 58.0699045129)
StarCannon.SetRepairComplexity(3.2)
StarCannon.SetDisabledPercentage(0.75)
StarCannon.SetRadius(0.150000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(2)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(0.12)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(140)
StarCannon.SetIconPositionY(55)
StarCannon.SetIconAboveShip(0)
StarCannon.SetFireSound('FTB Klingon Pulse')
StarCannon.SetMaxCharge(5.0)
StarCannon.SetMaxDamage(200.0)
StarCannon.SetMaxDamageDistance(50.0)
StarCannon.SetMinFiringCharge(1.0)
StarCannon.SetNormalDischargeRate(1.0)
StarCannon.SetRechargeRate(0.167)
StarCannon.SetIndicatorIconNum(513)
StarCannon.SetIndicatorIconPositionX(122)
StarCannon.SetIndicatorIconPositionY(62)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.436332, 0.436332)
StarCannon.SetArcHeightAngles(-0.436332, 0.436332)
StarCannon.SetCooldownTime(0.2)
StarCannon.SetModuleName('ftb.Projectiles.FTBMk6PulseDisruptor')
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1508.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.315000, 0.250000)
ShieldGenerator.SetPosition2D(64.0, 57.1227719705)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.050000)
ShieldGenerator.SetNormalPowerPerSecond(550.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.109804, 0.549020, 0.137255, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 4125.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 2062.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 4125.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 4125.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 2750.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 2750.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 6.56159068865)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 3.93695441319)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 6.56159068865)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 6.56159068865)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 3.93695441319)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 3.93695441319)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(2350.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.300000, 0.140000)
WarpCore.SetPosition2D(64.0, 58.4431997521)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.100000)
WarpCore.SetMainBatteryLimit(616000.0)
WarpCore.SetBackupBatteryLimit(220000.0)
WarpCore.SetMainConduitCapacity(5280.0)
WarpCore.SetBackupConduitCapacity(1760.0)
WarpCore.SetPowerOutput(4400.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")
CloakingDevice.SetMaxCondition(1563.0)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(1)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(0.000000, 0.450000, 0.142241)
CloakingDevice.SetPosition2D(64.0, 79.3600336503)
CloakingDevice.SetRepairComplexity(3.0)
CloakingDevice.SetDisabledPercentage(0.5)
CloakingDevice.SetRadius(0.080000)
CloakingDevice.SetNormalPowerPerSecond(90.002899)
CloakingDevice.SetCloakStrength(90.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(6549.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.150000, 0.100000)
Hull.SetPosition2D(64.0, 62.4280621647)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.680000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Bridge = App.HullProperty_Create("Bridge")
Bridge.SetMaxCondition(2982.0)
Bridge.SetCritical(1)
Bridge.SetTargetable(1)
Bridge.SetPrimary(1)
Bridge.SetPosition(0.000000, 0.375000, 0.150000)
Bridge.SetPosition2D(64.0, 78.1474405179)
Bridge.SetRepairComplexity(4.0)
Bridge.SetDisabledPercentage(0.5)
Bridge.SetRadius(0.035000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Bridge)
# Property load function.
FwdTorpedo = App.TorpedoTubeProperty_Create("Fwd Torpedo")
FwdTorpedo.SetMaxCondition(1464.0)
FwdTorpedo.SetCritical(0)
FwdTorpedo.SetTargetable(1)
FwdTorpedo.SetPrimary(1)
FwdTorpedo.SetPosition(0.002000, 0.510000, 0.099235)
FwdTorpedo.SetPosition2D(64.3791042477, 75.2989240395)
FwdTorpedo.SetRepairComplexity(4.0)
FwdTorpedo.SetDisabledPercentage(0.75)
FwdTorpedo.SetRadius(0.025000)
FwdTorpedo.SetDumbfire(1)
FwdTorpedo.SetWeaponID(1)
FwdTorpedo.SetGroups(1)
FwdTorpedo.SetDamageRadiusFactor(0.17)
FwdTorpedo.SetIconNum(370)
FwdTorpedo.SetIconPositionX(77)
FwdTorpedo.SetIconPositionY(23)
FwdTorpedo.SetIconAboveShip(1)
FwdTorpedo.SetImmediateDelay(2.0)
FwdTorpedo.SetReloadDelay(20.0)
FwdTorpedo.SetMaxReady(3)
FwdTorpedoDirection = App.TGPoint3()
FwdTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo.SetDirection(FwdTorpedoDirection)
FwdTorpedoRight = App.TGPoint3()
FwdTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo.SetRight(FwdTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.516107, 0.127703)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.398420, 0.195167)
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
ViewscreenLeftPosition.SetXYZ(-0.041828, 0.394966, 0.131751)
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
ViewscreenRightPosition.SetXYZ(0.041828, 0.394966, 0.131751)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.398253, 0.153486)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.468679, 0.028335)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.920000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
DisruptorCannons = App.WeaponSystemProperty_Create("Disruptor Cannons")
DisruptorCannons.SetMaxCondition(1544.0)
DisruptorCannons.SetCritical(0)
DisruptorCannons.SetTargetable(0)
DisruptorCannons.SetPrimary(1)
DisruptorCannons.SetPosition(0.000000, 0.450000, 0.060000)
DisruptorCannons.SetPosition2D(64.0, 69.8004506123)
DisruptorCannons.SetRepairComplexity(3.0)
DisruptorCannons.SetDisabledPercentage(0.5)
DisruptorCannons.SetRadius(0.070000)
DisruptorCannons.SetNormalPowerPerSecond(767.0)
DisruptorCannons.SetWeaponSystemType(DisruptorCannons.WST_PULSE)
DisruptorCannons.SetSingleFire(0)
DisruptorCannons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorCannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
#################################################
Brel = App.ShipProperty_Create("Brel")
Brel.SetGenus(1)
Brel.SetSpecies(401)
Brel.SetMass(3.0)
Brel.SetRotationalInertia(1501.0)
Brel.SetShipName("FTB_Brel")
Brel.SetModelFilename("Custom/FTB/Ships/FTBBrel/FTB_Brel.nif")
Brel.SetDamageResolution(10.000000)
Brel.SetAffiliation(0)
Brel.SetStationary(0)
Brel.SetAIString("NonFedAttack")
Brel.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Brel)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(1553.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, -0.100000, 0.150000)
Engineering.SetPosition2D(64.0, 64.1473691721)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(0.075000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(0.21)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(2258.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000926, 0.335000, 0.080000)
SensorArray.SetPosition2D(64.1755252667, 70.1462769361)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.050000)
SensorArray.SetNormalPowerPerSecond(960.0)
SensorArray.SetBaseSensorRange(1200.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
WarpEngines.SetMaxCondition(1600.0)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.237953, -0.306927, 0.053082)
WarpEngines.SetPosition2D(109.104496532, 61.1862489773)
WarpEngines.SetRepairComplexity(3.0)
WarpEngines.SetDisabledPercentage(0.5)
WarpEngines.SetRadius(0.100000)
WarpEngines.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
Torpedoes.SetMaxCondition(1425.0)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.0, 64.0)
Torpedoes.SetRepairComplexity(3.0)
Torpedoes.SetDisabledPercentage(0.5)
Torpedoes.SetRadius(0.002)
Torpedoes.SetNormalPowerPerSecond(767.0)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 35)
Torpedoes.SetTorpedoScript(0, "ftb.Projectiles.FTBFastKlingonTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
def LoadPropertySet(pObj):


	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Brel", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bridge", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
