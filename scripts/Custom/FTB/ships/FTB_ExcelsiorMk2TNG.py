import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_ExcelsiorMk2TNG'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Lakota'				# Name of icon .tga file
longName = 'Excelsior Mk2 (TNG)'				# Long name with spaces
shipFile = 'FTB_ExcelsiorMk2TNG'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBLakota Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBExcelsiorMk2TNG = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBExcelsiorMk2TNG.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBExcelsiorMk2TNG.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBExcelsiorMk2TNG.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The refits of the Excelsior Mk2 have helped keep the class in service for almost as long as the venerable Miranda, and are capable modern vessels."""
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBExcelsiorMk2TNG.desc = desc


Foundation.ShipDef.FTBExcelsiorMk2TNG.SubMenu = "Excelsior"
