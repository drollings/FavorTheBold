## Load ATP
import Foundation

ATP_mode = Foundation.MutatorDef('ATP 3')
Foundation.MutatorDef.ATP_3 = ATP_mode
ATP_mode.bBase = 1
dATP_mode = { 'modes': [ ATP_mode ] }

DIM_mode = Foundation.MutatorDef('ATP Dimensions')
Foundation.MutatorDef.ATP_Dimensions = DIM_mode
DIM_mode.bBase = 1
dDIM_mode = { 'modes': [ DIM_mode ] }

## ATP 3 Overrides
###########################

### QB
Foundation.OverrideDef.SetupEventHandlers = Foundation.OverrideDef('SetupEventHandlers','QuickBattle.QuickBattle.SetupEventHandlers','Custom.AdvancedTechnologies.Data.QuickBattleAddon.SetupEventHandlers',dATP_mode )

### Shipdisplay
# Foundation.OverrideDef.ShipDisplay = Foundation.OverrideDef('ShipDisplay','Tactical.Interface.ShipDisplay.SetShipID','Custom.AdvancedTechnologies.Data.GUI.ATP_ShipDisplay.SetShipID',dATP_mode)

### AI
Foundation.OverrideDef.AvoidObstacles		= Foundation.OverrideDef('AvoidObstacles', 		'AI.Preprocessors.AvoidObstacles', 		'Custom.AdvancedTechnologies.Data.AI.ATP_Preprocessors.AvoidObstacles', 	dATP_mode )
Foundation.OverrideDef.QuickBattleAI		= Foundation.OverrideDef('QuickBattleAI', 		'QuickBattle.QuickBattleAI.CreateAI', 		'Custom.AdvancedTechnologies.Data.AI.ATP_QuickBattleAI.CreateAI', 		dATP_mode )
Foundation.OverrideDef.QuickBattleFriendlyAI	= Foundation.OverrideDef('QuickBattleFriendlyAI',	'QuickBattle.QuickBattleFriendlyAI.CreateAI', 	'Custom.AdvancedTechnologies.Data.AI.ATP_QuickBattleFriendlyAI.CreateAI',	dATP_mode )


## ATP Dimensions Overrides
###############################

### Enable
CT_UNIVERSE_MODE = 1
Foundation.OverrideDef.EnableUniverse = Foundation.OverrideDef('EnableUniverse', 'Custom.AdvancedTechnologies.Data.QuickBattleAddon.CT_UNIVERSE_MODE', __name__+'.CT_UNIVERSE_MODE', dDIM_mode )

### Folders
Foundation.LoadExtraPlugins('scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\FoundationDef')

Foundation.FolderDef('ship', 	'Custom.AdvancedTechnologies.Data.Universe.ObjectDef.ShipDef.NodeDef.',		dDIM_mode)
Foundation.FolderDef('hp',	'Custom.AdvancedTechnologies.Data.Universe.ObjectDef.ShipDef.SubsystemDef.',	dDIM_mode)
Foundation.LoadExtraShips(	'scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\ShipDef\\NodeDef',
				'scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\ShipDef\\SubsystemDef'	)

Foundation.FolderDef('ship', 	'Custom.AdvancedTechnologies.Data.Universe.ObjectDef.PlanetDef.NodeDef.',	dDIM_mode)
Foundation.FolderDef('hp',	'Custom.AdvancedTechnologies.Data.Universe.ObjectDef.PlanetDef.SubsystemDef.',	dDIM_mode)
Foundation.LoadExtraShips(	'scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\PlanetDef\\NodeDef',
				'scripts\\Custom\\AdvancedTechnologies\\Data\\Universe\\ObjectDef\\PlanetDef\\SubsystemDef'	)







