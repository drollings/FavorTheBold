import Foundation

mode = Foundation.MutatorDef('Shifting Intercept')

Foundation.OverrideDef.Intercept_Shift = Foundation.OverrideDef('Intercept_Shift', 'AI.PlainAI.Intercept.Intercept', 'AI.PlainAI.Intercept_Shift.Intercept_Dasher', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.Orbit_Shift = Foundation.OverrideDef('Orbit_Shift', 'AI.Player.OrbitPlanet.CreateAI', 'AI.Player.OrbitPlanet_Dasher.CreateAI', dict = { 'modes': [ mode ] } )

