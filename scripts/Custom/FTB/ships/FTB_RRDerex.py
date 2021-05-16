import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Rrderex'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Rrderex'				# Name of icon .tga file
longName = 'R\'Rderex'				# Long name with spaces
shipFile = 'FTB_Rrderex'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Romulan Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Romulan Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_WARBIRD		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Rrderex',			# The full name of your mod if applicable
	'author': '',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBRrderex = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBRrderex.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBRrderex.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBRrderex.AddToMutator(Foundation.MutatorDef.FTB)

desc = """This highly sleek design is the Romulan Empire's best scout ship, and has proved worthy in some refits as a science vessel and a testbed for new technology.  Speed and rugged shields make it a worthy escort ship."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBRrderex.desc = desc
