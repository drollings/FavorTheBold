import App
from ATP_Object import *

def Launch():
	## Create the universe if necessary
	UniverseGame()	

class UniverseGame(ATP_EventHandlerObject):

	def __init__(self):
		## Sync events
		import ATP_Object
		ATP_Object.SynchroniseWithGame()

		## Superclass
		ATP_EventHandlerObject.__init__(self,UNIVERSE_GAME_ID)

		## Sync with game
		self.Node = App.Game_GetCurrentGame()

		## Enable Profiling
		App.TGProfilingInfo_EnableProfiling()	

		## Add handler when the game terminates	
		self.AddHandler ( App.ET_EXIT_GAME , 'Terminate' )
		
		## Sync with foundation intercept
		try:
			import AI.FoundationAI
			AI.FoundationAI.speedBoost = (300000.0*3600.0/50000.0)*scale*500.0
			AI.FoundationAI.accelBoost = 90
		except ImportError:
			pass

		## Load the first phase
		self.AddDelay('LaunchPhaseAlpha',0.1)

	def LaunchPhaseAlpha(self,gEvent):
		## Sync with interface
		import ATP_UniverseInterface
		ATP_UniverseInterface.SynchroniseWithGame()

		## Create the animation manager
		import ATP_Animations
		ATP_Animations.AnimationManager()
		ATP_Animations.SynchroniseWithGame()

		## First load the playership
		# ...

		## Display the choose universe type
		import ATP_UniverseInterface
		pButton = ATP_UniverseInterface.ButtonInterface('Launch Universe' , self.ID , ATP_UniverseInterface.GetInterface('Commander') )

		## Launch the second phase on that click
		self.AddHandler( pButton.GetClickEventType() , 'LaunchPhaseBeta' )	

	def LaunchPhaseBeta(self,gEvent):
		self.LaunchPhaseGamma(None)	
		self.LaunchPhaseDelta(None)		
			
	def LaunchPhaseGamma(self,gEvent):
		## Create the Starcharts
		import ATP_Starcharts
		pStarChart = ATP_Starcharts.StarCharts()

		## Load the universe state
		import UniverseState.LoadUniverse
		UniverseState.LoadUniverse.LoadUniverse('Stardate510001')

		## Preload the ships
		import loadspacehelper
		lShips = GetPlayerShip().GetSolar().GetAllShips()
		for pShip in lShips:
			loadspacehelper.PreloadShip(pShip.sGfx, 1)

	def LaunchPhaseDelta(self,gEvent):
		## Remove the previous handlers
		self.PurgeHandlers()

		## Regulise the player
		GetPlayerShip().Regulise()	

		## Render that system
		GetPlayerShip().GetSolar().RenderAndRandomise()		
		
		## Camera Manager
		import ATP_Camera
		ATP_Camera.CameraManager()

		## Create the Systeminterface en interstellarinterface
		import ATP_UniverseInterface
		ATP_UniverseInterface.InterstellarInterface()	
		ATP_UniverseInterface.SystemInterface()			

		## Create the music
		import ATP_UniverseMusic
		pMusic = ATP_UniverseMusic.Music()

		## Sync the bridge
		import ATP_Bridge
		ATP_Bridge.SynchroniseWithGame()

		## Sync the characters
		import ATP_Characters
		ATP_Characters.SynchroniseWithGame()

		## Create the savefunction
		import ATP_UniverseInterface
		pSaffi = ATP_UniverseInterface.GetInterface('Commander')
		pButton = ATP_UniverseInterface.ButtonInterface( 'Save Universe' , self.ID , pSaffi )
		self.AddHandler( pButton.GetClickEventType() , 'Save' )
		pButton = ATP_UniverseInterface.ButtonInterface( 'Credits' , self.ID , pSaffi )
		self.AddHandler( pButton.GetClickEventType() , 'Credits' )

		## Delete the launch button
		pSaffi.GetInterface('Launch Universe').delete()

	def Credits(self,gEvent):
		## Load the movie
		import ATP_UniverseMovies
		pMovie = ATP_UniverseMovies.Movie('ATP_LOADING',bSkippable = FALSE)

		## Play it
		pMovie.Play()		

	def Save(self,gEvent):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *

		## All objects
		Dict = ATP_EventHandlerObject.Dict

		## Effective save
		open_save_file('Universe_000.py')
		write_save_file('#### SAVING UNIVERSE STATE ####')
		write_save_file('import App')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Object import *')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Vessels import *')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Starbase import *')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Shipyard import *')
		write_save_file('from Custom.AdvancedTechnologies.Data.Universe.ATP_Race import *')
		write_save_file('')
	
		keys = Dict.keys()
		keys.sort()
		for ID in keys:
			write_save_file('#### SAVING OBJECT WITH ID='+str(ID)+' ####')
			Dict[ID].save()
			write_save_file('#### DONE SAVING OBJECT WITH ID='+str(ID)+' ####\n')

		for ID in keys:
			write_save_file('#### POSTSAVING OBJECT WITH ID='+str(ID)+' ####')
			Dict[ID].post_save()
			write_save_file('#### DONE POSTSAVING OBJECT WITH ID='+str(ID)+' ####\n')
		
		write_save_file('#### FINISHED SAVING UNIVERSE STATE ####')
		
		## Done
		close_save_file()

	def GetMouseEventType(self):
		return App.ET_MOUSE

	def GetMission(self):
		import MissionLib
		return MissionLib.GetMission()

	def GameOver(self):
		pSequence = App.TGSequence_Create()
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ExitGame"))
		pSequence.Play()

	def Terminate(self,gEvent):
		## Terminate the universe

		### Delete all ATP_EventHandlerObjects
		# for ID in ATP_EventHandlerObject.Dict.keys():
		#	if ATP_EventHandlerObject.Dict.has_key(ID):
		#		ATP_EventHandlerObject.Dict[ID].exit_game_delete()
		ATP_EventHandlerObject.Dict = {}

		## Save the profiling data
		App.TGProfilingInfo_SaveRawData('DimensionProfile.txt')

		## End profiling
		App.TGProfilingInfo_Terminate()
	