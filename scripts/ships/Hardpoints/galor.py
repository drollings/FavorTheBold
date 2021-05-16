# C:\Utopia\Current\Build\scripts\ships\Hardpoints\galor.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")
PortImpulse.SetMaxCondition(2092.0)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.638000, -0.300000, -0.036000)
PortImpulse.SetPosition2D(-10.1725703906, 64.865339263)
PortImpulse.SetRepairComplexity(3.0)
PortImpulse.SetDisabledPercentage(0.5)
PortImpulse.SetRadius(0.200000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")
StarImpulse.SetMaxCondition(2092.0)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.638000, -0.300000, -0.036000)
StarImpulse.SetPosition2D(138.172570391, 64.865339263)
StarImpulse.SetRepairComplexity(3.0)
StarImpulse.SetDisabledPercentage(0.5)
StarImpulse.SetRadius(0.200000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
WarpEngine1 = App.EngineProperty_Create("Warp Engine 1")
WarpEngine1.SetMaxCondition(2935.0)
WarpEngine1.SetCritical(0)
WarpEngine1.SetTargetable(1)
WarpEngine1.SetPrimary(1)
WarpEngine1.SetPosition(0.000000, -1.200000, 0.000000)
WarpEngine1.SetPosition2D(64.0, 64.0)
WarpEngine1.SetRepairComplexity(3.0)
WarpEngine1.SetDisabledPercentage(0.5)
WarpEngine1.SetRadius(0.500000)
WarpEngine1.SetEngineType(WarpEngine1.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngine1)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1817.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.400000, -0.180000, 0.020000)
ImpulseEngines.SetPosition2D(110.503178928, 63.7546017533)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.080000)
ImpulseEngines.SetNormalPowerPerSecond(1608.23414634)
ImpulseEngines.SetMaxAccel(2.175)
ImpulseEngines.SetMaxAngularAccel(0.078)
ImpulseEngines.SetMaxAngularVelocity(0.195)
ImpulseEngines.SetMaxSpeed(10.4328125)
ImpulseEngines.SetEngineSound('Cardassian Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
ForwardBeam = App.PhaserProperty_Create("Forward Beam")
ForwardBeam.SetMaxCondition(1860.0)
ForwardBeam.SetCritical(0)
ForwardBeam.SetTargetable(1)
ForwardBeam.SetPrimary(1)
ForwardBeam.SetPosition(0.000000, 0.740000, -0.044600)
ForwardBeam.SetPosition2D(64.0, 61.6634252201)
ForwardBeam.SetRepairComplexity(2.4)
ForwardBeam.SetDisabledPercentage(0.75)
ForwardBeam.SetRadius(0.100000)
ForwardBeam.SetDumbfire(0)
ForwardBeam.SetWeaponID(1)
ForwardBeam.SetGroups(1)
ForwardBeam.SetDamageRadiusFactor(0.1)
ForwardBeam.SetIconNum(364)
ForwardBeam.SetIconPositionX(66)
ForwardBeam.SetIconPositionY(25)
ForwardBeam.SetIconAboveShip(0)
ForwardBeam.SetFireSound('Galor Phaser')
ForwardBeam.SetMaxCharge(3.5)
ForwardBeam.SetMaxDamage(1000.0)
ForwardBeam.SetMaxDamageDistance(30.0)
ForwardBeam.SetMinFiringCharge(2.0)
ForwardBeam.SetNormalDischargeRate(1.0)
ForwardBeam.SetRechargeRate(0.08)
ForwardBeam.SetIndicatorIconNum(510)
ForwardBeam.SetIndicatorIconPositionX(59)
ForwardBeam.SetIndicatorIconPositionY(35)
ForwardBeamForward = App.TGPoint3()
ForwardBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardBeamUp = App.TGPoint3()
ForwardBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardBeam.SetOrientation(ForwardBeamForward, ForwardBeamUp)
ForwardBeam.SetWidth(0.001000)
ForwardBeam.SetLength(0.001000)
ForwardBeam.SetArcWidthAngles(-0.872665, 0.872665)
ForwardBeam.SetArcHeightAngles(-1.134464, 0.349066)
ForwardBeam.SetPhaserTextureStart(1)
ForwardBeam.SetPhaserTextureEnd(15)
ForwardBeam.SetPhaserWidth(0.5)
ForwardBeam.SetNumSides(6)
ForwardBeam.SetMainRadius(0.06)
ForwardBeam.SetTaperRadius(0.03)
ForwardBeam.SetCoreScale(0.3)
ForwardBeam.SetTaperRatio(0.25)
ForwardBeam.SetTaperMinLength(5.0)
ForwardBeam.SetTaperMaxLength(30.0)
ForwardBeam.SetLengthTextureTilePerUnit(0.1)
ForwardBeam.SetPerimeterTile(1.0)
ForwardBeam.SetTextureSpeed(2.5)
ForwardBeam.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
ForwardBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
ForwardBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
ForwardBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForwardBeam.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardBeam)
#################################################
PortBeam = App.PhaserProperty_Create("Port Beam")
PortBeam.SetMaxCondition(1860.0)
PortBeam.SetCritical(0)
PortBeam.SetTargetable(1)
PortBeam.SetPrimary(1)
PortBeam.SetPosition(-1.100000, -0.139000, -0.024563)
PortBeam.SetPosition2D(-63.8837420527, 64.2835824857)
PortBeam.SetRepairComplexity(2.4)
PortBeam.SetDisabledPercentage(0.75)
PortBeam.SetRadius(0.100000)
PortBeam.SetDumbfire(0)
PortBeam.SetWeaponID(2)
PortBeam.SetGroups(1)
PortBeam.SetDamageRadiusFactor(0.1)
PortBeam.SetIconNum(361)
PortBeam.SetIconPositionX(-16)
PortBeam.SetIconPositionY(75)
PortBeam.SetIconAboveShip(0)
PortBeam.SetFireSound('Galor Phaser')
PortBeam.SetMaxCharge(3.5)
PortBeam.SetMaxDamage(1000.0)
PortBeam.SetMaxDamageDistance(30.0)
PortBeam.SetMinFiringCharge(2.0)
PortBeam.SetNormalDischargeRate(1.0)
PortBeam.SetRechargeRate(0.08)
PortBeam.SetIndicatorIconNum(508)
PortBeam.SetIndicatorIconPositionX(-3)
PortBeam.SetIndicatorIconPositionY(78)
PortBeamForward = App.TGPoint3()
PortBeamForward.SetXYZ(-1.000000, 0.000000, 0.000000)
PortBeamUp = App.TGPoint3()
PortBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortBeam.SetOrientation(PortBeamForward, PortBeamUp)
PortBeam.SetWidth(0.020000)
PortBeam.SetLength(0.020000)
PortBeam.SetArcWidthAngles(-1.396263, 1.570796)
PortBeam.SetArcHeightAngles(-0.698132, 1.221731)
PortBeam.SetPhaserTextureStart(1)
PortBeam.SetPhaserTextureEnd(15)
PortBeam.SetPhaserWidth(0.5)
PortBeam.SetNumSides(6)
PortBeam.SetMainRadius(0.06)
PortBeam.SetTaperRadius(0.03)
PortBeam.SetCoreScale(0.3)
PortBeam.SetTaperRatio(0.25)
PortBeam.SetTaperMinLength(5.0)
PortBeam.SetTaperMaxLength(30.0)
PortBeam.SetLengthTextureTilePerUnit(0.1)
PortBeam.SetPerimeterTile(1.0)
PortBeam.SetTextureSpeed(2.5)
PortBeam.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
PortBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
PortBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
PortBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
PortBeam.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortBeam)
#################################################
StarBeam = App.PhaserProperty_Create("Star Beam")
StarBeam.SetMaxCondition(1860.0)
StarBeam.SetCritical(0)
StarBeam.SetTargetable(1)
StarBeam.SetPrimary(1)
StarBeam.SetPosition(1.100000, -0.139000, -0.024563)
StarBeam.SetPosition2D(191.883742053, 64.2835824857)
StarBeam.SetRepairComplexity(2.4)
StarBeam.SetDisabledPercentage(0.75)
StarBeam.SetRadius(0.100000)
StarBeam.SetDumbfire(0)
StarBeam.SetWeaponID(3)
StarBeam.SetGroups(1)
StarBeam.SetDamageRadiusFactor(0.1)
StarBeam.SetIconNum(362)
StarBeam.SetIconPositionX(158)
StarBeam.SetIconPositionY(75)
StarBeam.SetIconAboveShip(0)
StarBeam.SetFireSound('Galor Phaser')
StarBeam.SetMaxCharge(3.5)
StarBeam.SetMaxDamage(1000.0)
StarBeam.SetMaxDamageDistance(30.0)
StarBeam.SetMinFiringCharge(2.0)
StarBeam.SetNormalDischargeRate(1.0)
StarBeam.SetRechargeRate(0.08)
StarBeam.SetIndicatorIconNum(509)
StarBeam.SetIndicatorIconPositionX(140)
StarBeam.SetIndicatorIconPositionY(78)
StarBeamForward = App.TGPoint3()
StarBeamForward.SetXYZ(1.000000, 0.000000, 0.000000)
StarBeamUp = App.TGPoint3()
StarBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarBeam.SetOrientation(StarBeamForward, StarBeamUp)
StarBeam.SetWidth(0.020000)
StarBeam.SetLength(0.020000)
StarBeam.SetArcWidthAngles(-1.570796, 1.396263)
StarBeam.SetArcHeightAngles(-0.698132, 1.221731)
StarBeam.SetPhaserTextureStart(1)
StarBeam.SetPhaserTextureEnd(15)
StarBeam.SetPhaserWidth(0.5)
StarBeam.SetNumSides(6)
StarBeam.SetMainRadius(0.06)
StarBeam.SetTaperRadius(0.03)
StarBeam.SetCoreScale(0.3)
StarBeam.SetTaperRatio(0.25)
StarBeam.SetTaperMinLength(5.0)
StarBeam.SetTaperMaxLength(30.0)
StarBeam.SetLengthTextureTilePerUnit(0.1)
StarBeam.SetPerimeterTile(1.0)
StarBeam.SetTextureSpeed(2.5)
StarBeam.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
StarBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
StarBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
StarBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
StarBeam.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarBeam)
#################################################
AftBeam = App.PhaserProperty_Create("Aft Beam")
AftBeam.SetMaxCondition(1860.0)
AftBeam.SetCritical(0)
AftBeam.SetTargetable(1)
AftBeam.SetPrimary(1)
AftBeam.SetPosition(0.000000, -2.060000, 0.120000)
AftBeam.SetPosition2D(64.0, 46.4732432988)
AftBeam.SetRepairComplexity(2.4)
AftBeam.SetDisabledPercentage(0.75)
AftBeam.SetRadius(0.100000)
AftBeam.SetDumbfire(0)
AftBeam.SetWeaponID(4)
AftBeam.SetGroups(0)
AftBeam.SetDamageRadiusFactor(0.1)
AftBeam.SetIconNum(363)
AftBeam.SetIconPositionX(65)
AftBeam.SetIconPositionY(137)
AftBeam.SetIconAboveShip(1)
AftBeam.SetFireSound('Galor Phaser')
AftBeam.SetMaxCharge(2.1)
AftBeam.SetMaxDamage(1000.0)
AftBeam.SetMaxDamageDistance(30.0)
AftBeam.SetMinFiringCharge(1.2)
AftBeam.SetNormalDischargeRate(1.0)
AftBeam.SetRechargeRate(0.064)
AftBeam.SetIndicatorIconNum(511)
AftBeam.SetIndicatorIconPositionX(56)
AftBeam.SetIndicatorIconPositionY(127)
AftBeamForward = App.TGPoint3()
AftBeamForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftBeamUp = App.TGPoint3()
AftBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftBeam.SetOrientation(AftBeamForward, AftBeamUp)
AftBeam.SetWidth(0.020000)
AftBeam.SetLength(0.020000)
AftBeam.SetArcWidthAngles(-0.698132, 0.698132)
AftBeam.SetArcHeightAngles(0.087266, 0.610865)
AftBeam.SetPhaserTextureStart(1)
AftBeam.SetPhaserTextureEnd(15)
AftBeam.SetPhaserWidth(0.5)
AftBeam.SetNumSides(6)
AftBeam.SetMainRadius(0.06)
AftBeam.SetTaperRadius(0.03)
AftBeam.SetCoreScale(0.3)
AftBeam.SetTaperRatio(0.25)
AftBeam.SetTaperMinLength(5.0)
AftBeam.SetTaperMaxLength(30.0)
AftBeam.SetLengthTextureTilePerUnit(0.1)
AftBeam.SetPerimeterTile(1.0)
AftBeam.SetTextureSpeed(2.5)
AftBeam.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
AftBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
AftBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
AftBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
AftBeam.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(AftBeam)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1973.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.100000, 0.130000)
ShieldGenerator.SetPosition2D(64.0, 65.8353127905)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.150000)
ShieldGenerator.SetNormalPowerPerSecond(1650.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 12375.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 8250.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 9900.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 9900.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 8250.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 8250.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 13.4738589212)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 13.4738589212)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 13.4738589212)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 13.4738589212)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 13.4738589212)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 13.4738589212)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(2892.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.300000, -0.120000)
WarpCore.SetPosition2D(64.0, 67.4060093994)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.170000)
WarpCore.SetMainBatteryLimit(312000.0)
WarpCore.SetBackupBatteryLimit(312000.0)
WarpCore.SetMainConduitCapacity(4680.0)
WarpCore.SetBackupConduitCapacity(1560.0)
WarpCore.SetPowerOutput(3900.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(6679.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, -0.100000)
Hull.SetPosition2D(64.0, 64.5174059418)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ForwardTorpedo = App.TorpedoTubeProperty_Create("Forward Torpedo")
ForwardTorpedo.SetMaxCondition(1754.0)
ForwardTorpedo.SetCritical(0)
ForwardTorpedo.SetTargetable(1)
ForwardTorpedo.SetPrimary(1)
ForwardTorpedo.SetPosition(0.000000, 0.752000, -0.070000)
ForwardTorpedo.SetPosition2D(64.0, 60.3626362295)
ForwardTorpedo.SetRepairComplexity(4.0)
ForwardTorpedo.SetDisabledPercentage(0.75)
ForwardTorpedo.SetRadius(0.050000)
ForwardTorpedo.SetDumbfire(1)
ForwardTorpedo.SetWeaponID(0)
ForwardTorpedo.SetGroups(2)
ForwardTorpedo.SetDamageRadiusFactor(0.17)
ForwardTorpedo.SetIconNum(370)
ForwardTorpedo.SetIconPositionX(77)
ForwardTorpedo.SetIconPositionY(28)
ForwardTorpedo.SetIconAboveShip(0)
ForwardTorpedo.SetImmediateDelay(0.25)
ForwardTorpedo.SetReloadDelay(30.0)
ForwardTorpedo.SetMaxReady(2)
ForwardTorpedoDirection = App.TGPoint3()
ForwardTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo.SetDirection(ForwardTorpedoDirection)
ForwardTorpedoRight = App.TGPoint3()
ForwardTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTorpedo.SetRight(ForwardTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 1.000000, 0.190000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -2.000000, 0.000000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 1.000000, 0.190000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 1.000000, 0.190000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 1.000000, 0.190000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 1.000000, 0.070000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 1.000000, 0.190000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)

# Property load function.
Compressors = App.WeaponSystemProperty_Create("Compressors")
Compressors.SetMaxCondition(1860.0)
Compressors.SetCritical(0)
Compressors.SetTargetable(0)
Compressors.SetPrimary(1)
Compressors.SetPosition(0.000000, 0.000000, 0.000000)
Compressors.SetPosition2D(64.0, 64.0)
Compressors.SetRepairComplexity(3.0)
Compressors.SetDisabledPercentage(0.5)
Compressors.SetRadius(0.100000)
Compressors.SetNormalPowerPerSecond(750.0)
Compressors.SetWeaponSystemType(Compressors.WST_PHASER)
Compressors.SetSingleFire(1)
Compressors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Compressors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Compressors)
#################################################
Galor = App.ShipProperty_Create("Galor")
Galor.SetGenus(1)
Galor.SetSpecies(201)
Galor.SetMass(88.0)
Galor.SetRotationalInertia(45001.0)
Galor.SetShipName("Galor")
Galor.SetModelFilename("data/Models/Ships/Galor.nif")
Galor.SetDamageResolution(10.000000)
Galor.SetAffiliation(0)
Galor.SetStationary(0)
Galor.SetAIString("NonFedAttack")
Galor.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Galor)
#################################################
RepairSubsystem = App.RepairSubsystemProperty_Create("Repair Subsystem")
RepairSubsystem.SetMaxCondition(1860.0)
RepairSubsystem.SetCritical(0)
RepairSubsystem.SetTargetable(1)
RepairSubsystem.SetPrimary(1)
RepairSubsystem.SetPosition(0.000000, -1.603000, 0.027000)
RepairSubsystem.SetPosition2D(64.0, 60.8385979553)
RepairSubsystem.SetRepairComplexity(2.0)
RepairSubsystem.SetDisabledPercentage(0.5)
RepairSubsystem.SetRadius(0.100000)
RepairSubsystem.SetNormalPowerPerSecond(1.0)
RepairSubsystem.SetMaxRepairPoints(7.65)
RepairSubsystem.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSubsystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(2668.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.750000, 0.240000)
SensorArray.SetPosition2D(64.0, 80.284982441)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.070000)
SensorArray.SetNormalPowerPerSecond(1000.0)
SensorArray.SetBaseSensorRange(1500.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngine = App.WarpEngineProperty_Create("Warp Engine")
WarpEngine.SetMaxCondition(1817.0)
WarpEngine.SetCritical(0)
WarpEngine.SetTargetable(0)
WarpEngine.SetPrimary(1)
WarpEngine.SetPosition(0.000000, -0.400000, 0.020000)
WarpEngine.SetPosition2D(64.0, 63.4293751614)
WarpEngine.SetRepairComplexity(3.0)
WarpEngine.SetDisabledPercentage(0.5)
WarpEngine.SetRadius(0.080000)
WarpEngine.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngine)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
Torpedoes.SetMaxCondition(1657.0)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.0, 64.0)
Torpedoes.SetRepairComplexity(3.0)
Torpedoes.SetDisabledPercentage(0.5)
Torpedoes.SetRadius(0.002)
Torpedoes.SetNormalPowerPerSecond(750.0)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 60)
Torpedoes.SetTorpedoScript(0, "ftb.Projectiles.FTBCardTorpedo")
Torpedoes.SetMaxTorpedoes(1, 0)
Torpedoes.SetTorpedoScript(1, "ftb.Projectiles.FTBCardPlasmaBurst")
Torpedoes.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
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
	prop = App.g_kModelPropertyManager.FindByName("Compressors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Subsystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Galor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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