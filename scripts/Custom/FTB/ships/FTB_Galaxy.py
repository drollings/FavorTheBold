import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Galaxy'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Galaxy'				# Name of icon .tga file
longName = 'Columbia'				# Long name with spaces
shipFile = 'FTB_Galaxy'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALAXY		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Galaxy',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBGalaxy = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBGalaxy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBGalaxy.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBGalaxy.AddToMutator(Foundation.MutatorDef.FTB)
Foundation.MutatorDef.FTB.startShipDef = Foundation.ShipDef.FTBGalaxy
Foundation.ShipDef.FTBGalaxy.SubMenu = 'Galaxy'
Foundation.ShipDef.FTBGalaxy.MVAM = 'Galaxy'

desc = """Designed to usher in a new era of space exploration the Galaxy class has the capacity to support nearly two thousand humanoids in deep space for years, allowing to operate in unexplored areas of space with extreme autonomy. Unfortunately, the Dominion War has caused most of these ships refitted for battle and stripped of their more luxurious components."""


import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBGalaxy.desc = desc

Foundation.ShipDef.FTBGalaxyDauntless = Foundation.ShipDef.FTBGalaxy.Clone()
Foundation.ShipDef.FTBGalaxyDauntless.name = 'Dauntless'
if menuGroup:			Foundation.ShipDef.FTBGalaxyDauntless.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBGalaxyDauntless.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBGalaxyDauntless.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBGalaxyVenture = Foundation.ShipDef.FTBGalaxy.Clone()
Foundation.ShipDef.FTBGalaxyVenture.name = 'Venture'
if menuGroup:			Foundation.ShipDef.FTBGalaxyVenture.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBGalaxyVenture.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBGalaxyVenture.AddToMutator(Foundation.MutatorDef.FTB)
