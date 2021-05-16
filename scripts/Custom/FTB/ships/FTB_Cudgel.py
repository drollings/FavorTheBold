import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Cudgel'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Cudgel'				# Name of icon .tga file
longName = 'Cudgel'				# Long name with spaces
shipFile = 'FTB_Cudgel'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Dominion Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Dominion Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Cudgel Ship',			# The full name of your mod if applicable
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
Foundation.ShipDef.FTBCudgel = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBCudgel.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBCudgel.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBCudgel.AddToMutator(Foundation.MutatorDef.FTB)

desc = """While the Cudgel is outmatched in speed by most other corvettes, it boasts superior firepower, able to bring an intimidating array of heavy weapons to the fray in a platform that's still fast enough to outpace larger targets."""
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBCudgel.desc = desc
