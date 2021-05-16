# Favor the Bold, March 2004 TOSFederation pack release

import Foundation

__version__ = 20040318

dMode = { 'modes': [ Foundation.MutatorDef.FTB ] }

Foundation.Federation.TOSmusic = Foundation.MusicDef()
Foundation.Federation.TOSmusic.dMain = {
	'sfx/Music/EpisGen2.mp3':		'Starting Ambient',
	'sfx/Music/Starbase12.mp3':		'Starbase12 Ambient',
	'Custom/FTB/Music/TOSFederation/Transition/Foreboding.mp3':		'Nebula Ambient',
	'Custom/FTB/Music/TOSFederation/Transition/TOS_Defeat.mp3':		'Lose',
	'Custom/FTB/Music/TOSFederation/Transition/CheeryInterlude_-_The_Doomsday_Machine_Violent_Shakes_24.mp3':		'Win',
	'Custom/FTB/Music/TOSFederation/Transition/PositiveInterlude.mp3':	'EnemyBlewUp',
	'Custom/FTB/Music/TOSFederation/Transition/TOS_Playerdeath.mp3':	'PlayerBlewUp',
}

Foundation.Federation.TOSmusic.AddFolder('Custom/Music/TOSFederation/Combat Confident', 'Combat Confident')
Foundation.Federation.TOSmusic.AddFolder('Custom/Music/TOSFederation/Combat Neutral', 'Combat Neutral')
Foundation.Federation.TOSmusic.AddFolder('Custom/Music/TOSFederation/Combat Panic', 'Combat Panic')

Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBTOSDisruptor.wav", "FTB TOS Disruptor", 0.4, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBTOSPhoton.wav", "FTB TOS Photon", 0.6, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/Blank.wav", "FTB TOS Phaser Start", 0.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBTOSPhaser.wav", "FTB TOS Phaser Loop", 0.15, dMode)


import Custom.FTB.ships.FTB_TOSConstitution

Foundation.ShipDef.FTBConstitution.music = Foundation.Federation.TOSmusic