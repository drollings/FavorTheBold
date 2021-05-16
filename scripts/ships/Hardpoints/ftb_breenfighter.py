# D:\Games\FTB\scripts\ships\Hardpoints\ftb_breenfighter.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")
PortWarp.SetMaxCondition(1312.0)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.400000, -0.200000, -0.025000)
PortWarp.SetPosition2D(-63.680798005, 67.029831904)
PortWarp.SetRepairComplexity(3.0)
PortWarp.SetDisabledPercentage(0.5)
PortWarp.SetRadius(0.150000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")
StarWarp.SetMaxCondition(1237.0)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.000000, -0.425000, -0.022500)
StarWarp.SetPosition2D(64.0, 69.5257865312)
StarWarp.SetRepairComplexity(3.0)
StarWarp.SetDisabledPercentage(0.5)
StarWarp.SetRadius(0.100000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
ImpulseDrive = App.EngineProperty_Create("Impulse Drive")
ImpulseDrive.SetMaxCondition(1166.0)
ImpulseDrive.SetCritical(0)
ImpulseDrive.SetTargetable(1)
ImpulseDrive.SetPrimary(1)
ImpulseDrive.SetPosition(0.000000, -0.500000, -0.022500)
ImpulseDrive.SetPosition2D(64.0, 70.466079191)
ImpulseDrive.SetRepairComplexity(3.0)
ImpulseDrive.SetDisabledPercentage(0.5)
ImpulseDrive.SetRadius(0.050000)
ImpulseDrive.SetEngineType(ImpulseDrive.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseDrive)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
ImpulseEngines.SetMaxCondition(1112.0)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.026495, -0.117500, -0.006000)
ImpulseEngines.SetPosition2D(72.4572568579, 64.4068750816)
ImpulseEngines.SetRepairComplexity(3.0)
ImpulseEngines.SetDisabledPercentage(0.5)
ImpulseEngines.SetRadius(0.010000)
ImpulseEngines.SetNormalPowerPerSecond(5400.08429268)
ImpulseEngines.SetMaxAccel(8.175)
ImpulseEngines.SetMaxAngularAccel(0.75)
ImpulseEngines.SetMaxAngularVelocity(1.25)
ImpulseEngines.SetMaxSpeed(13.2)
ImpulseEngines.SetEngineSound('Federation Engines')
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
DisruptorBeam1 = App.PhaserProperty_Create("Disruptor Beam 1")
DisruptorBeam1.SetMaxCondition(1297.0)
DisruptorBeam1.SetCritical(0)
DisruptorBeam1.SetTargetable(1)
DisruptorBeam1.SetPrimary(1)
DisruptorBeam1.SetPosition(0.049769, 0.380460, 0.000204)
DisruptorBeam1.SetPosition2D(79.8863640898, 64.0432634761)
DisruptorBeam1.SetRepairComplexity(4.0)
DisruptorBeam1.SetDisabledPercentage(0.75)
DisruptorBeam1.SetRadius(0.140000)
DisruptorBeam1.SetDumbfire(0)
DisruptorBeam1.SetWeaponID(0)
DisruptorBeam1.SetGroups(0)
DisruptorBeam1.SetDamageRadiusFactor(0.100000)
DisruptorBeam1.SetIconNum(365)
DisruptorBeam1.SetIconPositionX(85)
DisruptorBeam1.SetIconPositionY(33)
DisruptorBeam1.SetIconAboveShip(1)
DisruptorBeam1.SetFireSound('FTB Breen Phaser')
DisruptorBeam1.SetMaxCharge(1.5)
DisruptorBeam1.SetMaxDamage(2000.0)
DisruptorBeam1.SetMaxDamageDistance(20.0)
DisruptorBeam1.SetMinFiringCharge(0.75)
DisruptorBeam1.SetNormalDischargeRate(1.0)
DisruptorBeam1.SetRechargeRate(0.05)
DisruptorBeam1.SetIndicatorIconNum(512)
DisruptorBeam1.SetIndicatorIconPositionX(67)
DisruptorBeam1.SetIndicatorIconPositionY(30)
DisruptorBeam1Forward = App.TGPoint3()
DisruptorBeam1Forward.SetXYZ(-0.017452, 0.933438, 0.358313)
DisruptorBeam1Up = App.TGPoint3()
DisruptorBeam1Up.SetXYZ(0.000000, -0.358368, 0.933580)
DisruptorBeam1.SetOrientation(DisruptorBeam1Forward, DisruptorBeam1Up)
DisruptorBeam1.SetWidth(0.001000)
DisruptorBeam1.SetLength(0.001000)
DisruptorBeam1.SetArcWidthAngles(-0.523599, 0.349066)
DisruptorBeam1.SetArcHeightAngles(-0.349066, 0.349066)
DisruptorBeam1.SetPhaserTextureStart(0)
DisruptorBeam1.SetPhaserTextureEnd(7)
DisruptorBeam1.SetPhaserWidth(0.3)
DisruptorBeam1.SetNumSides(6)
DisruptorBeam1.SetMainRadius(0.075)
DisruptorBeam1.SetTaperRadius(0.03)
DisruptorBeam1.SetCoreScale(0.2)
DisruptorBeam1.SetTaperRatio(0.25)
DisruptorBeam1.SetTaperMinLength(5.0)
DisruptorBeam1.SetTaperMaxLength(30.0)
DisruptorBeam1.SetLengthTextureTilePerUnit(0.1)
DisruptorBeam1.SetPerimeterTile(1.0)
DisruptorBeam1.SetTextureSpeed(2.5)
DisruptorBeam1.SetTextureName('Custom/FTB/textures/Tactical/Firesaber_PulseBeam.tga')
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.721569, 0.039216, 1.000000)
DisruptorBeam1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.721569, 0.039216, 1.000000)
DisruptorBeam1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.513726, 1.000000, 0.501961, 1.000000)
DisruptorBeam1.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
DisruptorBeam1.SetInnerCoreColor(kColor)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorBeam1)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(1166.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.185000, 0.040000)
ShieldGenerator.SetPosition2D(64.0, 60.5007182791)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(0.050000)
ShieldGenerator.SetNormalPowerPerSecond(100.0)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.564706, 0.831373, 0.737255, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.1)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 1000.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 500.0)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 500.0)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.959985014868)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.959985014868)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.959985014868)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.959985014868)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.959985014868)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.959985014868)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")
PowerPlant.SetMaxCondition(1746.0)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(-0.100000, -0.125000, -0.005000)
PowerPlant.SetPosition2D(32.0798004988, 64.3580077238)
PowerPlant.SetRepairComplexity(2.0)
PowerPlant.SetDisabledPercentage(0.5)
PowerPlant.SetRadius(0.050000)
PowerPlant.SetMainBatteryLimit(1200000.0)
PowerPlant.SetBackupBatteryLimit(384000.0)
PowerPlant.SetMainConduitCapacity(5760.0)
PowerPlant.SetBackupConduitCapacity(1920.0)
PowerPlant.SetPowerOutput(4800.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")
CloakingDevice.SetMaxCondition(1208.0)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(1)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(-0.213140, -0.968785, 0.094872)
CloakingDevice.SetPosition2D(-4.03471321696, 16.297165805)
CloakingDevice.SetRepairComplexity(3.0)
CloakingDevice.SetDisabledPercentage(0.5)
CloakingDevice.SetRadius(0.080000)
CloakingDevice.SetNormalPowerPerSecond(30.000008)
CloakingDevice.SetCloakStrength(90.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(4722.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.0, 64.0)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(0.300000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Cockpit = App.HullProperty_Create("Cockpit")
Cockpit.SetMaxCondition(1139.0)
Cockpit.SetCritical(0)
Cockpit.SetTargetable(0)
Cockpit.SetPrimary(0)
Cockpit.SetPosition(0.000000, 0.300000, 0.020000)
Cockpit.SetPosition2D(64.0, 67.4992817209)
Cockpit.SetRepairComplexity(3.0)
Cockpit.SetDisabledPercentage(0.5)
Cockpit.SetRadius(0.030000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)
#################################################
ForwardTorpedo = App.TorpedoTubeProperty_Create("Forward Torpedo")
ForwardTorpedo.SetMaxCondition(1392.0)
ForwardTorpedo.SetCritical(0)
ForwardTorpedo.SetTargetable(1)
ForwardTorpedo.SetPrimary(1)
ForwardTorpedo.SetPosition(-0.371729, 0.259356, -0.022148)
ForwardTorpedo.SetPosition2D(-54.656638404, 60.990593785)
ForwardTorpedo.SetRepairComplexity(4.0)
ForwardTorpedo.SetDisabledPercentage(0.75)
ForwardTorpedo.SetRadius(0.200000)
ForwardTorpedo.SetDumbfire(1)
ForwardTorpedo.SetWeaponID(0)
ForwardTorpedo.SetGroups(1)
ForwardTorpedo.SetDamageRadiusFactor(0.17)
ForwardTorpedo.SetIconNum(370)
ForwardTorpedo.SetIconPositionX(18)
ForwardTorpedo.SetIconPositionY(39)
ForwardTorpedo.SetIconAboveShip(0)
ForwardTorpedo.SetImmediateDelay(0.25)
ForwardTorpedo.SetReloadDelay(15.0)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.400000, 0.030000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.400000, 0.030000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 0.400000, 0.030000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.600000, 0.002736)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.100000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.050000, -0.100000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.400000, 0.030000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
DisruptorBeams = App.WeaponSystemProperty_Create("Disruptor Beams")
DisruptorBeams.SetMaxCondition(1112.0)
DisruptorBeams.SetCritical(0)
DisruptorBeams.SetTargetable(0)
DisruptorBeams.SetPrimary(1)
DisruptorBeams.SetPosition(-0.060648, 0.060143, -0.004520)
DisruptorBeams.SetPosition2D(44.6410374065, 63.8564931862)
DisruptorBeams.SetRepairComplexity(3.0)
DisruptorBeams.SetDisabledPercentage(0.5)
DisruptorBeams.SetRadius(0.010000)
DisruptorBeams.SetNormalPowerPerSecond(300.0)
DisruptorBeams.SetWeaponSystemType(DisruptorBeams.WST_PHASER)
DisruptorBeams.SetSingleFire(1)
DisruptorBeams.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorBeams.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorBeams)
#################################################
BreenFighter = App.ShipProperty_Create("BreenFighter")
BreenFighter.SetGenus(1)
BreenFighter.SetSpecies(301)
BreenFighter.SetMass(1.0)
BreenFighter.SetRotationalInertia(5.0)
BreenFighter.SetShipName("FTB_BreenFighter")
BreenFighter.SetModelFilename("data/Models/Ships/Warbird.nif")
BreenFighter.SetDamageResolution(12.000000)
BreenFighter.SetAffiliation(0)
BreenFighter.SetStationary(0)
BreenFighter.SetAIString("NonFedAttack")
BreenFighter.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(BreenFighter)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(1125.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.026000, -0.026293, 0.008602)
Engineering.SetPosition2D(72.2992518703, 63.902835699)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(0.020000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(0.0)
Engineering.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")
SensorArray.SetMaxCondition(1712.0)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.400000, -0.010000)
SensorArray.SetPosition2D(64.0, 61.8101628721)
SensorArray.SetRepairComplexity(0.5)
SensorArray.SetDisabledPercentage(0.4)
SensorArray.SetRadius(0.025000)
SensorArray.SetNormalPowerPerSecond(960.0)
SensorArray.SetBaseSensorRange(1200.0)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
WarpEngines.SetMaxCondition(1132.0)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(-0.057857, -0.081576, -0.000907)
WarpEngines.SetPosition2D(45.5319301746, 64.0415485579)
WarpEngines.SetRepairComplexity(3.0)
WarpEngines.SetDisabledPercentage(0.5)
WarpEngines.SetRadius(0.025000)
WarpEngines.SetNormalPowerPerSecond(0.0)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
Torpedoes.SetMaxCondition(1102.0)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.0, 64.0)
Torpedoes.SetRepairComplexity(3.0)
Torpedoes.SetDisabledPercentage(0.5)
Torpedoes.SetRadius(0.002)
Torpedoes.SetNormalPowerPerSecond(300.0)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 50)
Torpedoes.SetTorpedoScript(0, "ftb.Projectiles.FTBBreenTorpedo")
Torpedoes.SetMaxTorpedoes(1, 1)
Torpedoes.SetTorpedoScript(1, "ftb.Projectiles.FTBBreenDamper")
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
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Beams", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cockpit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BreenFighter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Impulse Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Beam 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)