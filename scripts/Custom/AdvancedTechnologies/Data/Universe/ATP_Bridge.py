import App

from ATP_Object import *

sSetsPath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Sets/'
sAnimPath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Animations/'


class Bridge(UniverseElement):

	def __init__(self,ID=0):
		## Superclass
		UniverseElement.__init__(self,ID)

		## Additional attr
		self.sBridgeType = 'Galaxy'
		self.pCam = None
		self.bSpaceSet = FALSE
		self.sStarGfx = GFX_PATH_STARS
		self.Node = None
		self.pBridge = None
		self.pSequence = None

		self.dCharacters = { }

	def Bind(self,pShip,sBridgeType):
		## Binds the bridge to a ship
		self.pShip = pShip

		## Remember the BridgeType
		self.sBridgeType = sBridgeType
		
		## Name
		self.sName = 'GenericBridge_'+str(self.ID)

		## Our race
		pRace = self.pShip.GetFleet().GetRace()

		## Create some characters (hhhm, not clean.....!!!!!!!!!)
		import ATP_Characters

		if not dBridges.has_key(self.sBridgeType):
			return

		pBridgeType = dBridges[self.sBridgeType]
		dict = pBridgeType.dLoc
		for key in dict.keys():
			lLocs = dict[key] 
			for sLoc in lLocs:
				pCharacter = ATP_Characters.Character()
				sHeadType,sBodyType,sName = pRace.GetCharacterData(key)
				if not (sHeadType and sBodyType):
					raise RuntimeError, 'character type \''+key+'\' not defined for race '+str(pRace)
				pCharacter.Bind(self,sName,sHeadType,sBodyType,sLoc)

	def Load(self):
		debug('begin rendering bridge '+self.sName)
		print 'begin rendering bridge '+self.sName

		pBridgeType = dBridges[self.sBridgeType]
		self.bSpaceSet = pBridgeType.bSpaceSet

		# Make a space or bridgeset ?
		if not self.Node:
			if self.bSpaceSet:
				## Spaceset	
				#############################

				## Create this needed file 
				from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
				open_save_file(sfilename=self.sName+'.py',sfilepath='scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\Dummy\\Bridges')		
				write_save_file('import App')
				write_save_file('def GetSet():')
				write_save_file('return App.g_kSetManager.GetSet(\''+self.sName+'\')',1)
				close_save_file()
			
				## Create the set
				self.Node = App.SetClass_Create()
				App.g_kSetManager.AddSet(self.Node,self.sName)

				## Save the name of the region file that's creating the set.
				self.Node.SetRegionModule('Custom.AdvancedTechnologies.Data.Universe.Dummy.Bridges.'+self.sName)

				## Activate the proximity manager for our set.
				self.Node.SetProximityManagerActive(1)

				## Load and place the grid.
				pGrid = App.GridClass_Create()
				self.Node.AddObjectToSet(pGrid, 'grid')
				pGrid.SetHidden(1)

				## Add a starbackdrop
				pStars = App.StarSphere_Create()
				pStars.SetName('Backdrop stars')
				pStars.SetTranslateXYZ(0.000000, 0.000000, 0.000000)		
				pStars.SetTextureFileName(self.sStarGfx)
				pStars.SetTargetPolyCount(256)#256
				pStars.SetHorizontalSpan(1.0)
				pStars.SetVerticalSpan(1.0)
				pStars.SetSphereRadius(300.0)
				pStars.SetTextureHTile(22.0)#22
				pStars.SetTextureVTile(11.0)#11
				pStars.Rebuild()
				self.Node.AddBackdropToSet(pStars,'Backdrop stars')
				pStars.UpdateNodeOnly()

				## Create ambient light source
				self.Node.CreateAmbientLight (1.0, 1.0, 1.0, 19.0, 'ambientlight1')

				## Place the backdropmodel
				self.pBridge = App.BridgeObjectClass_Create(pBridgeType.sGfx)
				self.Node.AddObjectToSet(self.pBridge, 'bridge')
				self.pBridge.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
				#self.pBridge.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

				## Camera
				pCamera = App.CameraObjectClass_Create(0, 0, 0, 0, 0, 0, 1, 'maincamera')
				self.Node.AddCameraToSet (pCamera, 'maincamera')
				pCamera.SetNearAndFarDistance(1.0, 800.0)
				pCamera.SetTranslateXYZ(pBridgeType.vCam.GetX(), pBridgeType.vCam.GetY(), pBridgeType.vCam.GetZ())
				pCamera.AlignToVectors(pBridgeType.vCamForward,pBridgeType.vCamUp)	
				self.pCam = pCamera

			else:
				## Bridgeset
				#######################

				## Create the set
				self.Node = App.SetClass_Create()
				App.g_kSetManager.AddSet(self.Node,self.sName)

				## Create ambient light source
				self.Node.CreateAmbientLight (1.0, 1.0, 1.0, 19.0, 'ambientlight1')

				## Tell the set what background model to use
				self.Node.SetBackgroundModel(pBridgeType.sGfx, 0.0, 0.0, 0.0)

				## Camera
				pCamera = App.CameraObjectClass_Create(pBridgeType.vCam.GetX(), pBridgeType.vCam.GetY(), pBridgeType.vCam.GetZ(), 0, 0, 0, 1, 'maincamera')
				pCamera.AlignToVectors(pBridgeType.vCamForward,pBridgeType.vCamUp)
				self.Node.AddCameraToSet (pCamera, 'maincamera')
				pCamera.SetNearAndFarDistance(1.0, 800.0)
				
				self.pCam = pCamera


		debug('savepoint rendering bridge'+self.sName)

		## Character
		for pCharacter in self.GetCharacters():
			pCharacter.Render(self.Node)

		## Add a clock to unrender us when not active
		self.AddClock('PulsedUnrender',20.0)

		debug('end rendering bridge'+self.sName)

	def PulsedUnrender(self,gEvent):
		## Active?
		if self.pSequence:
			return

		## Remove clock
		self.RemoveClock('PulsedUnrender',gEvent.GetEventType())

		## Unrender
		self.Unrender()
	
	def Unrender(self):
		debug('begin unrendering bridge '+self.sName)

		## Upperclass
		UniverseElement.Unrender(self)

		## Delete the set
		App.g_kSetManager.RemoveSet(self.sName)
		self.Node = None

		debug('end unrendering bridge '+self.sName)	

	def Render(self,pSet):
		pass
	def Randomise(self,type=UNIVERSE_ELEMENT,radix=1.1,fMinAngle=0.0,fMaxAngle=360.0):
		pass
	def Enhance(self):
		pass
	def AssignAI(self,kArgs,force=TRUE):
		pass

	def GetEnterBridgeActionPath(self):
		pBridgeType = dBridges[self.sBridgeType]
		return pBridgeType.sEnterWalk

	def GetDoorActionPath(self):
		pBridgeType = dBridges[self.sBridgeType]
		return pBridgeType.sDoorOpen

	def GetBridgeObject(self):
		return self.pBridge

	def Contact(self):
		## Render us
		self.Load()	

		## Create a sequence
		self.pSequence = App.TGSequence_Create()		

		## Add the openchannel action
		pAction = App.TGScriptAction_Create(__name__,'OpenChannel', self.ID)
		self.pSequence.AddAction(pAction)		
		
		## Sound
		pAction = App.TGSoundAction_Create('ViewOn')
		self.pSequence.AppendAction(pAction)

		## Close the channel
		pAction = App.TGScriptAction_Create(__name__,'CloseChannel', self.ID)
		self.pSequence.AppendAction(pAction,10.0)

		## Play the Viewscreen off sound
		pAction = App.TGSoundAction_Create('ViewOff')
		self.pSequence.AppendAction(pAction)

		## Unload
		pAction = App.TGScriptAction_Create(__name__,'Unload', self.ID)
		self.pSequence.AppendAction(pAction)

		## Play
		self.pSequence.Play()

	def OpenChannel(self):
		## Get the playerbridge
		pBridge = GetPlayerBridge().Node
		pViewScreen = pBridge.GetViewScreen()
		pTop = App.TopWindow_GetTopWindow()

		## Static 
		fMinStatic, fMaxStatic = 0.0 , 0.0

		## Needed ?
		pZoomCamera = GetCameraManager().GetBridgeCamera()
		if pTop.IsCutsceneMode():
			pZoomCamera.LookForward()
			if (pTop.IsBridgeVisible()):
				import BridgeHandlers
				BridgeHandlers.DropMenusTurnBack()

		## Setup the cam
		pViewScreen.SetRemoteCam(self.pCam)
		pViewScreen.SetIsOn(1)
			
		## Some static
		if (fMaxStatic > 0):
			pViewScreen.SetStaticTextureIconGroup('View Screen Static')
			pViewScreen.SetStaticIsOn(1)
			pViewScreen.SetStaticVariation(fMinStatic, fMaxStatic)

	def CloseChannel(self):			
		## Restore the viewscreen
		pCamera = GetCameraManager().GetPlayerCamera()
		if not pCamera:
			return

		## Reset the Viewscreen
		pBridge = GetPlayerBridge().Node
		if pBridge:
			pViewScreen = pBridge.GetViewScreen()
			if pViewScreen:
				pViewScreen.SetRemoteCam(pCamera)
				pViewScreen.SetIsOn(1)

				# If the static in on, turn it off
				if pViewScreen.IsStaticOn():
					pViewScreen.SetStaticIsOn(0)

	def Unload(self):
		## Unload the sequence	
		if self.pSequence:
			self.pSequence.Destroy()
		self.pSequence = None

	def GetCaptain(self):
		return self.GetDirectChildByName('Captain')
	def GetCommander(self):
		return self.GetDirectChildByName('Commander')
	def GetHelm(self):
		return self.GetDirectChildByName('Helm')
	def GetTactical(self):
		return self.GetDirectChildByName('Tactical')
	def GetEngineer(self):
		return self.GetDirectChildByName('Engineer')
	def GetScience(self):
		return self.GetDirectChildByName('Science')
	def GetGuest(self):
		return self.GetDirectChildByName('Guest')
	def GetExtras(self):
		return self.GetDirectChildrenByName('Extras')


## Ugly but needed

def OpenChannel(pAction,ID):
	pBridge = GetByID(ID)
	if pBridge:
		pBridge.OpenChannel()
	return 0

def CloseChannel(pAction,ID):
	pBridge = GetByID(ID)
	if pBridge:
		pBridge.CloseChannel()
	return 0

def Unload(pAction,ID):
	pBridge = GetByID(ID)
	if pBridge:
		pBridge.Unload()
	return 0

def SynchroniseWithGame(sBridgeType = 'Galaxy'):
	## Create a wrapper for the playerbridge
	pBridge = Bridge(PLAYER_BRIDGE_ID)
	pBridge.Bind(GetPlayerShip(),sBridgeType)
	pBridge.Node = App.BridgeSet_Cast(App.g_kSetManager.GetSet('bridge'))
	pBridge.pCam = App.ZoomCameraObjectClass_GetObject(pBridge.Node, 'maincamera')
	pBridge.pBridge = App.BridgeObjectClass_GetObject (pBridge.Node, 'bridge')



class BridgeType:

	def __init__(self,sGfx,vCam,vCamForward,vCamUp,dLoc,sEnterWalk='',sDoorOpen='',bSpaceSet=FALSE):
		## Attr
		self.sGfx = sGfx[:]
		self.vCam = copyVector(vCam)		
		self.vCamForward = copyVector(vCamForward)
		self.vCamUp = copyVector(vCamUp)
		self.dLoc = dLoc
		self.bSpaceSet = bSpaceSet
		self.sEnterWalk	= sEnterWalk
		self.sDoorOpen = sDoorOpen


dBridges = {	'Galaxy' :	BridgeType(	'data/Models/Sets/DBridge/DBridge.nif',
						Vector(0.0,-200.0,46.0),
						Vector(0.0,1.0,0.0),
						Vector(0.0,0.0,1.0),
						{ 	'Captain': 	('data/animations/GalaxySeated01.nif',),
							'Commander':	('data/animations/db_stand_c_m.nif',),
							'Helm':		('data/animations/db_stand_h_m.nif',),
							'Tactical': 	('data/animations/db_stand_t_l.nif',),
							'Engineer':	('data/animations/db_EtoL1_s.nif',),
							'Science':	('data/animations/db_StoL1_S.nif',),
							'Guest': 	('data/animations/Seated_P.nif',)
						},
						sEnterWalk = 'data/animations/db_camera_walk_capt.nif',
						sDoorOpen  = 'data/animations/DB_Door_L1.nif'
				),

		'Sovereign' :	BridgeType(	'data/Models/Sets/EBridge/EBridge.nif',
						Vector(0.0,-200.0,46.0),
						Vector(0.0,1.0,0.0),
						Vector(0.0,0.0,1.0),
						{ 	'Captain': 	('data/animations/SovereignSeated01.NIF',),
							'Commander':	('data/animations/EB_stand_c_m.nif',),
							'Helm':		('data/animations/EB_stand_h_m.nif',),
							'Tactical': 	('data/animations/EB_stand_t_l.nif',),
							'Engineer':	('data/animations/EB_stand_e_s.nif',),
							'Science':	('data/animations/EB_stand_s_s.nif',),
							'Guest': 	('data/animations/EB_stand_X_m.nif',)
						},
						sEnterWalk = 'data/animations/eb_camera_capt_walk.nif',
						sDoorOpen  = 'data/animations/EB_Door_L1.nif'
				),

		'Marauder' :	BridgeType(	'data/Models/Sets/Ferengi/ferengibridge.nif',
						Vector(0.0,-52.0,45.0),
						Vector(0.0,1.0,0.0),
						Vector(0.0,0.0,1.0),
						{ 	'Captain': 	('data/animations/FerengiSeated01.NIF',)
						}
				),

		'FedBase' :	BridgeType(	'data/Models/Sets/FedOutpost/fedoutpost.nif',
						Vector(307.197021, 8.186405, 59.336189),
						Vector(-0.882600, 0.462577, -0.083906),
						Vector(0.0,0.0,1.0),
						{ 	'Commander': 	('data/animations/FedOutpostSeated01.NIF',)
						}
					),

		'Conference' :	BridgeType(	sSetsPath + 'Conference/Conference.nif',
						Vector(30.519501, 47.792694, 55.491398),
						Vector(-0.942035, -0.273277, -0.194655),
						Vector(-0.181065, -0.074355, 0.980656),
						{ 	'Admiral': 	(sAnimPath + 'Conference_Rombaut_Seated.NIF',)
						},
						
					),

		'Warbird' :	BridgeType(	'data/Models/Sets/Romulan/romulanbridge.nif',
						Vector(0.0,-215.0,50.0),
						Vector(0.0,1.0,0.0),
						Vector(0.0,0.0,1.0),
						{ 	'Captain': 	('data/animations/RomulanSeated01.NIF',)
						},
						
					),

			
			
	   }


	
		
		
		

	
	