# ShipListSubMenu Addition V2.
# This modification of the Foundation allows you to get a submenu in the race list (ie Federation Ships -> Galaxy Class)
# This modification is by MLeoDaalder

import App
import Foundation

if int(Foundation.version[0:8]) < 20040627:
	import FoundationMenu

	class ShipMenuBuilderDef(FoundationMenu.MenuBuilderDef):
		def __init__(self, tglDatabase):
			FoundationMenu.MenuBuilderDef.__init__(self, tglDatabase)

		def __call__(self, raceShipList, menu, buttonType, uiHandler, fWidth = 0.0, fHeight = 0.0):
			foundShips = {}
			for race in raceShipList.keys():
				for ship in raceShipList[race][0]:
					foundShips[race] = 1
					break

			raceList = foundShips.keys()
			raceList.sort()

			for race in raceList:
				self.textButton(race)
				pRaceButton = self.textButton.MakeSubMenu()
				menu.AddChild(pRaceButton)

				shipList = raceShipList[race][1].keys()
				shipList.sort()

				for key in shipList:
					ship = raceShipList[race][1][key]
					self.textButton(ship.name)
					pSubMenu = None
					if(ship.__dict__.has_key("SubMenu")):
						if(ship.SubMenu != None and str(ship.SubMenu) != ""):
							if(str(ship.SubMenu)[0] == "[" and str(ship.SubMenu)[len(str(ship.SubMenu)) - 1] == "]" and len(ship.SubMenu) > 0):
								pMenu = pRaceButton
								for name in ship.SubMenu:
									pSubMenu = pMenu.GetSubmenuW(App.TGString(name))
									if(pSubMenu == None):
										pSubMenu = App.STCharacterMenu_Create(name)
										pMenu.AddChild(pSubMenu)
										pMenu.ForceUpdate(0)
									pMenu = pSubMenu
							else:
								pSubMenu = pRaceButton.GetSubmenuW(App.TGString(ship.SubMenu))
								if(pSubMenu == None):
									pSubMenu = App.STCharacterMenu_Create(ship.SubMenu)
									pRaceButton.AddChild(pSubMenu)
									pRaceButton.ForceUpdate(0)
							if(ship.__dict__.has_key("SubSubMenu")):
								if pSubMenu == None:
									pSubMenu = pRaceButton
								if(ship.SubSubMenu != None and str(ship.SubSubMenu) != ""):
									if(str(ship.SubSubMenu)[0] == "[" and str(ship.SubSubMenu)[len(str(ship.SubSubMenu)) - 1] == "]" and len(ship.SubMenu) > 0):
										for name in ship.SubSubMenu:
											pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(name))
											if(pSubSubMenu == None):
												pSubSubMenu = App.STCharacterMenu_Create(name)
												pSubMenu.AddChild(pSubSubMenu)
												pSubMenu.ForceUpdate(0)
											pSubMenu = pSubSubMenu
									else:
										pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(ship.SubSubMenu))
										if(pSubSubMenu == None):
											pSubSubMenu = App.STCharacterMenu_Create(ship.SubSubMenu)
											pSubMenu.AddChild(pSubSubMenu)
											pSubMenu.ForceUpdate(0)
										pSubMenu = pSubSubMenu
						if not DoMVAMMenus(pSubMenu, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight):
							pSubMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
							pSubMenu.ForceUpdate(0)
					elif(ship.__dict__.has_key("SubSubMenu")):
						pSubMenu = pRaceButton
						if(ship.SubSubMenu != None and str(ship.SubSubMenu) != ""):
							if(str(ship.SubSubMenu)[0] == "[" and str(ship.SubSubMenu)[len(str(ship.SubSubMenu)) - 1] == "]" and len(ship.SubSubMenu) > 0):
								for name in ship.SubSubMenu:
									pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(name))
									if(pSubSubMenu == None):
										pSubSubMenu = App.STCharacterMenu_Create(name)
										pSubMenu.AddChild(pSubSubMenu)
										pSubMenu.ForceUpdate(0)
									pSubMenu = pSubSubMenu
							else:
								pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(ship.SubSubMenu))
								if(pSubSubMenu == None):
									pSubSubMenu = App.STCharacterMenu_Create(ship.SubSubMenu)
									pSubMenu.AddChild(pSubSubMenu)
									pSubMenu.ForceUpdate(0)
								pSubMenu = pSubSubMenu
						if not DoMVAMMenus(pSubMenu, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight):
							pSubMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
							pSubMenu.ForceUpdate(0)
					else:
						if not DoMVAMMenus(pRaceButton, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight):
							pRaceButton.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))

				pRaceButton.ForceUpdate(0)

	FoundationMenu.ShipMenuBuilderDef = ShipMenuBuilderDef
	Foundation.version = "20040627"
	print "Updating FoundationMenu.ShipMenuBuilderDef V3 - MVAM addition"

	def DoMVAMMenus(pMenu, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight):
		try:
			import Custom.Autoload.Mvam
		except:
			return 0

		import nt
		import string
		if ship.__dict__.has_key("MvamMenu"):
			if len(str(ship.MvamMenu)) > 1:
				pParentShipMenu = pMenu.GetSubmenuW(App.TGString(ship.MvamMenu))
				if not pParentShipMenu:
					List = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

					Mod = None
					for i in range(len(List)):
						PosModName = string.split(List[i], ".")
						if len(PosModName) > 1 and PosModName[0] != "__init__":
							try:
								PosMod = __import__("Custom.Autoload.Mvam." + PosModName[0])
								if PosMod and hasattr(PosMod, "MvamShips"):
									if IsInList(ship.shipFile, PosMod.MvamShips):
										Mod = PosMod
										break
							except:
								continue

					if not Mod:
						return 0

					# Now we have the MVAM plug. Now the hard part, tracing back the correct ship plugin for the full ship...
					#	Well, not hard, just tedious at times... -MLeoDaalder
					foundShips = {}
					for race in raceShipList.keys():
						for shipA in raceShipList[race][0]:
							foundShips[race] = 1

					raceList = foundShips.keys()
					raceList.sort()

					shipC = None
					for race in raceList:
						shipList = raceShipList[race][1].keys()
						shipList.sort()
						for key in shipList:
							shipB = raceShipList[race][1][key]
							if shipB.shipFile == Mod.MvamShips[0]:
								shipC = shipB
					if shipC == None:
						return 0
					pParentShipMenu = App.STCharacterMenu_Create(shipC.name)
					pEvent = App.TGIntEvent_Create()
					pEvent.SetEventType(buttonType)
					pEvent.SetDestination(uiHandler)
					pEvent.SetSource(pParentShipMenu)
					pEvent.SetInt(shipC.num)
					pParentShipMenu.SetActivationEvent(pEvent)
					pParentShipMenu.SetTwoClicks()
					pMenu.AddChild(pParentShipMenu)
					pMenu.ForceUpdate(0)

				pParentShipMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
				pParentShipMenu.ForceUpdate(0)
				return 1
			elif ship.MvamMenu != 0:
				# Well, no string... *Sigh* This is going to be much searching...
				# Or maybe not....
				List = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

				Mod = None
				for i in range(len(List)):
					PosModName = string.split(List[i], ".")
					if len(PosModName) > 1 and PosModName[0] != "__init__":
						try:
							PosMod = __import__("Custom.Autoload.Mvam." + PosModName[0])
							if PosMod and hasattr(PosMod, "MvamShips"):
								if IsInList(ship.shipFile, PosMod.MvamShips):
									Mod = PosMod
									break
						except:
							continue
				if not Mod:
					return 0
				# Now, let's get the parent ship...
				foundShips = {}
				for race in raceShipList.keys():
					for shipA in raceShipList[race][0]:
						foundShips[race] = 1

				raceList = foundShips.keys()
				raceList.sort()

				shipC = None
				for race in raceList:
					shipList = raceShipList[race][1].keys()
					shipList.sort()
					for key in shipList:
						shipB = raceShipList[race][1][key]
						if shipB.shipFile == Mod.MvamShips[0]:
							shipC = shipB
				if shipC == None:
					return 0
				pParentShipMenu = pMenu.GetSubmenuW(App.TGString(shipC.name))
				if not pParentShipMenu:
					pParentShipMenu = App.STCharacterMenu_Create(shipC.name)
					pEvent = App.TGIntEvent_Create()
					pEvent.SetEventType(buttonType)
					pEvent.SetDestination(uiHandler)
					pEvent.SetSource(pParentShipMenu)
					pEvent.SetInt(shipC.num)
					pParentShipMenu.SetActivationEvent(pEvent)
					pParentShipMenu.SetTwoClicks()
					pMenu.AddChild(pParentShipMenu)
					pMenu.ForceUpdate(0)
				pParentShipMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
				pParentShipMenu.ForceUpdate(0)
				return 1

		else:# Let's see if this ship is the full ship...
			List = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

			Mod = None
			for i in range(len(List)):
				PosModName = string.split(List[i], ".")
				if len(PosModName) > 1 and PosModName[0] != "__init__":
					try:
						PosMod = __import__("Custom.Autoload.Mvam." + PosModName[0])
						if PosMod and hasattr(PosMod, "MvamShips"):
							if ship.shipFile == PosMod.MvamShips[0]:
								Mod = PosMod
							elif IsInList(ship.shipFile, PosMod.MvamShips):# But is it a sep ship?
								ship.MvamMenu = 1
								DoMVAMMenus(pMenu, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight)
								return 1
					except:
						continue

			if not Mod:
				return 0

			if not pMenu.GetSubmenuW(App.TGString(ship.name)):
				pParentShipMenu = App.STCharacterMenu_Create(ship.name)
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(buttonType)
				pEvent.SetDestination(uiHandler)
				pEvent.SetSource(pParentShipMenu)
				pEvent.SetInt(ship.num)
				pParentShipMenu.SetActivationEvent(pEvent)
				pParentShipMenu.SetTwoClicks()
				pMenu.AddChild(pParentShipMenu)
				pMenu.ForceUpdate(0)
			return 1
		return 0

	def IsInList(item, list):
		for i in list:
			if i == item:
				return 1
		return 0
