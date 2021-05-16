import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Brel'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Brel'				# Name of icon .tga file
longName = 'B\'rel'				# Long name with spaces
shipFile = 'FTB_Brel'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Klingon Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Klingon Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Brel Ship',			# The full name of your mod if applicable
	'author': 'Charvell, Dolphoenix, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBBrel = Foundation.KlingonShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9, 
})
Foundation.ShipDef.FTBBrel.dTechs = { 'Damper Immune': 100 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBBrel.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBBrel.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBBrel.AddToMutator(Foundation.MutatorDef.FTB)

desc = """Speed and versatility make the B'rel one of the most common Klingon ships, frequently seen patrolling the borders and supporting cruisers in fleet action.  It must compensate its for thin armor and shields with speed and firepower."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBBrel.desc = desc
