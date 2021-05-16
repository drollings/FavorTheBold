# C:\Utopia\Current\Build\scripts\ships\Hardpoints\drydock.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(14851.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(1.900000, 0.000000, 2.300000)
ShieldGenerator.SetPosition2D(101.409629288, 71.8505736022)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(3.000000)
ShieldGenerator.SetNormalPowerPerSecond(30000.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
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
PowerPlant.SetMaxCondition(9083.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(-1.900000, 0.000000, 2.300000)
PowerPlant.SetPosition2D(26.5903707122, 71.8505736022)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(2.000000)
PowerPlant.SetMainBatteryLimit(5875000.0)
PowerPlant.SetBackupBatteryLimit(1880000.0)
PowerPlant.SetMainConduitCapacity(28200.0)
PowerPlant.SetBackupConduitCapacity(9400.0)
PowerPlant.SetPowerOutput(23500.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(79991.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 1.300000)
Hull.SetPosition2D(64.0, 66.5080282396)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(8.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")
Tractors.SetMaxCondition(1780.0)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.000000, 0.000000)
Tractors.SetPosition2D(64.0, 64.0)
Tractors.SetRepairComplexity(3.0)
Tractors.SetDisabledPercentage(0.5)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(10100.0)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
AftTractor1 = App.TractorBeamProperty_Create("Aft Tractor 1")
AftTractor1.SetMaxCondition(2356.0)
AftTractor1.SetCritical(0)
AftTractor1.SetTargetable(1)
AftTractor1.SetPrimary(1)
AftTractor1.SetPosition(-1.900000, -6.400000, 2.100000)
AftTractor1.SetPosition2D(26.5903707122, 42.0510428022)
AftTractor1.SetRepairComplexity(3.0)
AftTractor1.SetDisabledPercentage(0.75)
AftTractor1.SetRadius(0.500000)
AftTractor1.SetDumbfire(0)
AftTractor1.SetWeaponID(7)
AftTractor1.SetGroups(0)
AftTractor1.SetDamageRadiusFactor(0.300000)
AftTractor1.SetIconNum(0)
AftTractor1.SetIconPositionX(63)
AftTractor1.SetIconPositionY(107)
AftTractor1.SetIconAboveShip(1)
AftTractor1.SetFireSound("Tractor Beam")
AftTractor1.SetMaxCharge(5.000000)
AftTractor1.SetMaxDamage(24.0)
AftTractor1.SetMaxDamageDistance(100.0)
AftTractor1.SetMinFiringCharge(3.000000)
AftTractor1.SetNormalDischargeRate(1.000000)
AftTractor1.SetRechargeRate(0.300000)
AftTractor1.SetIndicatorIconNum(0)
AftTractor1.SetIndicatorIconPositionX(63)
AftTractor1.SetIndicatorIconPositionY(107)
AftTractor1Forward = App.TGPoint3()
AftTractor1Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractor1Up = App.TGPoint3()
AftTractor1Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor1.SetOrientation(AftTractor1Forward, AftTractor1Up)
AftTractor1.SetArcWidthAngles(-0.610865, 0.610865)
AftTractor1.SetArcHeightAngles(-1.745329, 0.000000)
AftTractor1.SetTractorBeamWidth(0.300000)
AftTractor1.SetTextureStart(0)
AftTractor1.SetTextureEnd(0)
AftTractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor1.SetInnerCoreColor(kColor)
AftTractor1.SetNumSides(12)
AftTractor1.SetMainRadius(0.075000)
AftTractor1.SetTaperRadius(0.000000)
AftTractor1.SetCoreScale(0.450000)
AftTractor1.SetTaperRatio(0.200000)
AftTractor1.SetTaperMinLength(1.000000)
AftTractor1.SetTaperMaxLength(5.000000)
AftTractor1.SetLengthTextureTilePerUnit(0.250000)
AftTractor1.SetPerimeterTile(1.000000)
AftTractor1.SetTextureSpeed(0.200000)
AftTractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTractor1)
#################################################
AftTractor2 = App.TractorBeamProperty_Create("Aft Tractor 2")
AftTractor2.SetMaxCondition(2356.0)
AftTractor2.SetCritical(0)
AftTractor2.SetTargetable(1)
AftTractor2.SetPrimary(1)
AftTractor2.SetPosition(1.900000, -6.400000, 2.100000)
AftTractor2.SetPosition2D(101.409629288, 42.0510428022)
AftTractor2.SetRepairComplexity(3.0)
AftTractor2.SetDisabledPercentage(0.75)
AftTractor2.SetRadius(0.500000)
AftTractor2.SetDumbfire(0)
AftTractor2.SetWeaponID(0)
AftTractor2.SetGroups(0)
AftTractor2.SetDamageRadiusFactor(0.300000)
AftTractor2.SetIconNum(0)
AftTractor2.SetIconPositionX(96)
AftTractor2.SetIconPositionY(107)
AftTractor2.SetIconAboveShip(1)
AftTractor2.SetFireSound("Tractor Beam")
AftTractor2.SetMaxCharge(5.000000)
AftTractor2.SetMaxDamage(24.0)
AftTractor2.SetMaxDamageDistance(100.0)
AftTractor2.SetMinFiringCharge(3.000000)
AftTractor2.SetNormalDischargeRate(1.000000)
AftTractor2.SetRechargeRate(0.300000)
AftTractor2.SetIndicatorIconNum(0)
AftTractor2.SetIndicatorIconPositionX(96)
AftTractor2.SetIndicatorIconPositionY(107)
AftTractor2Forward = App.TGPoint3()
AftTractor2Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractor2Up = App.TGPoint3()
AftTractor2Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor2.SetOrientation(AftTractor2Forward, AftTractor2Up)
AftTractor2.SetArcWidthAngles(-0.610865, 0.610865)
AftTractor2.SetArcHeightAngles(-1.919862, 0.000000)
AftTractor2.SetTractorBeamWidth(0.300000)
AftTractor2.SetTextureStart(0)
AftTractor2.SetTextureEnd(0)
AftTractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor2.SetInnerCoreColor(kColor)
AftTractor2.SetNumSides(12)
AftTractor2.SetMainRadius(0.075000)
AftTractor2.SetTaperRadius(0.000000)
AftTractor2.SetCoreScale(0.450000)
AftTractor2.SetTaperRatio(0.200000)
AftTractor2.SetTaperMinLength(1.000000)
AftTractor2.SetTaperMaxLength(5.000000)
AftTractor2.SetLengthTextureTilePerUnit(0.250000)
AftTractor2.SetPerimeterTile(1.000000)
AftTractor2.SetTextureSpeed(0.200000)
AftTractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTractor2)
#################################################
ForwardTractor1 = App.TractorBeamProperty_Create("Forward Tractor 1")
ForwardTractor1.SetMaxCondition(2356.0)
ForwardTractor1.SetCritical(0)
ForwardTractor1.SetTargetable(1)
ForwardTractor1.SetPrimary(1)
ForwardTractor1.SetPosition(-1.900000, 6.500000, 2.100000)
ForwardTractor1.SetPosition2D(26.5903707122, 99.4834054496)
ForwardTractor1.SetRepairComplexity(3.0)
ForwardTractor1.SetDisabledPercentage(0.75)
ForwardTractor1.SetRadius(0.500000)
ForwardTractor1.SetDumbfire(0)
ForwardTractor1.SetWeaponID(0)
ForwardTractor1.SetGroups(0)
ForwardTractor1.SetDamageRadiusFactor(0.300000)
ForwardTractor1.SetIconNum(0)
ForwardTractor1.SetIconPositionX(63)
ForwardTractor1.SetIconPositionY(16)
ForwardTractor1.SetIconAboveShip(1)
ForwardTractor1.SetFireSound("Tractor Beam")
ForwardTractor1.SetMaxCharge(5.000000)
ForwardTractor1.SetMaxDamage(24.0)
ForwardTractor1.SetMaxDamageDistance(100.0)
ForwardTractor1.SetMinFiringCharge(3.000000)
ForwardTractor1.SetNormalDischargeRate(1.000000)
ForwardTractor1.SetRechargeRate(0.300000)
ForwardTractor1.SetIndicatorIconNum(0)
ForwardTractor1.SetIndicatorIconPositionX(63)
ForwardTractor1.SetIndicatorIconPositionY(16)
ForwardTractor1Forward = App.TGPoint3()
ForwardTractor1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractor1Up = App.TGPoint3()
ForwardTractor1Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor1.SetOrientation(ForwardTractor1Forward, ForwardTractor1Up)
ForwardTractor1.SetArcWidthAngles(-0.610865, 0.610865)
ForwardTractor1.SetArcHeightAngles(-1.919862, 0.000000)
ForwardTractor1.SetTractorBeamWidth(0.300000)
ForwardTractor1.SetTextureStart(0)
ForwardTractor1.SetTextureEnd(0)
ForwardTractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor1.SetInnerCoreColor(kColor)
ForwardTractor1.SetNumSides(12)
ForwardTractor1.SetMainRadius(0.075000)
ForwardTractor1.SetTaperRadius(0.000000)
ForwardTractor1.SetCoreScale(0.450000)
ForwardTractor1.SetTaperRatio(0.200000)
ForwardTractor1.SetTaperMinLength(1.000000)
ForwardTractor1.SetTaperMaxLength(5.000000)
ForwardTractor1.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor1.SetPerimeterTile(1.000000)
ForwardTractor1.SetTextureSpeed(0.200000)
ForwardTractor1.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor1)
#################################################
ForwardTractor2 = App.TractorBeamProperty_Create("Forward Tractor 2")
ForwardTractor2.SetMaxCondition(2356.0)
ForwardTractor2.SetCritical(0)
ForwardTractor2.SetTargetable(1)
ForwardTractor2.SetPrimary(1)
ForwardTractor2.SetPosition(1.900000, 6.500000, 2.100000)
ForwardTractor2.SetPosition2D(101.409629288, 99.4834054496)
ForwardTractor2.SetRepairComplexity(3.0)
ForwardTractor2.SetDisabledPercentage(0.75)
ForwardTractor2.SetRadius(0.500000)
ForwardTractor2.SetDumbfire(0)
ForwardTractor2.SetWeaponID(0)
ForwardTractor2.SetGroups(0)
ForwardTractor2.SetDamageRadiusFactor(0.300000)
ForwardTractor2.SetIconNum(0)
ForwardTractor2.SetIconPositionX(96)
ForwardTractor2.SetIconPositionY(16)
ForwardTractor2.SetIconAboveShip(1)
ForwardTractor2.SetFireSound("Tractor Beam")
ForwardTractor2.SetMaxCharge(5.000000)
ForwardTractor2.SetMaxDamage(24.0)
ForwardTractor2.SetMaxDamageDistance(100.0)
ForwardTractor2.SetMinFiringCharge(3.000000)
ForwardTractor2.SetNormalDischargeRate(1.000000)
ForwardTractor2.SetRechargeRate(0.300000)
ForwardTractor2.SetIndicatorIconNum(0)
ForwardTractor2.SetIndicatorIconPositionX(96)
ForwardTractor2.SetIndicatorIconPositionY(16)
ForwardTractor2Forward = App.TGPoint3()
ForwardTractor2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractor2Up = App.TGPoint3()
ForwardTractor2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor2.SetOrientation(ForwardTractor2Forward, ForwardTractor2Up)
ForwardTractor2.SetArcWidthAngles(-0.610865, 0.610865)
ForwardTractor2.SetArcHeightAngles(-1.919862, 0.000000)
ForwardTractor2.SetTractorBeamWidth(0.300000)
ForwardTractor2.SetTextureStart(0)
ForwardTractor2.SetTextureEnd(0)
ForwardTractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor2.SetInnerCoreColor(kColor)
ForwardTractor2.SetNumSides(12)
ForwardTractor2.SetMainRadius(0.075000)
ForwardTractor2.SetTaperRadius(0.000000)
ForwardTractor2.SetCoreScale(0.450000)
ForwardTractor2.SetTaperRatio(0.200000)
ForwardTractor2.SetTaperMinLength(1.000000)
ForwardTractor2.SetTaperMaxLength(5.000000)
ForwardTractor2.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor2.SetPerimeterTile(1.000000)
ForwardTractor2.SetTextureSpeed(0.200000)
ForwardTractor2.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor2)
# Property load function.
DryDock = App.ShipProperty_Create("Dry Dock")
DryDock.SetGenus(2)
DryDock.SetSpecies(706)
DryDock.SetMass(440.0)
DryDock.SetRotationalInertia(225001.0)
DryDock.SetShipName("Dry Dock")
DryDock.SetModelFilename("data/Models/Bases/SpaceFacility/SpaceFacility.nif")
DryDock.SetDamageResolution(15.000000)
DryDock.SetAffiliation(0)
DryDock.SetStationary(1)
DryDock.SetAIString("StarbaseAttack")
DryDock.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(DryDock)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(33667.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 2.000000, 2.000000)
Engineering.SetPosition2D(64.0, 78.4163922482)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(5.000000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(38.4125)
Engineering.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(15551.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(1.800000, 3.000000, 2.300000)
SensorArray.SetPosition2D(99.4407014305, 86.4789716187)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(3.000000)
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
	prop = App.g_kModelPropertyManager.FindByName("Dry Dock", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
