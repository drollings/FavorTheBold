import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Excelsior'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Excelsior'				# Name of icon .tga file
longName = 'NCC Excelsior'				# Long name with spaces
shipFile = 'FTB_Excelsior'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBExcelsior Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBExcelsior = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBExcelsior.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBExcelsior.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBExcelsior.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBExcelsior.SubMenu = 'Excelsior'

desc = """Called at one time "the great experiment" by Starfleet engineers, the original Excelsior design called for transwarp engines. The experiment failed, but instead of scrapping the design altogether, it was decided to equip the ship with conventional engines. The result was a resounding success; the Excelsior class is one of the most space-worthy ships ever fielded by Starfleet, and has been in use for over a hundred years."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBExcelsior.desc = desc
