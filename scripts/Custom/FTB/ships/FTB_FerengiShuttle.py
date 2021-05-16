import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_FerengiShuttle'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_FerengiShuttle'				# Name of icon .tga file
longName = 'Ferengi shuttle'				# Long name with spaces
shipFile = 'FTB_FerengiShuttle'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Ferengi Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Ferengi Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBFerengiShuttle Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBFerengiShuttle = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBFerengiShuttle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBFerengiShuttle.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBFerengiShuttle.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Ferengi Shuttle is often seen in crowded interstellar trade routes, either en route to a new deal or escaping from a recently completed one. Their greatest assests are, of course, their volume allocated to cargo space, and their nearly unlimited range."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBFerengiShuttle.desc = desc

