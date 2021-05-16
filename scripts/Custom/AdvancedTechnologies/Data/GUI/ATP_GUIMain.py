import App
import MissionLib
import ATP_GUIUtils
import ATP_PowerDisplay
import ATP_WeaponsControl

FALSE=0
TRUE=1

DEBUG=FALSE

ET_CORBONITE_SET_ON=App.Game_GetNextEventType()
ET_CORBONITE_SET_RELOAD=App.Game_GetNextEventType()
ET_CORBONITE_DUMMY=App.Game_GetNextEventType()
ET_CORBONITE_SET_READY=App.Game_GetNextEventType()

def Initialise():
	#Reinitialise the GUI
	ATP_GUIUtils.InitGUIUtils()

	#Initialise the Corbonite
	ATP_WeaponsControl.Initialise()
	
def Setup():
	#Create GUI for weapons control
	ATP_WeaponsControl.Setup()
	
	#Create GUI for the engineering window
	ATP_PowerDisplay.Setup()


def CycleHandle(TGObject,pEvent):
	ATP_PowerDisplay.CycleHandle(TGObject,pEvent)

def CycleHandle4(TGObject,pEvent):
	ATP_PowerDisplay.CycleHandle4(TGObject,pEvent)	

	
