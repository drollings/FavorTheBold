import App
from ATP_Object import *

sMovieGfxFolder = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Movies'

class Movie(ATP_EventHandlerObject):

	def __init__(self,sMovieName,bSkippable = TRUE ,bEndGame = FALSE):
		## Superclass
		ATP_EventHandlerObject.__init__(self)

		## Attr's
		self.pSequence  = None
		self.sMovieName = sMovieName + '.bik'
		self.bEndGame   = bEndGame
		self.bMusicEnabled = TRUE
		self.bSkippable = bSkippable
		self.ET_MOVIE_DONE = GetNextEventType()
		

	def GetDoneEvent(self):
		return self.ET_MOVIE_DONE

	def Play(self):
		## Check if the movie exists
		import Foundation
		lsFileNames = Foundation.GetFileNames(sMovieGfxFolder,'bik')
		if not lsFileNames.count(self.sMovieName):
			## Illegal movie
			raise ImportError , 'ATP_universeMovies: Movie '+sMovieName+' not found'
		self.sMovieName = sMovieGfxFolder + '/' + self.sMovieName

		## Create a sequence
		self.pSequence = App.TGSequence_Create()		

		## Movies are not skippable
		self.pSequence.SetSkippable(self.bSkippable)
		if self.bSkippable:
			## Add a handler for skipactions
			self.AddHandler( App.ET_KEYBOARD , 'Abort' )			

		## Add the fade in action
		pAction = App.TGScriptAction_Create(__name__,'FadeIn', self.ID)
		self.pSequence.AddAction(pAction)		

		## Add the movie load action
		pAction = App.TGMovieAction_Create(self.sMovieName , 1, 1)
		pAction.SetSkippable(self.bSkippable)
		self.pSequence.AppendAction(pAction)	

		## Add the fade out action
		pAction = App.TGScriptAction_Create(__name__,'FadeOut', self.ID)
		self.pSequence.AppendAction(pAction)
		
		## Endgame ?
		if self.bEndGame:
			## Endgame
			pAction = App.TGScriptAction_Create("MissionLib", "ExitGame")
			self.pSequence.AppendAction(pAction,0.5)		
		else:
			## Unload
			pAction = App.TGScriptAction_Create(__name__,'Unload', self.ID)
			self.pSequence.AppendAction(pAction,0.5)

		## Lights, camera, action !!
		self.pSequence.Play()

		## ok
		return FALSE

	def FadeIn(self):
		## Pause the game.
		App.g_kUtopiaModule.Pause(TRUE)

		## Was there music allowed ?		
		self.bMusicEnabled = App.g_kMusicManager.IsEnabled()

		## Stop music.
		App.g_kMusicManager.SetEnabled(0)

		## Topwindow hiding
		pTopWindow = App.TopWindow_GetTopWindow()
		if pTopWindow:
			## Not visible
			pTopWindow.SetNotVisible()

			## Disable options menu
			pTopWindow.DisableOptionsMenu (1)

			## Mouse
			pTopWindow.AllowMouseInput(0)	

			## Keyboard
			if not self.bSkippable:
				pTopWindow.AllowKeyboardInput(0)

	def FadeOut(self):
		## Pause the game.
		App.g_kUtopiaModule.Pause(FALSE)

		## Unpause the game.
		App.g_kMusicManager.SetEnabled(self.bMusicEnabled)

		## Switch out of moviemode
		App.g_kMovieManager.SwitchOutOfMovieMode()

		## Topwindow hiding
		pTopWindow = App.TopWindow_GetTopWindow()
		if pTopWindow:
			## Visible
			pTopWindow.SetVisible()

			## Undisable options menu
			pTopWindow.DisableOptionsMenu (0)
			pTopWindow.AllowKeyboardInput(1)
			pTopWindow.AllowMouseInput(1)

	def Abort(self,gEvent):
		## Forced fade-out
		self.FadeOut()

		## Unload
		self.Unload()

	def Unload(self):
		## Unload the sequence	
		if self.pSequence:
			self.pSequence.Destroy()
		self.pSequence = None

		## Raise a done event
		self.Raise(self.ET_MOVIE_DONE)

		## Unload ourself
		self.delete()
		

def FadeIn(pAction, IDmovie):
	pMovie =GetByID(IDmovie)
	if pMovie:
		pMovie.FadeIn()
	return 0

def FadeOut(pAction, IDmovie):
	pMovie =GetByID(IDmovie)
	if pMovie:
		pMovie.FadeOut()
	return 0

def Unload(pAction, IDmovie):
	pMovie =GetByID(IDmovie)
	if pMovie:
		pMovie.Unload()
	return 0