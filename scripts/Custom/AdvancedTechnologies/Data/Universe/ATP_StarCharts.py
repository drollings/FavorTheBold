import App
import MissionLib
import MainMenu.mainmenu
from math import *

from ATP_Object import *
from ATP_Constellations import *

FALSE=0
TRUE=1
SUCCES=0
ERROR=1
x=0
y=1

w  = App.globals.DEFAULT_ST_INDENT_HORIZ
h  = App.globals.DEFAULT_ST_INDENT_VERT
hb = MainMenu.mainmenu.g_kBigFontSize[MainMenu.mainmenu.g_iRes]*h
hs = MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes]*h
fb = MainMenu.mainmenu.g_pcBigFont
fs = MainMenu.mainmenu.g_pcFlightSmallFont

ORANGE              = App.NiColorA(225.0/255.0,204.0/255.0,102.0/255.0,1.0)
LIGHT_BLUE          = App.NiColorA(51.0/255.0,204.0/255.0,255.0/255.0,1.0)
YELLOW              = App.g_kEngineeringSensorsColor
WHITE               = App.NiColorA_WHITE
RED                 = App.NiColorA(255.0/255.0,100.0/255.0,50.0/255.0,1.0)

ClassToSpectral        =  {'O':"O3III",'B':"B3IV",'A':"A0V" ,'F':"F5IV",'G':"G2V",'K':"K3V",'M':"M8V"}
NumToSumName           =  {0:"Void",1:"Single",2:"Binary",3:"Trinary",4:"Quadrinary",5:"Nursery"}
NumToEnumName          =  {0:"???",1:"Primary",2:"Secondary",3:"Tertiary",4:"Quadrinary",5:"???"}
MagnitudeToScale       =  {-7:2.0,-6:1.8,-5:1.75,-4:1.6,-3:1.5,-2:1.0,-1:1.25,0:1.1,+1:1.0,+2:0.95,+3:0.9,+4:0.8,+5:0.7,+6:0.6,+7:0.5,+8:0.4,+9:0.3}

SUPER_PANE             = 0
MAIN_PANE              = 1
TITLE_WINDOW           = 2
CLOSE_BUTTON           = 3
ADD_BUTTON             = 4
SYSTEM_WINDOW          = 5
SYSTEM_MENU            = 6
GALAXY_WINDOW          = 7
GALAXY_ICON            = 8
GALAXY_GLASS           = 9
TRAJECTORY_WINDOW      = 10
TRAJECTORY_TEXT        = 11
CURRENT_WINDOW         = 12
CURRENT_TEXT           = 13
TARGET_WINDOW          = 14
TARGET_TEXT            = 15
MAIN_GLASS	       = 16
GALAXY_BORDER          = 17
WARP_BAR               = 18
CURRENT_TITLE          = 19
TARGET_TITLE           = 20
TARGET_ICON            = 21
CURRENT_ICON           = 22
TARGET_HORZ            = 23
TARGET_VERT            = 24
CURRENT_HORZ           = 25
CURRENT_VERT           = 26
GALAXY_3D_CONTAINER    = 27
GALAXY_2D_CONTAINER    = 28
VIEW_CONTROL           = 29
PLUS_BUTTON            = 30
MIN_BUTTON             = 31

DIM2 = 0
DIM3 = 1
PLUS = 2
MIN  = 3
TARGET_UPDATE = 4  

MIN_2D_ZOOM = 2.0
MAX_2D_ZOOM = 10.0
MAX_3D_ZOOM = 20.0
MIN_3D_ZOOM = 1.0

SUPER_PANE_WIDTH    = 1.00
SUPER_PANE_HEIGHT   = 1.00

MAIN_PANE_PARENT    = SUPER_PANE
MAIN_PANE_WIDTH     = 0.90 * SUPER_PANE_WIDTH
MAIN_PANE_HEIGHT    = 0.90 * SUPER_PANE_HEIGHT
MAIN_PANE_X         = 0.05 * SUPER_PANE_WIDTH
MAIN_PANE_Y         = 0.05 * SUPER_PANE_HEIGHT

TITLE_WINDOW_PARENT = MAIN_PANE
TITLE_WINDOW_WIDTH  = 1.00 * MAIN_PANE_WIDTH
TITLE_WINDOW_HEIGHT = 0.12 * MAIN_PANE_HEIGHT
TITLE_WINDOW_X 	    = 0.00 * MAIN_PANE_WIDTH
TITLE_WINDOW_Y      = 0.00 * MAIN_PANE_HEIGHT
TITLE_BAR           = 0.24 * TITLE_WINDOW_HEIGHT

CLOSE_BUTTON_PARENT = TITLE_WINDOW
CLOSE_BUTTON_WIDTH  = 0.25 * TITLE_WINDOW_WIDTH
CLOSE_BUTTON_HEIGHT = 0.35 * TITLE_WINDOW_HEIGHT
CLOSE_BUTTON_X      = 0.15 * TITLE_WINDOW_WIDTH
CLOSE_BUTTON_Y      = 0.10 * (TITLE_WINDOW_HEIGHT - CLOSE_BUTTON_HEIGHT)

ADD_BUTTON_PARENT   = TITLE_WINDOW
ADD_BUTTON_WIDTH    = CLOSE_BUTTON_WIDTH 
ADD_BUTTON_HEIGHT   = CLOSE_BUTTON_HEIGHT 
ADD_BUTTON_X        = 0.60 * TITLE_WINDOW_WIDTH
ADD_BUTTON_Y        = CLOSE_BUTTON_Y 

SYSTEM_WINDOW_PARENT= MAIN_PANE
SYSTEM_WINDOW_WIDTH = 0.30 * MAIN_PANE_WIDTH 
SYSTEM_WINDOW_HEIGHT= 0.48 *(MAIN_PANE_HEIGHT - TITLE_WINDOW_HEIGHT)
SYSTEM_WINDOW_X     = 0.00 * MAIN_PANE_WIDTH
SYSTEM_WINDOW_Y     = 1.00 * TITLE_WINDOW_HEIGHT + 0.02 * (MAIN_PANE_HEIGHT - TITLE_WINDOW_HEIGHT)

SYSTEM_MENU_PARENT  = SYSTEM_WINDOW
SYSTEM_MENU_WIDTH   = 1.00 * SYSTEM_WINDOW_WIDTH 
SYSTEM_MENU_HEIGHT  = 1.00 * SYSTEM_WINDOW_HEIGHT
SYSTEM_MENU_X       = 0.00 * SYSTEM_WINDOW_X
SYSTEM_MENU_Y       = 0.00 * SYSTEM_WINDOW_Y

GALAXY_WINDOW_PARENT= MAIN_PANE
GALAXY_WINDOW_WIDTH = 0.98 *MAIN_PANE_WIDTH - SYSTEM_WINDOW_WIDTH
GALAXY_WINDOW_HEIGHT= SYSTEM_WINDOW_HEIGHT
GALAXY_WINDOW_X     = SYSTEM_WINDOW_WIDTH + SYSTEM_WINDOW_X + (MAIN_PANE_WIDTH - SYSTEM_WINDOW_WIDTH)/2.0 - GALAXY_WINDOW_WIDTH/2.0
GALAXY_WINDOW_Y     = SYSTEM_WINDOW_Y

GALAXY_ICON_PARENT  = GALAXY_WINDOW
GALAXY_ICON_WIDTH   = 1.00 * GALAXY_WINDOW_WIDTH
GALAXY_ICON_HEIGHT  = 1.00 * GALAXY_WINDOW_HEIGHT
GALAXY_ICON_X       = 0.00
GALAXY_ICON_Y       = 0.00

GALAXY_BORDER_PARENT= GALAXY_WINDOW
GALAXY_GLASS_PARENT = GALAXY_WINDOW
TARGET_ICON_PARENT  = GALAXY_ICON
CURRENT_ICON_PARENT = GALAXY_ICON

CURRENT_WINDOW_PARENT = MAIN_PANE 
CURRENT_WINDOW_WIDTH  = SYSTEM_WINDOW_WIDTH
CURRENT_WINDOW_HEIGHT = (MAIN_PANE_HEIGHT - TITLE_WINDOW_HEIGHT - SYSTEM_WINDOW_HEIGHT) - 0.02 * MAIN_PANE_HEIGHT
CURRENT_WINDOW_X      = SYSTEM_WINDOW_X
CURRENT_WINDOW_Y      = MAIN_PANE_HEIGHT - CURRENT_WINDOW_HEIGHT 

CURRENT_TEXT_PARENT   = CURRENT_WINDOW

TARGET_WINDOW_PARENT  = MAIN_PANE 
TARGET_WINDOW_WIDTH   = CURRENT_WINDOW_WIDTH
TARGET_WINDOW_HEIGHT  = CURRENT_WINDOW_HEIGHT
TARGET_WINDOW_X       = MAIN_PANE_WIDTH - TARGET_WINDOW_WIDTH
TARGET_WINDOW_Y       = CURRENT_WINDOW_Y

TARGET_TEXT_PARENT    = TARGET_WINDOW

MAIN_GLASS_PARENT     = MAIN_PANE

VIEW_CONTROL_PARENT    = MAIN_PANE 
VIEW_CONTROL_WIDTH     = MAIN_PANE_WIDTH - TARGET_WINDOW_WIDTH - CURRENT_WINDOW_WIDTH - 0.04 * MAIN_PANE_WIDTH
VIEW_CONTROL_HEIGHT    = CURRENT_WINDOW_HEIGHT * 0.29
VIEW_CONTROL_X         = CURRENT_WINDOW_X + CURRENT_WINDOW_WIDTH + 0.02 * MAIN_PANE_WIDTH
VIEW_CONTROL_Y         = CURRENT_WINDOW_Y

TRAJECTORY_WINDOW_PARENT = MAIN_PANE 
TRAJECTORY_WINDOW_WIDTH  = VIEW_CONTROL_WIDTH
TRAJECTORY_WINDOW_HEIGHT = CURRENT_WINDOW_HEIGHT * 0.39
TRAJECTORY_WINDOW_X      = VIEW_CONTROL_X
TRAJECTORY_WINDOW_Y      = VIEW_CONTROL_Y  + VIEW_CONTROL_HEIGHT + 0.02 * CURRENT_WINDOW_HEIGHT
TRAJECTORY_TEXT_PARENT   = TRAJECTORY_WINDOW

WARP_BAR_PARENT          = MAIN_PANE
WARP_BAR_WIDTH           = TRAJECTORY_WINDOW_WIDTH
WARP_BAR_HEIGHT          = CURRENT_WINDOW_HEIGHT *0.15
WARP_BAR_X               = TRAJECTORY_WINDOW_X
WARP_BAR_Y               = MAIN_PANE_HEIGHT -  CURRENT_WINDOW_HEIGHT * 0.29 * 0.5 - WARP_BAR_HEIGHT * 0.5

GALAXY_ICON_REAL_X = 0.0
GALAXY_ICON_REAL_Y = 0.0


def Close(pMission,pEvent):
	pStarChart = GetStarCharts()
	pStarChart.close()

def UpdateAfterWarp(pSolar):
	pStarChart = GetStarCharts()
	pStarChart.updateAfterWarp(pSolar)
			
def AddSolarSystem(pSolar):
	pStarChart = GetStarCharts()
	pStarChart.addSystem(pSolar)

def AddToNavigation(pGame,pEvent):
	pStarChart = GetStarCharts()
	pStarChart.addToNavigation()

def WarpBarSlided(pGame,pEvent):
	pStarChart = GetStarCharts()
	pStarChart.updateWarpSpeed(pEvent.GetFloat())


class StarCharts(ATP_EventHandlerObject):
	RACE 			= 0
	MENU 			= 1
	PRIMARY_PLANETS 	= 2
	SECONDARY_PLANETS 	= 3
	STARBASES 		= 4
	OUTPOSTS 		= 5
	COMMS 			= 6
	UNINHABITED 		= 7

	def __init__(self,ID=0):
		## Superclass
		ATP_EventHandlerObject.__init__(self,STARCHARTS_ID)

		## Imports
		import ATP_UniverseInterface
		ButtonInterface = ATP_UniverseInterface.ButtonInterface
		MenuInterface	= ATP_UniverseInterface.MenuInterface

		## We will use this to cache the pointers to the different GUI parts
		self.ItemContainer	= {}
		self.OldFocus		= None
		self.Active		= FALSE
		self.SolarDict		= {}
		self.CurrentSystem	= None
		self.TargetSystem	= None
		self.WarpSpeed		= 1.0
		self.ViewMode		= DIM2
		self.ViewObject		= None
		self.Dim2Zoom		= 4
		self.Dim3Zoom		= 1.0
		self.Offset		= [0.0,0.0]
	
		## Events
		self.ET_ADD_TO_NAVIGATION	= GetNextEventType()
		self.ET_SOLAR_SELECTED		= GetNextEventType()
		self.ET_CLOSE           	= GetNextEventType()
		self.ET_ADD             	= GetNextEventType()
		self.ET_WARP_BAR_UPDATE		= GetNextEventType()
		self.ET_UPDATE_VIEW		= GetNextEventType()

		## Handlers
		self.AddHandler(self.ET_SOLAR_SELECTED	, 'SystemClicked'	)
		self.AddHandler(self.ET_UPDATE_VIEW	, 'updateViewHandler'	)

		## Graphics info
		pMode	= App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pMode.GetLcarsString()
				
		## Register some icons
		self.preRegisterGalaxyIcon()

		## Restore font
		self.SmallFont()

		#Find the main window and add the super pane to it
		pSuperPane = App.TGPane_Create (1.0,1.0)
		pSuperPane.SetNotVisible()
		pTopWindow = App.TopWindow_GetTopWindow()
		pTopWindow.AddChild(pSuperPane,0.0,0.0)
		self.ItemContainer[SUPER_PANE]=pSuperPane
		
		#Create the main center window
		pMainPane = App.TGPane_Create(MAIN_PANE_WIDTH,MAIN_PANE_HEIGHT)
		self.ItemContainer[SUPER_PANE].AddChild(pMainPane,MAIN_PANE_X,MAIN_PANE_Y)
		self.ItemContainer[MAIN_PANE]=pMainPane	
	
		#Create the title window
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])
		pStylizedWindow = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize","Star Chart",0.0, 0.0, None,1,TITLE_WINDOW_WIDTH,TITLE_WINDOW_HEIGHT,App.g_kMainMenuBorderMainColor)
		pStylizedWindow.SetUseScrolling(0)
		pStylizedWindow.SetTitleBarThickness(TITLE_BAR)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow)
		self.ItemContainer[TITLE_WINDOW]=pStylizedWindow
		
		#Add the close button to the title window
		pCloseButton = CreateInterfaceButton("Close",self.ET_CLOSE,__name__+".Close",CLOSE_BUTTON_WIDTH,CLOSE_BUTTON_HEIGHT)
		pCloseButton.SetNormalColor(App.g_kMainMenuButtonColor)
		pCloseButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
		pCloseButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
		#pCloseButton.SetColorBasedOnFlags()
		pCloseButton.SetSelected(0)
		pCloseButton.SetEnabled()
		self.ItemContainer[TITLE_WINDOW].AddChild(pCloseButton,CLOSE_BUTTON_X,CLOSE_BUTTON_Y)
		self.ItemContainer[CLOSE_BUTTON]=pCloseButton

		#Add the add button to the title window
		pAddButton = CreateInterfaceButton("Add to Navigation",self.ET_ADD,__name__+".AddToNavigation",ADD_BUTTON_WIDTH,ADD_BUTTON_HEIGHT)
		pAddButton.SetNormalColor(App.g_kMainMenuButtonColor)
		pAddButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
		pAddButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
		#pAddButton.SetColorBasedOnFlags()
		pAddButton.SetSelected (0)
		pAddButton.SetDisabled()
		self.ItemContainer[TITLE_WINDOW].AddChild(pAddButton,ADD_BUTTON_X,ADD_BUTTON_Y)
		self.ItemContainer[ADD_BUTTON]=pAddButton
		
		## Restore font
		self.SmallFont()	

		#Make the system window and menu
		pStylizedWindow = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize","Stellar Systems",0.0, 0.0, None,1,SYSTEM_WINDOW_WIDTH,SYSTEM_WINDOW_HEIGHT)
		pStylizedWindow.SetFixedSize(SYSTEM_WINDOW_WIDTH, SYSTEM_WINDOW_HEIGHT)
		pMenu = App.STSubPane_Create(SYSTEM_MENU_WIDTH,SYSTEM_MENU_HEIGHT,1)
		pMenu.Resize(SYSTEM_MENU_WIDTH - pStylizedWindow.GetBorderWidth(), SYSTEM_MENU_HEIGHT - pStylizedWindow.GetBorderHeight())
		pStylizedWindow.AddChild(pMenu,SYSTEM_MENU_X,SYSTEM_MENU_Y)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow,SYSTEM_WINDOW_X,SYSTEM_WINDOW_Y)
		pMenu.ResizeToContents()
		self.ItemContainer[SYSTEM_WINDOW]=pStylizedWindow
		self.ItemContainer[SYSTEM_MENU]=pMenu

		## Register it
		pWrappedMenu = MenuInterface('Stellar Systems')
		pWrappedMenu.Node = pMenu
		MenuInterface.StaticMenus['Stellar Systems'] = pWrappedMenu

		## Create the view controls
		pPane=App.TGPane_Create(VIEW_CONTROL_WIDTH,VIEW_CONTROL_HEIGHT)
		self.ItemContainer[MAIN_PANE].AddChild(pPane)
		pPane.SetPosition(VIEW_CONTROL_X,VIEW_CONTROL_Y)

		## Register it
		pWrappedMenu = MenuInterface('View Controls')
		pWrappedMenu.Node = pPane
		MenuInterface.StaticMenus['View Controls'] = pWrappedMenu

		## Set font
		self.BigFont()

		ww = VIEW_CONTROL_WIDTH
		hh = ww/pMode.GetPixelWidth()*pMode.GetPixelHeight()

		## Add the buttons "2D" "-" VIEW CONTROL "+" "3D"		
		pButton = ButtonInterface('2D',DIM2,pWrappedMenu,self.ET_UPDATE_VIEW,0.15*ww*0.75,0.15*hh*0.75)
		pButton.Node.SetPosition(0.025*ww,(VIEW_CONTROL_HEIGHT-0.15*hh)/2.0)

		pButton = ButtonInterface('-',MIN,pWrappedMenu,self.ET_UPDATE_VIEW,0.15*ww*0.75,0.15*hh*0.75)
		pButton.Node.SetPosition(0.20*ww,(VIEW_CONTROL_HEIGHT-0.15*hh)/2.0)
		self.ItemContainer[MIN_BUTTON] = pButton.Node

		pButton = ButtonInterface('+',PLUS,pWrappedMenu,self.ET_UPDATE_VIEW,0.15*ww*0.75,0.15*hh*0.75)
		pButton.Node.SetPosition(0.65*ww,(VIEW_CONTROL_HEIGHT-0.15*hh)/2.0)
		self.ItemContainer[PLUS_BUTTON] = pButton.Node

		pButton = ButtonInterface('3D',DIM3,pWrappedMenu,self.ET_UPDATE_VIEW,0.15*ww*0.75,0.15*hh*0.75)
		pButton.Node.SetPosition(0.825*ww,(VIEW_CONTROL_HEIGHT-0.15*hh)/2.0)

		pText = App.TGParagraph_Create("View Sets")
		pPane.AddChild(pText)
		pText.Resize(0.25*ww,VIEW_CONTROL_HEIGHT)
		pText.RecalcBounds()
		pText.SetPosition(0.50*ww-pText.GetWidth()/2.0,(pButton.Node.GetTop()+pButton.Node.GetBottom())/2.0-pText.GetHeight()/2.0)
		
		## Restore font
		self.SmallFont()

		## Save the pane away
		self.ItemContainer[VIEW_CONTROL]=pPane

		#Create the 3D overview
		pStylizedWindow = App.TGPane_Create(GALAXY_WINDOW_WIDTH,GALAXY_WINDOW_HEIGHT)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow,GALAXY_WINDOW_X,GALAXY_WINDOW_Y)
		self.ItemContainer[GALAXY_WINDOW]=pStylizedWindow

		#Some mode info
		pMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pMode.GetLcarsString()
		
		pBorder      = App.TGIcon_Create("ShipIcons",100*GALAXY_ICON)
		pContainer   = App.TGPane_Create(1.0,1.0)
		pIcon        = App.TGIcon_Create("ShipIcons",100*GALAXY_ICON+1)
		pTarget      = App.TGIcon_Create("WeaponIcons",370,ORANGE)
		pCurrent     = App.TGIcon_Create("WeaponIcons",370,LIGHT_BLUE)
		pTargetHorz  = App.TGIcon_Create(pcLCARS, 200,ORANGE)
		pTargetVert  = App.TGIcon_Create(pcLCARS, 200,ORANGE)
		pCurrentHorz = App.TGIcon_Create(pcLCARS, 200,LIGHT_BLUE)
		pCurrentVert = App.TGIcon_Create(pcLCARS, 200,LIGHT_BLUE)
		
		pContainer.AddChild(pTarget,0,0)
		pContainer.AddChild(pCurrent,0,0)
		pContainer.AddChild(pTargetHorz,0,0)
		pContainer.AddChild(pTargetVert,0,0)
		pContainer.AddChild(pCurrentHorz,0,0)
		pContainer.AddChild(pCurrentVert,0,0)
		pContainer.AddChild(pIcon,0,0)

		self.ItemContainer[GALAXY_3D_CONTAINER]  = pContainer
		self.ItemContainer[TARGET_ICON]          = pTarget
		self.ItemContainer[CURRENT_ICON]         = pCurrent
		self.ItemContainer[TARGET_HORZ]          = pTargetHorz
		self.ItemContainer[CURRENT_HORZ]         = pCurrentHorz
		self.ItemContainer[TARGET_VERT]          = pTargetVert
		self.ItemContainer[CURRENT_VERT]         = pCurrentVert
		self.ItemContainer[GALAXY_ICON]          = pIcon
		self.ItemContainer[GALAXY_BORDER]        = pBorder

		#Some hardcoded stuff ;-(
		AutoXYBorder=739.0/511.0
		AutoXYRect=GALAXY_WINDOW_WIDTH/GALAXY_WINDOW_HEIGHT
		InnerXX=(654.0-91.0)/739.0
		InnerYY=(465.0-47.0)/416.0

		if AutoXYBorder > AutoXYRect:
			#X is the limiting size
			pBorder.Resize(GALAXY_WINDOW_WIDTH,GALAXY_WINDOW_HEIGHT*AutoXYRect/AutoXYBorder)
		else:
			#Y is the limiting size
			pBorder.Resize(GALAXY_WINDOW_WIDTH/AutoXYRect*AutoXYBorder,GALAXY_WINDOW_HEIGHT)

		pContainer.Resize(InnerXX*pBorder.GetWidth(),InnerYY*pBorder.GetHeight()*0.85)
		pIcon.Resize(pContainer.GetWidth(),pContainer.GetHeight())
		# It works, so I don't touch it anymore ;-(

		#Resize the indicators
		pTarget.SizeToArtwork()
		pCurrent.SizeToArtwork()
		pTarget.Resize(pTarget.GetHeight(),pTarget.GetHeight())
		pCurrent.Resize(pTarget.GetHeight(),pTarget.GetHeight())
		pTargetHorz.Resize(pIcon.GetWidth(),pTarget.GetHeight()/4.0)
		pTargetVert.Resize(pTarget.GetWidth()/4.0,pIcon.GetHeight())
		pCurrentHorz.Resize(pIcon.GetWidth(),pCurrent.GetHeight()/4.0)
		pCurrentVert.Resize(pCurrent.GetWidth()/4.0,pIcon.GetHeight())

		pContainer.SetPosition((pBorder.GetWidth()-pContainer.GetWidth())/2.0,(pBorder.GetHeight()-pContainer.GetHeight())/2.0)
		pStylizedWindow.SetPosition((MAIN_PANE_WIDTH + SYSTEM_WINDOW_X + SYSTEM_WINDOW_WIDTH)/2.0 - pBorder.GetWidth()/2.0,(TARGET_WINDOW_Y+SYSTEM_WINDOW_Y)/2.0-pBorder.GetHeight()/2.0)

		#Create the 2D overview
		pGalaxyIcon = GalaxyIcon(pContainer.GetWidth(),pContainer.GetHeight())
		pStylizedWindow.AddChild(pGalaxyIcon.GetPane(),pContainer.GetLeft(),pContainer.GetTop())
		self.ItemContainer[GALAXY_2D_CONTAINER]=pGalaxyIcon

		#By default the 2D view is active
		pContainer.SetNotVisible()
		pGalaxyIcon.GetPane().SetVisible()

		#Add the border as almost last for the galaxywindow
		pStylizedWindow.AddChild(pContainer,0,0)
		pStylizedWindow.AddChild(pBorder,0,0)

		pContainer.SetPosition((pBorder.GetWidth()-pContainer.GetWidth())/2.0,(pBorder.GetHeight()-pContainer.GetHeight())/2.0)
		pStylizedWindow.SetPosition((MAIN_PANE_WIDTH + SYSTEM_WINDOW_X + SYSTEM_WINDOW_WIDTH)/2.0 - pBorder.GetWidth()/2.0,(TARGET_WINDOW_Y+SYSTEM_WINDOW_Y)/2.0-pBorder.GetHeight()/2.0)

		## Exact galaxy position
		global GALAXY_ICON_REAL_X,GALAXY_ICON_REAL_Y
		GALAXY_ICON_REAL_X = pMainPane.GetLeft() + pStylizedWindow.GetLeft() + pGalaxyIcon.GetPane().GetLeft()
		GALAXY_ICON_REAL_Y = pMainPane.GetTop()  + pStylizedWindow.GetTop()  + pGalaxyIcon.GetPane().GetTop()
	
		#Add a glass		
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()
		pGlass = App.TGIcon_Create(pcLCARS, 120)
		pGlass.Resize(pIcon.GetWidth(),pIcon.GetHeight())
		self.ItemContainer[GALAXY_WINDOW].AddChild(pGlass, 0, 0)
		self.ItemContainer[GALAXY_GLASS]=pGlass		

		#Add the trajectory window
		pStylizedWindow = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize","Trajectory Analysis",0.0, 0.0, None,1,TRAJECTORY_WINDOW_WIDTH,TRAJECTORY_WINDOW_HEIGHT)
		pStylizedWindow.SetFixedSize(TRAJECTORY_WINDOW_WIDTH, TRAJECTORY_WINDOW_HEIGHT)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow,TRAJECTORY_WINDOW_X,TRAJECTORY_WINDOW_Y)
		self.ItemContainer[TRAJECTORY_WINDOW]=pStylizedWindow
		
		g_pShipsText = App.TGParagraph_Create("", pStylizedWindow.GetMaximumInteriorWidth (), None, "", pStylizedWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
		g_pShipsText.Resize(TRAJECTORY_WINDOW_WIDTH - pStylizedWindow.GetBorderWidth(), TRAJECTORY_WINDOW_HEIGHT - pStylizedWindow.GetBorderHeight())
		pStylizedWindow.AddChild (g_pShipsText, 0, 0, 0)
		self.ItemContainer[TRAJECTORY_TEXT]=g_pShipsText		

		#Add the selfsys window
		pStylizedWindow = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize","Current System Analysis",0.0, 0.0, None,1,CURRENT_WINDOW_WIDTH,CURRENT_WINDOW_HEIGHT)
		pStylizedWindow.SetFixedSize(CURRENT_WINDOW_WIDTH, CURRENT_WINDOW_HEIGHT)
		pStylizedWindow.SetUseScrolling(TRUE)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow,CURRENT_WINDOW_X,CURRENT_WINDOW_Y)
		self.ItemContainer[CURRENT_WINDOW]=pStylizedWindow
		
		g_pShipsText = App.TGParagraph_Create("", pStylizedWindow.GetMaximumInteriorWidth (), None, "", pStylizedWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
		g_pShipsText.Resize(CURRENT_WINDOW_WIDTH - pStylizedWindow.GetBorderWidth(),hb)
		pStylizedWindow.AddChild (g_pShipsText, 0, 0, 0)
		self.ItemContainer[CURRENT_TITLE]=g_pShipsText
		
		g_pShipsText = App.TGParagraph_Create("", pStylizedWindow.GetMaximumInteriorWidth (), None, "", pStylizedWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
		g_pShipsText.Resize(CURRENT_WINDOW_WIDTH - pStylizedWindow.GetBorderWidth(), CURRENT_WINDOW_HEIGHT - pStylizedWindow.GetBorderHeight()-6.0*h)
		pStylizedWindow.AddChild (g_pShipsText, 0,h*6.0, 0)
		self.ItemContainer[CURRENT_TEXT]=g_pShipsText
		

		#Add the targetsys window
		pStylizedWindow = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize","Target System Analysis",0.0, 0.0, None,1,TARGET_WINDOW_WIDTH,TARGET_WINDOW_HEIGHT)
		pStylizedWindow.SetFixedSize(TARGET_WINDOW_WIDTH, TARGET_WINDOW_HEIGHT)
		pStylizedWindow.SetUseScrolling(TRUE)
		self.ItemContainer[MAIN_PANE].AddChild(pStylizedWindow,TARGET_WINDOW_X,TARGET_WINDOW_Y)
		self.ItemContainer[TARGET_WINDOW]=pStylizedWindow
				
		g_pShipsText = App.TGParagraph_Create("", pStylizedWindow.GetMaximumInteriorWidth (), None, "", pStylizedWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
		g_pShipsText.Resize(TARGET_WINDOW_WIDTH - pStylizedWindow.GetBorderWidth(), TARGET_WINDOW_HEIGHT - pStylizedWindow.GetBorderHeight()-6.0*h)
		pStylizedWindow.AddChild (g_pShipsText, 0,h*6.0, 0)
		self.ItemContainer[TARGET_TEXT]=g_pShipsText

		g_pShipsText2 = App.TGParagraph_Create("", pStylizedWindow.GetMaximumInteriorWidth (), None, "", pStylizedWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
		g_pShipsText2.Resize(TARGET_WINDOW_WIDTH - pStylizedWindow.GetBorderWidth(),hb)
		pStylizedWindow.AddChild (g_pShipsText2, 0, 0, 0)
		self.ItemContainer[TARGET_TITLE]=g_pShipsText2
		
	
		#Create a warp slider button
		pBar=CreateSlider("Warp Speed",self.ET_WARP_BAR_UPDATE,__name__+".WarpBarSlided",1.0,self.GetWindow())
		pBar.Resize(WARP_BAR_WIDTH,WARP_BAR_HEIGHT)
		self.ItemContainer[MAIN_PANE].AddChild(pBar,WARP_BAR_X,WARP_BAR_Y)
		self.ItemContainer[WARP_BAR]=pBar	


		# Glass background for the main pane
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()
		pGlass = App.TGIcon_Create(pcLCARS, 120)
		pGlass.Resize(self.ItemContainer[MAIN_PANE].GetWidth(),self.ItemContainer[MAIN_PANE].GetHeight())
		self.ItemContainer[MAIN_PANE].AddChild(pGlass, 0, 0)
		self.ItemContainer[MAIN_GLASS]=pGlass
	
		## Restore font
		self.SmallFont()

		## Make sure we start closed
		self.close()

	def GetInterface(self,s):
		import ATP_UniverseInterface
		return ATP_UniverseInterface.GetInterface(s)

	def GetWindow(self):
		return self.ItemContainer[SUPER_PANE]

	def GetGalaxyMap(self):
		return self.ItemContainer[GALAXY_2D_CONTAINER]		

	def GetAddToNavigationEvent(self):
		return self.ET_ADD_TO_NAVIGATION

	def BigFont(self):
		## In bigger font
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	def SmallFont(self):
		#Restore font
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
		
	def delete(self):
		App.g_kFocusManager.RemoveAllObjectsUnder(self.ItemContainer[SUPER_PANE])
		pTopWindow = App.TopWindow_GetTopWindow()
		pTopWindow.DeleteChild(self.ItemContainer[SUPER_PANE])

		## Upper class
		ATP_EventHandlerObject.delete(self)

	def exit_game_delete(self):
		self.delete()

	def open(self,gEvent):
		self.Active=TRUE
		pPane=self.ItemContainer[SUPER_PANE]
		pPane.SetVisible()
		pPane.SetEnabled()
		pTopWindow = App.TopWindow_GetTopWindow()
		self.OldFocus=pTopWindow.GetFocus()
		pTopWindow.MoveToFront(pPane)
		pTopWindow.SetFocus(pPane)
		pPane.SetAlwaysHandleEvents()

		## Update the current system
		self.updateCurrentSystem(GetPlayerShip().GetSolar())		


	def close(self):
		self.Active=FALSE
		pPane=self.ItemContainer[SUPER_PANE]
		pPane.SetNotVisible()

		pTopWindow = App.TopWindow_GetTopWindow()
		pTopWindow.MoveToBack(pPane)
		if self.OldFocus:
			pTopWindow.SetFocus(self.OldFocus)
		pPane.SetNotAlwaysHandleEvents()

		## Pass close call
		self.GetGalaxyMap().Close()
	
	def addSystem(self,pSolar):
		import ATP_UniverseInterface
		ButtonInterface = ATP_UniverseInterface.ButtonInterface

		## Check
		if not pSolar:
			return
		
		## Already defined ?
		if self.SolarDict.has_key(pSolar.GetID()):
			return

		## Controlling race
		pRace = pSolar.GetRace()

		## Menu of the race
		pRaceMenu = self.GetInterface('Stellar Systems').GetInterface(pRace.sName)

		if not pRaceMenu:
			## No menu yet, make one
			pRaceMenu = self.NewRaceMenu(pRace)			
			
		## Which menu ?
		pMenu = None
		if pSolar.IsExactTypeOf(SOLAR):
			if pSolar.GetPop() == 0.0:
				pMenu = pRaceMenu.GetInterface('Uninhabited')
			elif pSolar.IsCoreSystem():
				pMenu = pRaceMenu.GetInterface('Core Systems')
			else:
				pMenu = pRaceMenu.GetInterface('Secondary Systems')
		elif pSolar.IsExactTypeOf(STARBASE_SYSTEM):
			if pSolar.GetClass() == StarbaseSystem.STARBASE:
				pMenu = pRaceMenu.GetInterface('Starbases')
			elif pSolar.GetClass() == StarbaseSystem.OUTPOST:
				pMenu = pRaceMenu.GetInterface('Outposts')
			elif pSolar.GetClass() == StarbaseSystem.COMM:
				pMenu = pRaceMenu.GetInterface('Relay Stations')
		elif pSolar.IsExactTypeOf(BLACKHOLE_SYSTEM):
			pMenu = pRaceMenu
		else:
			raise RuntimeError
			
		## Add the system to a menu
		pButton = ButtonInterface(pSolar.GetName(),pSolar.GetID(),pMenu,self.ET_SOLAR_SELECTED)		
		
		## Register the button
		self.SolarDict[pSolar.GetID()] = pButton

	def NewRaceMenu(self,pRace):
		import ATP_UniverseInterface
		MenuInterface = ATP_UniverseInterface.MenuInterface

		## Basic menu
		pStellarSystems = self.GetInterface('Stellar Systems')

		if pRace.ID == ARCHITECT_ID:
			## Menu of the race
			pRaceMenu = MenuInterface('Spatial Phenomena',pStellarSystems)
		
		else:
			## Menu of the race
			pRaceMenu = MenuInterface(pRace.sName,pStellarSystems)

			## Submenus
			MenuInterface('Core Systems'		,pRaceMenu)
			MenuInterface('Secondary Systems'	,pRaceMenu)
			MenuInterface('Starbases'		,pRaceMenu)
			MenuInterface('Outposts'		,pRaceMenu)
			MenuInterface('Relay Stations'		,pRaceMenu)
			MenuInterface('Uninhabited'		,pRaceMenu)

		## Return
		return pRaceMenu

	def SystemClicked(self,gEvent):
		## ID from Event
		ID = gEvent.GetInt()

		## The solar system
		pSolar = GetByID(ID)

		## Valid ?
		if not pSolar:
			return
		if not pSolar.IsTypeOf(SOLAR):		
			return	
			
		## Update
		self.updateTargetSystem(pSolar)		
		
	def updateTargetSystem(self,pSolar):
		self.TargetSystem=pSolar
		self.ViewObject=pSolar

		pChar=""

		if not pSolar:
			#Edit the fields
			App.g_kFontManager.SetDefaultFont(fb,hb)
			self.ItemContainer[TARGET_TITLE].SetString("No target system selected")
			self.ItemContainer[TARGET_TITLE].SetColor(ORANGE)
			self.ItemContainer[TARGET_TEXT].SetString("")
			self.ItemContainer[ADD_BUTTON].SetDisabled()
		else:
			if pSolar.GetID()==self.CurrentSystem.GetID():
				raise RuntimeError
			else:
				#Edit the fields
				App.g_kFontManager.SetDefaultFont(fb,hb)
				self.ItemContainer[TARGET_TITLE].SetString(pSolar.GetName())
				self.ItemContainer[TARGET_TITLE].SetColor(ORANGE)
				App.g_kFontManager.SetDefaultFont(fs,hs)
				self.ItemContainer[ADD_BUTTON].SetEnabled()

				#Construct the info
				InfoConstruction(self.ItemContainer[TARGET_TEXT],pSolar)

		#Restore font
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
		
		#Coupled changes
		self.updateTrajectory()
		self.updateView(TARGET_UPDATE)

		#Seize change
		self.ItemContainer[TARGET_WINDOW].InteriorChangedSize()
		self.ItemContainer[TARGET_WINDOW].Layout()
		self.ItemContainer[TARGET_WINDOW].ScrollToTop()

			
	def updateWarpSpeed(self,fVal):
		self.WarpSpeed=fVal
		self.updateTrajectory()

	def updateTrajectory(self):
		pChar=""

		if not self.TargetSystem or not self.CurrentSystem:
			pChar="N/A"
		else:
			U=self.TargetSystem.GetLoc()
			V=self.CurrentSystem.GetLoc()
			U.Subtract(V)

			#One Unit is 20ly
			fDist=U.Length()*20.0
			fSpeed=WarpSpeedToLyd(self.WarpSpeed)
			if fSpeed<=0.0:
				pChar=pChar+ "Warp Speed: %2.1f"  % (self.WarpSpeed) + ""
				pChar=pChar+ "Distance: %2.2f ly" % (fDist)          + ""
				pChar=pChar+ "ETA: N/A"                              + ""
			else:
				pChar=pChar+ "Warp Speed: %2.1f"  % (self.WarpSpeed) + ""
				pChar=pChar+ "Distance: %2.2f ly" % (fDist)          + ""
				fTime=fDist/fSpeed #time in days
				if fTime>=365:
					fTime=fTime/365.0
					pChar=pChar+ "ETA: %2.2f years" % (fTime)    + ""
				else:
					pChar=pChar+ "ETA: %2.2f days"  % (fTime)    + ""

		self.ItemContainer[TRAJECTORY_TEXT].SetString(pChar)
		

	def updateCurrentSystem(self,pSolar):
		pChar=""

		#Undisable the previous button
		if self.CurrentSystem:
			pOldButton=self.SolarDict[self.CurrentSystem.GetID()].Node
			pOldButton.SetEnabled()
		
		#Disable the current system
		self.CurrentSystem = pSolar
		
		if self.CurrentSystem:
			pNewButton = self.SolarDict[self.CurrentSystem.GetID()].Node
			pNewButton.SetDisabled()

		#Edit the title
		App.g_kFontManager.SetDefaultFont(fb,hb)
		self.ItemContainer[CURRENT_TITLE].SetString(pSolar.GetName())
		self.ItemContainer[CURRENT_TITLE].SetColor(LIGHT_BLUE)
		App.g_kFontManager.SetDefaultFont(fs,hs)

		#Construct the info
		InfoConstruction(self.ItemContainer[CURRENT_TEXT],pSolar)

		#Restore font
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

		#Coupled changes
		self.updateTrajectory()
		self.updateView(DIM2)

		#Size change
		self.ItemContainer[CURRENT_WINDOW].InteriorChangedSize()
		self.ItemContainer[CURRENT_WINDOW].Layout()
		self.ItemContainer[CURRENT_WINDOW].ScrollToTop()


	def updateViewHandler(self,gEvent):
		## Game event, get information out of it
		iState = gEvent.GetInt()

		## Call it
		self.updateView(iState)
		
	def updateView(self,iState):		
		## Analysis
		if iState==TARGET_UPDATE:
			#Center on the target
			self.ViewObject=self.TargetSystem
			
			if self.ViewMode==DIM2:
				#Focus on the viewed system
				pSolar=self.ViewObject
				if pSolar:
					X0,Y0 = GetUniverse().GetSectorCoords(pSolar)
					Z0 = 2*self.Dim2Zoom
					self.ItemContainer[GALAXY_2D_CONTAINER].display(X0,Y0,Z0)
			
			if self.ViewMode==DIM3:
				self.ItemContainer[GALAXY_3D_CONTAINER].SetVisible()
				self.ItemContainer[GALAXY_2D_CONTAINER].GetPane().SetNotVisible()

				#Position the targeticon and rulers
				if not self.TargetSystem:
					self.ItemContainer[TARGET_ICON].SetNotVisible()
					self.ItemContainer[TARGET_HORZ].SetNotVisible()
					self.ItemContainer[TARGET_VERT].SetNotVisible()
				else:
					self.ItemContainer[TARGET_ICON].SetVisible()
					self.ItemContainer[TARGET_HORZ].SetVisible()
					self.ItemContainer[TARGET_VERT].SetVisible()

				if self.TargetSystem:
					nX,nY=self.generateCoords(self.TargetSystem)
					self.ItemContainer[TARGET_ICON].SetPosition(nX,nY)

					nX=nX+self.ItemContainer[TARGET_ICON].GetWidth()/2.0-self.ItemContainer[TARGET_VERT].GetWidth()/2.0
					nY=nY+self.ItemContainer[TARGET_ICON].GetHeight()/2.0-self.ItemContainer[TARGET_HORZ].GetHeight()/2.0
			
					self.ItemContainer[TARGET_HORZ].SetPosition(0.0,nY)
					self.ItemContainer[TARGET_VERT].SetPosition(nX,0.0)

				if self.CurrentSystem:
					nX,nY=self.generateCoords(self.CurrentSystem)
					self.ItemContainer[CURRENT_ICON].SetPosition(nX,nY)

					nX=nX+self.ItemContainer[CURRENT_ICON].GetWidth()/2.0-self.ItemContainer[CURRENT_VERT].GetWidth()/2.0
					nY=nY+self.ItemContainer[CURRENT_ICON].GetHeight()/2.0-self.ItemContainer[CURRENT_HORZ].GetHeight()/2.0
			
					self.ItemContainer[CURRENT_HORZ].SetPosition(0.0,nY)
					self.ItemContainer[CURRENT_VERT].SetPosition(nX,0.0)
			
					
		elif iState==DIM2:
			#We want a two dimensional view
			self.ViewMode=DIM2
			self.ViewObject=self.CurrentSystem

			#Check for valid zooms
			if self.Dim2Zoom<MIN_2D_ZOOM:
				self.ItemContainer[PLUS_BUTTON].SetDisabled()
			else:
				self.ItemContainer[PLUS_BUTTON].SetEnabled()

			if self.Dim2Zoom>MAX_2D_ZOOM:
				self.ItemContainer[MIN_BUTTON].SetDisabled()
			else:
				self.ItemContainer[MIN_BUTTON].SetEnabled()

			#Set the 3D view active
			self.ItemContainer[GALAXY_2D_CONTAINER].GetPane().SetVisible()
			self.ItemContainer[GALAXY_3D_CONTAINER].SetNotVisible()

			#Focus on the current system
			pSolar=self.CurrentSystem
			if pSolar:
				X0,Y0 = GetUniverse().GetSectorCoords(pSolar)
				Z0 = 2*self.Dim2Zoom
				self.ItemContainer[GALAXY_2D_CONTAINER].display(X0,Y0,Z0)

		elif iState==DIM3:
			#We want a two dimensional view
			self.ViewMode=DIM3
			self.ViewObject=self.CurrentSystem

			if not self.CurrentSystem:
				return
		
			#Check for valid zooms
			if self.Dim3Zoom<MIN_3D_ZOOM:
				self.ItemContainer[MIN_BUTTON].SetDisabled()
			else:
				self.ItemContainer[MIN_BUTTON].SetEnabled()

			if self.Dim3Zoom>MAX_3D_ZOOM:
				self.ItemContainer[PLUS_BUTTON].SetDisabled()
			else:
				self.ItemContainer[PLUS_BUTTON].SetEnabled()		
		
			#By default the 3D view is active
			self.ItemContainer[GALAXY_3D_CONTAINER].SetVisible()
			self.ItemContainer[GALAXY_2D_CONTAINER].GetPane().SetNotVisible()

			if self.CurrentSystem:
				nX,nY=self.generateCoords(self.CurrentSystem)
				self.ItemContainer[CURRENT_ICON].SetPosition(nX,nY)

				nX=nX+self.ItemContainer[CURRENT_ICON].GetWidth()/2.0-self.ItemContainer[CURRENT_VERT].GetWidth()/2.0
				nY=nY+self.ItemContainer[CURRENT_ICON].GetHeight()/2.0-self.ItemContainer[CURRENT_HORZ].GetHeight()/2.0
			
				self.ItemContainer[CURRENT_HORZ].SetPosition(0.0,nY)
				self.ItemContainer[CURRENT_VERT].SetPosition(nX,0.0)

			if self.TargetSystem:
				nX,nY=self.generateCoords(self.TargetSystem)
				self.ItemContainer[TARGET_ICON].SetPosition(nX,nY)

				nX=nX+self.ItemContainer[TARGET_ICON].GetWidth()/2.0-self.ItemContainer[TARGET_VERT].GetWidth()/2.0
				nY=nY+self.ItemContainer[TARGET_ICON].GetHeight()/2.0-self.ItemContainer[TARGET_HORZ].GetHeight()/2.0
			
				self.ItemContainer[TARGET_HORZ].SetPosition(0.0,nY)
				self.ItemContainer[TARGET_VERT].SetPosition(nX,0.0)
			

		elif iState==MIN:
			if self.ViewMode==DIM2:
				self.Dim2Zoom=self.Dim2Zoom+1

				#Check for valid zooms
				if self.Dim2Zoom<MIN_2D_ZOOM:
					self.ItemContainer[PLUS_BUTTON].SetDisabled()
				else:
					self.ItemContainer[PLUS_BUTTON].SetEnabled()

				if self.Dim2Zoom>MAX_2D_ZOOM:
					self.ItemContainer[MIN_BUTTON].SetDisabled()
				else:
					self.ItemContainer[MIN_BUTTON].SetEnabled()
							

			if self.ViewMode==DIM3:
				self.Dim3Zoom=self.Dim3Zoom*0.5

				#Check for valid zooms
				if self.Dim3Zoom<MIN_3D_ZOOM:
					self.ItemContainer[MIN_BUTTON].SetDisabled()
				else:
					self.ItemContainer[MIN_BUTTON].SetEnabled()

				if self.Dim3Zoom>MAX_3D_ZOOM:
					self.ItemContainer[PLUS_BUTTON].SetDisabled()
				else:
					self.ItemContainer[PLUS_BUTTON].SetEnabled()
						
			
			if self.CurrentSystem.GetID()==self.ViewObject.GetID():
				if self.ViewMode==DIM2:
					self.updateView(DIM2)
				if self.ViewMode==DIM3:
					self.updateView(DIM3)

			if self.TargetSystem and self.ViewObject:
				if self.TargetSystem.GetID()==self.ViewObject.GetID():
					self.updateView(TARGET_UPDATE)


			#Redraw the galaxy icon
			self.registerGalaxyIcon()


		elif iState==PLUS:
			if self.ViewMode==DIM2:
				self.Dim2Zoom=self.Dim2Zoom-1

				#Check for valid zooms
				if self.Dim2Zoom<MIN_2D_ZOOM:
					self.ItemContainer[PLUS_BUTTON].SetDisabled()
				else:
					self.ItemContainer[PLUS_BUTTON].SetEnabled()

				if self.Dim2Zoom>MAX_2D_ZOOM:
					self.ItemContainer[MIN_BUTTON].SetDisabled()
				else:
					self.ItemContainer[MIN_BUTTON].SetEnabled()
			
			if self.ViewMode==DIM3:
				self.Dim3Zoom=self.Dim3Zoom*2.05

				#Check for valid zooms
				if self.Dim3Zoom<MIN_3D_ZOOM:
					self.ItemContainer[MIN_BUTTON].SetDisabled()
				else:
					self.ItemContainer[MIN_BUTTON].SetEnabled()

				if self.Dim3Zoom>MAX_3D_ZOOM:
					self.ItemContainer[PLUS_BUTTON].SetDisabled()
				else:
					self.ItemContainer[PLUS_BUTTON].SetEnabled()
			
			self.CurrentSystem.GetID()
			self.ViewObject.GetID()

			if self.CurrentSystem.GetID()==self.ViewObject.GetID():
				if self.ViewMode==DIM2:
					self.updateView(DIM2)
				if self.ViewMode==DIM3:
					self.updateView(DIM3)

			if self.TargetSystem and self.ViewObject:
				if self.TargetSystem.GetID()==self.ViewObject.GetID():
					self.updateView(TARGET_UPDATE)

			#Redraw the galaxy icons
			self.registerGalaxyIcon()


		else:
			raise RuntimeError
			

	def updateAfterWarp(self,pSolar):
		self.updateCurrentSystem(pSolar)
		self.updateTargetSystem(None)

	def addToNavigation(self):
		# if self.TargetSystem:
		#	self.TargetSystem.Setup()

		## Kiska ACK
		GetPlayerBridge().GetHelm().SayYes()

		## Close the menus
		self.GetInterface('Stellar Systems').FullClose()

		## Raise an event
		self.Raise(self.ET_ADD_TO_NAVIGATION,self.TargetSystem,self)

	def generateCoords(self,pSolar):
		import math
		if not pSolar:
			return
				
		H=self.ItemContainer[GALAXY_ICON].GetHeight()
		W=self.ItemContainer[GALAXY_ICON].GetWidth()

		X0=155.0/478.0*W
		Y0=185.0/297.0*H

		aspX=20.0/100000.0*math.sqrt((431.0-44.0)*(431.0-44.0)+(55.0-239.0)*(55.0-239.0))/478.0*W
		aspY=20.0/100000.0*math.sqrt((323.0-141.0)*(323.0-141.0)+(225.0-175.0)*(225.0-175.0))/297.0*H
		aspX=20.0/100000.0*W*0.5
		aspY=20.0/100000.0*H

		ricoX=(225.0-75.0)/(323.0-141.0)
		ricoY=(55.0-239.0)/(431.0-44.0)

		tXX=1/math.sqrt(1+ricoX*ricoX)
		tXY=ricoX/math.sqrt(1+ricoX*ricoX)
		tYY=ricoY/math.sqrt(1+ricoY*ricoY)
		tYX=1/math.sqrt(1+ricoY*ricoY)
		
		tXX=tXX*aspX
		tXY=tXY*aspX
		tYX=tYX*aspY
		tYY=tYY*aspY
		
		space=pSolar.GetLoc()
		X=space.GetX()
		Y=space.GetY()
		XX=X-5000.0/self.Dim3Zoom
		YY=Y+5000.0/self.Dim3Zoom
		
		nX  = X0+tXX*X +tYX*Y
		nY  = Y0+tXY*X +tYY*Y
		nXX = X0+tXX*XX+tYX*YY
		nYY = Y0+tXY*XX+tYY*YY
		nXX=0
		nYY=0

		if nXX<=0.0:
			nXX=0.0
		if nYY<=0.0:
			nYY=0.0

		if self.ViewObject:
			if pSolar.GetID()==self.ViewObject.GetID():
				self.Offset=[nXX,nYY]
			else:
				nXX,nYY=self.Offset[x],self.Offset[y]

		nX=(nX-nXX)*self.Dim3Zoom
		nY=(nY-nYY)*self.Dim3Zoom
		
		#print nX/W,nY/H

		return nX,nY

	def preRegisterGalaxyIcon(self):
		UniverseIcons = App.g_kIconManager.GetIconGroup("ShipIcons")

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyBorder2.tga")
		UniverseIcons.SetIconLocation(100*GALAXY_ICON,TextureHandle, 0, 0,511,511)
			
		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyIcon2.tga")
		UniverseIcons.SetIconLocation(100*GALAXY_ICON+1,TextureHandle, 0, 0,511,511)
	
	def registerGalaxyIcon(self):
		
		UniverseIcons = App.g_kIconManager.GetIconGroup("ShipIcons")

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyBorder2.tga")
		UniverseIcons.SetIconLocation(100*GALAXY_ICON,TextureHandle, 0, 0,511,511)
		
		H=self.ItemContainer[GALAXY_ICON].GetHeight()
		W=self.ItemContainer[GALAXY_ICON].GetWidth()

		XA=self.Offset[x]/W*511.0
		YA=self.Offset[y]/H*511.0
		XB=int(XA+511.0/self.Dim3Zoom)
		YB=int(YA+511.0/self.Dim3Zoom)
		XA=0
		YA=0
		XB=511
		YB=511
		
		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyIcon2.tga")
		UniverseIcons.SetIconLocation(100*GALAXY_ICON+1,TextureHandle,XA,YA,XB,YB)
		return
		

	def GetTargetSystem(self):
		return self.TargetSystem



class GalaxyIcon(ATP_EventHandlerObject):
	MAIN_PANE      = 0
	BACKGROUND     = 1
	SYSTEM_PANE    = 2
	GRID           = 3
	SPHERE_PANE    = 4
	NEBULA_PANE    = 5

	SYSTEM_TAG_0     		= 10000*GALAXY_ICON + 0
	SYSTEM_TAG_1     		= 10000*GALAXY_ICON + 1
	SYSTEM_TAG_2A    		= 10000*GALAXY_ICON + 2
	SYSTEM_TAG_2B    		= 10000*GALAXY_ICON + 3
	SYSTEM_TAG_3A    		= 10000*GALAXY_ICON + 4
 	SYSTEM_TAG_3B    		= 10000*GALAXY_ICON + 5
	SYSTEM_TAG_3C    		= 10000*GALAXY_ICON + 6
	SYSTEM_TAG_4A    		= 10000*GALAXY_ICON + 7
	SYSTEM_TAG_4B    		= 10000*GALAXY_ICON + 8
	SYSTEM_TAG_4C    		= 10000*GALAXY_ICON + 9
	SYSTEM_TAG_4D    		= 10000*GALAXY_ICON + 10
	SYSTEM_TAG_Z    		= 10000*GALAXY_ICON + 11
	SYSTEM_TAG_TRIANGLE         	= 10000*GALAXY_ICON + 12
	SYSTEM_TAG_ROUND            	= 10000*GALAXY_ICON + 13
	SYSTEM_TAG_CIRCLE           	= 10000*GALAXY_ICON + 14	
	SYSTEM_TAG_DOTTED_TRIANGLE  	= 10000*GALAXY_ICON + 15
	SYSTEM_SPHERE	            	= 10000*GALAXY_ICON + 16
	SYSTEM_BLACKHOLE_1		= 10000*GALAXY_ICON + 52
	SYSTEM_NEBULA_1		    	= 10000*GALAXY_ICON + 17
	SYSTEM_NEBULA_2		    	= 10000*GALAXY_ICON + 18
	SYSTEM_NEBULA_3		    	= 10000*GALAXY_ICON + 19
	SYSTEM_NEBULA_4		    	= 10000*GALAXY_ICON + 20
	SYSTEM_NEBULA_5		    	= 10000*GALAXY_ICON + 21
	SYSTEM_NEBULA_6		    	= 10000*GALAXY_ICON + 22	
	SYSTEM_NEBULA_7		    	= 10000*GALAXY_ICON + 23
	SYSTEM_NEBULA_8		    	= 10000*GALAXY_ICON + 24
	SYSTEM_NEBULA_9		    	= 10000*GALAXY_ICON + 25
	SYSTEM_NEBULA_10	    	= 10000*GALAXY_ICON + 26
	SYSTEM_NEBULA_11	    	= 10000*GALAXY_ICON + 27
	SYSTEM_NEBULA_12	    	= 10000*GALAXY_ICON + 49
	SYSTEM_NEBULA_13	    	= 10000*GALAXY_ICON + 50
	SYSTEM_NEBULA_14	    	= 10000*GALAXY_ICON + 51

	BORDER_BBBB			= 10000*GALAXY_ICON + 28
	BORDER_ZBBB			= 10000*GALAXY_ICON + 29
	BORDER_BZBB			= 10000*GALAXY_ICON + 30
	BORDER_BBZB			= 10000*GALAXY_ICON + 31
	BORDER_BBBZ			= 10000*GALAXY_ICON + 32
	BORDER_ZZBB			= 10000*GALAXY_ICON + 33
	BORDER_BZZB			= 10000*GALAXY_ICON + 34
	BORDER_BBZZ			= 10000*GALAXY_ICON + 35
	BORDER_ZBBZ			= 10000*GALAXY_ICON + 36
	BORDER_ZBZB			= 10000*GALAXY_ICON + 37
	BORDER_BZBZ			= 10000*GALAXY_ICON + 38
	BORDER_ZZZB			= 10000*GALAXY_ICON + 39
	BORDER_BZZZ			= 10000*GALAXY_ICON + 40
	BORDER_ZBZZ			= 10000*GALAXY_ICON + 41
	BORDER_ZZBZ			= 10000*GALAXY_ICON + 42
	BORDER_ZZZZ			= 10000*GALAXY_ICON + 43
	BORDER_IXXX			= 10000*GALAXY_ICON + 44
	BORDER_XIXX			= 10000*GALAXY_ICON + 45
	BORDER_XXIX			= 10000*GALAXY_ICON + 46
	BORDER_XXXI			= 10000*GALAXY_ICON + 47
	
	SYSTEM_SPHERE_WIDE		= 10000*GALAXY_ICON + 48 

	TAG_SCALE      		= 0.12
	AURA_SCALE     		= 1.5
	NAME_SWAP_THRESHOLD	= 8

	BorderStringToNum = {}

	cBackGround    = App.NiColorA_BLACK
	cGrid          = App.NiColorA_WHITE
	
	def __init__(self,fWidth,fHeight):
		## Base class
		ATP_EventHandlerObject.__init__(self,GALAXY_MAP_ID)

		## Attributes
		self.W=fWidth
		self.H=fHeight
		self.Dict={}
		self.Zoom=4.0
		self.lSquares = []
		
		#Load LCARS
		pMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pMode.GetLcarsString()

		#Create the main pane
		pMainPane=App.TGPane_Create(self.W,self.H)
		self.Dict[GalaxyIcon.MAIN_PANE]=pMainPane

		#Create a pane to contain the system icons
		pSystemPane=App.TGPane_Create(self.W,self.H)
		pMainPane.AddChild(pSystemPane)
		self.Dict[GalaxyIcon.SYSTEM_PANE]=pSystemPane

		#Create the grid
		pGrid=Grid(self.W,self.H,GalaxyIcon.cGrid)
		pMainPane.AddChild(pGrid.GetPane())
		self.Dict[GalaxyIcon.GRID]=pGrid

		## The Nebulas
		pNebulaPane=App.TGPane_Create(self.W,self.H)
		pMainPane.AddChild(pNebulaPane)
		self.Dict[GalaxyIcon.NEBULA_PANE]=pNebulaPane

		## Create a sphere pane
		pSpherePane=App.TGPane_Create(self.W,self.H)
		pMainPane.AddChild(pSpherePane)
		self.Dict[GalaxyIcon.SPHERE_PANE]=pSpherePane
	
		#Create a black background icon
		pIcon  = App.TGIcon_Create(pcLCARS, 200,GalaxyIcon.cBackGround)
		self.Dict[GalaxyIcon.BACKGROUND]=pIcon
		pIcon.Resize(self.W,self.H)
		pMainPane.AddChild(pIcon,0.0,0.0)		

		#Register some new Icon types
		UniverseIcons = App.g_kIconManager.GetIconGroup("ShipIcons")

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag0.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_0,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTagZ.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_Z,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag1.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_1,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag2.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_2A,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag2.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_2B,TextureHandle,0,0,63,63,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_VERTICAL)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag3a.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_3A,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag3b.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_3B,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag3b.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_3C,TextureHandle,0,0,63,63,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_HORIZONTAL)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag4.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_4A,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag4.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_4B,TextureHandle,0,0,63,63,App.TGIconGroup.ROTATE_90)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag4.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_4C,TextureHandle,0,0,63,63,App.TGIconGroup.ROTATE_180)
	
		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTag4.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_4D,TextureHandle,0,0,63,63,App.TGIconGroup.ROTATE_270)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTagTriangle.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_TRIANGLE,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTagBall.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_ROUND,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTagCircle.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_CIRCLE,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/GalaxyTagDottedTriangle.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_TAG_DOTTED_TRIANGLE,TextureHandle,0,0,63,63)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/StellarAura.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_SPHERE,TextureHandle,0,0,255,255)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/StarCharts/Blackhole001.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_BLACKHOLE_1,TextureHandle,0,0,127,127)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula001.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_1,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula002.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_2,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula003.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_3,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula004.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_4,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula005.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_5,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula006.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_6,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula007.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_7,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula008.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_8,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula009.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_9,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula010.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_10,TextureHandle,0,0,1023,1023)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula011.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_11,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula012.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_12,TextureHandle,0,0,511,511)
	
		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula013.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_13,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Nebulas/Nebula014.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_NEBULA_14,TextureHandle,0,0,511,511)

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_BBBB.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BBBB,TextureHandle,0,0,127,127)
		GalaxyIcon.BorderStringToNum["BBBB"] = GalaxyIcon.BORDER_BBBB

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_BZZZ.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZBBB,TextureHandle,0,0,127,127)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BZBB,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_HORIZONTAL)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BBZB,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_180)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BBBZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_VERTICAL)
		GalaxyIcon.BorderStringToNum["ZBBB"] = GalaxyIcon.BORDER_ZBBB
		GalaxyIcon.BorderStringToNum["BZBB"] = GalaxyIcon.BORDER_BZBB
		GalaxyIcon.BorderStringToNum["BBZB"] = GalaxyIcon.BORDER_BBZB
		GalaxyIcon.BorderStringToNum["BBBZ"] = GalaxyIcon.BORDER_BBBZ

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_ZZBB.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZZBB,TextureHandle,0,0,127,127)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BZZB,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_90)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BBZZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_180)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZBBZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_270)
		GalaxyIcon.BorderStringToNum["ZZBB"] = GalaxyIcon.BORDER_ZZBB
		GalaxyIcon.BorderStringToNum["BZZB"] = GalaxyIcon.BORDER_BZZB
		GalaxyIcon.BorderStringToNum["BBZZ"] = GalaxyIcon.BORDER_BBZZ
		GalaxyIcon.BorderStringToNum["ZBBZ"] = GalaxyIcon.BORDER_ZBBZ

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_ZBZB.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZBZB,TextureHandle,0,0,127,127)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BZBZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0,App.TGIconGroup.MIRROR_HORIZONTAL)
		GalaxyIcon.BorderStringToNum["BZBZ"] = GalaxyIcon.BORDER_BZBZ
		GalaxyIcon.BorderStringToNum["ZBZB"] = GalaxyIcon.BORDER_ZBZB

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_ZZZB.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZZZB,TextureHandle,0,0,127,127)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_BZZZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_VERTICAL)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZBZZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_180)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZZBZ,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_HORIZONTAL)
		GalaxyIcon.BorderStringToNum["ZZZB"] = GalaxyIcon.BORDER_ZZZB
		GalaxyIcon.BorderStringToNum["BZZZ"] = GalaxyIcon.BORDER_BZZZ
		GalaxyIcon.BorderStringToNum["ZBZZ"] = GalaxyIcon.BORDER_ZBZZ
		GalaxyIcon.BorderStringToNum["ZZBZ"] = GalaxyIcon.BORDER_ZZBZ
	
		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_ZZZZ.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_ZZZZ,TextureHandle,0,0,127,127)
		GalaxyIcon.BorderStringToNum["ZZZZ"] = GalaxyIcon.BORDER_ZZZZ

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/Border_IXXX.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_IXXX,TextureHandle,0,0,127,127)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_XIXX,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_HORIZONTAL)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_XXIX,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_180)
		UniverseIcons.SetIconLocation(GalaxyIcon.BORDER_XXXI,TextureHandle,0,0,127,127,App.TGIconGroup.ROTATE_0, App.TGIconGroup.MIRROR_VERTICAL)
		GalaxyIcon.BorderStringToNum["IXXX"] = GalaxyIcon.BORDER_IXXX
		GalaxyIcon.BorderStringToNum["XIXX"] = GalaxyIcon.BORDER_XIXX
		GalaxyIcon.BorderStringToNum["XXIX"] = GalaxyIcon.BORDER_XXIX
		GalaxyIcon.BorderStringToNum["XXXI"] = GalaxyIcon.BORDER_XXXI

		TextureHandle = UniverseIcons.LoadIconTexture("scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Icons/StellarAuraWide.tga")
		UniverseIcons.SetIconLocation(GalaxyIcon.SYSTEM_SPHERE_WIDE,TextureHandle,0,0,255,255)


	def GetPane(self):
		return self.Dict[GalaxyIcon.MAIN_PANE]

	def Close(self):
		## Remove the handler
		self.RemoveHandler( GetGame().GetMouseEventType() , 'MousePressed' )

	def MousePressed(self,gEvent):
		## Get data
		if not gEvent.IsButtonEvent():
			return
		
		## Correct move ?
		oFlags = gEvent.GetFlags()
		if not (	(App.TGMouseEvent.MEF_BUTTON_LEFT & oFlags) and
				(App.TGMouseEvent.MEF_BUTTON_DOWN & oFlags) 		):
			return

		## Place
		fX,fY = gEvent.GetX(),gEvent.GetY()

		## Is it in our spot ?
		pPane = self.Dict[GalaxyIcon.MAIN_PANE]
		
		## The window
		global GALAXY_ICON_REAL_X,GALAXY_ICON_REAL_Y
		fXa,fYa = GALAXY_ICON_REAL_X,GALAXY_ICON_REAL_Y
		
		## Translate
		fX = fX - fXa 
		fY = fY - fYa
				
		## Outside the window ?
		if not Square(0,0,self.W,self.H).Contains(fX,fY):
			return

		print str(fX) + ' , ' + str(fY)
		
		## Now match to our defined Squares
		for pSquare in self.lSquares:
			## A matching square?
			if pSquare.Contains(fX,fY):
				## Found it
				GetStarCharts().updateTargetSystem( pSquare.GetSolar() )
				print 'Match, '+str(pSquare.GetSolar())						
				return
		print 'No Match'			
		

	def display(self,iX,iY,iNum):
		#This creates a specific view of the galaxy for several sectors
		if iNum < 1:
			return

		## Add a handler for mouse events
		self.AddHandler( GetGame().GetMouseEventType() , 'MousePressed' )

		#Get the pane where the tags will go to
		pPane=self.Dict[GalaxyIcon.SYSTEM_PANE]

		#Load LCARS
		pMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pMode.GetLcarsString()
		
		## Smaller font
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,4)

		#Delete all previous TAGS
		pPane.KillChildren()
	
		#Determine the sectorcube dimensions
		x=self.W/iNum
		y=x/pMode.GetPixelWidth()*pMode.GetPixelHeight()
		w=x*GalaxyIcon.TAG_SCALE
		h=y*GalaxyIcon.TAG_SCALE

		## Reset the squares
		self.lSquares = []

		## Rectangle
		iAX = iX - iNum / 2
		iBX = iX + iNum / 2		
		iAY = math.floor(iY + self.H/y/2.0)
		iBY = math.floor(iY - self.H/y/2.0)			

		## Update the grid
		self.Dict[GalaxyIcon.GRID].display(Grid.TILE_XY,x)
		
		## Get the solars
		lSolars = GetUniverse().GetSectorRectangleSolars(iAX,iBY,iBX,iAY)

		for pSolar in lSolars:		
			if pSolar:
				## Location
				V = pSolar.GetLoc()
				
				lSuns=pSolar.GetAllSuns()
				iSuns=len(lSuns)

				# Racecolour
				cColour = pSolar.GetRace().GetColour()
		
				#Now position the tag and text according to the position on the map
				tX = V.GetX() - iAX
				tY =(V.GetY() - iAY) * (-1.0)

				# Name
				sName = pSolar.GetName()

				#Create a solar tag:
				#Modify the seize of the tag according to the primary star
				w=x*GalaxyIcon.TAG_SCALE
				h=y*GalaxyIcon.TAG_SCALE			

				if pSolar.IsExactTypeOf(SOLAR):
					if iSuns>=1:
						w=x*GalaxyIcon.TAG_SCALE*MagnitudeToScale[lSuns[0].GetMagnitude()]
						h=y*GalaxyIcon.TAG_SCALE*MagnitudeToScale[lSuns[0].GetMagnitude()]

						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_0)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[0].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

					if iSuns>=2:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_Z)
						pIcon.Resize(w,h)
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
				
					if iSuns==2:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_1)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[1].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
					
					elif iSuns==3:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_2A)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[1].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_2B)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[2].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

					elif iSuns==4:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_3A)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[1].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_3B)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[2].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_3C)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[3].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

					elif iSuns==5:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_4A)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[1].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_4B)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[2].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_4C)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[3].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_4D)
						pIcon.Resize(w,h)
						pIcon.SetColor(lSuns[4].GetColour())
						pPane.AddChild(pIcon)
						pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

				elif pSolar.IsTypeOf(STARBASE_SYSTEM):
					if pSolar.GetClass() == StarbaseSystem.OUTPOST:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_TRIANGLE)
					elif pSolar.GetClass() == StarbaseSystem.STARBASE:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_CIRCLE)
					elif pSolar.GetClass() == StarbaseSystem.COMM:
						pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_DOTTED_TRIANGLE)
					pIcon.Resize(w,h)
					pPane.AddChild(pIcon)
					pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

					#Use short names for starbases
					sName = pSolar.GetShortName()

				elif pSolar.IsTypeOf(BLACKHOLE_SYSTEM):
					pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_BLACKHOLE_1)
					w=x*GalaxyIcon.TAG_SCALE*3.0
					h=y*GalaxyIcon.TAG_SCALE*3.0
					pIcon.Resize(w,h)
					pPane.AddChild(pIcon)
					pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)
				
								
				else:
					pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_TAG_TRIANGLE)
					pIcon.Resize(w,h)
					pIcon.SetColor(RED)
					pPane.AddChild(pIcon)
					pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

				## Define the square and log it
				pSquare = Square(x*tX-w/2.0,y*tY-h/2.0,x*tX+w/2.0,y*tY+h/2.0,pSolar)
				self.lSquares.append(pSquare)

				# Modify the text
				if iNum < GalaxyIcon.NAME_SWAP_THRESHOLD:
					#Create a solar text:
					pText = App.TGParagraph_Create(sName)
					pText.RecalcBounds()
					pPane.AddChild(pText)
					pTextColour = copyColour(cColour)
					PasteliseColour(pTextColour,0.45)
					pText.SetColor(pTextColour)
					pText.SetPosition(pIcon.GetLeft(),pIcon.GetTop()-pText.GetHeight())

		# Display the nebulas
		pNebulaPane = self.Dict[GalaxyIcon.NEBULA_PANE]
		pNebulaPane.KillChildren()
		
		Nebulas = GetUniverse().GetNebulas()
		for Nebula  in Nebulas:
			#Check if the system falls on the map
			V=Nebula.GetLoc()
			if V.GetX() <= iAX-w or V.GetX() >= iBX+w or V.GetY()>=iAY+h or V.GetY()<=iBY-h:
				#Out of map
				continue

			# Now position the tag and text according to the position on the map
			tX = V.GetX() - iAX
			tY =(V.GetY() - iAY) * (-1.0)

			# Add a aurasphere
			w = x*Nebula.GetRadius()*2.5
			h = y*Nebula.GetRadius()*2.5

			## Create the sphere
			pIcon  = App.TGIcon_Create("ShipIcons",Nebula.GetIconID())
			pIcon.Resize(w,h)
			pNebulaPane.AddChild(pIcon)
			pIcon.SetPosition(x*tX-w/2.0,y*tY-h/2.0)

			## The name
			if iNum < GalaxyIcon.NAME_SWAP_THRESHOLD:
				pText = App.TGParagraph_Create(Nebula.GetName())
				pText.SetColor(Colour(0.9,0.9,0.9,1.0))
				pText.RecalcBounds()
				pNebulaPane.AddChild(pText)
				pText.SetPosition(pIcon.GetLeft(),pIcon.GetTop()-pText.GetHeight())

		
		## We iterate through all available systems:
		pSherePane = self.Dict[GalaxyIcon.SPHERE_PANE]
		pSherePane.KillChildren()
		
		## Compose a bordermatrix
		f  = 2
		g  = f * 2.0
		XX = self.W/iNum
		YY = XX/pMode.GetPixelWidth()*pMode.GetPixelHeight()
		heu = sqrt(2.0)
		w = XX/f * heu
		h = YY/f * heu
		# Matrix = GetUniverse().Borderise(iAX,iAY,iNum,f)
		for x in range(iAX,iAX+iNum):
			break
			for y in range(iAY-iNum+1,iAY+1):
				cell = Matrix[x,y]
				for i in range(f):
					xx = x + (1.0+2.0*i)/g
					for j in range(f):
						yy = y - (1.0+2.0*j)/g
						CSW,CSE,CNE,CNW,CC,RSW,RSE,RNE,RNW = cell[i][j]
						
						## Race controlling the subsector
						pRace = GetByID(CC)
						c =None
						if pRace:
							c = pRace.GetColour()
						
						## Gfx string
						s = CSW+CSE+CNE+CNW					

						## Some dimensions
						tX = xx - iAX
						tY =(yy - iAY) * (-1.0)

						## The main icon
						if pRace:
							pIconID = GalaxyIcon.BorderStringToNum[s]
							pIconID = GalaxyIcon.SYSTEM_SPHERE_WIDE
							pIcon  = App.TGIcon_Create("ShipIcons",pIconID)
							c.a = 0.85
							pIcon.SetColor(c)
							pIcon.Resize(w,h)
							pSherePane.AddChild(pIcon)
							pIcon.SetPosition(XX*tX-w/2.0,YY*tY-h/2.0)

						## Grid point sphere
						if pRace:
							for xxx,yyy,char in ((xx-1/g,yy+1/g,CNW),(xx+1/g,yy+1/g,CNE),(xx+1/g,yy-1/g,CSE),(xx-1/g,yy-1/g,CSW)):
								if char == 'Z':
									pIconID = GalaxyIcon.BorderStringToNum[s]
									pIconID = GalaxyIcon.SYSTEM_SPHERE_WIDE
									pIcon  = App.TGIcon_Create("ShipIcons",pIconID)
									c.a = 0.75
									pIcon.SetColor(c)
									pIcon.Resize(w,h)
									pSherePane.AddChild(pIcon)

									## Some dimensions
									ttX = xxx - iAX
									ttY =(yyy - iAY) * (-1.0)
									pIcon.SetPosition(XX*ttX-w/2.0,YY*ttY-h/2.0)
							

						## Incursion Icons
						for race,gfx in ((RSW,"IXXX"),(RSE,"XIXX"),(RNE,"XXIX"),(RNW,"XXXI")):
							if race == 0:
								continue							
							pIconID = GalaxyIcon.BorderStringToNum[gfx]
							pIconID = GalaxyIcon.SYSTEM_SPHERE
							pOtherRace = GetByID(race)								
							pIcon  = App.TGIcon_Create("ShipIcons",pIconID)
							c = pOtherRace.GetColour()
							c.a = 0.85
							pIcon.SetColor(c)
							pIcon.Resize(w,h)
							pSherePane.AddChild(pIcon)
							pIcon.SetPosition(XX*tX-w/2.0,YY*tY-h/2.0)


		XX = self.W/iNum
		YY = XX/pMode.GetPixelWidth()*pMode.GetPixelHeight()
		pUniverse = GetUniverse()
		for x in range(iAX,iAX+iNum):
			for y in range(iAY-iNum+1,iAY+1):
				pSolars = pUniverse.GetExactSolarGroup(x,y)

				for pSolar in pSolars:
					pRace = pSolar.GetRace()
					if pRace.ID == ARCHITECT_ID:
						continue
					V = pSolar.GetLoc()

					#Now position the tag according to the position on the map
					tX = V.GetX() - iAX
					tY =(V.GetY() - iAY) * (-1.0)
	
					# Add an aurasphere
					w = XX*GalaxyIcon.AURA_SCALE*pSolar.GetWeight()
					h = YY*GalaxyIcon.AURA_SCALE*pSolar.GetWeight()

					# Racecolour
					c = pRace.GetColour()									

					## Create the sphere
					pIcon  = App.TGIcon_Create("ShipIcons",GalaxyIcon.SYSTEM_SPHERE)
					pIcon.Resize(w,h)
					pIcon.SetColor(c)
					pSherePane.AddChild(pIcon)
					pIcon.SetPosition(XX*tX-w/2.0,YY*tY-h/2.0)
		
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])


class Square:

	def __init__(self,fXa,fYa,fXb,fYb,pSolar=None):
		if fXa > fXb:
			fXa,fXb=fXb,fXa
		if fYa > fYb:
			fYa,fYb=fYb,fYa
		self.fXa = fXa
		self.fXb = fXb
		self.fYa = fYa
		self.fYb = fYb
		if pSolar:
			self.iSolar = pSolar.ID
		else:
			self.iSolar = 0

	def GetSolar(self):
		return GetByID(self.iSolar)
	
	def Contains(self,fX,fY):
		if fX < self.fXa:
			return FALSE
		if fX > self.fXb:
			return FALSE
		if fY < self.fYa:
			return FALSE
		if fY > self.fYb:
			return FALSE
		return TRUE 


class Grid:
	TILE_X     = 0
	TILE_Y     = 2
	TILE_XY    = 1
	TILE_SCALE = 0.0025
		
	def __init__(self,W,H,cColour=WHITE):
		self.W=W
		self.H=H
		self.List=[]
		self.Colour=cColour
			
		#Create the main pane
		pPane=App.TGPane_Create(self.W,self.H)
		self.Pane=pPane

	def GetPane(self):
		return self.Pane
		
	def display(self,iState,fVal):
		if not (iState==Grid.TILE_X or iState==Grid.TILE_Y or iState==Grid.TILE_XY):
			return

		#Load LCARS
		pMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pMode.GetLcarsString()
		
		#Kill all previous lines
		self.Pane.KillChildren()
		self.List=[]
			
		#Iterate to place the lines
		w=Grid.TILE_SCALE*self.W
		h=w/pMode.GetPixelWidth()*pMode.GetPixelHeight()
		X=fVal
		Y=fVal/pMode.GetPixelWidth()*pMode.GetPixelHeight()

		fPos=0.0
		if iState==Grid.TILE_X or iState==Grid.TILE_XY:
			while fPos<=self.W:			
				pIcon  = App.TGIcon_Create(pcLCARS,200,self.Colour)
				self.List.append(pIcon)
				self.Pane.AddChild(pIcon,0.0,0.0)
				pIcon.Resize(w,self.H)
				pIcon.SetPosition(fPos-w/2.0,0.0)

				fPos=fPos+X
								
		fPos=0.0
		if iState==Grid.TILE_Y or iState==Grid.TILE_XY:
			while fPos<=self.H:
				pIcon  = App.TGIcon_Create(pcLCARS,200,self.Colour)
				self.List.append(pIcon)
				self.Pane.AddChild(pIcon,0.0,0.0)
				pIcon.Resize(self.W,h)
				pIcon.SetPosition(0.0,fPos-h/2.0)

				fPos=fPos+Y

		
					
def CreateInterfaceButton(pName,eType,sFunctionHandler,fWidth,fHeight):
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(eType)

	App.g_kEventManager.RemoveBroadcastHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)

	return (App.STRoundedButton_Create(pName,pEvent, fWidth, fHeight))

def CreateIntButton(pName,iVal,eType,sFunctionHandler,fWidth=0.0,fHeight=0.0):
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetInt(iVal)

	App.g_kEventManager.RemoveBroadcastHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)

	if fWidth==0.0 or fHeight==0.0:
		return (App.STButton_Create(pName,pEvent))
	else:	
		return (App.STRoundedButton_Create(pName,pEvent, fWidth, fHeight))

def CreateSlider(pName,eType,sFunctionHandler,fValue,Window):
	#A great experiment...
	pBar = App.STNumericBar_Create ()

	pBar.SetRange(0.0,10.0)
	pBar.SetKeyInterval(0.02)
	pBar.SetMarkerValue(1.0)
	pBar.SetValue(fValue)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	kNormalColor = App.g_kSTMenu3NormalBase
	kEmptyColor  = App.g_kSTMenu3Disabled

	pBar.SetNormalColor(kNormalColor)
	pBar.SetEmptyColor(kEmptyColor)
	pText = pBar.GetText()
	pText.SetString("Warp Speed")
	
	pEvent = App.TGFloatEvent_Create ()
	pEvent.SetDestination(pBar)
	pEvent.SetFloat (fValue)
	pEvent.SetEventType(eType)
	
	#App.g_kEventManager.RemoveBroadcastHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)
	#App.g_kEventManager.AddBroadcastPythonFuncHandler(eType,App.Game_GetCurrentGame(),sFunctionHandler)
	App.g_kEventManager.RemoveBroadcastHandler(eType,Window,sFunctionHandler)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(eType,Window,sFunctionHandler)
	
	pBar.SetUpdateEvent(pEvent)

	return pBar


def InfoConstruction(pText,pSolar):
	pChar=""	
			
	#Collect Data
	fPop,iInh=0,0
	for pPlanet in pSolar.GetAllPlanets():
		fPop=fPop+pPlanet.GetPopulation()
		if pPlanet.GetPopulation()>0.0:
			iInh=iInh+1

	if pSolar.IsExactTypeOf(SOLAR) or pSolar.IsExactTypeOf(STARBASE_SYSTEM):
		#Political Data
		pChar=pChar+"Political Analysis:"+"\n"
		pChar=pChar+"Empire: "+str(pSolar.GetRace())+""
		pChar=pChar+"Total population: %2.2f billion" % (fPop)+""
		lpChar=pSolar.GetMeta()
		if len(lpChar)>0:
			pChar=pChar+"Special remarks:"+""
			for pTempChar in lpChar:
				pChar=pChar+"\t"+pTempChar+""
		
		pChar=pChar+""		

	# Military Data
	Fleets = pSolar.GetAllFleets()
	nShips = 0
	for Fleet in Fleets:
		nShips = nShips + Fleet.GetNumShips()
	
	pChar=pChar+"Military Analysis:"+""
	if pSolar.IsTypeOf(STARBASE_SYSTEM):
		pChar=pChar+"Primary base: "+pSolar.GetBase().GetName()+""
	pChar=pChar+"Number of fleets: "+str(len(Fleets))+""
	pChar=pChar+"Number of ships: "+str(nShips)+""
	if Fleets:
		pChar=pChar+"Fleets:"+""
		for Fleet in Fleets:
			pChar=pChar+"\t"+Fleet.GetName()+"\tShips: "+str(Fleet.GetNumShips())+"" 
	pChar=pChar+""
	
	if pSolar.IsExactTypeOf(SOLAR) or pSolar.IsExactTypeOf(BLACKHOLE_SYSTEM):
		#Sun info
		pChar=pChar+"Stellar Analysis:"+""
		pChar=pChar+"Type: "+NumToSumName[pSolar.GetNumAllSuns()]+""

		i=0
		for pSun in pSolar.GetAllSuns():
			i=i+1
			pChar=pChar+"Name of "+NumToEnumName[i]+": "+pSun.GetName()+""
			pChar=pChar+"Spectral Class: "+ClassToSpectral[pSun.GetClass()]+""
			pChar=pChar+"Absolute Magnitude: "+str(pSun.GetMagnitude())+""	
		pChar=pChar+""	

		## Specials
		lHolesA = pSolar.GetAllSolarWormholes() 
		lHolesB = pSolar.GetAllBlackholes()
		lHolesC = pSolar.GetInsideNebulas()
		if lHolesA or lHolesB or lHolesC:
			pChar=pChar+"Phenomena:"+""
		for pHole in lHolesA:
			pChar=pChar+'\t'+pHole.GetWormhole().GetName()+'\n'
		for pHole in lHolesB:
			pChar=pChar+'\t'+pHole.GetName()+'\n'
		for pHole in lHolesC:
			pChar=pChar+'\t'+pHole.GetName()+'\n'
		pChar=pChar+""
			
		#Planet Info
		pChar=pChar+"Planetary Analysis:"+""
		pChar=pChar+"Number of planets: "+str(pSolar.GetNumAllPlanets())+""
		pChar=pChar+"Inhabited planets: "+str(iInh)+""
						
		if pSolar.GetNumAllPlanets()!=0:
			pChar=pChar+"Planets:"
			for pPlanet in pSolar.GetAllPlanets():
				#print pPlanet
				if pPlanet.IsTypeOf(MOON):
					continue
				pName=pPlanet.GetName()
				pChar=pChar+pName
				pNumTabs=4-len(pName)/5
				if pNumTabs<0:
					pNumTabs=0
				pChar=pChar+pNumTabs*"\t"			
				pChar=pChar+"Class-"+pPlanet.GetClass()+"  Pop: %2.2f billion" % (pPlanet.GetPopulation())+""

				for pMoon in pPlanet.GetMoons():
					pChar=pChar+"\t"+pMoon.GetName()
					pNumTabs=3-len(pMoon.GetName())/5
					if pNumTabs<0:
						pNumTabs=0
					pChar=pChar+pNumTabs*"\t"			
					pChar=pChar+"Class-"+pMoon.GetClass()+"  Pop: %2.2f billion" % (pMoon.GetPopulation())+""
	
	pText.SetString(pChar)
	pText.Layout()	

def WarpSpeedToLyd(fVal):
	#Warpspeed to lightyears per day
	#Equations taken from http://www.stdimension.de/int/Cartography/index.htm
	alpha=1/365.0

	import math
	if fVal < 0:
		return 0.0
	elif fVal >=10.0:
		return 1.0e+20
	elif fVal <9.0:
		return math.pow(fVal,10.0/3.0)*alpha
	elif fVal>=9.0:
		return (math.pow(fVal,10.0/3.0)+pow(10.0-fVal,-11.0/3.0))*alpha