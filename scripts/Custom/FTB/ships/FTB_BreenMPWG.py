import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_BreenMPWG'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_BreenMPWG'				# Name of icon .tga file
longName = 'Breen MPWG'				# Long name with spaces
shipFile = 'FTB_BreenMPWG'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Breen Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Breen Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'BreenMPWG Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBBreenMPWG = Foundation.ShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, 
})
Foundation.ShipDef.FTBBreenMPWG.dTechs = { 'Reflector': 80 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBBreenMPWG.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBBreenMPWG.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBBreenMPWG.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The MPWG (multi phasic wave generator) was designed to complement the more conventional Breen Destroyer by providing more effective systems interference technology through a larger power core. The cost is speed and conventional firepower, however."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBBreenMPWG.desc = desc
