import App
import MissionLib

TRUE=1
FALSE=0

pSpecialPowerWindow=None
pTurretWindow=None
SpecialPowerDone=FALSE
TurretList=[]


L=0

w=App.globals.DEFAULT_ST_INDENT_HORIZ
h=App.globals.DEFAULT_ST_INDENT_VERT

SPECIAL_POWER_TEXT=0
SPECIAL_POWER_CONTAINER=1
SPECIAL_POWER_RULER=2
SPECIAL_POWER_HAZARD=3

SPECIAL_POWER_CONTAINER_MARKS=0
SPECIAL_POWER_CONTAINER_FULL=1
SPECIAL_POWER_CONTAINER_EMPTY=2


def Setup():
	CreateSpecialPowerWindow()
	CreateTurretWindow()


def CycleHandle(TGObject,pEvent):
	global TurretList
	global pTurretWindow
	
	if not pTurretWindow:
		return

	W=pTurretWindow.GetWidth()
	
	i=0
	for pTurret in TurretList:
		if pTurret:
			fVal=pTurret.GetConditionPercentage()
		else:
			fVal=0.0

		pContainerFull=pTurretWindow.GetNthChild(1+i*3)
		pContainerEmpty=pTurretWindow.GetNthChild(2+i*3)
		pContainerFull.Resize(fVal*pContainerEmpty.GetWidth(),pContainerFull.GetHeight(),0)

		i=i+1

def CycleHandle4(TGObject,pEvent):
	pass
	

def Initialise():
	pass


def CreateSpecialPowerWindow():
	pMode = App.GraphicsModeInfo_GetCurrentMode()
	pcLCARS = pMode.GetLcarsString()
	pPowerDisplay = App.EngPowerDisplay_GetPowerDisplay()

	kMainEmptyColor = App.TGColorA()
	kMainEmptyColor.SetRGBA(91.0 / 255.0, 85.0 / 255.0, 53.0 / 255.0, 1.0)

	W=pPowerDisplay.GetWidth()
	H=pPowerDisplay.GetHeight()

	global pSpecialPowerWindow
	pSpecialPowerWindow=App.TGPane_Create(W,h)
	pPowerDisplay.AddChild(pSpecialPowerWindow,0,H, 0)

	#Adding the "Special Power" text 
	pSpecialPowerUsedText = App.TGParagraph_Create("Special Power")
	pSpecialPowerUsedText.SetColor(App.NiColorA_WHITE)
	pSpecialPowerUsedText.Layout()
	pSpecialPowerWindow.AddChild(pSpecialPowerUsedText,0,0,0)

	#Create a container for the inner bars and fill it
	pSpecialPowerContainer = App.TGPane_Create()
	pContainerEmpty = App.TGIcon_Create(pcLCARS, 200, kMainEmptyColor)
	pContainerFull  = App.TGIcon_Create(pcLCARS, 200, App.g_kEngineeringSensorsColor)
	pSpecialPowerUsedMarks = App.STTiledIcon_Create(pcLCARS, 4101, App.NiColorA_BLACK)
	pSpecialPowerUsedMarks.SetTiling(App.STTiledIcon.DIRECTION_X, 1)
	pSpecialPowerUsedMarks.SetTileSize(App.STTiledIcon.DIRECTION_X, 1)
	pSpecialPowerContainer.AddChild(pSpecialPowerUsedMarks, 0.0, 0.0, 0)
	pSpecialPowerContainer.AddChild(pContainerFull, 0.0, 0.0, 0)
	pSpecialPowerContainer.AddChild(pContainerEmpty, 0.0, 0.0, 0)
	pSpecialPowerWindow.AddChild(pSpecialPowerContainer,0,0,0)
	pSpecialPowerContainer.Layout()

	#Create the ruler
	pPowerIcons = App.g_kIconManager.GetIconGroup(pcLCARS)
	pSpecialPowerRuler = App.TGFrame_Create(pcLCARS, 4330)
	pSpecialPowerRuler.SetNiColor(App.g_kEngineeringWarpCoreColor.r, App.g_kEngineeringWarpCoreColor.g,App.g_kEngineeringWarpCoreColor.b,App.g_kEngineeringWarpCoreColor.a)
	pSpecialPowerRuler.SetEdgeStretch(App.TGFrame.NO_STRETCH_LR)
	pSpecialPowerRuler.SetNoFocus()
	pSpecialPowerWindow.AddChild(pSpecialPowerRuler,0,0,0)
	
	# Add the hazard icon.
	pSpecialHazardIcon = App.STTiledIcon_Create(pcLCARS, 4200)
	pSpecialHazardIcon.SetTiling(App.STTiledIcon.DIRECTION_X, 1)
	pSpecialHazardIcon.SetTileSize(App.STTiledIcon.DIRECTION_X, 1)
	pSpecialHazardIcon.SetTiling(App.STTiledIcon.DIRECTION_Y, 1)
	pSpecialHazardIcon.SetTileSize(App.STTiledIcon.DIRECTION_Y, 1)
	pSpecialPowerWindow.AddChild(pSpecialHazardIcon,0,0,0)

	#Let's position and resize things
	pSpecialPowerUsedText.SetPosition(0.0,2.0*w,0)
	pSpecialPowerRuler.SetPosition(0.0,pSpecialPowerUsedText.GetBottom()+h,0)
	pSpecialPowerRuler.Resize(W,20.0*h,0)
	pSpecialPowerRulerInner=pSpecialPowerRuler.GetInnerRect()
	ww = pSpecialPowerRulerInner.GetLeft()
	hh = pSpecialPowerRulerInner.GetTop()
	pSpecialPowerContainer.SetPosition(pSpecialPowerRuler.GetLeft()+ww,pSpecialPowerRuler.GetTop()+hh,0)
	pSpecialPowerContainer.Resize(pSpecialPowerRuler.GetWidth()-ww-ww,pSpecialPowerRuler.GetHeight()-hh-hh,0)
	pSpecialPowerUsedMarks.Resize(pSpecialPowerContainer.GetWidth(),pSpecialPowerContainer.GetHeight(),0)
	pContainerEmpty.Resize(pSpecialPowerContainer.GetWidth(),pSpecialPowerContainer.GetHeight(),0)
	pContainerFull.Resize(pSpecialPowerContainer.GetWidth(),pSpecialPowerContainer.GetHeight(),0)
	pSpecialHazardIcon.SetPosition(pSpecialPowerRuler.GetLeft(),pSpecialPowerContainer.GetTop(),0)
	pSpecialHazardIcon.Resize(W,pSpecialPowerContainer.GetHeight(),0)

	#Resize the main window before layout
	pSpecialPowerWindow.Resize(W,pSpecialPowerRuler.GetBottom(),0)
	pSpecialPowerWindow.Layout()
	pPowerDisplay.Resize(W,pSpecialPowerWindow.GetBottom()+2.0*h,0)
	pPowerDisplay.Layout()
	pPowerDisplay.GetParent().Resize(pPowerDisplay.GetWidth(), pPowerDisplay.GetHeight(), 0)
	pWindow = App.STStylizedWindow_Cast(pPowerDisplay.GetConceptualParent())
	if pWindow:
		pWindow.InteriorChangedSize()



def UpdateSpecialPowerWindow(fSpecialPower,fWarpCore):
	global pSpecialPowerWindow
	pPlayer=MissionLib.GetPlayer()
	if not pPlayer:
		return

	#Get our panes
	W=pSpecialPowerWindow.GetWidth()
	pContainer=App.TGPane_Cast(pSpecialPowerWindow.GetNthChild(SPECIAL_POWER_CONTAINER))
	pMarks=App.STTiledIcon_Cast(pContainer.GetNthChild(SPECIAL_POWER_CONTAINER_MARKS))	
	pFull=App.TGIcon_Cast(pContainer.GetNthChild(SPECIAL_POWER_CONTAINER_FULL))
	pEmpty=App.TGIcon_Cast(pContainer.GetNthChild(SPECIAL_POWER_CONTAINER_EMPTY))
	pRuler=App.TGFrame_Cast(pSpecialPowerWindow.GetNthChild(SPECIAL_POWER_RULER))
	
	#First we resize to match the current warp core condition
	pRuler.Resize(fWarpCore*W,pRuler.GetHeight())
	pRuler.SetPosition((1-fWarpCore)*W,pRuler.GetTop(),0)
	pInner=pRuler.GetInnerRect()
	ww = pInner.GetLeft()-pRuler.GetLeft()
	pContainer.SetPosition(pRuler.GetLeft()+ww,pContainer.GetTop(),0)
	pContainer.Resize(pRuler.GetWidth()-ww-ww,pContainer.GetHeight(),0)
	pMarks.Resize(pContainer.GetWidth(),pContainer.GetHeight(),0)
	pEmpty.Resize(pContainer.GetWidth(),pContainer.GetHeight(),0)
	pFull.Resize (pContainer.GetWidth(),pContainer.GetHeight(),0)

	#Now we setup to match the current special power condition
	pFull.Resize(pFull.GetWidth()*fSpecialPower,pFull.GetHeight(),0)

	#Finalise things
	pSpecialPowerWindow.Layout()
	
	

def CreateTurretWindow():
	global pTurretWindow
	#Add the turret controls
	from Custom.AdvancedTechnologies.Data.Actions import ATP_ActionDecoder
	pMode = App.GraphicsModeInfo_GetCurrentMode()
	pcLCARS = pMode.GetLcarsString()

	pPowerDisplay = App.EngPowerDisplay_GetPowerDisplay()
	
	W=pPowerDisplay.GetWidth()
	H=pPowerDisplay.GetHeight()
	
	pTurretWindow=App.TGPane_Create(W,h)
	pPowerDisplay.AddChild(pTurretWindow,0,H, 0)
	
	global TurretList
	TurretList=[]
	pPlayer=MissionLib.GetPlayer()
	if not pPlayer:
		return

	i=3.0*h	
	if ATP_ActionDecoder.HasTurrets(pPlayer):
		TurretList=ATP_ActionDecoder.GiveTurretList(pPlayer)

		pString=App.TGString()
		kFillColor = App.TGColorA()
		kFillColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
		kEmptyColor = App.TGColorA()
		kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r,App.g_kSubsystemEmptyColor.g,App.g_kSubsystemEmptyColor.b,App.g_kSubsystemEmptyColor.a)
	
		
		for pTurret in TurretList:
			if pTurret:
				#Add the gaugetext
				pCharList=pTurret.GetName()
				#pString.SetString(pCharList[7:])
				pString.SetString(pCharList[:])
				pText = App.TGParagraph_CreateW(pString)
				pText.SetColor(App.NiColorA_WHITE)
				pText.Layout()
				pTurretWindow.AddChild(pText,w,i,0)
			
				# Create health gauges
				pContainerEmpty = App.TGIcon_Create(pcLCARS, 200, kEmptyColor)
				pContainerFull  = App.TGIcon_Create(pcLCARS, 200, kFillColor)
				pTurretWindow.AddChild(pContainerFull,4.0*w,i+1.25*pText.GetHeight(),0)
				pTurretWindow.AddChild(pContainerEmpty,4.0*w,i+1.25*pText.GetHeight(),0)
				pContainerEmpty.Resize(W-8.0*w,pText.GetHeight()*0.5,0)
				pContainerFull.Resize(W-8.0*w,pText.GetHeight()*0.5,0)

				#Increment the counter
				i=i+2.0*pText.GetHeight()+h
		
	else:
		pText = App.TGParagraph_Create("No turrets present")
		pText.SetColor(App.NiColorA_WHITE)
		pText.Layout()
		pTurretWindow.AddChild(pText,w,i,0)
		i=i+pText.GetHeight()+2.0*h
		

	pTurretWindow.Resize(W,i,0)
	pTurretWindow.Layout()
	pPowerDisplay.Resize(W,H+i,0)
	pPowerDisplay.Layout()
	pPowerDisplay.GetParent().Resize(pPowerDisplay.GetWidth(), pPowerDisplay.GetHeight(), 0)
	pWindow = App.STStylizedWindow_Cast(pPowerDisplay.GetConceptualParent())
	if pWindow:
		pWindow.InteriorChangedSize()



 		




	

	

