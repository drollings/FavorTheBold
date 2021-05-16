import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_NXNeptune'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_ENTNXIntrepid'				# Name of icon .tga file
longName = 'Neptune'				# Long name with spaces
shipFile = 'FTB_ENTNXNeptune'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Human Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Human Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_AKIRA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'NXNeptune',			# The full name of your mod if applicable
	'author': 'ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNXNeptune = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_ENT })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNXNeptune.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNXNeptune.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNXNeptune.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Neptune class destroyer was one of Starfleet's earliest attempt to create a large scale vessel designed for extended independent fleet operations. The direct predecessor to the NX class, most Neptunes could only fly as fast as Warp 3, but were upgraded with faster engines in anticipation of conflict with the Feds."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNXNeptune.desc = desc

