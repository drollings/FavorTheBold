import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'FTB_Nebula'				# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Nebula'				# Name of icon .tga file
longName = 'Tempest'				# Long name with spaces
shipFile = 'FTB_Nebula'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_NEBULA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Nebula',			# The full name of your mod if applicable
	'author': 'Howedar, Dolphoenix, Vorlon',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBNebula = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })

Foundation.ShipDef.FTBNebula.SubMenu = 'Nebula'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBNebula.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebula.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBNebula.AddToMutator(Foundation.MutatorDef.FTB)

desc = """The Nebula melds the easy reconfigurability of the Miranda to the finesse of the Galaxy class.  Its compact and efficient design and simple construction make it easier to field for defensive and utility purposes than the Galaxy."""


import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBNebula.desc = desc

Foundation.ShipDef.FTBNebulaPeregrine = Foundation.FedShipDef('FTB_NebulaPeregrine', species, { 'name': 'Peregrine', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaPeregrine.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaPeregrine.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaPeregrine.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaPeregrine.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBNebulaKhitomer = Foundation.FedShipDef('FTB_NebulaKhitomer', species, { 'name': 'Khitomer', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaKhitomer.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaKhitomer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaKhitomer.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaKhitomer.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBNebulaBerkeley = Foundation.FedShipDef('FTB_NebulaBerkeley', species, { 'name': 'Berkeley', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaBerkeley.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaBerkeley.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaBerkeley.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaBerkeley.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBNebulaNightingale = Foundation.FedShipDef('FTB_NebulaNightingale', species, { 'name': 'Nightingale', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaNightingale.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaNightingale.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaNightingale.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaNightingale.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBNebulaPrometheus = Foundation.FedShipDef('FTB_NebulaPrometheus', species, { 'name': 'Prometheus', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaPrometheus.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaPrometheus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaPrometheus.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaPrometheus.AddToMutator(Foundation.MutatorDef.FTB)

Foundation.ShipDef.FTBNebulaSanFrancisco = Foundation.FedShipDef('FTB_NebulaSanFrancisco', species, { 'name': 'San Francisco', 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TNG | Foundation.ERA_DS9 | Foundation.ERA_NEMESIS, })
Foundation.ShipDef.FTBNebulaSanFrancisco.SubMenu = 'Nebula'
if menuGroup:			Foundation.ShipDef.FTBNebulaSanFrancisco.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBNebulaSanFrancisco.RegisterQBPlayerShipMenu(playerMenuGroup)
Foundation.ShipDef.FTBNebulaSanFrancisco.AddToMutator(Foundation.MutatorDef.FTB)

