#########################################################################################
#	ATP_GUIUtils									#
#########################################################################################
# Foundation made by Evan Light aka sleight42						#
# Expanded by Alexis Rombaut aka Apollo							#
#											#
#########################################################################################

import App
import MissionLib

FALSE=0
TRUE=1

DEBUG=FALSE

CountDownButtonDict={}
CountDownButtonCacheDict={}

StandardButtonDict={}

dropDownMenuDict={}

pCountDownTimer=None

ET_COUNT_DOWN_TIMER=App.Mission_GetNextEventType()
ET_DUMMY=App.Mission_GetNextEventType()


#########################################################################################
#	Original code made by sleight42							#
#########################################################################################
# GUIUtils										#
#											#
# by Evan Light aka sleight42								#
# All Rights Reserved									#
#											#
# <rant-mode>										#
# Man, I can't tell you just how much I hate learning new windowing toolkits!		#
# Who the fuck wants to learn fifty different ways of painting a window or		#
# button on-screen.  Just give me one clean API that I could use everywhere		#
# and I'd be OK with that.  But, no, nearly every damn developer out there		#
# has to write a new fucking windowing toolkit with a different API from		#
# every other windowing toolkit out there.  Just how many times do we have		#
# to reinvent this damn wheel???							#
# </rant-mode>										#
# 											#
# That's why I wrote this stupid module.  I'm going to forget everything that		#
# I ever learned about this windowing toolkit in short order.  As such, this		#
# module is going to become an aggregate of every little thing that I need		#
# to write more than once to muck around in the BC GUI.					#
#########################################################################################


def FindLowestChild( pane):
    index = pane.GetNumChildren() - 1
    iBottom = 0
    lowestChild = None
    current = None
    while index >= 0:
        current = pane.GetNthChild( index)
        currentBottom = current.GetBottom()
        if( currentBottom > iBottom):
            iBottom = currentBottom
            lowestChild = current
        index = index - 1
    return lowestChild

def GetScienceMenu():
    pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
    if(pDatabase is None):
        return 0
    return pTactCtrlWindow.FindMenu(pDatabase.GetString("Science"))

def FindButtonPosInMenu( menu, button):
    retval = 0
    currentButton = menu.GetFirstChild()
    while( currentButton != None):
        castButton = App.STButton_Cast( currentButton)
        if( castButton != None and castButton.this == button.this):
            break
        retval = retval + 1
        currentButton = menu.GetNextChild( currentButton)
    if( currentButton == None):
        retval = -1
    return retval

def GetNumChildrenThatCastTo( pane, cast):
    retval = 0
    current = pane.GetFirstChild()
    while( current != None):
        castVal = cast( current)
        if( castVal != None):
            retval = retval + 1
        current = pane.GetNextChild( current)
    return retval
    
def CreateIntButton( name, eventType, eventDest, intVal, tglDatabase = None):
    button = None
    event = App.TGIntEvent_Create()
    event.SetEventType( eventType)
    event.SetInt( intVal)
    event.SetDestination( eventDest)
    if( tglDatabase == None):
        button = App.STButton_Create( name, event)
    else:
        button = App.STButton_CreateW( tglDatabase.GetString( name), event)
    return button



#########################################################################################################################################
#	Expansion by Apollo														#
#########################################################################################################################################
# 	ATP_GUIUtils															#
#																	#
#  	These functions allow easy use of the GUI											#
#  	You can create a button in one line of code, view ATG_GUIMain for an implementation						#
#########################################################################################################################################

#########################################################################################################################################
# 	CreateDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name that you want to give your menu "Warp Speed"							#
#	Return: None															#
#																	#
#	Full Example: CreateDropDownMenu("Helm","Warp Speed")										#	
#																	#
#########################################################################################################################################
#########################################################################################################################################
#	Note on eventType & sFunctionHandler												#
#		__name__ is a Python variable representing your current module.								#
#		If you are working in eg. Scripts/Custom/ButtonTest/TesterFile.py, __name__ will be "Custom.ButonTest.TesterFile"	#
#		__name__+".Test" is then "Custom.ButonTest.TesterFile.Test"								#
#		The def Test(pObject,pEvent): in that file will be called when the event is activated					#
#########################################################################################################################################

def CreateDropDownMenu(menuName,dropDownMenuName):
	global dropDownMenuDict
		
	pMenu=GetMenu(menuName)

	if dropDownMenuDict.has_key((menuName,dropDownMenuName,"__Root__")):
		RemoveDropDownMenu(menuName,dropDownMenuName)	
	
       	dropDownMenu = App.STMenu_Create(dropDownMenuName)

	pMenu.AddChild(dropDownMenu)
       
        pLowest = FindLowestChild(pMenu)
	dropDownMenu.SetPosition( pLowest.GetLeft(), pLowest.GetBottom(), 0)

	pMenu.AddChild(None)

	dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")]=dropDownMenu,ET_DUMMY,"?"

#########################################################################################################################################
# 	CloseDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name of the menu eg "Warp Speed"									#
#	Return: None															#
#																	#
#	Full Example: CloseDropDownMenu("Helm","Warp Speed")										#	
#																	#
#########################################################################################################################################

def CloseDropDownMenu(menuName,dropDownMenuName):
	try:
		tuple=dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")]
	except:
		return

	tuple[0].Close()


#########################################################################################################################################
# 	RemoveDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		dropDownMenuName- name of menu button you want to delete button eg "Warp Speed"						#
#	Return: None															#
#																	#
#	Full Example: RemoveDropDownMenu("Science","Secondary Targets")									#
#																	#
#########################################################################################################################################

def RemoveDropDownMenu(menuName,dropDownMenuName):
	global dropDownMenuDict
	
	try:
		tuple=dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")]
	except:
		return

	dropDownMenu=tuple[0]

	for s in dropDownMenuDict.keys():
		if s[0]==menuName and s[1]==dropDownMenuName and s[2] !="__Root__":
			dropDownMenu.DeleteChild(dropDownMenuDict[s][0])
			App.g_kEventManager.RemoveBroadcastHandler(dropDownMenuDict[s][1],MissionLib.GetMission(),dropDownMenuDict[s][2])
			del dropDownMenuDict[s]			

	GetMenu(menuName).DeleteChild(dropDownMenu)
	del dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")]


#########################################################################################################################################
# 	AddButtonToDropDownMenu(eventType,sFunctionHandler,menuName,dropDownMenuName,buttonName)					#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name of the submenu eg "Warp Speed"									#
#		buttonName	  - name that you want to give your button eg "Warp 1"							#
#	Return: None															#
#																	#
#	Full Example: AddButtonToDropDownMenu(ET_WARP_1,__name__+".Warp1","Helm","Warp Speed","Warp 1")					#
#																	#
#########################################################################################################################################


def AddButtonToDropDownMenu(eventType,sFunctionHandler,menuName,dropDownMenuName,buttonName,setDisabled=FALSE,pHandler=None):
	global dropDownMenuDict
	
	App.g_kEventManager.RemoveBroadcastHandler(eventType,MissionLib.GetMission(),sFunctionHandler)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,MissionLib.GetMission(),sFunctionHandler)

	try:
		dropDownMenu=dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")][0]
	except:
		return

	if dropDownMenuDict.has_key((menuName,dropDownMenuName,buttonName)):
		pMenu.DeleteChild(dropDownMenuDict[(menuName,dropDownMenuName,buttonName)][0])
		del dropDownMenuDict[(menuName,dropDownMenuName,buttonName)]


	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eventType)
	pEvent.SetInt(0)
    
	if not pHandler:
		pHandler=dropDownMenu
	pButton=CreateIntButton(buttonName,eventType,MissionLib.GetMission() ,pHandler.GetObjID())   
	
	dropDownMenu.AddChild(pButton)
	pLowest = FindLowestChild(dropDownMenu)
	pButton.SetPosition( pLowest.GetLeft(), pLowest.GetBottom(), 0)
	dropDownMenu.AddChild(None)

	if setDisabled:
		pButton.SetDisabled()

	dropDownMenuDict[(menuName,dropDownMenuName,buttonName)]=pButton,eventType,sFunctionHandler



#########################################################################################################################################
# 	RemoveButtonFromDropDownMenu(menuName,dropDownMenuName,buttonName)								#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - the name of the submenu where your button is in eg "Warp Speed"					#
#		buttonName	  - name of the button you want to delete button eg "Warp 10"						#
#	Return: None															#
#																	#
#	Full Example: RemoveButtonFromDropDownMenu("Helm","Warp Speed","Warp 10")							#
#																	#
#########################################################################################################################################

def RemoveButtonFromDropDownMenu(menuName,dropDownMenuName,buttonName):
	global dropDownMenuDict
		
	try:
		tuple=dropDownMenuDict[(menuName,dropDownMenuName,buttonName)]
	except:
		return

	dropDownMenuDict[(menuName,dropDownMenuName,"__Root__")][0].DeleteChild(tuple[0])
	App.g_kEventManager.RemoveBroadcastHandler(tuple[1],MissionLib.GetMission(),tuple[2])

	del dropDownMenuDict[(menuName,dropDownMenuName,buttonName)]




#########################################################################################################################################
# 	CreateStandardButton(eventType,sFunctionHandler,menuName,buttonName)								#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		buttonName	  - name that you want to give your button eg "Test Button"						#
#	Return: None															#
#																	#
#	Full Example: CreateStandardButton(ET_CORBONITE_SET_ON,__name__+".SetCorboniteOn","Tactical","CR Ready")			#
#																	#
#########################################################################################################################################
#########################################################################################################################################
#	Note on eventType & sFunctionHandler												#
#		__name__ is a Python variable representing your current module.								#
#		If you are working in eg. Scripts/Custom/ButtonTest/TesterFile.py, __name__ will be "Custom.ButonTest.TesterFile"	#
#		__name__+".Test" is then "Custom.ButonTest.TesterFile.Test"								#
#		The def Test(pObject,pEvent): in that file will be called when the event is activated					#
#########################################################################################################################################

def CreateStandardButton(eventType,sFunctionHandler,menuName,buttonName,pHandler=None):
	global StandardButtonDict
		
	App.g_kEventManager.RemoveBroadcastHandler(eventType,MissionLib.GetMission(),sFunctionHandler)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,MissionLib.GetMission(),sFunctionHandler)

	pMenu=GetMenu(menuName)

	if StandardButtonDict.keys().count((menuName,buttonName))!=0:
		pMenu.DeleteChild(StandardButtonDict[(menuName,buttonName)][0])
		del StandardButtonDict[(menuName,buttonName)]	
	
	if not pHandler:
		pHandler=pMenu
	pButton=CreateIntButton(buttonName,eventType,MissionLib.GetMission() ,pHandler.GetObjID())  

        pMenu.AddChild(pButton)
        pLowest = FindLowestChild(pMenu)
	pButton.SetPosition( pLowest.GetLeft(), pLowest.GetBottom(), 0)
	pMenu.AddChild(None)

	StandardButtonDict[(menuName,buttonName)]=pButton,eventType,sFunctionHandler



#########################################################################################################################################
# 	RemoveStandardButton(menuName,buttonName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		buttonName	- name of the button you want to delete button eg "CR Ready"						#
#	Return: None															#
#																	#
#	Full Example: RemoveStandardButton("Tactical","CR Ready")									#
#																	#
#########################################################################################################################################

def RemoveStandardButton(menuName,buttonName):
	global StandardButtonDict
	
	try:
		tuple=StandardButtonDict[(menuName,buttonName)]
	except:
		return

	GetMenu(menuName).DeleteChild(tuple[0])
	
	App.g_kEventManager.RemoveBroadcastHandler(tuple[1],MissionLib.GetMission(),tuple[2])

	del StandardButtonDict[(menuName,buttonName)]



#########################################################################################################################################
# 	CreateCountDownButton(eventType1,sFunctionHandler1,eventType2,sFunctionHandler2,menuName,buttonName,counterStart)		#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		eventType2	  - global registered event; called when the time is up; eg. ET_Y=App.Mission_GetNextEventType()	#
# 		sFunctionHandler2 - name of the function; called when the time is up; eg. __name__ +".DoY"				#
#				  													#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		buttonName	  - name that you want to give your button eg "Test Button"						#
#		counterStart	  - the initial value of the timer, time is up when the counter has dropped to 0			#
#	Return: None															#
#																	#
#	Full Example: CreateCountDownButton(ET_STOP,__name__+".StopGoWarp",ET_WARP,__name__+".Warp","Helm","Warping in",5)		#
#																	#
#########################################################################################################################################
#########################################################################################################################################
#	Note on eventType & sFunctionHandler												#
#		__name__ is a Python variable representing your current module.								#
#		If you are working in eg. Scripts/Custom/ButtonTest/TesterFile.py, __name__ will be "Custom.ButonTest.TesterFile"	#
#		__name__+".Test" is then "Custom.ButonTest.TesterFile.Test"								#
#		The def Test(pObject,pEvent): in that file will be called when the event is activated					#
#########################################################################################################################################

def CreateCountDownButton(eventType1,sFunctionHandler1,eventType2,sFunctionHandler2,menuName,buttonName,counterStart,pHandler=None):
	global CountDownButtonDict
	global CountDownButtonCacheDict
	global pCountDownTimer
	
	App.g_kEventManager.RemoveBroadcastHandler(eventType1,MissionLib.GetMission(),sFunctionHandler1)
	App.g_kEventManager.RemoveBroadcastHandler(eventType2,MissionLib.GetMission(),sFunctionHandler2)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType1,MissionLib.GetMission(),sFunctionHandler1)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType2,MissionLib.GetMission(),sFunctionHandler2)

	pMenu=GetMenu(menuName)

	if CountDownButtonDict.keys().count((menuName,buttonName))!=0:
		pMenu.DeleteChild(CountDownButtonDict[(menuName,buttonName)][0])
		del CountDownButtonDict[(menuName,buttonName)]
		del CountDownButtonCacheDict[(menuName,buttonName)]
	
	
	buttonLabel = buttonName+" "+str(counterStart)

	if not pHandler:
		pHandler=pMenu		
        pButton = CreateIntButton(buttonLabel,eventType1,MissionLib.GetMission(),0)
        pMenu.AddChild(pButton)
        pLowest = FindLowestChild(pMenu)
	pButton.SetPosition(pLowest.GetLeft(),pLowest.GetBottom(),0)
	pMenu.AddChild(None)

	CountDownButtonDict[(menuName,buttonName)]=pButton,counterStart-1
	

	CountDownButtonCacheDict[(menuName,buttonName)]=eventType1,sFunctionHandler1,eventType2,sFunctionHandler2

	if pCountDownTimer==None:
		pCountDownTimer=MissionLib.CreateTimer(ET_COUNT_DOWN_TIMER,__name__ +".CycleCountDownHandle",App.g_kUtopiaModule.GetGameTime()+1.0,1.0,-1.0)



#########################################################################################################################################
# 	RemoveCountDownButton(menuName,buttonName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		buttonName	- name of the count down button you want to delete button eg "CR Ready"					#
#	Return: None															#
#																	#
#	Full Example: RemoveCountDownButton("Helm","Warping in")									#
#																	#
#########################################################################################################################################

def RemoveCountDownButton(menuName,buttonName):
	global CountDownButtonDict
	global CountDownButtonCacheDict
	global pCountDownTimer
	
	try:
		cachetuple=CountDownButtonCacheDict[(menuName,buttonName)]
	except:
		return

	GetMenu(menuName).DeleteChild(CountDownButtonDict[(menuName,buttonName)][0])
	
	App.g_kEventManager.RemoveBroadcastHandler(cachetuple[0],MissionLib.GetMission(),cachetuple[1])
	App.g_kEventManager.RemoveBroadcastHandler(cachetuple[2],MissionLib.GetMission(),cachetuple[3])

	del CountDownButtonDict[(menuName,buttonName)]
	del CountDownButtonCacheDict[(menuName,buttonName)]

	if len(CountDownButtonDict.keys())==0:
		if pCountDownTimer:
			App.g_kTimerManager.DeleteTimer(pCountDownTimer.GetObjID())
			pCountDownTimer=None
		
	

def MutateButton(menuName,buttonName,newButtonName,eventType,sFunctionHandler,pHandler=None):
	
	if StandardButtonDict.has_key((menuName,buttonName)):
		tuple=StandardButtonDict[(menuName,buttonName)]
		pButton=tuple[0]
		
		if not pHandler:
			pHandler=pButton

		if pButton:
			## Change the name
			S = App.TGString()
			S.SetString(newButtonName[:])
			pButton.SetName(S)
			
			## New event
			event = pButton.GetActivationEvent()
			event = App.TGIntEvent_Cast(event)
   			event.SetEventType( eventType)
			event.SetInt(pHandler.GetObjID())
			event.SetDestination(pButton)
			pButton.SetActivationEvent(event)

			## New handlers
			App.g_kEventManager.RemoveBroadcastHandler(tuple[1],MissionLib.GetMission(),tuple[2])
			App.g_kEventManager.RemoveBroadcastHandler(eventType,MissionLib.GetMission(),sFunctionHandler)
			App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType,MissionLib.GetMission(),sFunctionHandler)

			## New cache
			del StandardButtonDict[(menuName,buttonName)]
			StandardButtonDict[(menuName,newButtonName)]=pButton,eventType,sFunctionHandler
			
						
def GetButton(menuName,buttonName):	
	if StandardButtonDict.has_key((menuName,buttonName)):
		return StandardButtonDict[(menuName,buttonName)][0]
	elif CountDownButtonDict.has_key((menuName,buttonName)):
		return CountDownButtonDict[(menuName,buttonName)][0]

def GetMenu(menuName):
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

#########################################################################################
# 	Innerfunctions, no need to call them						#
#											#
# 											#
#########################################################################################

def CycleCountDownHandle(pObject,pEvent):

	from Custom.AdvancedTechnologies.Data import QuickBattleAddon
	global CountDownButtonDict
	global CountDownButtonCacheDict

	for s in CountDownButtonDict.keys():
		tuple=CountDownButtonDict[s]
		
		if tuple[1]>0:			

			pMenu=GetMenu(s[0])
		
			pMenu.DeleteChild(tuple[0])
			
			buttonLabel =s[1]+" "+str(tuple[1])

       			pButton = CreateIntButton(buttonLabel,CountDownButtonCacheDict[s][0],MissionLib.GetMission(),0)
			pMenu.AddChild(pButton)
			pLowest = FindLowestChild(pMenu)
			pButton.SetPosition( pLowest.GetLeft(), pLowest.GetBottom(), 0)
			pMenu.AddChild(None)

			CountDownButtonDict[s]=pButton,tuple[1]-1
		
		else:
			callEvent(CountDownButtonCacheDict[s][2])

				
			

def callEvent(eventType,pInt=0,pSource=None,pDestination=None):
	pEvent = App.TGIntEvent_Create()
	pEvent.SetInt(pInt)
	pEvent.SetEventType(eventType)
	pEvent.SetDestination(pDestination)
	pEvent.SetSource(pSource)	
	MissionLib.GetMission().ProcessEvent(pEvent)


def InitGUIUtils():
	global CountDownButtonDict
	global CountDownButtonCacheDict
	global StandardButtonDict
	global dropDownMenuDict
	global pCountDownTimer

	for s in CountDownButtonDict.keys():
		RemoveCountDownButton(s[0],s[1])
	for t in StandardButtonDict.keys():
		RemoveStandardButton(t[0],t[1])
	for u in dropDownMenuDict.keys():
		if u[2]!="__Root__":
			RemoveButtonFromDropDownMenu(u[0],u[1],u[2])
	for v in dropDownMenuDict.keys():
		if v[2]=="__Root__":
			RemoveDropDownMenu(v[0],v[1])

	StandardButtonDict={}
	CountDownButtonDict={}
	CountDownButtonCacheDict={}
	dropDownMenuDict={}
	
	if pCountDownTimer:
		App.g_kTimerManager.DeleteTimer(pCountDownTimer.GetObjID())
	pCountDownTimer=None
		
		
