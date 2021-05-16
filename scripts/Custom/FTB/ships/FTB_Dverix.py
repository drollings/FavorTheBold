import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Dverix'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Dverix'				# Name of icon .tga file
longName = 'D\'verix'				# Long name with spaces
shipFile = 'FTB_Dverix'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Romulan Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Romulan Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_WARBIRD		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Dverix',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBDverix = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBDverix.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBDverix.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBDverix.AddToMutator(Foundation.MutatorDef.FTB)

desc = """A contemporary of the D'Deridex Warbird, the D'Verix is medium cruiser that provides a more maneuverable escort to the hulking D'Deridex. Some variants of the D'Verix have a special graviton field generator that uses the artificial singularity in the ship's warp core to generate a field of graviton particles that renders enemy ships immobile."""
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBDverix.desc = desc


