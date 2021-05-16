import App
import MissionLib

ET_CORBONITE_SET_OFF    = App.Mission_GetNextEventType()
ET_CORBONITE_SET_ON	= App.Mission_GetNextEventType()
ET_DUMMY                = App.Mission_GetNextEventType()

INTERFACE_PANE	= 0
WEAPONS_CONTROL	= 8

w=App.globals.DEFAULT_ST_INDENT_HORIZ
h=App.globals.DEFAULT_ST_INDENT_VERT

pButton=None
unset=None

def Initialise():
	global pButton
	global pIcon

	if pButton:
		pTacCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		kInterfacePane = App.TGPane_Cast(pTacCtrlWindow.GetNthChild(INTERFACE_PANE))
		pControl = App.TGPane_Cast(kInterfacePane.GetNthChild(WEAPONS_CONTROL))

		pControl.Resize(unset[0],unset[1],0)
		pControl.SetPosition(unset[2],unset[3],0)
		pControl.DeleteChild(pButton)

		pControl.Layout()
		pTacCtrlWindow.Layout()
	
		#Update the eventhandlers
		pMission=MissionLib.GetMission()
		pMission.RemoveHandlerForInstance(ET_CORBONITE_SET_OFF,__name__+".CorboniteSetOff")
		pMission.RemoveHandlerForInstance(ET_CORBONITE_SET_ON,__name__+".CorboniteSetOn")

		pButton=None	
	

def Setup():
	global unset
	global pButton
	global pIcon

	from Custom.AdvancedTechnologies.Data import QuickBattleAddon 
	if not QuickBattleAddon.IsPlayerCorbonite():
		#Nothing to do
		return
	
	pTacCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pControl = pTacCtrlWindow.GetWeaponsControl()
	pWeaponDisplay=pTacCtrlWindow.GetWeaponsDisplay()

	pLast=App.TGPane_Cast(pControl.GetLastChild())
	pToggle=App.TGPane_Cast(pControl.GetTorpTypeToggle())
	if not pLast or pButton:
		return

	#Maintain the state for a clean setback:
	unset=pControl.GetWidth(),pControl.GetHeight(),pControl.GetLeft(),pControl.GetTop()

	#Create the button and the button
	pMission=MissionLib.GetMission()
	pButton=CreateButton("Dummy",ET_DUMMY,pMission,0)
	pControl.AddChild(pButton,0.0,0.0,0)

	#Model the button
	pButton.Resize(pToggle.GetWidth(),pToggle.GetHeight(),0)
	pButton.SetPosition(pToggle.GetLeft(),pLast.GetBottom()+h)
	pButton.SetHighlightedColor(App.g_kMainMenuButton3HighlightedColor)
	
	#Resize the windows
	if pButton.GetBottom()>pControl.GetHeight():
		pControl.SetPosition(pControl.GetLeft(),pControl.GetTop()-(pButton.GetBottom()+h-pControl.GetHeight()),0)
		pControl.Resize(pButton.GetBottom()+h,pControl.GetWidth())
		pControl.Layout()
		pTacCtrlWindow.Layout()

	#Add one to the weapons display
	pIcon = App.TGIcon_Create("DamageIcons",5)
	pIcon.SetColor(App.g_kEngineeringWarpCoreColor)
	pWeaponDisplay.AddChild(pIcon,0.5*(pWeaponDisplay.GetWidth()-pIcon.GetWidth()),0.1*pWeaponDisplay.GetHeight(),0)


	#Make it default Off
	CorboniteSetOffNoArg()

def CorboniteSetOff(pMission,pObject):
	CorboniteSetOffNoArg()

def CorboniteSetOffNoArg():
	pTacCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	kInterfacePane = App.TGPane_Cast(pTacCtrlWindow.GetNthChild(INTERFACE_PANE))
	pControl = App.TGPane_Cast(kInterfacePane.GetNthChild(WEAPONS_CONTROL))

	if not pButton:
		return

	#Update the eventhandlers
	pMission=MissionLib.GetMission()
	pMission.RemoveHandlerForInstance(ET_CORBONITE_SET_OFF,__name__+".CorboniteSetOff")
	pMission.AddPythonFuncHandlerForInstance(ET_CORBONITE_SET_ON,__name__+".CorboniteSetOn")

	#Reset the button
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(ET_CORBONITE_SET_ON)
	pEvent.SetInt(0)
	pEvent.SetDestination(pMission)
	pString=App.TGString()
	pString.SetString("Corbonite Off  ")
	pButton.SetName(pString)
	pButton.SetActivationEvent(pEvent)

	#pIcon
	pIcon.SetNotVisible()

def CorboniteSetOn(pMission,pObject):
	CorboniteSetOnNoArg()

def CorboniteSetOnNoArg():
	pTacCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pControl = pTacCtrlWindow.GetWeaponsControl()
	pWeaponDisplay=pTacCtrlWindow.GetWeaponsDisplay()

	if not pButton:
		return

	#Update the eventhandlers
	pMission=MissionLib.GetMission()
	pMission.RemoveHandlerForInstance(ET_CORBONITE_SET_ON,__name__+".CorboniteSetOn")
	pMission.AddPythonFuncHandlerForInstance(ET_CORBONITE_SET_OFF,__name__+".CorboniteSetOff")

	#Reset the button
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(ET_CORBONITE_SET_OFF)
	pEvent.SetInt(0)
	pEvent.SetDestination(pMission)
	pString=App.TGString()
	pString.SetString("Corbonite On   ")
	pButton.SetName(pString)
	pButton.SetActivationEvent(pEvent)

	#pIcon
	pIcon.SetVisible()

	

	
def GetOffEvent():
	return ET_CORBONITE_SET_OFF

def GetOnEvent():
	return ET_CORBONITE_SET_ON


def CreateButton(pName,eventType,eventDest,intVal):
	button = None
	event = App.TGIntEvent_Create()
	event.SetEventType(eventType)
	event.SetInt(intVal)
	event.SetDestination(eventDest)
	button=App.STRoundedButton_Create(pName,event,1.0,1.0)
	return button