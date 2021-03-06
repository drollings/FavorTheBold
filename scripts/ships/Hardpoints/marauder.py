# C:\Utopia\Current\Build\scripts\ships\Hardpoints\marauder.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")
StarWarp.SetMaxCondition(2059.0)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(1.350000, -0.750000, 0.120000)
StarWarp.SetPosition2D(171.932542161, 61.2062932248)
StarWarp.SetRepairComplexity(3.0)
StarWarp.SetDisabledPercentage(0.5)
StarWarp.SetRadius(0.600000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")
PortWarp.SetMaxCondition(2059.0)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-1.350000, -0.750000, 0.120000)
PortWarp.SetPosition2D(-43.9325421611, 61.2062932248)
PortWarp.SetRepairComplexity(3.0)
PortWarp.SetDisabledPercentage(0.5)
PortWarp.SetRadius(0.600000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")
StarImpulse.SetMaxCondition(1201.0)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.290000, -1.800000, 0.151000)
StarImpulse.SetPosition2D(87.1855090568, 55.0568069847)
StarImpulse.SetRepairComplexity(3.0)
StarImpulse.SetDisabledPercentage(0.5)
StarImpulse.SetRadius(0.120000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")
PortImpulse.SetMaxCondition(1201.0)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.290000, -1.800000, 0.151000)
PortImpulse.SetPosition2D(40.8144909432, 55.0568069847)
PortImpulse.SetRepairComplexity(3.0)
PortImpulse.SetDisabledPercentage(0.5)
PortImpulse.SetRadius(0.120000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1201.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.735000, -1.192000, 0.200000)
ImpulseEngines.SetPosition2D(122.763272954, 56.6451963775)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.120000)
ImpulseEngines.SetNormalPowerPerSecond(2986.78390244)
ImpulseEngines.SetMaxAccel(2.1)
ImpulseEngines.SetMaxAngularAccel(0.13585)
ImpulseEngines.SetMaxAngularVelocity(0.375725)
ImpulseEngines.SetMaxSpeed(12.325)
ImpulseEngines.SetEngineSound('Ferengi Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
VentralPhaser = App.PhaserProperty_Create("Ventral Phaser")
VentralPhaser.SetMaxCondition(1398.0)
VentralPhaser.SetCritical(0)
VentralPhaser.SetTargetable(1)
VentralPhaser.SetPrimary(1)
VentralPhaser.SetPosition(0.000000, 0.280000, -0.040000)
VentralPhaser.SetPosition2D(64.0, 63.6476405869)
VentralPhaser.SetRepairComplexity(2.4)
VentralPhaser.SetDisabledPercentage(0.75)
VentralPhaser.SetRadius(0.250000)
VentralPhaser.SetDumbfire(0)
VentralPhaser.SetWeaponID(1)
VentralPhaser.SetGroups(0)
VentralPhaser.SetDamageRadiusFactor(0.1)
VentralPhaser.SetIconNum(363)
VentralPhaser.SetIconPositionX(65)
VentralPhaser.SetIconPositionY(94)
VentralPhaser.SetIconAboveShip(0)
VentralPhaser.SetFireSound('Galor Phaser')
VentralPhaser.SetMaxCharge(4.5)
VentralPhaser.SetMaxDamage(900.0)
VentralPhaser.SetMaxDamageDistance(40.0)
VentralPhaser.SetMinFiringCharge(3.0)
VentralPhaser.SetNormalDischargeRate(1.0)
VentralPhaser.SetRechargeRate(0.247)
VentralPhaser.SetIndicatorIconNum(511)
VentralPhaser.SetIndicatorIconPositionX(56)
VentralPhaser.SetIndicatorIconPositionY(84)
VentralPhaserForward = App.TGPoint3()
VentralPhaserForward.SetXYZ(0.000000, -1.000000, 0.000000)
VentralPhaserUp = App.TGPoint3()
VentralPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
VentralPhaser.SetOrientation(VentralPhaserForward, VentralPhaserUp)
VentralPhaser.SetWidth(0.020000)
VentralPhaser.SetLength(0.020000)
VentralPhaser.SetArcWidthAngles(-1.221731, 1.221731)
VentralPhaser.SetArcHeightAngles(-2.792527, 0.017453)
VentralPhaser.SetPhaserTextureStart(1)
VentralPhaser.SetPhaserTextureEnd(15)
VentralPhaser.SetPhaserWidth(0.5)
VentralPhaser.SetNumSides(6)
VentralPhaser.SetMainRadius(0.06)
VentralPhaser.SetTaperRadius(0.03)
VentralPhaser.SetCoreScale(0.3)
VentralPhaser.SetTaperRatio(0.25)
VentralPhaser.SetTaperMinLength(5.0)
VentralPhaser.SetTaperMaxLength(30.0)
VentralPhaser.SetLengthTextureTilePerUnit(0.1)
VentralPhaser.SetPerimeterTile(1.0)
VentralPhaser.SetTextureSpeed(2.5)
VentralPhaser.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
VentralPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
VentralPhaser.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPhaser)
#################################################
PortEmitter = App.PulseWeaponProperty_Create("Port Emitter")
PortEmitter.SetMaxCondition(1398.0)
PortEmitter.SetCritical(0)
PortEmitter.SetTargetable(1)
PortEmitter.SetPrimary(1)
PortEmitter.SetPosition(-1.300000, 0.300000, 0.060000)
PortEmitter.SetPosition2D(-39.9350405996, 64.7173030909)
PortEmitter.SetRepairComplexity(4.0)
PortEmitter.SetDisabledPercentage(0.75)
PortEmitter.SetRadius(0.250000)
PortEmitter.SetDumbfire(1)
PortEmitter.SetWeaponID(1)
PortEmitter.SetGroups(1)
PortEmitter.SetDamageRadiusFactor(0.08)
PortEmitter.SetIconNum(365)
PortEmitter.SetIconPositionX(22)
PortEmitter.SetIconPositionY(56)
PortEmitter.SetIconAboveShip(1)
PortEmitter.SetFireSound('Klingon Disruptor')
PortEmitter.SetMaxCharge(3.0)
PortEmitter.SetMaxDamage(600.0)
PortEmitter.SetMaxDamageDistance(80.0)
PortEmitter.SetMinFiringCharge(2.0)
PortEmitter.SetNormalDischargeRate(1.0)
PortEmitter.SetRechargeRate(0.149)
PortEmitter.SetIndicatorIconNum(512)
PortEmitter.SetIndicatorIconPositionX(4)
PortEmitter.SetIndicatorIconPositionY(53)
PortEmitterForward = App.TGPoint3()
PortEmitterForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortEmitterUp = App.TGPoint3()
PortEmitterUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortEmitter.SetOrientation(PortEmitterForward, PortEmitterUp)
PortEmitter.SetArcWidthAngles(-0.349066, 0.349066)
PortEmitter.SetArcHeightAngles(-0.349066, 0.349066)
PortEmitter.SetCooldownTime(0.4)
PortEmitter.SetModuleName('ftb.Projectiles.FTBFusionBolt')
App.g_kModelPropertyManager.RegisterLocalTemplate(PortEmitter)
#################################################
StarEmitter = App.PulseWeaponProperty_Create("Star Emitter")
StarEmitter.SetMaxCondition(1398.0)
StarEmitter.SetCritical(0)
StarEmitter.SetTargetable(1)
StarEmitter.SetPrimary(1)
StarEmitter.SetPosition(1.300000, 0.300000, 0.060000)
StarEmitter.SetPosition2D(167.9350406, 64.7173030909)
StarEmitter.SetRepairComplexity(4.0)
StarEmitter.SetDisabledPercentage(0.75)
StarEmitter.SetRadius(0.250000)
StarEmitter.SetDumbfire(1)
StarEmitter.SetWeaponID(2)
StarEmitter.SetGroups(1)
StarEmitter.SetDamageRadiusFactor(0.08)
StarEmitter.SetIconNum(365)
StarEmitter.SetIconPositionX(133)
StarEmitter.SetIconPositionY(56)
StarEmitter.SetIconAboveShip(1)
StarEmitter.SetFireSound('Klingon Disruptor')
StarEmitter.SetMaxCharge(3.0)
StarEmitter.SetMaxDamage(600.0)
StarEmitter.SetMaxDamageDistance(80.0)
StarEmitter.SetMinFiringCharge(2.0)
StarEmitter.SetNormalDischargeRate(1.0)
StarEmitter.SetRechargeRate(0.149)
StarEmitter.SetIndicatorIconNum(513)
StarEmitter.SetIndicatorIconPositionX(115)
StarEmitter.SetIndicatorIconPositionY(53)
StarEmitterForward = App.TGPoint3()
StarEmitterForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarEmitterUp = App.TGPoint3()
StarEmitterUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarEmitter.SetOrientation(StarEmitterForward, StarEmitterUp)
StarEmitter.SetArcWidthAngles(-0.349066, 0.349066)
StarEmitter.SetArcHeightAngles(-0.349066, 0.349066)
StarEmitter.SetCooldownTime(0.4)
StarEmitter.SetModuleName('ftb.Projectiles.FTBFusionBolt')
App.g_kModelPropertyManager.RegisterLocalTemplate(StarEmitter)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1320.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.300000, 0.100000)
ShieldGenerator.SetPosition2D(64.0, 63.1960053074)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.200000)
ShieldGenerator.SetNormalPowerPerSecond(1250.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.949020, 0.831373, 0.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 10937.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 10937.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 9375.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 9375.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 4687.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 4687.5)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 6.89075630252)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 6.89075630252)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 6.89075630252)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 6.89075630252)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 6.89075630252)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 6.89075630252)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(1948.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -1.276000, 0.300000)
WarpCore.SetPosition2D(64.0, 52.8209781441)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.250000)
WarpCore.SetMainBatteryLimit(1100000.0)
WarpCore.SetBackupBatteryLimit(220000.0)
WarpCore.SetMainConduitCapacity(5280.0)
WarpCore.SetBackupConduitCapacity(1760.0)
WarpCore.SetPowerOutput(4400.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(6144.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.502000, 0.270000)
Hull.SetPosition2D(64.0, 61.0458438492)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(1.000000)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 1.600000, 0.200000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -1.900000, 0.200000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 1.600000, 0.200000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 1.600000, 0.200000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 1.600000, 0.200000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 1.600000, 0.000000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 1.600000, 0.200000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)

# Property load function.
Phasers = App.WeaponSystemProperty_Create("Phasers")
Phasers.SetMaxCondition(1201.0)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(-1.336000, -0.392000, 0.100000)
Phasers.SetPosition2D(-42.8132417239, 62.8744074304)
Phasers.SetRepairComplexity(3.0)
Phasers.SetDisabledPercentage(0.5)
Phasers.SetRadius(0.120000)
Phasers.SetNormalPowerPerSecond(767.0)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")
Tractors.SetMaxCondition(1320.0)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.960000, 0.200000)
Tractors.SetPosition2D(64.0, 71.6903840159)
Tractors.SetRepairComplexity(3.0)
Tractors.SetDisabledPercentage(0.5)
Tractors.SetRadius(0.200000)
Tractors.SetNormalPowerPerSecond(613.6)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
PlasmaEmitters = App.WeaponSystemProperty_Create("Plasma Emitters")
PlasmaEmitters.SetMaxCondition(1398.0)
PlasmaEmitters.SetCritical(0)
PlasmaEmitters.SetTargetable(0)
PlasmaEmitters.SetPrimary(1)
PlasmaEmitters.SetPosition(0.000000, 0.000000, 0.000000)
PlasmaEmitters.SetPosition2D(64.0, 64.0)
PlasmaEmitters.SetRepairComplexity(3.0)
PlasmaEmitters.SetDisabledPercentage(0.5)
PlasmaEmitters.SetRadius(0.250000)
PlasmaEmitters.SetNormalPowerPerSecond(767.0)
PlasmaEmitters.SetWeaponSystemType(PlasmaEmitters.WST_PULSE)
PlasmaEmitters.SetSingleFire(1)
PlasmaEmitters.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PlasmaEmitters.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PlasmaEmitters)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")
ForwardTractor.SetMaxCondition(1320.0)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.000000, 1.600000, 0.080000)
ForwardTractor.SetPosition2D(64.0, 68.6310094292)
ForwardTractor.SetRepairComplexity(3.0)
ForwardTractor.SetDisabledPercentage(0.75)
ForwardTractor.SetRadius(0.200000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(0)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(80)
ForwardTractor.SetIconPositionY(20)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Tractor Beam")
ForwardTractor.SetMaxCharge(50.000000)
ForwardTractor.SetMaxDamage(20.0)
ForwardTractor.SetMaxDamageDistance(100.0)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(80)
ForwardTractor.SetIndicatorIconPositionY(20)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.698132, 0.698132)
ForwardTractor.SetArcHeightAngles(-0.872665, 0.872665)
ForwardTractor.SetTractorBeamWidth(0.300000)
ForwardTractor.SetTextureStart(0)
ForwardTractor.SetTextureEnd(0)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerCoreColor(kColor)
ForwardTractor.SetNumSides(12)
ForwardTractor.SetMainRadius(0.075000)
ForwardTractor.SetTaperRadius(0.000000)
ForwardTractor.SetCoreScale(0.450000)
ForwardTractor.SetTaperRatio(0.200000)
ForwardTractor.SetTaperMinLength(1.000000)
ForwardTractor.SetTaperMaxLength(5.000000)
ForwardTractor.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor.SetPerimeterTile(1.000000)
ForwardTractor.SetTextureSpeed(0.200000)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor)
#################################################
AftTractor = App.TractorBeamProperty_Create("Aft Tractor")
AftTractor.SetMaxCondition(1320.0)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(0.000000, -1.550000, 0.420000)
AftTractor.SetPosition2D(64.0, 45.5598573815)
AftTractor.SetRepairComplexity(3.0)
AftTractor.SetDisabledPercentage(0.75)
AftTractor.SetRadius(0.200000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(0)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.300000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(80)
AftTractor.SetIconPositionY(107)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Tractor Beam")
AftTractor.SetMaxCharge(50.000000)
AftTractor.SetMaxDamage(20.0)
AftTractor.SetMaxDamageDistance(100.0)
AftTractor.SetMinFiringCharge(3.000000)
AftTractor.SetNormalDischargeRate(1.000000)
AftTractor.SetRechargeRate(0.300000)
AftTractor.SetIndicatorIconNum(0)
AftTractor.SetIndicatorIconPositionX(80)
AftTractor.SetIndicatorIconPositionY(107)
AftTractorForward = App.TGPoint3()
AftTractorForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractorUp = App.TGPoint3()
AftTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor.SetOrientation(AftTractorForward, AftTractorUp)
AftTractor.SetArcWidthAngles(-0.698132, 0.698132)
AftTractor.SetArcHeightAngles(-0.523599, 0.523599)
AftTractor.SetTractorBeamWidth(0.300000)
AftTractor.SetTextureStart(0)
AftTractor.SetTextureEnd(0)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetInnerCoreColor(kColor)
AftTractor.SetNumSides(12)
AftTractor.SetMainRadius(0.075000)
AftTractor.SetTaperRadius(0.000000)
AftTractor.SetCoreScale(0.450000)
AftTractor.SetTaperRatio(0.200000)
AftTractor.SetTaperMinLength(1.000000)
AftTractor.SetTaperMaxLength(5.000000)
AftTractor.SetLengthTextureTilePerUnit(0.250000)
AftTractor.SetPerimeterTile(1.000000)
AftTractor.SetTextureSpeed(0.200000)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTractor)
#################################################
Marauder = App.ShipProperty_Create("Marauder")
Marauder.SetGenus(1)
Marauder.SetSpecies(601)
Marauder.SetMass(371.0)
Marauder.SetRotationalInertia(190001.0)
Marauder.SetShipName("Marauder")
Marauder.SetModelFilename("data/Models/Ships/Marauder.nif")
Marauder.SetDamageResolution(12.000000)
Marauder.SetAffiliation(0)
Marauder.SetStationary(0)
Marauder.SetAIString("NonFedAttack")
Marauder.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Marauder)
#################################################
RepairSubsystem = App.RepairSubsystemProperty_Create("Repair Subsystem")
RepairSubsystem.SetMaxCondition(1173.0)
RepairSubsystem.SetCritical(0)
RepairSubsystem.SetTargetable(1)
RepairSubsystem.SetPrimary(1)
RepairSubsystem.SetPosition(-0.434000, -1.165000, 0.130000)
RepairSubsystem.SetPosition2D(29.301686446, 59.1194026532)
RepairSubsystem.SetRepairComplexity(2.0)
RepairSubsystem.SetDisabledPercentage(0.5)
RepairSubsystem.SetRadius(0.100000)
RepairSubsystem.SetNormalPowerPerSecond(1.0)
RepairSubsystem.SetMaxRepairPoints(20.39)
RepairSubsystem.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSubsystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(1870.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 1.150000, 0.200000)
SensorArray.SetPosition2D(64.0, 73.0187230732)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.200000)
SensorArray.SetNormalPowerPerSecond(1160.0)
SensorArray.SetBaseSensorRange(2700.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
WarpEngines.SetMaxCondition(1201.0)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(-0.735000, -1.192000, 0.200000)
WarpEngines.SetPosition2D(5.2367270456, 56.6451963775)
WarpEngines.SetRepairComplexity(3.0)
WarpEngines.SetDisabledPercentage(0.5)
WarpEngines.SetRadius(0.120000)
WarpEngines.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
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
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Subsystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Marauder", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Plasma Emitters", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Emitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Emitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
