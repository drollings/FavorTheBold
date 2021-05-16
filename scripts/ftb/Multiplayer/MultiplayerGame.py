import App
mpGameMode = None

def Initialize(pGame):
    import Foundation
    global mpGameMode
    # mpGameMode = Foundation.BuildGameMode()
    mpGameMode = Foundation.MutatorDef()
    mpGameMode.Update(Foundation.MutatorDef.FTB)
	mpGameMode.Activate()
    import LoadTacticalSounds
    LoadTacticalSounds.LoadSounds()
    pGame.LoadSound('sfx/redalert.wav', 'RedAlertSound', 0)
    pGame.LoadSound('sfx/yellowalert.wav', 'YellowAlertSound', 0)
    pGame.LoadSound('sfx/greenalert.wav', 'GreenAlertSound', 0)
    SetupMusic(pGame)
    App.g_kSetManager.ClearRenderedSet()
    pGame.LoadEpisode('Multiplayer.Episode.Episode')
    import Multiplayer.MultiplayerMenus
    Multiplayer.MultiplayerMenus.g_pClientButton.SetDisabled()
    Multiplayer.MultiplayerMenus.g_pHostButton.SetDisabled()
    Multiplayer.MultiplayerMenus.g_pExitButton.SetEnabled()


def SetupMusic(pGame):
    import DynamicMusic
    DynamicMusic.Initialize(pGame, (('sfx/Music/EpisGen3.mp3', 'Starting Ambient'), ('sfx/Music/Starbase12.mp3', 'Starbase12 Ambient'), ('sfx/Music/Nebula 1.mp3', 'Nebula Ambient'), ('sfx/Music/Panic-9a.mp3', 'Cbt Panic 1'), ('sfx/Music/Panic-9b.mp3', 'Cbt Panic 2'), ('sfx/Music/Panic-9c.mp3', 'Cbt Panic 3'), ('sfx/Music/Panic-9d.mp3', 'Cbt Panic 4'), ('sfx/Music/Panic-9e.mp3', 'Cbt Panic 5'), ('sfx/Music/Panic-9f.mp3', 'Cbt Panic 6'), ('sfx/Music/Panic-9g.mp3', 'Cbt Panic 7'), ('sfx/Music/Neutral-10i.mp3', 'Cbt Neutral 1'), ('sfx/Music/Neutral-10b.mp3', 'Cbt Neutral 2'), ('sfx/Music/Neutral-10c.mp3', 'Cbt Neutral 3'), ('sfx/Music/Neutral-10d.mp3', 'Cbt Neutral 4'), ('sfx/Music/Neutral-10e.mp3', 'Cbt Neutral 5'), ('sfx/Music/Neutral-10f.mp3', 'Cbt Neutral 6'), ('sfx/Music/Neutral-10g.mp3', 'Cbt Neutral 7'), ('sfx/Music/Neutral-10h.mp3', 'Cbt Neutral 8'), ('sfx/Music/Neutral-10a.mp3', 'Cbt Neutral 9'), ('sfx/Music/Confident-11a.mp3', 'Cbt Confident 1'), ('sfx/Music/Confident-11b.mp3', 'Cbt Confident 2'), ('sfx/Music/Confident-11c.mp3', 'Cbt Confident 3'), ('sfx/Music/Confident-11d.mp3', 'Cbt Confident 4'), ('sfx/Music/Confident-11e.mp3', 'Cbt Confident 5'), ('sfx/Music/Confident-11f.mp3', 'Cbt Confident 6'), ('sfx/Music/Confident-11g.mp3', 'Cbt Confident 7'), ('sfx/Music/Failure-8d.mp3', 'Lose'), ('sfx/Music/Success-12.mp3', 'Win')), (), (('Combat Panic', ('Cbt Panic 1', 'Cbt Panic 2', 'Cbt Panic 3', 'Cbt Panic 4', 'Cbt Panic 5', 'Cbt Panic 6', 'Cbt Panic 7')), ('Combat Neutral', ('Cbt Neutral 1', 'Cbt Neutral 2', 'Cbt Neutral 3', 'Cbt Neutral 4', 'Cbt Neutral 5', 'Cbt Neutral 6', 'Cbt Neutral 7', 'Cbt Neutral 8', 'Cbt Neutral 9')), ('Combat Confident', ('Cbt Confident 1', 'Cbt Confident 2', 'Cbt Confident 3', 'Cbt Confident 4', 'Cbt Confident 5', 'Cbt Confident 6', 'Cbt Confident 7'))), DynamicMusic.StandardCombatMusic)


def Terminate(pGame):
    mpGameMode.Deactivate()
    import DynamicMusic
    DynamicMusic.Terminate(pGame)
    import Multiplayer.MultiplayerMenus
    Multiplayer.MultiplayerMenus.g_pClientButton.SetEnabled()
    Multiplayer.MultiplayerMenus.g_pHostButton.SetEnabled()
    Multiplayer.MultiplayerMenus.g_pExitButton.SetDisabled()
    Multiplayer.MultiplayerMenus.HideMissionPane()
    App.g_kSetManager.DeleteAllSets()
