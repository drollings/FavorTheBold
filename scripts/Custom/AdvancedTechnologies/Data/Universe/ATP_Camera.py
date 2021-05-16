import App

from ATP_Object import *

class CameraManager(ATP_EventHandlerObject):

	def __init__(self,ID=0):
		## Upperclass
		ATP_EventHandlerObject.__init__(self,CAMERA_MANAGER_ID)

		## End trigger
		self.ET_DONE = GetNextEventType()

		## Anims
		self.dAnimations = {}
		self.bOnBridge   = TRUE

	def GetDoneEventType(self):
		return self.ET_DONE

	def UnloadAction(self):
		## Unload
		pAction = App.TGScriptAction_Create(__name__,'Unload', self.ID)
		return pAction

	def ShowBridgeAction(self):
		## Action
		pAction = App.TGScriptAction_Create(__name__,'ShowBridge', self.ID)
		return pAction

	def ShowSpaceAction(self):
		## Action
		pAction = App.TGScriptAction_Create(__name__,'ShowSpace', self.ID)
		return pAction

	def ShowNormalAction(self):
		## Action
		pAction = App.TGScriptAction_Create(__name__,'ShowNormal', self.ID)
		return pAction

	def Unload(self):
		## Unload the sequence	
		if self.pSequence:
			self.pSequence.Destroy()
		self.pSequence = None

		## Unload animations
		kAM = App.g_kAnimationManager
		for key in self.dAnimations.keys():
			kAM.FreeAnimation(key)
		self.dAnimations = {}

		## Raise a done event
		self.Raise(self.ET_DONE)

	def PlayChoise(self,bPlay=TRUE):
		if bPlay:
			## Play it
			self.pSequence.Play()
			return None
		else:
			## Return the sequence
			return self.pSequence

	def StartPlayerWarp(self,bPlay=TRUE):
		## Which set ?
		pSet = GetPlayerShip().GetSolar().Node
		pShip = GetPlayerShip().Node

		## Cimatic mode
		App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0).Play()

		## Set up the correct cutscene camera. Generate a side offset for the camera, for a little
		fSideOffset = (App.g_kSystemWrapper.GetRandomNumber(1400) - 700) / 100.0
		
		## A sequence
		self.pSequence = App.TGSequence_Create()
		pSeq = self.pSequence

		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", 
								 pSet.GetName(), "PreWarpCutsceneCamera"))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", 
											 pSet.GetName(), pShip.GetName()))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "AwayDistance", 100000.0))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "ForwardOffset", -7.0))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "SideOffset", fSideOffset))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "RangeAngle1", 230.0))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "RangeAngle2", 310.0))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "RangeAngle3", -10.0))
		pSeq.AddAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "SetModeAttribute",
											 pSet.GetName(), "PreWarpCutsceneCamera", "DropAndWatch",
											 "SetAttrFloat", "RangeAngle4", 10.0))
		pSeq.AddAction(App.TGScriptAction_Create("WarpSequence", "FixCamera", pSet.GetName(), "PreWarpCutsceneCamera"))

		## Handler to unload
		self.pSequence.AppendAction ( self.UnloadAction() , 0.5 )

		## Play?
		return self.PlayChoise(bPlay)		

	def EnterBridge(self,bPlay = TRUE):
		## Get the player bridge
		pBridge = GetPlayerBridge()
		
		## Animation paths
		sWalkPath = pBridge.GetEnterBridgeActionPath()
		sDoorPath = pBridge.GetDoorActionPath()
		sWalkAnim = pBridge.sName + 'WalkCameraToCapt'
		sDoorAnim = pBridge.sName + 'DoorOpen'

		## Valid paths?
		if not sWalkPath or not sDoorPath:
			print 'ATP_CameraManager::EnterBridge: Invalid animation paths.'
			return

		## Load animations
		kAM = GetAnimationManager().Node				
		kAM.LoadAnimation(sWalkPath,sWalkAnim)
		kAM.LoadAnimation(sDoorPath,sDoorAnim)

		## Register animations
		self.dAnimations[sWalkAnim] = 0
		self.dAnimations[sDoorAnim] = 0

		## A sequence
		self.pSequence = App.TGSequence_Create()

		## Take the bridge camera
		pCamera = self.GetBridgeCamera()

		## Force bridge visible
		self.pSequence.AddAction ( self.ShowBridgeAction() )		

		## Camera move.
		pAnimNode = pCamera.GetAnimNode()
		pAnimNode.UseAnimationPosition(sWalkAnim)
		pAnimAction = App.TGAnimAction_Create(pAnimNode, sWalkAnim, 1, 0, 0, 0)
		self.pSequence.AddAction(pAnimAction)
	
		## Open door.	
		pBridge = GetPlayerBridge()
		pDoorAction = App.TGScriptAction_Create('Actions.EffectScriptActions', 'LiftDoorAction', pBridge.GetBridgeObject(), sDoorAnim, 'LiftDoor')
		self.pSequence.AddAction (pDoorAction)

		## Speak action
		self.pSequence.AddAction ( GetPlayerBridge().GetScience().SpeakAction('CaptainOnTheBridge') )

		## Handler to unload
		self.pSequence.AppendAction ( self.UnloadAction() , 0.5 )
			
		## Play?
		return self.PlayChoise(bPlay)	

	def GetBridgeCamera(self):
		pBridge = GetPlayerBridge().Node
		pCamera = App.ZoomCameraObjectClass_GetObject(pBridge, 'maincamera')
		return pCamera

	def GetPlayerCamera(self):
		pGame = GetGame().Node
		pCamera = pGame.GetPlayerCamera()
		return pCamera

	def ShowBridge(self):
		pTopWindow = App.TopWindow_GetTopWindow()
		self.bOnBridge = pTopWindow.IsBridgeVisible()
		if not self.bOnBridge:
			pTopWindow.ForceBridgeVisible()

	def ShowSpace(self):
		pTopWindow = App.TopWindow_GetTopWindow()
		self.bOnBridge = pTopWindow.IsBridgeVisible()
		if self.bOnBridge: 
			pTopWindow.ForceTacticalVisible()

	def ShowNormal(self):
		pTopWindow = App.TopWindow_GetTopWindow()
		bOnBridge = pTopWindow.IsBridgeVisible()
		if self.bOnBridge and not bOnBridge:
			pTopWindow.ForceBridgeVisible()
		elif not self.bOnBridge and bOnBridge:
			pTopWindow.ForceTacticalVisible()


def Unload(pAction,ID):
	GetCameraManager().Unload()
	return 0

def ShowBridge(pAction,ID):
	GetCameraManager().ShowBridge()
	return 0

def ShowSpace(pAction,ID):
	GetCameraManager().ShowSpace()
	return 0

def ShowNormal(pAction,ID):
	GetCameraManager().ShowNormal()
	return 0


	
















