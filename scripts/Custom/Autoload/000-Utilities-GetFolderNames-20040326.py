import Foundation
import nt
import string

###############################################################################
## Get Folder Names which match expression from path sFolderPath
###############################################################################
def GetFolderNames(sFolderPath, matching = None):
	lsFiles = nt.listdir(sFolderPath)

	retList = []

	for i in lsFiles:
		if i == 'CVS':
			continue
		if not (nt.stat(sFolderPath + '//' + i)[0] & 0170000) == 0040000:
			continue
		if matching and string.find(string.lower(i), matching) == -1:
			continue
		retList.append(i)

	retList.sort()
	return retList

Foundation.GetFolderNames = GetFolderNames
GetFolderNames = None
