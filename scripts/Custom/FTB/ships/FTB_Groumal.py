import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Groumal'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Groumal'				# Name of icon .tga file
longName = 'Groumal'				# Long name with spaces
shipFile = 'FTB_Groumal'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Card Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Card Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_GALOR		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'FtB Groumal',			# The full name of your mod if applicable
	'author': 'Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBGroumal = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_NEMESIS, })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBGroumal.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBGroumal.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBGroumal.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Groumal military freighter is a common site in any Cardassian registered trade lane, and is favored by the Cardassian military due to its appreciable speed and durable hull. Several years before the war, many of these ships were sold to other interstellar powers, including the Klingons, earning them an even broader base of respect throughout the quadrant."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBGroumal.desc = desc

