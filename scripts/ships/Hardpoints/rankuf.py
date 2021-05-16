# D:\Games\FTB\scripts\ships\Hardpoints\FTB_Kvort.py
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
ShuttleBayOEP = App.ObjectEmitterProperty_Create("Shuttle Bay OEP")

ShuttleBayOEPForward = App.TGPoint3()
ShuttleBayOEPForward.SetXYZ(0.000000, -0.104826, -0.994491)
ShuttleBayOEPUp = App.TGPoint3()
ShuttleBayOEPUp.SetXYZ(0.183299, -0.977641, 0.103050)
ShuttleBayOEPRight = App.TGPoint3()
ShuttleBayOEPRight.SetXYZ(0.983057, 0.182289, -0.019215)
ShuttleBayOEP.SetOrientation(ShuttleBayOEPForward, ShuttleBayOEPUp, ShuttleBayOEPRight)
ShuttleBayOEPPosition = App.TGPoint3()
ShuttleBayOEPPosition.SetXYZ(0.000000, -0.797262, -0.231012)
ShuttleBayOEP.SetPosition(ShuttleBayOEPPosition)
ShuttleBayOEP.SetEmittedObjectType(ShuttleBayOEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBayOEP)
#################################################
ImpulseEngine = App.EngineProperty_Create("Impulse Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngine)
PortWarp = App.EngineProperty_Create("Port Warp")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
StarWarp = App.EngineProperty_Create("Star Warp")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
PortMk12Disruptor1 = App.PulseWeaponProperty_Create("Port Mk12 Disruptor 1")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortMk12Disruptor1)
StarMk12Disruptor1 = App.PulseWeaponProperty_Create("Star Mk12 Disruptor 1")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarMk12Disruptor1)
PortMk12Disruptor2 = App.PulseWeaponProperty_Create("Port Mk12 Disruptor 2")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortMk12Disruptor2)
StarMk12Disruptor2 = App.PulseWeaponProperty_Create("Star Mk12 Disruptor 2")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarMk12Disruptor2)
FwdMk6Disruptor1 = App.PulseWeaponProperty_Create("Fwd Mk6 Disruptor 1")
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdMk6Disruptor1)
FwdMk6Disruptor2 = App.PulseWeaponProperty_Create("Fwd Mk6 Disruptor 2")
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdMk6Disruptor2)
AftMk6Disruptor2 = App.PulseWeaponProperty_Create("Aft Mk6 Disruptor 2")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftMk6Disruptor2)
AftMk6Disruptor1 = App.PulseWeaponProperty_Create("Aft Mk6 Disruptor 1")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftMk6Disruptor1)
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
WarpCore = App.PowerProperty_Create("Warp Core")
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
Hull = App.HullProperty_Create("Hull")
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
ShuttleBay = App.HullProperty_Create("Shuttle Bay")
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)
FwdTorpedo = App.TorpedoTubeProperty_Create("Fwd Torpedo")
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo)
AftTorpedo = App.TorpedoTubeProperty_Create("Aft Torpedo")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTorpedo)
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, 1.672070, -0.015718)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.968174, 0.099023)
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
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
Kvort = App.ShipProperty_Create("Kvort")
App.g_kModelPropertyManager.RegisterLocalTemplate(Kvort)
Engineering = App.RepairSubsystemProperty_Create("Engineering")
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
SensorArray = App.SensorProperty_Create("Sensor Array")
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")
Torpedoes.SetMaxCondition(1748.0)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.0, 64.0)
Torpedoes.SetRepairComplexity(3.0)
Torpedoes.SetDisabledPercentage(0.5)
Torpedoes.SetRadius(0.002)
Torpedoes.SetNormalPowerPerSecond(670.0)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 85)
Torpedoes.SetTorpedoScript(0, "ftb.Projectiles.FTBKlingonTorpedo")
Torpedoes.SetMaxTorpedoes(1, 150)
Torpedoes.SetTorpedoScript(1, "ftb.Projectiles.FTBFastKlingonTorpedo")
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
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Kvort", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Port Mk12 Disruptor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Mk12 Disruptor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Mk12 Disruptor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Mk12 Disruptor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Mk6 Disruptor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Mk6 Disruptor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Mk6 Disruptor 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Mk6 Disruptor 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
