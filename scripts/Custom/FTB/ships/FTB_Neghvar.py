import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Neghvar'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Neghvar'				# Name of icon .tga file
longName = 'Negh\'var'				# Long name with spaces
shipFile = 'FTB_Neghvar'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Klingon Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Klingon Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Neghvar Ship',			# The full name of your mod if applicable
	'author': 'Redragon, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNeghvar = Foundation.KlingonShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, 
})
Foundation.ShipDef.FTBNeghvar.dTechs = { 'Damper Immune': 100 }

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNeghvar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNeghvar.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNeghvar.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Klingon flagship and its fearsome kin feature some of the most powerful weapons ever deployed on a mobile ship in the Alpha Quadrant.  Its twin Mk18 Disruptor cannons are capable of knocking down the shields of large starbases it leads the charge against.  Its only weakness is poor maneuverability, though its wide firing arcs make up for it in most cases."""
import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNeghvar.desc = desc
