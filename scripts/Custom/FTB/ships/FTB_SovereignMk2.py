import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_SovereignMk2'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Sovereign_Mk2'				# Name of icon .tga file
longName = 'Sovereign (Nem)'				# Long name with spaces
shipFile = 'FTB_SovereignMk2'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Sovereign',			# The full name of your mod if applicable
	'author': 'Redragon',					# Your name here
	'version': '2.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBSovereignMk2 = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBSovereignMk2.dTechs = { 'Ablative Armour': 5000, 'Regenerative Shields': 9.0 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBSovereignMk2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSovereignMk2.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBSovereignMk2.AddToMutator(Foundation.MutatorDef.FTB)
# Foundation.MutatorDef.FTB.startShipDef = Foundation.ShipDef.FTBSovereignMk2

Foundation.ShipDef.FTBSovereignMk2.SubMenu = 'Sovereign'

desc = """Though first and foremost an exploration vessel, the Sovereign is the Federation's best single warship made better in this refit.  This particular variant delivers more power to its larger complement of Type XII phasers and features extra aft torpedo tubes."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBSovereignMk2.desc = desc
