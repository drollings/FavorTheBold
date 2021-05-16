import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Virulent'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Virulent'				# Name of icon .tga file
longName = 'Virulent'				# Long name with spaces
shipFile = 'FTB_Virulent'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Virulent Ship',			# The full name of your mod if applicable
	'author': 'Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBVirulent = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBVirulent.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBVirulent.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBVirulent.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Virulent got its nickname after being discovered "infesting" an Allied supply line with its deadly anti-matter mines. While it is lightly armed with conventional standards, its real strength lies in its aft replication unit, which can fabricate new dozens of mines before it needs to be recharged."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBVirulent.desc = desc
