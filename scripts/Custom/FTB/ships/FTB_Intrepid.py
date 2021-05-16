import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Intrepid'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Intrepid'				# Name of icon .tga file
longName = 'Intrepid'				# Long name with spaces
shipFile = 'FTB_Intrepid'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALAXY		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Intrepid',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBIntrepid = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.FedShipDef.FTBIntrepid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.FedShipDef.FTBIntrepid.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBIntrepid.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Intrepid Class Starship is one of the newer additions to the Federation Starfleet. A combat patrol and reconnaissance vessel, she is a fast ship with a lot of teeth for her size. The Intrepid is usually deployed on high threat missions where speed is required along with firepower."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBIntrepid.desc = desc
