import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Norway'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Norway'				# Name of icon .tga file
longName = 'Norway'				# Long name with spaces
shipFile = 'FTB_Norway'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Norway',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNorway = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNorway.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNorway.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNorway.AddToMutator(Foundation.MutatorDef.FTB)

desc = """Best described as a "blockade runner," the Norway is a fast light cruiser/transport that distinguished itself during the Federation/Cardassian war by successfully delivering supplies through what seemed like the most solid defense. Some of these vessels have been converted to minelayers for the war against the Dominion, while others have been given small complements of fighter wings and serve as fast carriers."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNorway.desc = desc
