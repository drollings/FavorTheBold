import App
from ATP_Object import *

class AnimationManager(ATP_EventHandlerObject):

	def __init__(self,ID=0):
		## Upperclass
		ATP_EventHandlerObject.__init__(self,ANIMATION_MANAGER_ID)

		## A node
		self.Node = None

def SynchroniseWithGame():
	## Get the camera manager
	import App
	GetAnimationManager().Node = App.g_kAnimationManager
	

def Breathe(pCharacter):
	kAM = GetAnimationManager().Node
	kAM.LoadAnimation ("data/animations/breathing.NIF", "ATP_breathing")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "ATP_breathing", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence