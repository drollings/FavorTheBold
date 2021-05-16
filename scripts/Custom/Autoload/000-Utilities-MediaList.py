# April 17, 2004
# by Daniel Rollings AKA Dasher42

# PURPOSE:  Provide more reusable and efficient lists of randomly accessed sounds and textures

import App
# import DummyApp
# App = DummyApp.DummyApp()
import Foundation

class MediaListDef(Foundation.MutatorElementDef):
	def __init__(self, name, dict = None):
		self.dFiles = {}

	def LoadFolder(self, sGroup, sDir, sExt):
		lFiles = self.GetList(sGroup)
		lsFileNames = Foundation.GetFileNames(sDir, sExt)
		for i in lsFileNames:
			sFile = sDir + '/' + i
			sHandle = sGroup + str(len(lFiles) + 1)
			lFiles.append(Foundation.SoundDef(sFile, sHandle))
			# print sFile, sHandle

	def AddSoundDef(self, sGroup, oSoundDef):
		lFiles = self.GetList(sGroup)
		lFiles.append(oSoundDef)

	def GetList(self, sGroup):
		if self.dFiles.has_key(sGroup):
			lFiles = self.dFiles[sGroup]
		else:
			lFiles = []
			self.dFiles[sGroup] = lFiles
		return lFiles

	def __call__(self, sGroup):
		lFiles = self.dFiles[sGroup]
		return lFiles[int(App.g_kSystemWrapper.GetRandomNumber(len(lFiles)))].name


# if int(Foundation.version) < 20040417:
Foundation.MediaListDef = MediaListDef
# 	Foundation.version = '20040417'
