import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Type9'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Type9'				# Name of icon .tga file
longName = 'Type 9 Shuttle'				# Long name with spaces
shipFile = 'FTB_Type9'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Other Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Other Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SHUTTLE		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTB Type9',			# The full name of your mod if applicable
	'author': 'Redragon/ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBType9 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBType9.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBType9.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBType9.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Type 9 is one of the most common shuttlecraft aboard Federation starships."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBType9.desc = desc
