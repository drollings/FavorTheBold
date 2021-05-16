import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Sovereign'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Sovereign'				# Name of icon .tga file
longName = 'Sovereign'				# Long name with spaces
shipFile = 'FTB_Sovereign'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Sovereign',			# The full name of your mod if applicable
	'author': 'Redragon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBSovereign = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBSovereign.dTechs = { 'Ablative Armour': 5000, 'Regenerative Shields': 9.0 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBSovereign.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSovereign.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBSovereign.AddToMutator(Foundation.MutatorDef.FTB)
# Foundation.MutatorDef.FTB.startShipDef = Foundation.ShipDef.FTBSovereign

Foundation.ShipDef.FTBSovereign.SubMenu = 'Sovereign'

desc = """Starfleet's ship of the line, the Sovereign class is one of the most powerful and versatile vessels in the Alpha Quadrant. Her weapon systems and combined quantum and photon make for an intimidating foe, but it is regenerative shielding which manages to absorb the charge of enemy fire and ablative armor that places it in a league above previous Federation starships in battle."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBSovereign.desc = desc


Foundation.ShipDef.FTBSovereignSovereign = Foundation.ShipDef.FTBSovereign.Clone()
Foundation.ShipDef.FTBSovereignSovereign.name = 'Sovereign'
if menuGroup:			Foundation.ShipDef.FTBSovereignSovereign.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSovereignSovereign.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBSovereignSovereign.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBSovereignEnterprise = Foundation.ShipDef.FTBSovereign.Clone()
Foundation.ShipDef.FTBSovereignEnterprise.name = 'Enterprise'
if menuGroup:			Foundation.ShipDef.FTBSovereignEnterprise.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBSovereignEnterprise.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBSovereignEnterprise.AddToMutator(Foundation.MutatorDef.FTB)
