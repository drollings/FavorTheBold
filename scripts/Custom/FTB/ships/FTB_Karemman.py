import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Karemman'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Karemman'				# Name of icon .tga file
longName = 'Karemman Freighter'			# Long name with spaces
shipFile = 'FTB_Karemman'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Karemman Ship',			# The full name of your mod if applicable
	'author': 'StressPuppy, Dolphoenix',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBKaremman = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBKaremman.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBKaremman.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBKaremman.AddToMutator(Foundation.MutatorDef.FTB)


desc = """The Karemman Freighter is a common sight in the Gamma quadrant, a reliable transport maintained by a merchant race that serves the Founders. Many of these vessels had been conscripted by the Dominion to transport supplies and equipment through the wormhole before it was mined. Stranded on the wrong side of a closed door, they are now used for the war effort as the Dominion Military Command sees fit."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBKaremman.desc = desc
