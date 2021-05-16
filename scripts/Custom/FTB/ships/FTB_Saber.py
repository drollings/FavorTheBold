import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Saber'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Saber'				# Name of icon .tga file
longName = 'Saber'				# Long name with spaces
shipFile = 'FTB_Saber'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_AMBASSADOR		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBSaber',			# The full name of your mod if applicable
	'author': 'Redragon',					# Your name here
	'version': '2.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBSaber = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBSaber.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSaber.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBSaber.AddToMutator(Foundation.MutatorDef.FTB)

desc = """This light cruiser design first saw service during the later years of the first Federation/Cardassian conflict, and was meant to eventually replace the Miranda class as the standard light cruiser of the Federation.  Its quick speed and twin torpedo turrets have made it a boon to allied commanders, which have used it to great effect against under-defended enemy targets."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBSaber.desc = desc
