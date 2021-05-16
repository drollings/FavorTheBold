import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Steamrunner'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Steamrunner'				# Name of icon .tga file
longName = 'Steamrunner'				# Long name with spaces
shipFile = 'FTB_Steamrunner'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_AMBASSADOR	# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Steamrunner',			# The full name of your mod if applicable
	'author': '',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBSteamrunner = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBSteamrunner.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSteamrunner.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBSteamrunner.AddToMutator(Foundation.MutatorDef.FTB)

desc = """Fast but not very maneuverable, the Steamrunner is frequently seen circling in fleet engagements, firing its dorsal phasers and then unleashing a torpedo barrage.  This makes it ideal fire support for the lighter, faster modern fleet."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBSteamrunner.desc = desc
