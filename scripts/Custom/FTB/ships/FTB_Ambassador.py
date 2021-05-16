import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Ambassador'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Ambassador'				# Name of icon .tga file
longName = 'Ambassador'				# Long name with spaces
shipFile = 'FTB_Ambassador'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALAXY		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Ambassador',			# The full name of your mod if applicable
	'author': 'Watcher, Dolphoenix',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBAmbassador = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.FedShipDef.FTBAmbassador.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.FedShipDef.FTBAmbassador.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBAmbassador.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Ambassador was the first ship to field the technology of Starfleet's modern vessels.  Though it did not displace the Excelsior in service, it remains a solid ship.  Modern refits carry respectable shields and phaser arcs, and can fire torpedo spreads that make it powerful against larger targets."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBAmbassador.desc = desc
