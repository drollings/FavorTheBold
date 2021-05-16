import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Miranda'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Miranda'				# Name of icon .tga file
longName = 'Miranda (TNG)'				# Long name with spaces
shipFile = 'FTB_Miranda'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBMiranda Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBMiranda = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBMiranda.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBMiranda.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBMiranda.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBMiranda.SubMenu = 'Miranda'

desc = """The Miranda class light cruiser has proven time and again to be a versatile, reliable vessel that is always up to performing its tasks. Simple and easily reconfigurable design has kept it in service longer than the Excelsior.  The Dominion War has been cruel to these aging vessels, however."""


import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBMiranda.desc = desc
