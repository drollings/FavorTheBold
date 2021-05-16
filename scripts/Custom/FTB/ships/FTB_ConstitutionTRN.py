import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_ConstitutionTRN'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Enterprise'				# Name of icon .tga file
longName = 'Constitution (DS9)'				# Long name with spaces
shipFile = 'FTB_ConstitutionTRN'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FTBConstitutionTRN Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBConstitutionTRN = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBConstitutionTRN.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBConstitutionTRN.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBConstitutionTRN.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBConstitutionTRN.SubMenu = 'Constitution'

desc = """While the venerable Constitution Class has been long removed from active duty, several ships have been commissioned by Starfleet as cadet training vessels. These ships see periodic refits to their computer and sensor systems to keep the training hardware up to date. During the war, however, Starfleet needed as many ships as possible, so several Constitution trainers were recomissioned and hastily outfitted with modern shields and weaponry.  However, their power conduits and subsystems are outdated, forcing their crews to handle the aging ships carefully."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBConstitutionTRN.desc = desc
