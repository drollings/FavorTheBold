import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Bakrus'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Bakrus'				# Name of icon .tga file
longName = 'Bakrus'				# Long name with spaces
shipFile = 'FTB_Bakrus'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALOR		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Bakrus',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBBakrus = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBBakrus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBBakrus.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBBakrus.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Bakrus is entered service near the end of the Federation/Cardassian war of the 2350s. She is equipped with nearly twice as much firepower as the standard Galor Class warship, but her firing arc is limited to the fore section of the ship.  The design was plagued with problems until Dominion technology gave it a powerplant capable of sustaining its formidable weaponry."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBBakrus.desc = desc
