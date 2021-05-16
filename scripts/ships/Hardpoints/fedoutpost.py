# C:\Utopia\Current\Build\scripts\ships\Hardpoints\fedoutpost.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShuttleBay = App.ObjectEmitterProperty_Create("Shuttle Bay")

ShuttleBayForward = App.TGPoint3()
ShuttleBayForward.SetXYZ(-0.998036, -0.054259, 0.031293)
ShuttleBayUp = App.TGPoint3()
ShuttleBayUp.SetXYZ(0.033229, -0.035157, 0.998829)
ShuttleBayRight = App.TGPoint3()
ShuttleBayRight.SetXYZ(-0.053095, 0.997908, 0.036890)
ShuttleBay.SetOrientation(ShuttleBayForward, ShuttleBayUp, ShuttleBayRight)
ShuttleBayPosition = App.TGPoint3()
ShuttleBayPosition.SetXYZ(-3.700000, 0.000000, -3.900000)
ShuttleBay.SetPosition(ShuttleBayPosition)
ShuttleBay.SetEmittedObjectType(ShuttleBay.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)

# Property load function.
DorsalPhaser1 = App.PhaserProperty_Create("Dorsal Phaser 1")
DorsalPhaser1.SetMaxCondition(156312.0)
DorsalPhaser1.SetCritical(0)
DorsalPhaser1.SetTargetable(1)
DorsalPhaser1.SetPrimary(1)
DorsalPhaser1.SetPosition(0.000000, 0.000000, -6.000000)
DorsalPhaser1.SetPosition2D(64.0, 154.280684115)
DorsalPhaser1.SetRepairComplexity(2.4)
DorsalPhaser1.SetDisabledPercentage(0.75)
DorsalPhaser1.SetRadius(5.000000)
DorsalPhaser1.SetDumbfire(0)
DorsalPhaser1.SetWeaponID(1)
DorsalPhaser1.SetGroups(0)
DorsalPhaser1.SetDamageRadiusFactor(0.1)
DorsalPhaser1.SetIconNum(0)
DorsalPhaser1.SetIconPositionX(80)
DorsalPhaser1.SetIconPositionY(91)
DorsalPhaser1.SetIconAboveShip(0)
DorsalPhaser1.SetFireSound('Galor Phaser')
DorsalPhaser1.SetMaxCharge(3.5)
DorsalPhaser1.SetMaxDamage(4000.0)
DorsalPhaser1.SetMaxDamageDistance(50.0)
DorsalPhaser1.SetMinFiringCharge(2.0)
DorsalPhaser1.SetNormalDischargeRate(1.0)
DorsalPhaser1.SetRechargeRate(0.163)
DorsalPhaser1.SetIndicatorIconNum(0)
DorsalPhaser1.SetIndicatorIconPositionX(80)
DorsalPhaser1.SetIndicatorIconPositionY(101)
DorsalPhaser1Forward = App.TGPoint3()
DorsalPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
DorsalPhaser1Up = App.TGPoint3()
DorsalPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser1.SetOrientation(DorsalPhaser1Forward, DorsalPhaser1Up)
DorsalPhaser1.SetWidth(2.600000)
DorsalPhaser1.SetLength(2.600000)
DorsalPhaser1.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser1.SetArcHeightAngles(-1.658063, 0.261799)
DorsalPhaser1.SetPhaserTextureStart(1)
DorsalPhaser1.SetPhaserTextureEnd(15)
DorsalPhaser1.SetPhaserWidth(0.5)
DorsalPhaser1.SetNumSides(6)
DorsalPhaser1.SetMainRadius(0.1)
DorsalPhaser1.SetTaperRadius(0.02)
DorsalPhaser1.SetCoreScale(0.6)
DorsalPhaser1.SetTaperRatio(0.25)
DorsalPhaser1.SetTaperMinLength(5.0)
DorsalPhaser1.SetTaperMaxLength(30.0)
DorsalPhaser1.SetLengthTextureTilePerUnit(0.1)
DorsalPhaser1.SetPerimeterTile(1.0)
DorsalPhaser1.SetTextureSpeed(2.5)
DorsalPhaser1.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
DorsalPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
DorsalPhaser1.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser1)
#################################################
DorsalPhaser2 = App.PhaserProperty_Create("Dorsal Phaser 2")
DorsalPhaser2.SetMaxCondition(68952.0)
DorsalPhaser2.SetCritical(0)
DorsalPhaser2.SetTargetable(1)
DorsalPhaser2.SetPrimary(1)
DorsalPhaser2.SetPosition(0.000000, 0.000000, -6.000000)
DorsalPhaser2.SetPosition2D(64.0, 154.280684115)
DorsalPhaser2.SetRepairComplexity(2.4)
DorsalPhaser2.SetDisabledPercentage(0.75)
DorsalPhaser2.SetRadius(3.000000)
DorsalPhaser2.SetDumbfire(0)
DorsalPhaser2.SetWeaponID(2)
DorsalPhaser2.SetGroups(0)
DorsalPhaser2.SetDamageRadiusFactor(0.1)
DorsalPhaser2.SetIconNum(0)
DorsalPhaser2.SetIconPositionX(80)
DorsalPhaser2.SetIconPositionY(91)
DorsalPhaser2.SetIconAboveShip(0)
DorsalPhaser2.SetFireSound('Galor Phaser')
DorsalPhaser2.SetMaxCharge(3.5)
DorsalPhaser2.SetMaxDamage(4000.0)
DorsalPhaser2.SetMaxDamageDistance(50.0)
DorsalPhaser2.SetMinFiringCharge(2.0)
DorsalPhaser2.SetNormalDischargeRate(1.0)
DorsalPhaser2.SetRechargeRate(0.163)
DorsalPhaser2.SetIndicatorIconNum(0)
DorsalPhaser2.SetIndicatorIconPositionX(80)
DorsalPhaser2.SetIndicatorIconPositionY(101)
DorsalPhaser2Forward = App.TGPoint3()
DorsalPhaser2Forward.SetXYZ(1.000000, 0.000000, 0.000000)
DorsalPhaser2Up = App.TGPoint3()
DorsalPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser2.SetOrientation(DorsalPhaser2Forward, DorsalPhaser2Up)
DorsalPhaser2.SetWidth(2.600000)
DorsalPhaser2.SetLength(2.600000)
DorsalPhaser2.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser2.SetArcHeightAngles(-1.658063, 0.261799)
DorsalPhaser2.SetPhaserTextureStart(1)
DorsalPhaser2.SetPhaserTextureEnd(15)
DorsalPhaser2.SetPhaserWidth(0.5)
DorsalPhaser2.SetNumSides(6)
DorsalPhaser2.SetMainRadius(0.1)
DorsalPhaser2.SetTaperRadius(0.02)
DorsalPhaser2.SetCoreScale(0.6)
DorsalPhaser2.SetTaperRatio(0.25)
DorsalPhaser2.SetTaperMinLength(5.0)
DorsalPhaser2.SetTaperMaxLength(30.0)
DorsalPhaser2.SetLengthTextureTilePerUnit(0.1)
DorsalPhaser2.SetPerimeterTile(1.0)
DorsalPhaser2.SetTextureSpeed(2.5)
DorsalPhaser2.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
DorsalPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
DorsalPhaser2.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser2)
#################################################
DorsalPhaser3 = App.PhaserProperty_Create("Dorsal Phaser 3")
DorsalPhaser3.SetMaxCondition(68952.0)
DorsalPhaser3.SetCritical(0)
DorsalPhaser3.SetTargetable(1)
DorsalPhaser3.SetPrimary(1)
DorsalPhaser3.SetPosition(0.000000, 0.000000, -6.000000)
DorsalPhaser3.SetPosition2D(64.0, 154.280684115)
DorsalPhaser3.SetRepairComplexity(2.4)
DorsalPhaser3.SetDisabledPercentage(0.75)
DorsalPhaser3.SetRadius(3.000000)
DorsalPhaser3.SetDumbfire(0)
DorsalPhaser3.SetWeaponID(3)
DorsalPhaser3.SetGroups(0)
DorsalPhaser3.SetDamageRadiusFactor(0.1)
DorsalPhaser3.SetIconNum(0)
DorsalPhaser3.SetIconPositionX(80)
DorsalPhaser3.SetIconPositionY(91)
DorsalPhaser3.SetIconAboveShip(0)
DorsalPhaser3.SetFireSound('Galor Phaser')
DorsalPhaser3.SetMaxCharge(3.5)
DorsalPhaser3.SetMaxDamage(4000.0)
DorsalPhaser3.SetMaxDamageDistance(50.0)
DorsalPhaser3.SetMinFiringCharge(2.0)
DorsalPhaser3.SetNormalDischargeRate(1.0)
DorsalPhaser3.SetRechargeRate(0.163)
DorsalPhaser3.SetIndicatorIconNum(0)
DorsalPhaser3.SetIndicatorIconPositionX(80)
DorsalPhaser3.SetIndicatorIconPositionY(101)
DorsalPhaser3Forward = App.TGPoint3()
DorsalPhaser3Forward.SetXYZ(0.000000, -1.000000, 0.000000)
DorsalPhaser3Up = App.TGPoint3()
DorsalPhaser3Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser3.SetOrientation(DorsalPhaser3Forward, DorsalPhaser3Up)
DorsalPhaser3.SetWidth(2.600000)
DorsalPhaser3.SetLength(2.600000)
DorsalPhaser3.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser3.SetArcHeightAngles(-1.658063, 0.261799)
DorsalPhaser3.SetPhaserTextureStart(1)
DorsalPhaser3.SetPhaserTextureEnd(15)
DorsalPhaser3.SetPhaserWidth(0.5)
DorsalPhaser3.SetNumSides(6)
DorsalPhaser3.SetMainRadius(0.1)
DorsalPhaser3.SetTaperRadius(0.02)
DorsalPhaser3.SetCoreScale(0.6)
DorsalPhaser3.SetTaperRatio(0.25)
DorsalPhaser3.SetTaperMinLength(5.0)
DorsalPhaser3.SetTaperMaxLength(30.0)
DorsalPhaser3.SetLengthTextureTilePerUnit(0.1)
DorsalPhaser3.SetPerimeterTile(1.0)
DorsalPhaser3.SetTextureSpeed(2.5)
DorsalPhaser3.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser3.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser3.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
DorsalPhaser3.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
DorsalPhaser3.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser3)
#################################################
DorsalPhaser4 = App.PhaserProperty_Create("Dorsal Phaser 4")
DorsalPhaser4.SetMaxCondition(68952.0)
DorsalPhaser4.SetCritical(0)
DorsalPhaser4.SetTargetable(1)
DorsalPhaser4.SetPrimary(1)
DorsalPhaser4.SetPosition(0.000000, 0.000000, -6.000000)
DorsalPhaser4.SetPosition2D(64.0, 154.280684115)
DorsalPhaser4.SetRepairComplexity(2.4)
DorsalPhaser4.SetDisabledPercentage(0.75)
DorsalPhaser4.SetRadius(3.000000)
DorsalPhaser4.SetDumbfire(0)
DorsalPhaser4.SetWeaponID(4)
DorsalPhaser4.SetGroups(0)
DorsalPhaser4.SetDamageRadiusFactor(0.1)
DorsalPhaser4.SetIconNum(0)
DorsalPhaser4.SetIconPositionX(80)
DorsalPhaser4.SetIconPositionY(91)
DorsalPhaser4.SetIconAboveShip(0)
DorsalPhaser4.SetFireSound('Galor Phaser')
DorsalPhaser4.SetMaxCharge(3.5)
DorsalPhaser4.SetMaxDamage(4000.0)
DorsalPhaser4.SetMaxDamageDistance(50.0)
DorsalPhaser4.SetMinFiringCharge(2.0)
DorsalPhaser4.SetNormalDischargeRate(1.0)
DorsalPhaser4.SetRechargeRate(0.163)
DorsalPhaser4.SetIndicatorIconNum(0)
DorsalPhaser4.SetIndicatorIconPositionX(80)
DorsalPhaser4.SetIndicatorIconPositionY(101)
DorsalPhaser4Forward = App.TGPoint3()
DorsalPhaser4Forward.SetXYZ(-1.000000, 0.000000, 0.000000)
DorsalPhaser4Up = App.TGPoint3()
DorsalPhaser4Up.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser4.SetOrientation(DorsalPhaser4Forward, DorsalPhaser4Up)
DorsalPhaser4.SetWidth(2.600000)
DorsalPhaser4.SetLength(2.600000)
DorsalPhaser4.SetArcWidthAngles(-0.872665, 0.872665)
DorsalPhaser4.SetArcHeightAngles(-1.658063, 0.261799)
DorsalPhaser4.SetPhaserTextureStart(1)
DorsalPhaser4.SetPhaserTextureEnd(15)
DorsalPhaser4.SetPhaserWidth(0.5)
DorsalPhaser4.SetNumSides(6)
DorsalPhaser4.SetMainRadius(0.1)
DorsalPhaser4.SetTaperRadius(0.02)
DorsalPhaser4.SetCoreScale(0.6)
DorsalPhaser4.SetTaperRatio(0.25)
DorsalPhaser4.SetTaperMinLength(5.0)
DorsalPhaser4.SetTaperMaxLength(30.0)
DorsalPhaser4.SetLengthTextureTilePerUnit(0.1)
DorsalPhaser4.SetPerimeterTile(1.0)
DorsalPhaser4.SetTextureSpeed(2.5)
DorsalPhaser4.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser4.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
DorsalPhaser4.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
DorsalPhaser4.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
DorsalPhaser4.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser4)
#################################################
VentralPhaser1 = App.PhaserProperty_Create("Ventral Phaser 1")
VentralPhaser1.SetMaxCondition(183839.0)
VentralPhaser1.SetCritical(0)
VentralPhaser1.SetTargetable(1)
VentralPhaser1.SetPrimary(1)
VentralPhaser1.SetPosition(0.000000, 0.000000, 0.600000)
VentralPhaser1.SetPosition2D(64.0, 64.9028068412)
VentralPhaser1.SetRepairComplexity(2.4)
VentralPhaser1.SetDisabledPercentage(0.75)
VentralPhaser1.SetRadius(5.500000)
VentralPhaser1.SetDumbfire(0)
VentralPhaser1.SetWeaponID(5)
VentralPhaser1.SetGroups(0)
VentralPhaser1.SetDamageRadiusFactor(0.1)
VentralPhaser1.SetIconNum(0)
VentralPhaser1.SetIconPositionX(80)
VentralPhaser1.SetIconPositionY(59)
VentralPhaser1.SetIconAboveShip(1)
VentralPhaser1.SetFireSound('Galor Phaser')
VentralPhaser1.SetMaxCharge(3.5)
VentralPhaser1.SetMaxDamage(4000.0)
VentralPhaser1.SetMaxDamageDistance(50.0)
VentralPhaser1.SetMinFiringCharge(2.0)
VentralPhaser1.SetNormalDischargeRate(1.0)
VentralPhaser1.SetRechargeRate(0.163)
VentralPhaser1.SetIndicatorIconNum(0)
VentralPhaser1.SetIndicatorIconPositionX(80)
VentralPhaser1.SetIndicatorIconPositionY(59)
VentralPhaser1Forward = App.TGPoint3()
VentralPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
VentralPhaser1Up = App.TGPoint3()
VentralPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
VentralPhaser1.SetOrientation(VentralPhaser1Forward, VentralPhaser1Up)
VentralPhaser1.SetWidth(5.500000)
VentralPhaser1.SetLength(5.500000)
VentralPhaser1.SetArcWidthAngles(-0.872665, 0.872665)
VentralPhaser1.SetArcHeightAngles(0.034907, 1.658063)
VentralPhaser1.SetPhaserTextureStart(1)
VentralPhaser1.SetPhaserTextureEnd(15)
VentralPhaser1.SetPhaserWidth(0.5)
VentralPhaser1.SetNumSides(6)
VentralPhaser1.SetMainRadius(0.1)
VentralPhaser1.SetTaperRadius(0.02)
VentralPhaser1.SetCoreScale(0.6)
VentralPhaser1.SetTaperRatio(0.25)
VentralPhaser1.SetTaperMinLength(5.0)
VentralPhaser1.SetTaperMaxLength(30.0)
VentralPhaser1.SetLengthTextureTilePerUnit(0.1)
VentralPhaser1.SetPerimeterTile(1.0)
VentralPhaser1.SetTextureSpeed(2.5)
VentralPhaser1.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
VentralPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
VentralPhaser1.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPhaser1)
#################################################
VentralPhaser2 = App.PhaserProperty_Create("Ventral Phaser 2")
VentralPhaser2.SetMaxCondition(183839.0)
VentralPhaser2.SetCritical(0)
VentralPhaser2.SetTargetable(1)
VentralPhaser2.SetPrimary(1)
VentralPhaser2.SetPosition(0.000000, 0.000000, 0.600000)
VentralPhaser2.SetPosition2D(64.0, 64.9028068412)
VentralPhaser2.SetRepairComplexity(2.4)
VentralPhaser2.SetDisabledPercentage(0.75)
VentralPhaser2.SetRadius(5.500000)
VentralPhaser2.SetDumbfire(0)
VentralPhaser2.SetWeaponID(6)
VentralPhaser2.SetGroups(0)
VentralPhaser2.SetDamageRadiusFactor(0.1)
VentralPhaser2.SetIconNum(0)
VentralPhaser2.SetIconPositionX(80)
VentralPhaser2.SetIconPositionY(59)
VentralPhaser2.SetIconAboveShip(1)
VentralPhaser2.SetFireSound('Galor Phaser')
VentralPhaser2.SetMaxCharge(3.5)
VentralPhaser2.SetMaxDamage(4000.0)
VentralPhaser2.SetMaxDamageDistance(50.0)
VentralPhaser2.SetMinFiringCharge(2.0)
VentralPhaser2.SetNormalDischargeRate(1.0)
VentralPhaser2.SetRechargeRate(0.163)
VentralPhaser2.SetIndicatorIconNum(0)
VentralPhaser2.SetIndicatorIconPositionX(80)
VentralPhaser2.SetIndicatorIconPositionY(59)
VentralPhaser2Forward = App.TGPoint3()
VentralPhaser2Forward.SetXYZ(1.000000, 0.000000, 0.000000)
VentralPhaser2Up = App.TGPoint3()
VentralPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
VentralPhaser2.SetOrientation(VentralPhaser2Forward, VentralPhaser2Up)
VentralPhaser2.SetWidth(5.500000)
VentralPhaser2.SetLength(5.500000)
VentralPhaser2.SetArcWidthAngles(-0.872665, 0.872665)
VentralPhaser2.SetArcHeightAngles(0.034907, 1.658063)
VentralPhaser2.SetPhaserTextureStart(1)
VentralPhaser2.SetPhaserTextureEnd(15)
VentralPhaser2.SetPhaserWidth(0.5)
VentralPhaser2.SetNumSides(6)
VentralPhaser2.SetMainRadius(0.1)
VentralPhaser2.SetTaperRadius(0.02)
VentralPhaser2.SetCoreScale(0.6)
VentralPhaser2.SetTaperRatio(0.25)
VentralPhaser2.SetTaperMinLength(5.0)
VentralPhaser2.SetTaperMaxLength(30.0)
VentralPhaser2.SetLengthTextureTilePerUnit(0.1)
VentralPhaser2.SetPerimeterTile(1.0)
VentralPhaser2.SetTextureSpeed(2.5)
VentralPhaser2.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
VentralPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
VentralPhaser2.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPhaser2)
#################################################
VentralPhaser3 = App.PhaserProperty_Create("Ventral Phaser 3")
VentralPhaser3.SetMaxCondition(183839.0)
VentralPhaser3.SetCritical(0)
VentralPhaser3.SetTargetable(1)
VentralPhaser3.SetPrimary(1)
VentralPhaser3.SetPosition(0.000000, 0.000000, 0.600000)
VentralPhaser3.SetPosition2D(64.0, 64.9028068412)
VentralPhaser3.SetRepairComplexity(2.4)
VentralPhaser3.SetDisabledPercentage(0.75)
VentralPhaser3.SetRadius(5.500000)
VentralPhaser3.SetDumbfire(0)
VentralPhaser3.SetWeaponID(7)
VentralPhaser3.SetGroups(0)
VentralPhaser3.SetDamageRadiusFactor(0.1)
VentralPhaser3.SetIconNum(0)
VentralPhaser3.SetIconPositionX(80)
VentralPhaser3.SetIconPositionY(59)
VentralPhaser3.SetIconAboveShip(1)
VentralPhaser3.SetFireSound('Galor Phaser')
VentralPhaser3.SetMaxCharge(3.5)
VentralPhaser3.SetMaxDamage(4000.0)
VentralPhaser3.SetMaxDamageDistance(50.0)
VentralPhaser3.SetMinFiringCharge(2.0)
VentralPhaser3.SetNormalDischargeRate(1.0)
VentralPhaser3.SetRechargeRate(0.163)
VentralPhaser3.SetIndicatorIconNum(0)
VentralPhaser3.SetIndicatorIconPositionX(80)
VentralPhaser3.SetIndicatorIconPositionY(59)
VentralPhaser3Forward = App.TGPoint3()
VentralPhaser3Forward.SetXYZ(0.000000, -1.000000, 0.000000)
VentralPhaser3Up = App.TGPoint3()
VentralPhaser3Up.SetXYZ(0.000000, 0.000000, 1.000000)
VentralPhaser3.SetOrientation(VentralPhaser3Forward, VentralPhaser3Up)
VentralPhaser3.SetWidth(5.500000)
VentralPhaser3.SetLength(5.500000)
VentralPhaser3.SetArcWidthAngles(-0.872665, 0.872665)
VentralPhaser3.SetArcHeightAngles(0.034907, 1.658063)
VentralPhaser3.SetPhaserTextureStart(1)
VentralPhaser3.SetPhaserTextureEnd(15)
VentralPhaser3.SetPhaserWidth(0.5)
VentralPhaser3.SetNumSides(6)
VentralPhaser3.SetMainRadius(0.1)
VentralPhaser3.SetTaperRadius(0.02)
VentralPhaser3.SetCoreScale(0.6)
VentralPhaser3.SetTaperRatio(0.25)
VentralPhaser3.SetTaperMinLength(5.0)
VentralPhaser3.SetTaperMaxLength(30.0)
VentralPhaser3.SetLengthTextureTilePerUnit(0.1)
VentralPhaser3.SetPerimeterTile(1.0)
VentralPhaser3.SetTextureSpeed(2.5)
VentralPhaser3.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser3.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser3.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
VentralPhaser3.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
VentralPhaser3.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPhaser3)
#################################################
VentralPhaser4 = App.PhaserProperty_Create("Ventral Phaser 4")
VentralPhaser4.SetMaxCondition(183839.0)
VentralPhaser4.SetCritical(0)
VentralPhaser4.SetTargetable(1)
VentralPhaser4.SetPrimary(1)
VentralPhaser4.SetPosition(0.000000, 0.000000, 0.600000)
VentralPhaser4.SetPosition2D(64.0, 64.9028068412)
VentralPhaser4.SetRepairComplexity(2.4)
VentralPhaser4.SetDisabledPercentage(0.75)
VentralPhaser4.SetRadius(5.500000)
VentralPhaser4.SetDumbfire(0)
VentralPhaser4.SetWeaponID(8)
VentralPhaser4.SetGroups(0)
VentralPhaser4.SetDamageRadiusFactor(0.1)
VentralPhaser4.SetIconNum(0)
VentralPhaser4.SetIconPositionX(80)
VentralPhaser4.SetIconPositionY(59)
VentralPhaser4.SetIconAboveShip(1)
VentralPhaser4.SetFireSound('Galor Phaser')
VentralPhaser4.SetMaxCharge(3.5)
VentralPhaser4.SetMaxDamage(4000.0)
VentralPhaser4.SetMaxDamageDistance(50.0)
VentralPhaser4.SetMinFiringCharge(2.0)
VentralPhaser4.SetNormalDischargeRate(1.0)
VentralPhaser4.SetRechargeRate(0.163)
VentralPhaser4.SetIndicatorIconNum(0)
VentralPhaser4.SetIndicatorIconPositionX(80)
VentralPhaser4.SetIndicatorIconPositionY(59)
VentralPhaser4Forward = App.TGPoint3()
VentralPhaser4Forward.SetXYZ(-1.000000, 0.000000, 0.000000)
VentralPhaser4Up = App.TGPoint3()
VentralPhaser4Up.SetXYZ(0.000000, 0.000000, 1.000000)
VentralPhaser4.SetOrientation(VentralPhaser4Forward, VentralPhaser4Up)
VentralPhaser4.SetWidth(5.500000)
VentralPhaser4.SetLength(5.500000)
VentralPhaser4.SetArcWidthAngles(-0.872665, 0.872665)
VentralPhaser4.SetArcHeightAngles(0.034907, 1.658063)
VentralPhaser4.SetPhaserTextureStart(1)
VentralPhaser4.SetPhaserTextureEnd(15)
VentralPhaser4.SetPhaserWidth(0.5)
VentralPhaser4.SetNumSides(6)
VentralPhaser4.SetMainRadius(0.1)
VentralPhaser4.SetTaperRadius(0.02)
VentralPhaser4.SetCoreScale(0.6)
VentralPhaser4.SetTaperRatio(0.25)
VentralPhaser4.SetTaperMinLength(5.0)
VentralPhaser4.SetTaperMaxLength(30.0)
VentralPhaser4.SetLengthTextureTilePerUnit(0.1)
VentralPhaser4.SetPerimeterTile(1.0)
VentralPhaser4.SetTextureSpeed(2.5)
VentralPhaser4.SetTextureName('Custom/FTB/textures/Tactical/Laurelin_CardBeam03.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser4.SetOuterShellColor(kColor)
kColor.SetRGBA(0.721569, 0.556863, 0.000000, 1.000000)
VentralPhaser4.SetInnerShellColor(kColor)
kColor.SetRGBA(0.984314, 0.756863, 0.058824, 1.000000)
VentralPhaser4.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
VentralPhaser4.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPhaser4)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(68952.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, -2.000000)
ShieldGenerator.SetPosition2D(64.0, 74.0311871239)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(3.000000)
ShieldGenerator.SetNormalPowerPerSecond(10000.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 50000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 50000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 50000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 50000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 50000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 50000.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 102.233766234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 102.233766234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 102.233766234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 102.233766234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 102.233766234)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 102.233766234)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")
PowerPlant.SetMaxCondition(187089.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 5.000000)
PowerPlant.SetPosition2D(64.0, 126.694919524)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(5.500000)
PowerPlant.SetMainBatteryLimit(3250000.0)
PowerPlant.SetBackupBatteryLimit(1040000.0)
PowerPlant.SetMainConduitCapacity(15600.0)
PowerPlant.SetBackupConduitCapacity(5200.0)
PowerPlant.SetPowerOutput(13000.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(164812.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")
Phasers.SetMaxCondition(10939.0)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000000, 0.000000, 0.000000)
Phasers.SetPosition2D(64.0, 64.0)
Phasers.SetRepairComplexity(3.0)
Phasers.SetDisabledPercentage(0.5)
Phasers.SetRadius(0.500000)
Phasers.SetNormalPowerPerSecond(10517.0)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
FedOutpost = App.ShipProperty_Create("Fed Outpost")
FedOutpost.SetGenus(2)
FedOutpost.SetSpecies(702)
FedOutpost.SetMass(440.0)
FedOutpost.SetRotationalInertia(225001.0)
FedOutpost.SetShipName("Federation Outpost")
FedOutpost.SetModelFilename("data/Models/Bases/SpaceFacility/SpaceFacility.nif")
FedOutpost.SetDamageResolution(15.000000)
FedOutpost.SetAffiliation(0)
FedOutpost.SetStationary(0)
FedOutpost.SetAIString("StarbaseAttack")
FedOutpost.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(FedOutpost)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(68952.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(64.0, 64.0)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(3.000000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(142.68)
Engineering.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(159562.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, -7.000000)
SensorArray.SetPosition2D(64.0, 186.882042268)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(5.000000)
SensorArray.SetNormalPowerPerSecond(1600.0)
SensorArray.SetBaseSensorRange(6000.0)
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
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Phaser 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Phaser 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fed Outpost", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
