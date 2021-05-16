# C:\Utopia\Current\Build\scripts\ships\Hardpoints\matankeldon.py
# This file was automatically generated - modify at your own risk.
#

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.keldon"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.keldon", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
Hull = App.HullProperty_Create("Hull")
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
RepairSubsystem = App.RepairSubsystemProperty_Create("Repair Subsystem")
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSubsystem)
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
WarpCore = App.PowerProperty_Create("Warp Core")
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
def LoadPropertySet(pObj):

	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Subsystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
