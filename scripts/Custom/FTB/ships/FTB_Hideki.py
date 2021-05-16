import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Hideki'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Hideki'				# Name of icon .tga file
longName = 'Hideki'				# Long name with spaces
shipFile = 'FTB_Hideki'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_KELDON		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Hideki',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBHideki = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBHideki.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBHideki.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBHideki.AddToMutator(Foundation.MutatorDef.FTB)

desc = """A worthy counterpart to the Jem'Hadar "Dominator" attack ships, the Hideki is a small corvette designed for making precision strikes against larger enemy targets.  Originally designed as a modest patrol craft, it proved easy to refit en masse.  The renovated Hideki is deadly addition to the Cardassian fleet, which began production only six months after data concerning the Gamma Quadrant Dominion reached Cardassian Military Intelligence."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBHideki.desc = desc
