# D:\Games\FTB\scripts\ships\Hardpoints\ftb_kimal.py
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
Impulse = App.EngineProperty_Create("Impulse")
Impulse.SetMaxCondition(1170.0)
Impulse.SetCritical(0)
Impulse.SetTargetable(1)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, -0.280000, -0.017030)
Impulse.SetPosition2D(64.0, 64.0784726884)
Impulse.SetRepairComplexity(3.0)
Impulse.SetDisabledPercentage(0.5)
Impulse.SetRadius(0.060000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")
PortImpulse.SetMaxCondition(1301.0)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(0.398843, -0.008017, -0.004287)
PortImpulse.SetPosition2D(85.4277816253, 64.0007455742)
PortImpulse.SetRepairComplexity(3.0)
PortImpulse.SetDisabledPercentage(0.5)
PortImpulse.SetRadius(0.150000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")
StarImpulse.SetMaxCondition(1301.0)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(-0.398843, -0.008017, -0.004287)
StarImpulse.SetPosition2D(42.5722183747, 64.0007455742)
StarImpulse.SetRepairComplexity(3.0)
StarImpulse.SetDisabledPercentage(0.5)
StarImpulse.SetRadius(0.150000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
# Property load function.
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1198.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.400000, 0.700000, 0.020000)
ImpulseEngines.SetPosition2D(85.4899412804, 64.2254066647)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.080000)
ImpulseEngines.SetNormalPowerPerSecond(2157.36585366)
ImpulseEngines.SetMaxAccel(8.175)
ImpulseEngines.SetMaxAngularAccel(0.2)
ImpulseEngines.SetMaxAngularVelocity(0.333333333333)
ImpulseEngines.SetMaxSpeed(12.325)
ImpulseEngines.SetEngineSound('Cardassian Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
ForwardBeam = App.PhaserProperty_Create("Forward Spiral Wave")
ForwardBeam.SetMaxCondition(1227.0)
ForwardBeam.SetCritical(0)
ForwardBeam.SetTargetable(1)
ForwardBeam.SetPrimary(1)
ForwardBeam.SetPosition(0.000000, 0.726236, 0.002612)
ForwardBeam.SetPosition2D(64.0, 64.0300179835)
ForwardBeam.SetRepairComplexity(2.4)
ForwardBeam.SetDisabledPercentage(0.75)
ForwardBeam.SetRadius(0.100000)
ForwardBeam.SetDumbfire(0)
ForwardBeam.SetWeaponID(1)
ForwardBeam.SetGroups(1)
ForwardBeam.SetDamageRadiusFactor(0.1)
ForwardBeam.SetIconNum(364)
ForwardBeam.SetIconPositionX(66)
ForwardBeam.SetIconPositionY(34)
ForwardBeam.SetIconAboveShip(1)
ForwardBeam.SetFireSound('Galor Phaser')
ForwardBeam.SetMaxCharge(4.5)
ForwardBeam.SetMaxDamage(3000.0)
ForwardBeam.SetMaxDamageDistance(50.0)
ForwardBeam.SetMinFiringCharge(3.0)
ForwardBeam.SetNormalDischargeRate(1.0)
ForwardBeam.SetRechargeRate(0.223)
ForwardBeam.SetIndicatorIconNum(510)
ForwardBeam.SetIndicatorIconPositionX(59)
ForwardBeam.SetIndicatorIconPositionY(44)
ForwardBeamForward = App.TGPoint3()
ForwardBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardBeamUp = App.TGPoint3()
ForwardBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardBeam.SetOrientation(ForwardBeamForward, ForwardBeamUp)
ForwardBeam.SetWidth(0.001000)
ForwardBeam.SetLength(0.001000)
ForwardBeam.SetArcWidthAngles(-0.610865, 0.610865)
ForwardBeam.SetArcHeightAngles(-0.785398, 0.785398)
ForwardBeam.SetPhaserTextureStart(1)
ForwardBeam.SetPhaserTextureEnd(15)
ForwardBeam.SetPhaserWidth(0.5)
ForwardBeam.SetNumSides(6)
ForwardBeam.SetMainRadius(0.1)
ForwardBeam.SetTaperRadius(0.02)
ForwardBeam.SetCoreScale(0.6)
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
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1198.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.500000, -0.030000)
ShieldGenerator.SetPosition2D(64.0, 63.7731727051)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.080000)
ShieldGenerator.SetNormalPowerPerSecond(500.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 2500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 2500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 5000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 5000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 2500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 2500.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 4.67236467236)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 4.67236467236)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 4.67236467236)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 4.67236467236)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 4.67236467236)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 4.67236467236)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")
WarpCore.SetMaxCondition(1802.0)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, 0.300000, -0.036000)
WarpCore.SetPosition2D(64.0, 63.8438443241)
WarpCore.SetRepairComplexity(2.0)
WarpCore.SetDisabledPercentage(0.5)
WarpCore.SetRadius(0.100000)
WarpCore.SetMainBatteryLimit(675000.0)
WarpCore.SetBackupBatteryLimit(216000.0)
WarpCore.SetMainConduitCapacity(3240.0)
WarpCore.SetBackupConduitCapacity(1080.0)
WarpCore.SetPowerOutput(2700.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(5785.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.800000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ForwardTorpedo = App.TorpedoTubeProperty_Create("Forward Torpedo")
ForwardTorpedo.SetMaxCondition(1156.0)
ForwardTorpedo.SetCritical(0)
ForwardTorpedo.SetTargetable(1)
ForwardTorpedo.SetPrimary(1)
ForwardTorpedo.SetPosition(0.000000, 2.381510, 0.181090)
ForwardTorpedo.SetPosition2D(64.0, 71.169812812)
ForwardTorpedo.SetRepairComplexity(4.0)
ForwardTorpedo.SetDisabledPercentage(0.75)
ForwardTorpedo.SetRadius(0.050000)
ForwardTorpedo.SetDumbfire(1)
ForwardTorpedo.SetWeaponID(0)
ForwardTorpedo.SetGroups(2)
ForwardTorpedo.SetDamageRadiusFactor(0.17)
ForwardTorpedo.SetIconNum(370)
ForwardTorpedo.SetIconPositionX(77)
ForwardTorpedo.SetIconPositionY(18)
ForwardTorpedo.SetIconAboveShip(1)
ForwardTorpedo.SetImmediateDelay(0.25)
ForwardTorpedo.SetReloadDelay(40.0)
ForwardTorpedo.SetMaxReady(1)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.583860, 0.092391)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.600000, 0.007064)
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
ViewscreenLeftPosition.SetXYZ(-0.289760, 0.115103, -0.026938)
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
ViewscreenRightPosition.SetXYZ(0.289760, 0.115103, -0.026938)
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
ViewscreenUpPosition.SetXYZ(-0.002624, 0.063872, 0.064911)
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
ViewscreenDownPosition.SetXYZ(-0.002624, 0.063872, 0.064911)
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
#################################################
Compressors = App.WeaponSystemProperty_Create("Compressors")
Compressors.SetMaxCondition(1227.0)
Compressors.SetCritical(0)
Compressors.SetTargetable(0)
Compressors.SetPrimary(1)
Compressors.SetPosition(0.000000, 0.880000, 0.000000)
Compressors.SetPosition2D(64.0, 64.0)
Compressors.SetRepairComplexity(3.0)
Compressors.SetDisabledPercentage(0.5)
Compressors.SetRadius(0.100000)
Compressors.SetNormalPowerPerSecond(1433.0)
Compressors.SetWeaponSystemType(Compressors.WST_PHASER)
Compressors.SetSingleFire(1)
Compressors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Compressors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Compressors)
#################################################
Kimal = App.ShipProperty_Create("Kimal")
Kimal.SetGenus(1)
Kimal.SetSpecies(201)
Kimal.SetMass(14.0)
Kimal.SetRotationalInertia(7001.0)
Kimal.SetShipName("FTB_Kimal")
Kimal.SetModelFilename("Custom/FTB/Ships/FTBKimal/FTB_Kimal.nif")
Kimal.SetDamageResolution(10.000000)
Kimal.SetAffiliation(0)
Kimal.SetStationary(0)
Kimal.SetAIString("NonFedAttack")
Kimal.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Kimal)
#################################################
RepairSubsystem = App.RepairSubsystemProperty_Create("Repair Subsystem")
RepairSubsystem.SetMaxCondition(1129.0)
RepairSubsystem.SetCritical(0)
RepairSubsystem.SetTargetable(1)
RepairSubsystem.SetPrimary(1)
RepairSubsystem.SetPosition(0.000000, 0.034253, 0.050000)
RepairSubsystem.SetPosition2D(64.0, 64.05465717)
RepairSubsystem.SetRepairComplexity(2.0)
RepairSubsystem.SetDisabledPercentage(0.5)
RepairSubsystem.SetRadius(0.030000)
RepairSubsystem.SetNormalPowerPerSecond(1.0)
RepairSubsystem.SetMaxRepairPoints(0.78)
RepairSubsystem.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSubsystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(1718.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.360000, 0.010000)
SensorArray.SetPosition2D(64.0, 64.0579301442)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.040000)
SensorArray.SetNormalPowerPerSecond(1060.0)
SensorArray.SetBaseSensorRange(1950.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngine = App.WarpEngineProperty_Create("Warp Engine")
WarpEngine.SetMaxCondition(1198.0)
WarpEngine.SetCritical(0)
WarpEngine.SetTargetable(0)
WarpEngine.SetPrimary(1)
WarpEngine.SetPosition(0.000000, 0.200000, 0.020000)
WarpEngine.SetPosition2D(64.0, 64.0675588603)
WarpEngine.SetRepairComplexity(3.0)
WarpEngine.SetDisabledPercentage(0.5)
WarpEngine.SetRadius(0.080000)
WarpEngine.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngine)
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
	prop = App.g_kModelPropertyManager.FindByName("Compressors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Spiral Wave", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Subsystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Kimal", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
