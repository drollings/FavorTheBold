import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Galor'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Galor'				# Name of icon .tga file
longName = 'Galor'				# Long name with spaces
shipFile = 'FTB_Galor'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALOR		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Galor',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBGalor = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBGalor.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBGalor.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBGalor.AddToMutator(Foundation.MutatorDef.FTB)


desc = """The Galor Mark 3 Warship is the standard ship of the line for the Cardassian military. The design itself has been in service for the better part of a century, but as new technologies arrive in Cardassian hands through trade or conquest, they are applied to keep these war cruisers up to date. While it is underpowered compared to other ships of its size, its maneuverability and the tenacity of its commanders should not be underestimated."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBGalor.desc = desc