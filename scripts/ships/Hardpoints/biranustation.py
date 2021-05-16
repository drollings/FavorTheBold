# C:\Utopia\Current\Build\scripts\ships\Hardpoints\biranustation.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.spacefacility"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.spacefacility", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")
Hull.SetMaxCondition(140555.0)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.500000)
Hull.SetPosition2D(64.0, 64.9795101837)
Hull.SetRepairComplexity(3.0)
Hull.SetDisabledPercentage(0.0)
Hull.SetRadius(11.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")
Engineering.SetMaxCondition(3875.0)
Engineering.SetCritical(0)
Engineering.SetTargetable(1)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 4.000000)
Engineering.SetPosition2D(64.0, 126.688651756)
Engineering.SetRepairComplexity(2.0)
Engineering.SetDisabledPercentage(0.5)
Engineering.SetRadius(1.000000)
Engineering.SetNormalPowerPerSecond(1.0)
Engineering.SetMaxRepairPoints(38.4125)
Engineering.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
# Property load function.
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
ShieldGenerator.SetMaxCondition(8383.0)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, -0.200000)
ShieldGenerator.SetPosition2D(64.0, 64.1567216294)
ShieldGenerator.SetRepairComplexity(2.0)
ShieldGenerator.SetDisabledPercentage(0.5)
ShieldGenerator.SetRadius(2.000000)
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
def LoadPropertySet(pObj):

	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
