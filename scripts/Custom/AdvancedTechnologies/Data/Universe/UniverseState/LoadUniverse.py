## Imports
from Custom.AdvancedTechnologies.Data.Universe.ATP_Object import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Races import *
from Custom.AdvancedTechnologies.Data.Universe.ATP_Constellations import *
from Custom.AdvancedTechnologies.Data.ATP_Tools import *
from Custom.AdvancedTechnologies.Data.ATP_Config import *

def LoadUniverse(sActiveUniverse):
	## Import the activate universe
	sfile = sActiveUniverse + "." + "LoadUniverse"
	pModule = __import__(sfile)
	#try:
	#	pModule = __import__(sfile)
	#except ImportError:
	#	raise ImportError,"Corrupted UniverseState folder: "+sfile+" not found."

	## Load the basic universe instances
	LoadBasicUniverse()

	## Load the rest of that Universe
	pModule.LoadUniverse()
	
	
def LoadBasicUniverse():
	#########################################
	#	Essential base objects		#
	#	1: Universe			#
	#	2: Architect (dummy race)	#
	#	3: Matrix (dummy system)	#
	#########################################

	pUniverse = Universe(UNIVERSE_ID)
	pArchitect=Race(ARCHITECT_ID)
	pArchitect.SetName("__ARCHITECT__")
	pMatrix=SolarSystem(MATRIX_ID)
	pMatrix.Bind(pArchitect,"__MATRIX__")
	pMatrix.SetLocXYZ(-10000.0,-10000.0,-10000.0)

	
	