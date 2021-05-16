 	# Favor the Bold, March 2004 Federation pack release

import Foundation

__version__ = 20040318

dMode = { 'modes': [ Foundation.MutatorDef.FTB ] }

Foundation.Federation.music = Foundation.MusicDef()

Foundation.Federation.music.dMain = {
	"Custom/Music/Federation/Transitions/EpisGen2.mp3":		"Starting Ambient",
	"sfx/Music/Starbase12.mp3":					"Starbase12 Ambient",
	"sfx/Music/Nebula 1.mp3":					"Nebula Ambient",
	"Custom/Music/Federation/Transitions/Episode 2.mp3":					"Lose",
	"sfx/Music/Success-12.mp3":					"Win",
	"Custom/Music/Federation/Transitions/EnemyDestroyed.mp3":	"EnemyBlewUp",
	"Custom/Music/Federation/Transitions/PlayerDestroyed.mp3":	"PlayerBlewUp",
}

Foundation.Federation.music.AddFolder("Custom/Music/Federation/Combat Confident", "Combat Confident")
Foundation.Federation.music.AddFolder("Custom/Music/Federation/Combat Neutral", "Combat Neutral")
Foundation.Federation.music.AddFolder("Custom/Music/Federation/Combat Panic", "Combat Panic")

Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBPhotonTorp.wav", "FTB Photon Torp", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBPulsePhaser.wav", "FTB C1 Pulse Phaser", 0.4, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBPulsePhaser.wav", "FTB Pulse Phaser", 0.4, dMode)
Foundation.SoundDef("sfx/Weapons/Quantum Torp.wav", "FTB Quantum Torp", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBPulsePhaser.wav", "FTB Antimatter", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBPulsePhaser.wav", "FTB Antimatter", 1.0, dMode)
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBIntrepidPhaser_a.wav", "Intrepid Phaser Start", 1.0, dMode )
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBIntrepidPhaser_b.wav", "Intrepid Phaser Loop", 1.0, dMode )

Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBFastPhaser_a.wav", "FTB Phaser Emitter Start", 0.3, dMode )
Foundation.SoundDef("Custom/FTB/Sfx/Weapons/FTBIntrepidPhaser_b.wav", "FTB Phaser Emitter Loop", 1.0, dMode )
