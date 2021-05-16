# Foundation ShipDef upgrade for Bridge Commander and Favor the Bold
# Written July 15, 2004 by Daniel B. Rollings AKA Dasher42, all rights reserved.

import Foundation

if int(Foundation.version[0:8]) < 20040715:

	def Activate(self):
		pModule = Foundation.FolderManager('ship', self.shipFile)
		pModule.__dict__[self.name] = self
		pModule.__dict__[self.abbrev] = self

	Foundation.ShipDef.Activate = Activate


	Foundation.version = '20040715p'



