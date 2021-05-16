import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Insidious'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Insideous'				# Name of icon .tga file
longName = 'Insidious'				# Long name with spaces
shipFile = 'FTB_Insidious'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Insidious Ship',			# The full name of your mod if applicable
	'author': 'Redragon, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBInsidious = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBInsidious.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBInsidious.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBInsidious.AddToMutator(Foundation.MutatorDef.FTB)


desc = """The Insidious is a new addition to the Dominion attack fleets. The ship is designed to exploit the vulnerability of allied ships, especially Klingons, to fast attack fighters. While the smaller Horda fighters are equipped to deal with fighter class vessels, the Insidious is a bomber, and in swarms can bring down an enemy capital ship with surprising quickness. """

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBInsidious.desc = desc
