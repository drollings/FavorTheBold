import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Dominator'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Dominator'				# Name of icon .tga file
longName = 'Dominator'				# Long name with spaces
shipFile = 'FTB_Dominator'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Dominator Ship',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBDominator = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBDominator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBDominator.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBDominator.AddToMutator(Foundation.MutatorDef.FTB)

desc = """These Jem'Hadar attack ships nearly always travel in packs of three and can use their combined weaponry to disintegrate even the most intimidating opponent in moments. They quickly earned the name "Dominator" by Allied command after an early engagement saw the attack ships victorious without a single loss."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBDominator.desc = desc
