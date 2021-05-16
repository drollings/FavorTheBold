###############################################################################
#	Filename	ShipDisplay.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Scripts to create and update the ship display UI.
#	
#	Created	5112001 -	Erik Novales
###############################################################################

import App
from Tactical.Interface import DamageDisplay
from Tactical.Interface import ShieldsDisplay

TRUE=1
FALSE=0

SelfDisplay=None
EnemyDisplay=None

DEBUG=FALSE

ACTIVATE_ARMOUR=TRUE

pArmourGaugePass=None


###############################################################################
#	SetShipID(pDisplay)
#	
#	Sets the ID of the ship in the display.
#	
#	Args:	pDisplay	- the display
#			idNewShip	- the ID of the new ship in the display
#	
#	Return:	none
###############################################################################
def SetShipID(pDisplay, idNewShip):
	# Get the game object.
	pGame = App.Game_GetCurrentGame()

	kEmptyColor = App.TGColorA()
	kEmptyColor.SetRGBA(1.0,0.0,0.0,App.g_kSubsystemEmptyColor.a)

	kFillColor = App.TGColorA()
	kFillColor.SetRGBA(210.0/255.0,210.0/255.0,210.0/255.0,App.g_kSubsystemFillColor.a)

	idShip = pDisplay.GetShipID()
	pShieldsDisplay = pDisplay.GetShieldsDisplay()
	pDamageDisplay = pDisplay.GetDamageDisplay()
	pHealthGauge = pDisplay.GetHealthGauge()
	
	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idNewShip))


	if pShip:
 		succes=FALSE
		pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		while (pSubsystem != None):
			if(pSubsystem.GetName()=="Ablative Armour"):
				succes=TRUE
				break
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
		pShip.EndGetSubsystemMatch(pIterator)

		pArmour=pSubsystem

		if not succes:
			pArmour=None

		if pArmour:
			if DEBUG:
				print "Armour Detected, Registering it"
			kEmptyColor = App.TGColorA()
			kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
			kFillColor = App.TGColorA()
			kFillColor.SetRGBA(210.0/255.0,210.0/255.0,210.0/255.0,App.g_kSubsystemFillColor.a)

			pHealthGauge.SetFillColor(kFillColor)
			pHealthGauge.SetEmptyColor(kEmptyColor)
			
			from Custom.AdvancedTechnologies.Data import QuickBattleAddon
			QuickBattleAddon.RegisterShipForArmourBar(pShip.GetObjID(),pHealthGauge)

		else:
			kFillColor = App.TGColorA()
			kFillColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
			kEmptyColor = App.TGColorA()
			kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r,App.g_kSubsystemEmptyColor.g,App.g_kSubsystemEmptyColor.b,App.g_kSubsystemEmptyColor.a)

			pHealthGauge.SetFillColor(kFillColor)
			pHealthGauge.SetEmptyColor(kEmptyColor)
			


	# If we currently have a valid ship ID, remove events for it.
	if (idShip != App.NULL_ID):
		# Remove display specific events before setting new ShipID.
		pShieldsDisplay.RemoveEvents()
		pDamageDisplay.RemoveEvents()

	# Set new ship ID.
	pDisplay.SetShipIDVar(idNewShip)

	# If valid ship ID.
	if (idNewShip != App.NULL_ID):
		pHealthGauge.SetVisible(0)
	else:
		# No ship.
		pHealthGauge.SetNotVisible(0)

	
	# Update displays for new ship.
	pShieldsDisplay.UpdateForNewShip()
	pDamageDisplay.UpdateForNewShip()

	
	#Add and position the six icons
	pBeingUCB = App.TGIcon_Create("DamageIcons",0)
	pDoingUCB = App.TGIcon_Create("DamageIcons",0)
	pBeingINV = App.TGIcon_Create("DamageIcons",5)
	pDoingINV = App.TGIcon_Create("DamageIcons",5)
	pBeingASS = App.TGIcon_Create("DamageIcons",6)
	pDoingASS = App.TGIcon_Create("DamageIcons",6)
	pYellow=App.NiColorA()
	pYellow.r=1.0
	pYellow.g=1.0
	pYellow.b=0.0
	pYellow.a=1.0
	pBlue=App.NiColorA()
	pBlue.r=0.0
	pBlue.g=0.5
	pBlue.b=1.0
	pBlue.a=1.0
	pBeingUCB.SetColor(pYellow)
	pDoingUCB.SetColor(pBlue)
	pBeingINV.SetColor(pYellow)
	pDoingINV.SetColor(pBlue)
	pBeingASS.SetColor(pYellow)
	pDoingASS.SetColor(pBlue)
	pDamageDisplay.AddChild(pBeingUCB,0.0,0.0,0)
	pDamageDisplay.AddChild(pDoingUCB,1.00*(pDamageDisplay.GetWidth()-pDoingUCB.GetWidth()),0.0,0)
	pDamageDisplay.AddChild(pBeingINV,pBeingUCB.GetRight(),0.0,0)
	pDamageDisplay.AddChild(pDoingINV,pDoingUCB.GetLeft()-pDoingINV.GetWidth(),0.0,0)
	pDamageDisplay.AddChild(pBeingASS,pBeingINV.GetRight(),0.0,0)
	pDamageDisplay.AddChild(pDoingASS,pDoingINV.GetLeft()-pDoingASS.GetWidth(),0.0,0)
	pBeingUCB.SetNotVisible()
	pDoingUCB.SetNotVisible()
	pBeingINV.SetNotVisible()
	pDoingINV.SetNotVisible()
	pBeingASS.SetNotVisible()
	pDoingASS.SetNotVisible()

	global SelfDisplay
	global EnemyDisplay

	pControl = App.TacticalControlWindow_GetTacticalControlWindow()
	if pControl.GetShipDisplay().GetObjID()==pDisplay.GetObjID():
		SelfDisplay=pDisplay,pBeingUCB,pDoingUCB,pBeingINV,pDoingINV,pBeingASS,pDoingASS
	elif pControl.GetEnemyShipDisplay().GetObjID()==pDisplay.GetObjID():
		EnemyDisplay=pDisplay,pBeingUCB,pDoingUCB,pBeingINV,pDoingINV,pBeingASS,pDoingASS
	else:
		#print "Weird Shipdisplay....."
		pass
			

	if (pShip != None):
		if pArmour:
			pHealthGauge.SetObject(pArmour)
		else:
			pHealthGauge.SetObject(pShip.GetHull())
	else:
		pHealthGauge.SetObject(pShip)



def IsBeingUCB(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[1].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[1].SetVisible()

def IsDoingUCB(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[2].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[2].SetVisible()

def IsBeingINV(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[3].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[3].SetVisible()

def IsDoingINV(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[4].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[4].SetVisible()

def IsBeingASS(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[5].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[5].SetVisible()

def IsDoingASS(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[6].SetVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[6].SetVisible()

def StopBeingUCB(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[1].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[1].SetNotVisible()

def StopDoingUCB(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[2].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[2].SetNotVisible()

def StopBeingINV(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[3].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[3].SetNotVisible()

def StopDoingINV(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[4].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[4].SetNotVisible()

def StopBeingASS(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[5].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[5].SetNotVisible()

def StopDoingASS(pShip):
	if pShip.GetObjID()==SelfDisplay[0].GetShipID():
		SelfDisplay[6].SetNotVisible()
	elif pShip.GetObjID()==EnemyDisplay[0].GetShipID():
		EnemyDisplay[6].SetNotVisible()


