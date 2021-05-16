import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Akira'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Akira'				# Name of icon .tga file
longName = 'Akira'				# Long name with spaces
shipFile = 'FTB_Akira'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_AKIRA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Akira',				# The full name of your mod if applicable
	'author': 'Redragon',					# Your name here
	'version': '4',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBAkira = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'menugroup': menuGroup, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS } )

Foundation.ShipDef.FTBAkira.SubMenu = 'Akira'

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBAkira.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBAkira.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBAkira.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Akira class is one of Starfleet's more intimidating heavy cruisers. The standard load-out for an Akira has it equipped with a heavy compliment of torpedo tubes. A carrier variant also exists, providing a staging area for a squadron of Peregrine fighters."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBAkira.desc = desc

Foundation.ShipDef.FTBAkiraDevore = Foundation.ShipDef.FTBAkira.Clone()
Foundation.ShipDef.FTBAkiraDevore.name = 'Devore'
if menuGroup:			Foundation.ShipDef.FTBAkiraDevore.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBAkiraDevore.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBAkiraDevore.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBAkiraGeronimo = Foundation.ShipDef.FTBAkira.Clone()
Foundation.ShipDef.FTBAkiraGeronimo.name = 'Geronimo'
if menuGroup:			Foundation.ShipDef.FTBAkiraGeronimo.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBAkiraGeronimo.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBAkiraGeronimo.AddToMutator(Foundation.MutatorDef.FTB)
