import App

import FoundationTech
import MissionLib

# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.drainerWeapon() in Apollo's Advanced Technologies.

from DisablerYields import *

def MPDisable(pTarget, pParentID, pSubSys):
	# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs -Apollo

	pSet = pTarget.GetContainingSet()

	if not pSet:
		return

	pSubSystemProp = pSubSys.GetProperty()
	fDisabled = pSubSys.GetMaxCondition() * pSubSystemProp.GetDisabledPercentage() * 0.99
	fDam = pSubSys.GetCondition() - fDisabled
	if fDam < 0.0:
		return


	kPoint = pSubSys.GetWorldLocation()
	kA = pTarget.GetWorldLocation()

	print kA.x, kA.y, kA.z
	print kPoint.x, kPoint.y, kPoint.z

	# Create the torpedo.
	pTorp = App.Torpedo_Create('ftb.Projectiles.FTBDummy', kPoint)

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(pTarget.GetObjID())
	pTorp.SetParent(pParentID)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)
	pTorp.SetDamage(fDam)
	pTorp.SetTranslateXYZ(kPoint.x, kPoint.y, kPoint.z)

	pTorp.UpdateNodeOnly()



class DamperWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		if FoundationTech.EffectsLib:
			EffectsLib.CreateSpecialFXSeq(pShip, pEvent, 'Damper')

		pShipID = pShip.GetObjID()

		pPower = pShip.GetPowerSubsystem()
		if pPower:
			MPDisable(pShip, pTorp.GetParentID(), pPower)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pShields = pShip.GetShields()
		if pShields:
			MPDisable(pShip, pTorp.GetParentID(), pShields)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pCloak = pShip.GetCloakingSubsystem()
		if pCloak:
			MPDisable(pShip, pTorp.GetParentID(), pCloak)

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pPlayer = MissionLib.GetPlayer()
		if pPlayer.GetObjID() == pShip.GetObjID():
			# pSound = App.g_kSoundManager.GetSound("PowerDisabled")
			# if pSound:
			# 	pSound.Play()

			if FoundationTech.BridgeFX:
				FoundationTech.BridgeFX.CreateDrainEffect()


class _DamperWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
		if FoundationTech.EffectsLib:
			EffectsLib.CreateSpecialFXSeq(pShip, pEvent, 'Damper')

		pPlayer = MissionLib.GetPlayer()
		if pPlayer.GetObjID() == pShip.GetObjID():
			pSound = App.g_kSoundManager.GetSound("PowerDisabled")
			if pSound:
				pSound.Play()

			if FoundationTech.BridgeFX:
				FoundationTech.BridgeFX.CreateDrainEffect()

		pPower = pShip.GetPowerSubsystem()
		if pPower:
			pInstance.AdjustMainBattery(pShip, pPower, 0.0)
			pInstance.AdjustBackupBattery(pShip, pPower, 0.0)

		MultipleDisableDef.OnYield(self, pShip, pInstance, pEvent, pTorp)

oDamperWeapon = DamperWeaponDef('Damper Weapon', {
	'lYields':		[
		# TechDef Instance, Time
		(oWarpDisable,    60),
		(oImpulseDisable, 30),
		(oShieldDisable,  30),
		(oCloakDisable,   60),
		(oPowerDisable,   20),
	]
})


class DamperImmuneDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and oYield.IsDrainYield():
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)


oDamperImmune = DamperImmuneDef('Damper Immune')


# print 'Damper Weapon loaded'
