import Foundation
import App

# Usually, you need only edit these four lines
abbrev = 'FTB_Kvort'					# Short name, no spaces, used as a preface for descriptions
iconName = 'FTB_Kvort'				# Name of icon .tga file
longName = 'K\'vort'				# Long name with spaces
shipFile = 'FTB_Kvort'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Klingon Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Klingon Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Kvort Ship',			# The full name of your mod if applicable
	'author': 'Charvell, Dolphoenix, ThomasTheCat',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.trek-homeworld.co.uk' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.
Foundation.ShipDef.FTBKvort = Foundation.KlingonShipDef(abbrev, species, {
	'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'era': Foundation.ERA_TMP | Foundation.ERA_PRETNG | Foundation.ERA_TNG | Foundation.ERA_DS9, 
})
Foundation.ShipDef.FTBKvort.dTechs = { 'Damper Immune': 100 }

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.FTBKvort.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.FTBKvort.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.ShipDef.FTBKvort.AddToMutator(Foundation.MutatorDef.FTB)


desc = """The Klingon military command commissioned the K'vort class heavy cruiser """ + \
"""quickly in response to threats from both the Romulan and Federation in the early 24th""" + \
"""century, which till that point fielded many cruisers and heavy cruisers that dwarfed the""" + \
"""K't'inga and B'rel class starships. A rushed design, the K'vort is a scaled variant of""" + \
"""the B'rel class Bird of Prey that was given more weaponry and fixed attack wings. Despite""" + \
"""its age, it remains a formidable foe."""

import FTB_Support
FTB_Support.Register(shipFile, { 'desc': desc } )
Foundation.ShipDef.FTBKvort.desc = desc

Foundation.ShipDef.FTBKvort.AddToMutator(Foundation.MutatorDef.FTB)
