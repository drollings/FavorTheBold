import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Kimal'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Kimal'				# Name of icon .tga file
longName = 'Kimal'				# Long name with spaces
shipFile = 'FTB_Kimal'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_KELDON		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Kimal',			# The full name of your mod if applicable
	'author': 'Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBKimal = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBKimal.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBKimal.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBKimal.AddToMutator(Foundation.MutatorDef.FTB)

desc = """A small and swift Cardassian frigate, the Kimal offers a fast support ship that is best used in packs with other Kimals and main battleships.  It uses its maneuverability to choose its engagements, and sports a single spiral wave disruptor that can equal the punch of larger warships."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBKimal.desc = desc
