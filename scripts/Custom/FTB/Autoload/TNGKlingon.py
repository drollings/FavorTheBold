# Favor the Bold, March 2004 Klingon pack release

import Foundation

__version__ = 20040318

dMode = { 'modes': [ Foundation.MutatorDef.FTB ] }

Foundation.Klingon.music = Foundation.MusicDef()
Foundation.Klingon.music.dMain = {
	'sfx/Music/EpisGen2.mp3':		'Starting Ambient',
	'sfx/Music/Starbase12.mp3':		'Starbase12 Ambient',
	'sfx/Music/Nebula 1.mp3':		'Nebula Ambient',
	'sfx/Music/Failure-8d.mp3':		'Lose',
	'sfx/Music/Success-12.mp3':		'Win',
	'sfx/Music/Transition 13.mp3':	'EnemyBlewUp',
	'sfx/Music/Transition 14.mp3':	'PlayerBlewUp',
}

Foundation.Klingon.music.AddFolder('Custom/Music/Klingon/Combat Confident', 'Combat Confident')
Foundation.Klingon.music.AddFolder('Custom/Music/Klingon/Combat Neutral', 'Combat Neutral')
Foundation.Klingon.music.AddFolder('Custom/Music/Klingon/Combat Panic', 'Combat Panic')

Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBKlingonPulseDisruptor.wav", "FTB Klingon Pulse", 0.8, dMode)
Foundation.SoundDef("sfx/Weapons/Disruptor Cannon.wav", "FTB Klingon Disruptor", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBKlingonDisruptorBeam_a.wav", "FTB Disruptor Beam Start", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBKlingonDisruptorBeam_b.wav", "FTB Disruptor Beam Loop", 0.3, dMode)
Foundation.SoundDef("sfx/Weapons/Klingon Torp.wav", "FTB Klingon Plasma", 0.4, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBKlingonPhotonTorp.wav", "FTB Klingon Torp", 0.8, dMode)
