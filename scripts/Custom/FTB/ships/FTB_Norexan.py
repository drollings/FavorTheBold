import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Norexan'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Norexan'				# Name of icon .tga file
longName = 'Norexan'				# Long name with spaces
shipFile = 'FTB_Norexan'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Romulan Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Romulan Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_WARBIRD		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Norexan',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNorexan = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNorexan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNorexan.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNorexan.AddToMutator(Foundation.MutatorDef.FTB)

desc = """Outfitted with a deadly array of disruptors and some of the most advanced cloaking technology created, the Norexan has proven early on in its operational life to be a formidable warship, capable of holding its own against the most advanced vessels of other interstellar powers.  This variant is unarmored, but its extra speed makes it a fast and powerful escort."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNorexan.desc = desc
