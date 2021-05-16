import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Defiant'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Defiant'				# Name of icon .tga file
longName = 'Defiant'				# Long name with spaces
shipFile = 'FTB_Defiant'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Defiant',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBDefiant = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBDefiant.dTechs = { 'Ablative Armour': 5000 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBDefiant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBDefiant.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBDefiant.AddToMutator(Foundation.MutatorDef.FTB)
# Foundation.MutatorDef.FTB.startShipDef = Foundation.ShipDef.FTBDefiant

desc = """The Defiant class is a true warship. Its slim profile and high powered weapons make it a fierce and deadly opponent on the battlefield. Officially, it's an "escort" ship, but unofficially, it can match the best the Dominion has to offer in the way of warships."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBDefiant.desc = desc
