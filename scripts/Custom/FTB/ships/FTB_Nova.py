import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Nova'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Nova'				# Name of icon .tga file
longName = 'Nova'				# Long name with spaces
shipFile = 'FTB_Nova'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBNova Ship',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNova = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNova.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNova.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNova.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Nova class frigate is a small science ship designed to replace the aging Oberth class science vessel. The Nova is more heavily armed than its forbear; though its powerplant is easily overtaxed by its many phaser arrays in a sustained fight, it has enough teeth to fend off a light attack.  Its real strength is in its highly sensitive sensor arrays, which can give it great firing accuracy."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNova.desc = desc
