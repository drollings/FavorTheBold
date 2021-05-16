import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Mediterranean'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Centaur'				# Name of icon .tga file
longName = 'Mediterranean'				# Long name with spaces
shipFile = 'FTB_Mediterranean'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBMediterranean Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBMediterranean = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBMediterranean.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBMediterranean.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBMediterranean.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Mediterranean class is an older light cruiser design that was created to complement the Excelsior class explorers with a light cruiser that was more modern than the Miranda class. While the Mediterranean has had a good service record, not too many were made because the design just was not as cost effective as the older Miranda design."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBMediterranean.desc = desc
