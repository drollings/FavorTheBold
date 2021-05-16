import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Leviathan'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Leviathan'				# Name of icon .tga file
longName = 'Leviathan'				# Long name with spaces
shipFile = 'FTB_Leviathan'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Leviathan Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBLeviathan = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBLeviathan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBLeviathan.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBLeviathan.AddToMutator(Foundation.MutatorDef.FTB)


desc = """The Leviathan is the Dominion's dedicated carrier and support vessel. It is used as a mobile repair facility and fighter launching base, with a greater operational capacity than even the Enslaver class dreadnaughts. While lightly armed by Dominion standards, the Leviathan is not completely defenseless."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBLeviathan.desc = desc
