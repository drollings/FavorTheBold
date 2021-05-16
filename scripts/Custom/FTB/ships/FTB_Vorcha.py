import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Vorcha'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Vorcha'				# Name of icon .tga file
longName = 'Vor\'cha'				# Long name with spaces
shipFile = 'FTB_Vorcha'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Klingon Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Klingon Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Vorcha',			# The full name of your mod if applicable
	'author': 'Redragon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBVorcha = Foundation.KlingonShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, 
})
Foundation.ShipDef.FTBVorcha.dTechs = { 'Damper Immune': 100 }

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBVorcha.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBVorcha.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBVorcha.AddToMutator(Foundation.MutatorDef.FTB)

desc = """A heavy cruiser meant to replace the aging K't'inga, the Vor'cha is optimized for strafing and heavy bombardment.  It has a versatile arsenal, concentrated primarily in the forward arc, and its speed and modern cloak allow it to position itself to its advantage."""
Foundation.ShipDef.FTBVorcha.desc = desc
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )