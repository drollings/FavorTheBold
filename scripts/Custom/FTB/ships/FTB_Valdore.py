import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Valdore'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Valdore'				# Name of icon .tga file
longName = 'Valdore'				# Long name with spaces
shipFile = 'FTB_Valdore'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Romulan Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Romulan Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_WARBIRD		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Valdore',			# The full name of your mod if applicable
	'author': 'Redragon, Howedar',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBValdore = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBValdore.dTechs = { 'Ablative Armour': { 'hit': 1000 } }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBValdore.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBValdore.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBValdore.AddToMutator(Foundation.MutatorDef.FTB)

desc = """Outfitted with a deadly array of disruptors and some of the most advanced cloaking technology created, the Norexan has proven early on in its operational life to be a formidable warship, capable of holding its own against the most advanced vessels of other interstellar powers.  This variant packs the armor and power to distinguish it in heated battle."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBValdore.desc = desc
