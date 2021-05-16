import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_ENTDragon'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_ENTDragon'				# Name of icon .tga file
longName = 'Dragon'				# Long name with spaces
shipFile = 'FTB_ENTDragon'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Romulan Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Romulan Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_WARBIRD		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Dragon',			# The full name of your mod if applicable
	'author': 'ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBDragon = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_ENT })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBDragon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBDragon.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBDragon.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Dragon, a Romulan war frigate of the 2150s, was originally encountered by the NX-01 Enterprise several years before the infamous Earth-Romulan wars began. Many of these frigates served with distinction during that war, easily matching Earth's best starships in combat."""
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBDragon.desc = desc


