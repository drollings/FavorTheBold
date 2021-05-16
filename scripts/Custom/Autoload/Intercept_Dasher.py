import Foundation

mode = Foundation.MutatorDef('Acceleration Intercept')

Foundation.OverrideDef.Intercept_Dasher = Foundation.OverrideDef('Intercept_Dasher', 'AI.PlainAI.Intercept.Intercept', 'AI.PlainAI.Intercept_Dasher.Intercept_Dasher', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef.Orbit_Dasher = Foundation.OverrideDef('Orbit_Dasher', 'AI.Player.OrbitPlanet.CreateAI', 'AI.Player.OrbitPlanet_Dasher.CreateAI', dict = { 'modes': [ mode ] } )

