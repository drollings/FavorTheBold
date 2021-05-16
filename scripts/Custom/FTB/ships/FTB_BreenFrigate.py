import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_BreenFrigate'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_BreenFrigate'				# Name of icon .tga file
longName = 'Breen Frigate'				# Long name with spaces
shipFile = 'FTB_BreenFrigate'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Breen Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Breen Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'BreenFrigate Ship',			# The full name of your mod if applicable
	'author': 'Redragon, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBBreenFrigate = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBBreenFrigate.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBBreenFrigate.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBBreenFrigate.AddToMutator(Foundation.MutatorDef.FTB)

# Foundation.SoundDef("sfx/Weapons/Breen1.wav", "Breen1", 1.0)
# Foundation.SoundDef("sfx/Weapons/Breen2.wav", "Breen2", 1.0)

desc = """This destroyer is the ship of the line for the Breen military, capable of cloaking and of deploying a powerful weapon that wreaks havoc on the vital systems of enemy starships."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBBreenFrigate.desc = desc
