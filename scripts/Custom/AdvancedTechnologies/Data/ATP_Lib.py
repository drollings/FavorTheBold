import App
import QuickBattleAddon
import MissionLib
from GUI import ATP_GUIUtils

TRUE=1
FALSE=0

def InitGUIUtils():
	return ATP_GUIUtils.InitGUIUtils()

#################################################################################
#################################################################################
#	Object Lists								#
#################################################################################
#################################################################################

#################################################################################
#	GetShipListInSet([pSet])						#
#	Args: None or a specified set						#
#	Return: Gives a list with the ShipID's in a given set, if no set is	#
#		specified, the set containing the player is selected.		#
#################################################################################
def GetShipListInSet(pSet=None):
	if pSet==None:
		pPlayer = MissionLib.GetPlayer()
		pSet=pPlayer.GetContainingSet()
	
	g_EnemyShipList=QuickBattleAddon.makeEnemyShipList(pSet)
	g_FriendShipList=QuickBattleAddon.makeFriendShipList(pSet)
	g_NeutralShipList=QuickBattleAddon.makeNeutralShipList(pSet)
	List=g_NeutralShipList+g_FriendShipList+g_EnemyShipList
	return (List[:])


#########################################################################################
#	GetDebrisListInSet([pSet])						        #
#	Args: None or a specified set						        #
#	Return: Gives a list with the pointer to Debris in a given set, if no set is	#
#		specified, the set containing the player is selected.		 	#
#########################################################################################
def GetDebrisListInSet(pSet=None):
	return QuickBattleAddon.GetDebrisListInSet(pSet)
	
     
#################################################################################
#	GetShipListInSetDistanceSorted(kVect[,fMax][,pSet])			#
#	Args: a TGPoint3, denoting the reference point and an optional set	#
#	Return: Gives a list with the ShipID's in a given set, if no set is	#
#		specified, the set containing the player is selected. The ships	#
#		are ordered from close to far from the given point kVect.	#
#################################################################################	
def GetShipListInSetDistanceSorted(kVect,fMax=0,pSet=None):
	if pSet==None:
		pPlayer = MissionLib.GetPlayer ()
		pSet=pPlayer.GetContainingSet()
	
	List=GetShipListInSet(pSet)
	List=QuickBattleAddon.distanceSort(List,kVect,fMax)
	return (List[:])


##################################################################################
##################################################################################
##	Friends and Foes							##
##################################################################################
##################################################################################

#################################################################################
#	AreEnemies(pShip1,pShip2)						#
#	Args: two ships								#
#	Return:	Returns whether or not they are enemies, neutrals are never	#
#		enemy to any object						#
#################################################################################
def AreEnemies(pShip1,pShip2):
	return (QuickBattleAddon.AreEnemies(pShip1,pShip2))


#################################################################################
#	IsEnemy(pShip)								#
#	Args: One ship								#
#	Return:	Returns whether or not it belongs to the enemy group		#
#################################################################################
def IsEnemy(pShip):
	return (QuickBattleAddon.IsEnemy(pShip))


#################################################################################
#	IsFriend(pShip)								#
#	Args: One ship								#
#	Return:	Returns whether or not it belongs to the friend group		#
#################################################################################
def IsFriend(pShip):
	return (QuickBattleAddon.IsFriend(pShip))



##################################################################################
##################################################################################
##	GUI									##
##################################################################################
##################################################################################

#########################################################################################################################################
# 	CreateStandardButton(eventType,sFunctionHandler,menuName,buttonName)								#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		buttonName	  - name that you want to give your button eg "Test Button"						#
#		pShip		  - the event will be an IntEvent specifing the ship ID							#
#	Return: None															#
#																	#
#	Full Example: CreateStandardButton(ET_CORBONITE_SET_ON,__name__+".SetCorboniteOn","Tactical","CR Ready")			#
#																	#
#########################################################################################################################################
#########################################################################################################################################
#	Note on eventType & sFunctionHandler												#
#		__name__ is a Python variable representing your current module.								#
#		If you are working in eg. Scripts/Custom/ButtonTest/TesterFile.py, __name__ will be "Custom.ButonTest.TesterFile"	#
#		__name__+".Test" is then "Custom.ButonTest.TesterFile.Test"								#
#		The def Test(pObject,pEvent): in that file will be called when the event is activated					#
#########################################################################################################################################
def CreateStandardButton(eventType,sFunctionHandler,menuName,buttonName,pShip=None):
	ATP_GUIUtils.CreateStandardButton(eventType,sFunctionHandler,menuName,buttonName,pShip)
	return None


#########################################################################################################################################
# 	RemoveStandardButton(menuName,buttonName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		buttonName	- name of the button you want to delete button eg "CR Ready"						#
#	Return: None															#
#																	#
#	Full Example: RemoveStandardButton("Tactical","CR Ready")									#
#																	#
#########################################################################################################################################
def RemoveStandardButton(menuName,buttonName):
	ATP_GUIUtils.RemoveStandardButton(menuName,buttonName)
	return None


#########################################################################################################################################
# 	CreateCountDownButton(eventType1,sFunctionHandler1,eventType2,sFunctionHandler2,menuName,buttonName,counterStart)		#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		eventType2	  - global registered event; called when the time is up; eg. ET_Y=App.Mission_GetNextEventType()	#
# 		sFunctionHandler2 - name of the function; called when the time is up; eg. __name__ +".DoY"				#
#				  													#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		buttonName	  - name that you want to give your button eg "Test Button"						#
#		counterStart	  - the initial value of the timer, time is up when the counter has dropped to 0			#
#	Return: None															#
#																	#
#	Full Example: CreateCountDownButton(ET_STOP,__name__+".StopGoWarp",ET_WARP,__name__+".Warp","Helm","Warping in",5)		#
#																	#
#########################################################################################################################################
#########################################################################################################################################
#	Note on eventType & sFunctionHandler												#
#		__name__ is a Python variable representing your current module.								#
#		If you are working in eg. Scripts/Custom/ButtonTest/TesterFile.py, __name__ will be "Custom.ButonTest.TesterFile"	#
#		__name__+".Test" is then "Custom.ButonTest.TesterFile.Test"								#
#		The def Test(pObject,pEvent): in that file will be called when the event is activated					#
#########################################################################################################################################
def CreateCountDownButton(eventType1,sFunctionHandler1,eventType2,sFunctionHandler2,menuName,buttonName,counterStart):
	ATP_GUIUtils.CreateCountDownButton(eventType1,sFunctionHandler1,eventType2,sFunctionHandler2,menuName,buttonName,counterStart)
	return None


#########################################################################################################################################
# 	RemoveCountDownButton(menuName,buttonName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		buttonName	- name of the count down button you want to delete button eg "CR Ready"					#
#	Return: None															#
#																	#
#	Full Example: RemoveCountDownButton("Helm","Warping in")									#
#																	#
#########################################################################################################################################
def RemoveCountDownButton(menuName,buttonName):
	ATP_GUIUtils.RemoveCountDownButton(menuName,buttonName)
	return None


#########################################################################################################################################
# 	CreateDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name that you want to give your menu "Warp Speed"							#
#	Return: None															#
#																	#
#	Full Example: CreateDropDownMenu("Helm","Warp Speed")										#	
#																	#
#########################################################################################################################################
def CreateDropDownMenu(menuName,dropDownMenuName):
	ATP_GUIUtils.CreateDropDownMenu(menuName,dropDownMenuName)
	return None


#########################################################################################################################################
# 	CloseDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name of the menu eg "Warp Speed"									#
#	Return: None															#
#																	#
#	Full Example: CloseDropDownMenu("Helm","Warp Speed")										#	
#																	#
#########################################################################################################################################
def CloseDropDownMenu(menuName,dropDownMenuName):
	ATP_GUIUtils.CloseDropDownMenu(menuName,dropDownMenuName)
	return None


#########################################################################################################################################
# 	RemoveDropDownMenu(menuName,dropDownMenuName)											#
#																	#
#	Args:	menuName	- the name of the Character menu, the possible names are:						#
#				  "Helm","Tactical","Commander","Science","Engineering"							#
#		dropDownMenuName- name of menu button you want to delete button eg "Warp Speed"						#
#	Return: None															#
#																	#
#	Full Example: RemoveDropDownMenu("Science","Secondary Targets")									#
#																	#
#########################################################################################################################################
def RemoveDropDownMenu(menuName,dropDownMenuName):
	ATP_GUIUtils.RemoveDropDownMenu(menuName,dropDownMenuName)
	return None


#########################################################################################################################################
# 	AddButtonToDropDownMenu(eventType,sFunctionHandler,menuName,dropDownMenuName,buttonName)					#
#																	#
#	Args:	eventType1	  - global registered event; called when the button is pressed; eg. ET_X=App.Mission_GetNextEventType() #
# 		sFunctionHandler1 - name of the function; called when the button is pressed; eg. __name__ +".DoX"			#
#		menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - name of the submenu eg "Warp Speed"									#
#		buttonName	  - name that you want to give your button eg "Warp 1"							#
#	Return: None															#
#																	#
#	Full Example: AddButtonToDropDownMenu(ET_WARP_1,__name__+".Warp1","Helm","Warp Speed","Warp 1")					#
#																	#
#########################################################################################################################################
def AddButtonToDropDownMenu(eventType,sFunctionHandler,menuName,dropDownMenuName,buttonName):
	ATP_GUIUtils.AddButtonToDropDownMenu(eventType,sFunctionHandler,menuName,dropDownMenuName,buttonName)
	return None


#########################################################################################################################################
# 	RemoveButtonFromDropDownMenu(menuName,dropDownMenuName,buttonName)								#
#																	#
#	Args:	menuName	  - the name of the Character menu, the possible names are:						#
#				    "Helm","Tactical","Commander","Science","Engineering"						#
#		dropDownMenuName  - the name of the submenu where your button is in eg "Warp Speed"					#
#		buttonName	  - name of the button you want to delete button eg "Warp 10"						#
#	Return: None															#
#																	#
#	Full Example: RemoveButtonFromDropDownMenu("Helm","Warp Speed","Warp 10")							#
#																	#
#########################################################################################################################################
def RemoveButtonFromDropDownMenu(menuName,dropDownMenuName,buttonName):
	ATP_GUIUtils.RemoveButtonFromDropDownMenu(menuName,dropDownMenuName,buttonName)
	return None



##################################################################################
##################################################################################
##	Corbonite Functions							##
##################################################################################
##################################################################################

#################################################################################
#	IsCorboniteHitEvent							#
#										#
#	Args: a Weapon Hit Event						#
#	Return: TRUE it is a valid Corbonite Hit else FALSE			#
#################################################################################
def IsCorboniteHitEvent(pEvent):
	return QuickBattleAddon.IsCorboniteHitEvent()


#################################################################################
#	IsPlayerCorbonite()							#
#										#
#	Args: None								#
#	Return: TRUE if the player has corboniteshields that are working	#
#################################################################################
def IsPlayerCorbonite():
	return QuickBattleAddon.IsPlayerCorbonite()


#################################################################################
#	SetPlayerCorboniteOff()							#
#	Unpowers the corbonite reflector of the player if possible		#
#	Args: None								#
#	Return: None								#
#################################################################################
def SetPlayerCorboniteOff():
	QuickBattleAddon.SetPlayerCorboniteOff()


#################################################################################
#	SetPlayerCorboniteOn()							#
#	Powers the corbonite reflector of the player if possible		#
#	Args: None								#
#	Return: None								#
#################################################################################
def SetPlayerCorboniteOn():
	QuickBattleAddon.SetPlayerCorboniteOn()



##################################################################################
##################################################################################
##	Ablative Armour								##
##################################################################################
##################################################################################
def HasAblativeArmour(pShip):
	return QuickBattleAddon.HasAblativeArmour(pShip)

def GetAblativeArmour(pShip):
	return QuickBattleAddon.GetAblativeArmour(pShip)

def RegisterShipForArmourBar(ID,pHealthGauge):
	QuickBattleAddon.RegisterShipForArmourBar(ID,pHealthGauge)



##################################################################################
##################################################################################
##	Special Power								##
##################################################################################
##################################################################################
def HasSufficientSpecialPower(pShip,fAmount):
	return QuickBattleAddon.HasSufficientSpecialPower(pShip,fAmount)

def AdjustSpecialPower(pShip,fAmount):  #fAmount positive when draining, negative when charging power
	return QuickBattleAddon.AdjustSpecialPower(pShip,fAmount)



##################################################################################
##################################################################################
##	Warp Related Functions							##
##################################################################################
##################################################################################

#########################################################################################
#	GetWarpTravelTime(pShip)							#
#											#
#	Gives the time to warp travel (in seconds)					#	
#	Args: 	pShip 	A ship								#
#											#
#	Return: -1.0 if an error occured						#
#########################################################################################
def GetWarpTravelTime(pShip):
	try:
		from Universe import ATP_Constellations
		return ATP_Constellations.GetWarpTravelTime(pShip)
	except:
		return -1.0


#########################################################################################
#	GetDistance(pSet1,pSet2)							#
#											#
#	Gives the distance of two sets in lightyears					#	
#	Args: 	two pointers to a set							#
#											#
#	Return: -1.0 if an error occured (unbound in ATP_Constellations)		#
#		the distance in floating point						#
#########################################################################################
def GetDistance(pSet1,pSet2):
	from Universe import ATP_Constellations
	return ATP_Constellations.GetDistance(pSet1,pSet2)


#########################################################################################
#	ForceNacelles(pShip,sState)							#
#											#
#	Forces the nacelles if present from pShip up 					#	
#	Args: 	pShip 									#
#		sState: Move them "Up" or "Down"					#
#	Return: None									#
#########################################################################################
def ForceNacelles(pAction,pShip,sState):
	from Actions import ATP_Nacelle
	ATP_Nacelle.ForceNacelles(pShip,sState)
	
	return 0

#########################################################################################
#	GetNacellesSetTime(pShip,sState)						#
#											#
#	Gives the time it will take to move the nacelles of pShip			#	
#	Args: 	pShip 									#
#		sState: if Moving them "Up" or "Down"					#
#	Return: time to set the nacelles (in gameseconds)				#
#########################################################################################
def GetNacellesSetTime(pShip,sState):
	from Actions import ATP_Nacelle
	return ATP_Nacelle.GetNacellesSetTime(pShip,sState)


#################################################################################################
#	GetNacellePositions(pShip)								#
#												#
#	Gives a list of NiPoint3 (yuck!!!) vectors indicating the different warp coil locations	#
#												#
#	Args: 	pShip 										#
#	Return: a List of NiPoint3 pointers							#
#################################################################################################
def GetNacellePositions(pShip):
	from Actions import ATP_Nacelle
	return ATP_Nacelle.GetNacellePositions(pShip)
	
	