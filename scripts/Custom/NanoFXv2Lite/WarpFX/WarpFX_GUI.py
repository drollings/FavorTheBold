import App

try:
	from Custom.AdvancedTechnologies.Data import ATP_Lib
except:
	ERROR = "No ATP3"
		
TRUE=1
FALSE=0

DEBUG=FALSE

ET_WARP_1=App.Mission_GetNextEventType()
ET_WARP_2=App.Mission_GetNextEventType()
ET_WARP_3=App.Mission_GetNextEventType()
ET_WARP_4=App.Mission_GetNextEventType()
ET_WARP_5=App.Mission_GetNextEventType()
ET_WARP_6=App.Mission_GetNextEventType()
ET_WARP_7=App.Mission_GetNextEventType()
ET_WARP_8=App.Mission_GetNextEventType()
ET_WARP_9=App.Mission_GetNextEventType()

WarpSpeed=9

def SetupWarpSpeedButtons(iMaxWarp = 9):
	if DEBUG:
		print "Setting up the Warp Speed Menu"	
	try:
		from Custom.AdvancedTechnologies.Data import ATP_Lib
	except:
		ERROR = "No ATP3"
		return
	### Create a drop down menu called "Warp Speed" at Kiska ###
	ATP_Lib.CreateDropDownMenu("Helm","Warp Speed")

	### Create the nine warp speed buttons in it ###
	if (iMaxWarp >= 1):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_1,__name__+".Warp1","Helm","Warp Speed","Warp 1")	
	if (iMaxWarp >= 2):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_2,__name__+".Warp2","Helm","Warp Speed","Warp 2")
	if (iMaxWarp >= 3):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_3,__name__+".Warp3","Helm","Warp Speed","Warp 3")
	if (iMaxWarp >= 4):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_4,__name__+".Warp4","Helm","Warp Speed","Warp 4")
	if (iMaxWarp >= 5):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_5,__name__+".Warp5","Helm","Warp Speed","Warp 5")	
	if (iMaxWarp >= 6):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_6,__name__+".Warp6","Helm","Warp Speed","Warp 6")
	if (iMaxWarp >= 7):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_7,__name__+".Warp7","Helm","Warp Speed","Warp 7")
	if (iMaxWarp >= 8):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_8,__name__+".Warp8","Helm","Warp Speed","Warp 8")
	if (iMaxWarp >= 9):
		ATP_Lib.AddButtonToDropDownMenu(ET_WARP_9,__name__+".Warp9","Helm","Warp Speed","Warp 9")

	### Set the speed to default ###
	if (iMaxWarp > 3):
		SetWarpSpeed(iMaxWarp)
	else:
		SetWarpSpeed(iMaxWarp)

def Warp1(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(1)

def Warp2(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(2)

def Warp3(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(3)

def Warp4(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(4)

def Warp5(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(5)

def Warp6(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(6)

def Warp7(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(7)

def Warp8(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(8)

def Warp9(pObject,pEvent):
	ATP_Lib.CloseDropDownMenu("Helm","Warp Speed")
	SetWarpSpeed(9)


def ResetWarpSpeed():
	global WarpSpeed
	WarpSpeed=9

def SetWarpSpeed(i):
	global WarpSpeed
	WarpSpeed=i

def GetWarpSpeed():
	return WarpSpeed



