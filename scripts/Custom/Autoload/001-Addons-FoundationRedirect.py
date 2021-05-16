# Foundation Triggers Extension 20030305 for Bridge Commander
# Written March 5, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import Foundation
import Actions.EffectScriptActions ### Tisk tisk Dash, STOP Forgetting to import modules :P - Nano ###
								   # Baby why you gotta make me hitchoo?! -Dash
import App
import string
import nt


class RedirectMutatorDef(Foundation.MutatorDef):
	def __init__(self, name = None):
		Foundation.MutatorDef.__init__(self, name)

		self.folders = {
			'ship': [ 'ships.' ],
			'hp': [ 'ships.Hardpoints.' ],
		}

	def __call__(self, type, key):
		if self.folders.has_key(type):
			for i in self.folders[type]:
				try:
					# print 'importing', type, i + key
					mod = __import__(i + key)
					# print mod
					if mod is not None:
						return mod
				except ImportError:
					pass

		return None

	def Add(self, type, folder):
		if self.folders.has_key(type):
			self.folders[type].insert(0, folder)
		else:
			self.folders[type] = [ folder ]

	def Remove(self, type, folder):
		try:
			self.folders[type].remove(folder)
		except:
			pass


#########################################################
# System-related definitions

class FolderDef(Foundation.OverrideDef):

	def __init__(self, type, folder, dict = {}):
		Foundation.OverrideDef.__init__(self, type + folder + 'Folder', None, None, dict)
		self.type = type
		self.folder = folder

	def Activate(self):
		f = Foundation.FolderManager
		f.Add(self.type, self.folder)

	def Deactivate(self):
		Foundation.FolderManager.Remove(self.type, self.folder)


Foundation.FolderManager = RedirectMutatorDef()
Foundation.FolderDef = FolderDef

dStockMode = { 'modes': [ Foundation.MutatorDef.StockShips ] }
FolderDef('ship', 'ships.', dStockMode)
FolderDef('hp', 'ships.Hardpoints.', dStockMode)


def GetShipScript(pPlayer):
	import string
	l = string.split(pPlayer.GetScript(), '.')
	return l[-1]

Foundation.GetShipScript = GetShipScript


Foundation.version = '20030402'
