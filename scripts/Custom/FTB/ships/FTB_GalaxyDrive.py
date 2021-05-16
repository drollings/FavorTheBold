import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_GalaxyDrive'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Stardrive'				# Name of icon .tga file
longName = 'Galaxy Stardrive'				# Long name with spaces
shipFile = 'FTB_GalaxyDrive'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALAXY		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'GalaxyDrive',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, Vorlon, Redragon, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTB_GalaxyDrive = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTB_GalaxyDrive.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTB_GalaxyDrive.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTB_GalaxyDrive.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTB_GalaxyDrive.MVAM = 'Galaxy'
Foundation.ShipDef.FTB_GalaxyDrive.SubMenu = 'Galaxy'

desc = """The Galaxy class is one of several starships in Starfleet that can seperate its saucer section from the stardrive section. This allows the heavily armed stardrive section (where the warp engines are housed) to engage enemy forces without the added mass of the saucer section. While not employed as often as originally intended, this tactic has proven useful in many battles during the war."""


import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTB_GalaxyDrive.desc = desc
