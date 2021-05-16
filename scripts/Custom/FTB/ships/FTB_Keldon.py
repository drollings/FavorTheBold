import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Keldon'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Keldon'				# Name of icon .tga file
longName = 'Keldon'				# Long name with spaces
shipFile = 'FTB_Keldon'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_KELDON		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Keldon',			# The full name of your mod if applicable
	'author': 'Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBKeldon = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBKeldon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBKeldon.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBKeldon.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Keldon was originally visualized as entirely new battle cruiser intended to match the Federation's Ambassador class heavy cruiser ton for ton, but unfortunate circumstances during the original Cardassian/Federation conflict caused those plans to be scrapped, and instead an addition to existing Galor class hull was proposed. The result proved to be formidable heavy cruiser that sporting more weaponry and a beefier power core than its progenitor."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBKeldon.desc = desc
