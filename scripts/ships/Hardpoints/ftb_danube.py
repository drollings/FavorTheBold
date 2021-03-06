# D:\Games\FTB\scripts\ships\Hardpoints\ftb_danube.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")
PortImpulse.SetMaxCondition(1053.0)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.097824, -0.199282, -0.049071)
PortImpulse.SetPosition2D(-58.4941254732, 162.306998555)
PortImpulse.SetRepairComplexity(3.0)
PortImpulse.SetDisabledPercentage(0.5)
PortImpulse.SetRadius(0.009000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")
StarImpulse.SetMaxCondition(1053.0)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.097824, -0.199282, -0.049071)
StarImpulse.SetPosition2D(186.494125473, 162.306998555)
StarImpulse.SetRepairComplexity(3.0)
StarImpulse.SetDisabledPercentage(0.5)
StarImpulse.SetRadius(0.009000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")
PortWarp.SetMaxCondition(1119.0)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.100000, -0.080000, -0.050000)
PortWarp.SetPosition2D(-61.2188884867, 113.305526864)
PortWarp.SetRepairComplexity(3.0)
PortWarp.SetDisabledPercentage(0.5)
PortWarp.SetRadius(0.060000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")
StarWarp.SetMaxCondition(1119.0)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.100000, -0.080000, -0.050000)
StarWarp.SetPosition2D(189.218888487, 113.305526864)
StarWarp.SetRepairComplexity(3.0)
StarWarp.SetDisabledPercentage(0.5)
StarWarp.SetRadius(0.060000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1046.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(64.0, 64.0)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.003000)
ImpulseEngines.SetNormalPowerPerSecond(2400.07445854)
ImpulseEngines.SetMaxAccel(8.175)
ImpulseEngines.SetMaxAngularAccel(0.25)
ImpulseEngines.SetMaxAngularVelocity(0.416666666667)
ImpulseEngines.SetMaxSpeed(11.3)
ImpulseEngines.SetEngineSound('Federation Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
StarPhaser = App.PhaserProperty_Create("Star Phaser")
StarPhaser.SetMaxCondition(1045.0)
StarPhaser.SetCritical(0)
StarPhaser.SetTargetable(1)
StarPhaser.SetPrimary(1)
StarPhaser.SetPosition(0.101221, -0.023981, -0.034545)
StarPhaser.SetPosition2D(190.747811115, 78.2666490577)
StarPhaser.SetRepairComplexity(4.0)
StarPhaser.SetDisabledPercentage(0.75)
StarPhaser.SetRadius(0.002000)
StarPhaser.SetDumbfire(0)
StarPhaser.SetWeaponID(1)
StarPhaser.SetGroups(1)
StarPhaser.SetDamageRadiusFactor(0.100000)
StarPhaser.SetIconNum(364)
StarPhaser.SetIconPositionX(114)
StarPhaser.SetIconPositionY(75)
StarPhaser.SetIconAboveShip(0)
StarPhaser.SetFireSound('Galaxy Phaser')
StarPhaser.SetMaxCharge(3.2)
StarPhaser.SetMaxDamage(2000.0)
StarPhaser.SetMaxDamageDistance(80.0)
StarPhaser.SetMinFiringCharge(2.0)
StarPhaser.SetNormalDischargeRate(1.0)
StarPhaser.SetRechargeRate(0.006)
StarPhaser.SetIndicatorIconNum(510)
StarPhaser.SetIndicatorIconPositionX(107)
StarPhaser.SetIndicatorIconPositionY(95)
StarPhaserForward = App.TGPoint3()
StarPhaserForward.SetXYZ(0.573462, 0.000000, 0.819232)
StarPhaserUp = App.TGPoint3()
StarPhaserUp.SetXYZ(-0.894427, 0.000000, 0.447214)
StarPhaser.SetOrientation(StarPhaserForward, StarPhaserUp)
StarPhaser.SetWidth(0.001000)
StarPhaser.SetLength(0.001000)
StarPhaser.SetArcWidthAngles(-0.959931, 0.959931)
StarPhaser.SetArcHeightAngles(-1.047198, 0.610865)
StarPhaser.SetPhaserTextureStart(0)
StarPhaser.SetPhaserTextureEnd(7)
StarPhaser.SetPhaserWidth(0.5)
StarPhaser.SetNumSides(6)
StarPhaser.SetMainRadius(0.07)
StarPhaser.SetTaperRadius(0.01)
StarPhaser.SetCoreScale(0.3)
StarPhaser.SetTaperRatio(0.25)
StarPhaser.SetTaperMinLength(5.0)
StarPhaser.SetTaperMaxLength(30.0)
StarPhaser.SetLengthTextureTilePerUnit(0.02)
StarPhaser.SetPerimeterTile(1.0)
StarPhaser.SetTextureSpeed(2.5)
StarPhaser.SetTextureName('Custom/FTB/textures/Tactical/FedPhaser02.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.639216, 0.000000, 0.000000, 1.000000)
StarPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.992157, 0.192157, 0.054902, 1.000000)
StarPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.592157, 0.592157, 0.000000, 1.000000)
StarPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.803922, 0.803922, 0.000000, 1.000000)
StarPhaser.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarPhaser)
#################################################
PortPhaser = App.PhaserProperty_Create("Port Phaser")
PortPhaser.SetMaxCondition(1045.0)
PortPhaser.SetCritical(0)
PortPhaser.SetTargetable(1)
PortPhaser.SetPrimary(1)
PortPhaser.SetPosition(-0.101221, -0.023981, -0.034545)
PortPhaser.SetPosition2D(-62.7478111151, 78.2666490577)
PortPhaser.SetRepairComplexity(4.0)
PortPhaser.SetDisabledPercentage(0.75)
PortPhaser.SetRadius(0.002000)
PortPhaser.SetDumbfire(0)
PortPhaser.SetWeaponID(1)
PortPhaser.SetGroups(1)
PortPhaser.SetDamageRadiusFactor(0.100000)
PortPhaser.SetIconNum(364)
PortPhaser.SetIconPositionX(19)
PortPhaser.SetIconPositionY(75)
PortPhaser.SetIconAboveShip(0)
PortPhaser.SetFireSound('Galaxy Phaser')
PortPhaser.SetMaxCharge(3.2)
PortPhaser.SetMaxDamage(2000.0)
PortPhaser.SetMaxDamageDistance(80.0)
PortPhaser.SetMinFiringCharge(2.0)
PortPhaser.SetNormalDischargeRate(1.0)
PortPhaser.SetRechargeRate(0.006)
PortPhaser.SetIndicatorIconNum(510)
PortPhaser.SetIndicatorIconPositionX(12)
PortPhaser.SetIndicatorIconPositionY(95)
PortPhaserForward = App.TGPoint3()
PortPhaserForward.SetXYZ(-0.573462, 0.000000, 0.819232)
PortPhaserUp = App.TGPoint3()
PortPhaserUp.SetXYZ(0.894427, 0.000000, 0.447214)
PortPhaser.SetOrientation(PortPhaserForward, PortPhaserUp)
PortPhaser.SetWidth(0.001000)
PortPhaser.SetLength(0.001000)
PortPhaser.SetArcWidthAngles(-0.959931, 0.959931)
PortPhaser.SetArcHeightAngles(-1.047198, 0.610865)
PortPhaser.SetPhaserTextureStart(0)
PortPhaser.SetPhaserTextureEnd(7)
PortPhaser.SetPhaserWidth(0.5)
PortPhaser.SetNumSides(6)
PortPhaser.SetMainRadius(0.07)
PortPhaser.SetTaperRadius(0.01)
PortPhaser.SetCoreScale(0.3)
PortPhaser.SetTaperRatio(0.25)
PortPhaser.SetTaperMinLength(5.0)
PortPhaser.SetTaperMaxLength(30.0)
PortPhaser.SetLengthTextureTilePerUnit(0.02)
PortPhaser.SetPerimeterTile(1.0)
PortPhaser.SetTextureSpeed(2.5)
PortPhaser.SetTextureName('Custom/FTB/textures/Tactical/FedPhaser02.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.639216, 0.000000, 0.000000, 1.000000)
PortPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.992157, 0.192157, 0.054902, 1.000000)
PortPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.592157, 0.592157, 0.000000, 1.000000)
PortPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.803922, 0.803922, 0.000000, 1.000000)
PortPhaser.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortPhaser)
# Property load function.
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1045.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.011500, 0.011300)
ShieldGenerator.SetPosition2D(64.0, 63.6521430768)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.002000)
ShieldGenerator.SetNormalPowerPerSecond(52.5)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 525.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 262.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 262.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 262.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 262.5)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 262.5)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.503984364192)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.503984364192)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.503984364192)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.503984364192)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.503984364192)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.503984364192)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(1597.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.013000, -0.008400)
WarpCore.SetPosition2D(64.0, 65.359906455)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.004000)
WarpCore.SetMainBatteryLimit(500000.0)
WarpCore.SetBackupBatteryLimit(160000.0)
WarpCore.SetMainConduitCapacity(2400.0)
WarpCore.SetBackupConduitCapacity(800.0)
WarpCore.SetPowerOutput(2000.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(4330.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.140000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ForwardTorpedo1 = App.TorpedoTubeProperty_Create("Forward Torpedo 1")
ForwardTorpedo1.SetMaxCondition(1599.0)
ForwardTorpedo1.SetCritical(0)
ForwardTorpedo1.SetTargetable(1)
ForwardTorpedo1.SetPrimary(1)
ForwardTorpedo1.SetPosition(0.000000, -0.063560, 0.050179)
ForwardTorpedo1.SetPosition2D(64.0, 51.7651566845)
ForwardTorpedo1.SetRepairComplexity(4.0)
ForwardTorpedo1.SetDisabledPercentage(0.75)
ForwardTorpedo1.SetRadius(0.367250)
ForwardTorpedo1.SetDumbfire(1)
ForwardTorpedo1.SetWeaponID(1)
ForwardTorpedo1.SetGroups(1)
ForwardTorpedo1.SetDamageRadiusFactor(0.17)
ForwardTorpedo1.SetIconNum(370)
ForwardTorpedo1.SetIconPositionX(77)
ForwardTorpedo1.SetIconPositionY(100)
ForwardTorpedo1.SetIconAboveShip(1)
ForwardTorpedo1.SetImmediateDelay(4.0)
ForwardTorpedo1.SetReloadDelay(30.0)
ForwardTorpedo1.SetMaxReady(2)
ForwardTorpedo1Direction = App.TGPoint3()
ForwardTorpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo1.SetDirection(ForwardTorpedo1Direction)
ForwardTorpedo1Right = App.TGPoint3()
ForwardTorpedo1Right.SetXYZ(-1.000000, 0.000000, 0.000000)
ForwardTorpedo1.SetRight(ForwardTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo1)
#################################################
ForwardTorpedo2 = App.TorpedoTubeProperty_Create("Forward Torpedo 2")
ForwardTorpedo2.SetMaxCondition(1599.0)
ForwardTorpedo2.SetCritical(0)
ForwardTorpedo2.SetTargetable(1)
ForwardTorpedo2.SetPrimary(1)
ForwardTorpedo2.SetPosition(0.017785, -0.063560, 0.049298)
ForwardTorpedo2.SetPosition2D(86.2701793174, 51.7192716244)
ForwardTorpedo2.SetRepairComplexity(4.0)
ForwardTorpedo2.SetDisabledPercentage(0.75)
ForwardTorpedo2.SetRadius(0.367250)
ForwardTorpedo2.SetDumbfire(1)
ForwardTorpedo2.SetWeaponID(1)
ForwardTorpedo2.SetGroups(1)
ForwardTorpedo2.SetDamageRadiusFactor(0.17)
ForwardTorpedo2.SetIconNum(370)
ForwardTorpedo2.SetIconPositionX(88)
ForwardTorpedo2.SetIconPositionY(100)
ForwardTorpedo2.SetIconAboveShip(1)
ForwardTorpedo2.SetImmediateDelay(4.0)
ForwardTorpedo2.SetReloadDelay(30.0)
ForwardTorpedo2.SetMaxReady(2)
ForwardTorpedo2Direction = App.TGPoint3()
ForwardTorpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo2.SetDirection(ForwardTorpedo2Direction)
ForwardTorpedo2Right = App.TGPoint3()
ForwardTorpedo2Right.SetXYZ(-1.000000, 0.000000, 0.000000)
ForwardTorpedo2.SetRight(ForwardTorpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo2)
#################################################
ForwardTorpedo3 = App.TorpedoTubeProperty_Create("Forward Torpedo 3")
ForwardTorpedo3.SetMaxCondition(1599.0)
ForwardTorpedo3.SetCritical(0)
ForwardTorpedo3.SetTargetable(1)
ForwardTorpedo3.SetPrimary(1)
ForwardTorpedo3.SetPosition(-0.017785, -0.063560, 0.049298)
ForwardTorpedo3.SetPosition2D(41.7298206826, 51.7192716244)
ForwardTorpedo3.SetRepairComplexity(4.0)
ForwardTorpedo3.SetDisabledPercentage(0.75)
ForwardTorpedo3.SetRadius(0.367250)
ForwardTorpedo3.SetDumbfire(1)
ForwardTorpedo3.SetWeaponID(1)
ForwardTorpedo3.SetGroups(1)
ForwardTorpedo3.SetDamageRadiusFactor(0.17)
ForwardTorpedo3.SetIconNum(370)
ForwardTorpedo3.SetIconPositionX(67)
ForwardTorpedo3.SetIconPositionY(100)
ForwardTorpedo3.SetIconAboveShip(1)
ForwardTorpedo3.SetImmediateDelay(4.0)
ForwardTorpedo3.SetReloadDelay(30.0)
ForwardTorpedo3.SetMaxReady(2)
ForwardTorpedo3Direction = App.TGPoint3()
ForwardTorpedo3Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo3.SetDirection(ForwardTorpedo3Direction)
ForwardTorpedo3Right = App.TGPoint3()
ForwardTorpedo3Right.SetXYZ(-1.000000, 0.000000, 0.000000)
ForwardTorpedo3.SetRight(ForwardTorpedo3Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo3)
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
ViewscreenForwardPosition.SetXYZ(-0.009697, 0.160439, -0.014844)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.187761, -0.012891)
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
ViewscreenLeftPosition.SetXYZ(-0.060000, 0.060000, 0.020000)
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
ViewscreenRightPosition.SetXYZ(0.060000, 0.060000, 0.020000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.080000, 0.040000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.080000, -0.030000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.153794, -0.011759)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")
Phasers.SetMaxCondition(1045.0)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000175, 0.015236, -0.000475)
Phasers.SetPosition2D(64.2191330549, 63.9392970719)
Phasers.SetRepairComplexity(3.0)
Phasers.SetDisabledPercentage(0.5)
Phasers.SetRadius(0.002500)
Phasers.SetNormalPowerPerSecond(143.0)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(0)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")
Tractors.SetMaxCondition(1106.0)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, -0.050000, -0.010000)
Tractors.SetPosition2D(64.0, 68.8876783152)
Tractors.SetRepairComplexity(3.0)
Tractors.SetDisabledPercentage(0.5)
Tractors.SetRadius(0.050000)
Tractors.SetNormalPowerPerSecond(114.4)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")
ForwardTractor.SetMaxCondition(1045.0)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.000011, 0.018947, -0.007077)
ForwardTractor.SetPosition2D(64.0137740777, 63.1508373326)
ForwardTractor.SetRepairComplexity(3.0)
ForwardTractor.SetDisabledPercentage(0.75)
ForwardTractor.SetRadius(0.002000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(0)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(80)
ForwardTractor.SetIconPositionY(43)
ForwardTractor.SetIconAboveShip(0)
ForwardTractor.SetFireSound("Tractor Beam")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(4.0)
ForwardTractor.SetMaxDamageDistance(100.0)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(80)
ForwardTractor.SetIndicatorIconPositionY(43)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.855211, 0.698132)
ForwardTractor.SetArcHeightAngles(-0.698132, 0.104720)
ForwardTractor.SetTractorBeamWidth(0.100000)
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
ForwardTractor.SetMainRadius(0.030000)
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
Danube = App.ShipProperty_Create("Danube")
Danube.SetGenus(1)
Danube.SetSpecies(106)
Danube.SetMass(1.0)
Danube.SetRotationalInertia(8.0)
Danube.SetShipName("FTB_Danube")
Danube.SetModelFilename("Custom/FTB/Ships/FTBDanube/FTB_Danube.nif")
Danube.SetDamageResolution(6.000000)
Danube.SetAffiliation(0)
Danube.SetStationary(0)
Danube.SetAIString("FedAttack")
Danube.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Danube)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")
RepairSystem.SetMaxCondition(1398.0)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(64.0, 64.0)
RepairSystem.SetRepairComplexity(2.0)
RepairSystem.SetDisabledPercentage(0.5)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.0)
RepairSystem.SetMaxRepairPoints(0.0)
RepairSystem.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(1595.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.040000, -0.000900)
SensorArray.SetPosition2D(64.0, 63.6961664812)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.002000)
SensorArray.SetNormalPowerPerSecond(1000.0)
SensorArray.SetBaseSensorRange(1500.0)
SensorArray.SetMaxProbes(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
WarpEngines.SetMaxCondition(1055.0)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, -0.020000)
WarpEngines.SetPosition2D(64.0, 66.4009647864)
WarpEngines.SetRepairComplexity(3.0)
WarpEngines.SetDisabledPercentage(0.5)
WarpEngines.SetRadius(0.010000)
WarpEngines.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
Torpedoes.SetMaxCondition(1045.0)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.0, 64.0)
Torpedoes.SetRepairComplexity(3.0)
Torpedoes.SetDisabledPercentage(0.5)
Torpedoes.SetRadius(0.002)
Torpedoes.SetNormalPowerPerSecond(143.0)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 10)
Torpedoes.SetTorpedoScript(0, "ftb.Projectiles.FTBMicroPhotonTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
def LoadPropertySet(pObj):




















	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Danube", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
