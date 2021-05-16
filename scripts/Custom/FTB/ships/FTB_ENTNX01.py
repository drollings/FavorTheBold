import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_ENTNX01'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_ENTNX01'				# Name of icon .tga file
longName = 'NX-01 Enterprise'				# Long name with spaces
shipFile = 'FTB_ENTNX01'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Human Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Human Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBNX01 Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBNX01 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNX01.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNX01.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNX01.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The NX-01 was humanity's first starship to reach, and eventually break, the warp 5 barrier. For nearly half a decade, the NX-01 Enterprise was Starfleet's only presence in deep space, earning her a place of renown in the history of human spaceflight. Originally imagined as a vessell of peaceful exploration, the NX-01 had to adapt to the challenges of many hostile races, and was often outmatched by many alien vessels."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNX01.desc = desc

