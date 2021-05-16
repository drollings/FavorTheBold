import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_TOSAkula'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_TOSAkula'				# Name of icon .tga file
longName = 'Akula (TOS)'				# Long name with spaces
shipFile = 'FTB_TOSAkula'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBAkula Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBAkula = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TOS})

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBAkula.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBAkula.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBAkula.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Akula is a fast destroyer designed to compliment the larger Constitution class starships in large fleet engagements should the need arise. Many of these starships saw border patrol duty along both the Romulan and Klingon Neutral Zones in the mid 2200s."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBAkula.desc = desc
