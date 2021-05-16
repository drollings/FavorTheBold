import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Ktinga'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Ktinga'				# Name of icon .tga file
longName = 'K\'t\'inga'				# Long name with spaces
shipFile = 'FTB_Ktinga'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Klingon Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Klingon Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Ktinga Ship',			# The full name of your mod if applicable
	'author': 'Charvell, Dolphoenix, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBKtinga = Foundation.KlingonShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9, 
})
Foundation.ShipDef.FTBKtinga.dTechs = { 'Damper Immune': 100 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBKtinga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBKtinga.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBKtinga.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The K't'inga class battlecruiser has had one of the longest active service record of any known ship in Interstellar history, flying for the empire for over four centuries in one form or another. The Klingons continue to utilize these vessels even in their front line battle fleets, having refit them with modern disruptors and torpedo systems. The K't'inga does show its age with its relatively thin armor and inadequate power core, however."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBKtinga.desc = desc

