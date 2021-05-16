import App
import math
import string
import loadspacehelper
import MissionLib

from ATP_Object   import *
from ATP_Vessels  import *
from ATP_Extras   import *

class Starbase(Ship):
	GREEN		= 0
	ORANGE		= 1
	RED		= 2
	FULL		= 3
	EMPTY		= 4

	TO_ENTERPOOL	= 1
	AT_ENTERPOOL	= 2
	TO_ENTERSLOT	= 3
	AT_ENTERSLOT	= 4
	IN_MAIN		= 5
	IN_SHIP		= 6
	AT_DOCK		= 7
	AT_EXITPOOL	= 8
	TO_EXITSLOT	= 9
	AT_EXITSLOT	= 10
	OUTSIDE		= 11
	
	def __init__(self):
		Ship.__init__(self)
		
		self.ExitQueue		= []
		self.ExitSlot		= 0
		self.EnterQueue		= []
		self.EnterSlot		= 0
		self.VividThings	= []
		self.NumDocks		= 20
		self.Slots		= {}
		self.EnterTrafficLight	= Starbase.GREEN
		self.ExitTrafficLight	= Starbase.GREEN
		self.MainTrafficLight	= Starbase.GREEN

		for i in range(0,self.NumDocks):
			self.Slots[i]= (0,0)

		self.ET_ARRIVED_AT_QUEUE =  GetNextEventType()
		self.ET_DOCKING_DONE	 =  GetNextEventType()
		self.ET_UNDOCKING_DONE	 =  GetNextEventType()
		self.ET_DOCK_REACHED	 =  GetNextEventType()
		self.ET_ENTER_DONE	 =  GetNextEventType()
		self.ET_LEAVEDOCK_DONE   =  GetNextEventType()
		self.ET_EXIT_DONE	 =  GetNextEventType()
		self.ET_PREENTER_DONE	 =  GetNextEventType()
		self.ET_PREEXIT_DONE	 =  GetNextEventType()
		self.ET_DOCK_PLAYER	 =  GetNextEventType()
		self.ET_UNDOCK_PLAYER	 =  GetNextEventType()

		##Debug to log
		# debug(__name__+": __init__: Creating a Starbase "+str(self.GetName()))

	def save(self,first=TRUE):
		from Custom.AdvancedTechnologies.Data.Save.ATP_Save import *
		
		## Create the object
		if first:
			write_save_file("self = Starbase("+str(self.ID)+")")

		## Upperclass
		Ship.save(self,FALSE)

		## Our lines
		write_save_file("self.ExitQueue         = "+str(self.ExitQueue))
		write_save_file("self.ExitSlot          = "+str(self.ExitSlot))
		write_save_file("self.EnterQueue        = "+str(self.EnterQueue))
		write_save_file("self.EnterSlot         = "+str(self.EnterSlot))
		write_save_file("self.VividThings       = "+str(self.VividThings))
		write_save_file("self.NumDocks          = "+str(self.NumDocks))
		write_save_file("self.EnterTrafficLight = "+str(self.EnterTrafficLight))
		write_save_file("self.ExitTrafficLight  = "+str(self.ExitTrafficLight))
		write_save_file("self.MainTrafficLight  = "+str(self.MainTrafficLight))
		write_save_file("self.Slots             = "+str(self.Slots))

	def GetVividThings(self):
		ret=[]
		for ID in self.VividThings:
			ret.append(GetByID(ID))
		return ret

	def IsDockable(self):
		return TRUE
	
	## Dynamical Holder Methods
	################################
	def CanEnterFleet(self,pFleet):
		##Check if there is enough room to start
		if self.GetNumShips()+pFleet.GetNumShips()>self.NumDocks:
			return FALSE
		return TRUE

	def CanExitFleet(self,pFleet):
		## default TRUE
		return TRUE

	def ShipDestroyed(self,pShip,pFleet):
		debug("ship "+pShip.sName+" was destroyed in me, "+self.sName)

		## ID of the ship
		SID = pShip.ID

		## In what part is the ship?
		iState = self.GetSlotState(pShip)

		## Unassign its slot
		self.UnassignSlot(pShip)

		## Huge range of needed actions, ship destruction is a real annoying thing
		if pShip.State == NORMAL:
			pass

		elif pShip.State == INTERCEPTING:
			pass

		elif pShip.State == WARPING:
			pass

		elif pShip.State == ENTERING:

			if self.IsRendered():

				if iState == Starbase.TO_ENTERPOOL:
					pass

				elif iState == Starbase.AT_ENTERPOOL:
					assert self.EnterQueue.count(SID)
					self.EnterQueue.remove(SID)

				elif iState == Starbase.TO_ENTERSLOT:
					assert self.EnterTrafficLight == Starbase.ORANGE
					self.EnterTrafficLight = Starbase.GREEN
					self.PreDock()

				elif iState == Starbase.AT_ENTERSLOT:
					assert self.EnterTrafficLight == Starbase.RED
					assert self.EnterSlot == SID
					self.EnterTrafficLight = Starbase.GREEN
					self.EnterSlot = None
					self.PreDock()

				elif iState == Starbase.IN_MAIN:
					assert self.MainTrafficLight == Starbase.RED
					
					## Allow a new ship:
					self.MainTrafficLight=Starbase.GREEN
					trial=self.EffectiveDock()
					if trial==Starbase.EMPTY:
						trial=self.EffectiveUndock()

				elif iState == Starbase.IN_SHIP:
					pass

				elif iState == Starbase.AT_DOCK:
					pass

				else:
					raise RuntimeError
			
			else:
				## Remove the delay
				self.RemoveClock("DelayedEnterDone",None,pShip,self)

			## Update the state
			## All ships entered?
			for pOther in pFleet.GetShips():
				if pOther.ID == SID:
					continue
				if pOther.State != INSIDE:
					return
			if len(pFleet.GetShips()) <=1:
				return

			## All ships entered
			pFleet.SetState(INSIDE)
				
		elif pShip.State == INSIDE:
			pass

		elif pShip.State == REPAIR:
			if hasattr(self,'dRepair'):
				if self.dRepair.has_key(pShip.ID):
					## Remove it from the list
					del self.dRepair[pShip.ID]

					## Update the state
					## All ships entered?
					for pOther in pFleet.GetShips():
						if pOther.ID == SID:
							continue
						if pOther.State != INSIDE:
							return
					if len(pFleet.GetShips()) <= 1:
						return

					## All ships exited
					pFleet.SetState(INSIDE)

					## Ships left?
					if not self.dRepair:
						## Remove the clock
						self.RemoveClock('RepairCycle')

						## Remove the dict
						del self.dRepair

		elif pShip.State == EXITING:

			if self.IsRendered():
				
				if iState == Starbase.AT_EXITPOOL:
					assert self.ExitQueue.count(SID)
					self.ExitQueue.remove(SID)

				elif iState == Starbase.TO_EXITSLOT:
					assert self.ExitTrafficLight == Starbase.ORANGE
					self.ExitTrafficLight = Starbase.GREEN
					self.PreUndock()

				elif iState == Starbase.AT_EXITSLOT:
					assert self.ExitTrafficLight == Starbase.RED
					assert self.ExitSlot == SID
					self.ExitTrafficLight = Starbase.GREEN
					self.ExitSlot = None
					self.PreUndock()

				elif iState == Starbase.IN_MAIN:
					assert self.MainTrafficLight == Starbase.RED
					
					## Allow a new ship:
					self.MainTrafficLight=Starbase.GREEN
					trial=self.EffectiveUndock()
					if trial==Starbase.EMPTY:
						trial=self.EffectiveDock()

				elif iState == Starbase.OUTSIDE:
					pass
		
				elif iState == Starbase.AT_DOCK:
					pass

				else:
					raise RuntimeError
			else:
				## Remove the delay
				self.RemoveClock("DelayedExitDone",None,pShip,self)

			## Update the state
			## All ships entered?
			for pOther in pFleet.GetShips():
				if pOther.ID == SID:
					continue
				if pOther.State != NORMAL:
					return
			if len(pFleet.GetShips()) <= 1:
				return

			## All ships exited
			pFleet.SetState(INSIDE)

		elif pShip.State == BUILDING:
			pass

		else:
			raise RuntimeError

		


	## Interal dynamical holder interface
	#################################################################

	### Enterfleet
	################################
	def ConceptualEnterFleet(self,pFleet):
		## debug
		print "fleet "+pFleet.sName+" is entering me, "+self.sName+" in a conceptual way"

		## Conceptually enter the ships
		for pShip in pFleet.GetShips():
			assert pShip.State == NORMAL	## valid state
			self.AssignSlot(pShip)
			pShip.SetState(ENTERING)
			
			if self.fEnterDelay:
				self.AddDelay("DelayedEnterDone",self.fEnterDelay,pShip,self)
			else:
				self.EnterDone(pShip)

	def RenderedEnterFleet(self,pFleet):
		## debug
		debug("fleet "+pFleet.sName+" is entering me, "+self.sName+" in a real way")

		## Heuristal temp solution
		if pFleet.ID != PLAYER_FLEET_ID:
			way = self.GetChildByName("ATP_Dock_Queue").GetNode()
			V   = way.GetWorldForwardTG()
			V.Scale(-35.0)
			V.Add(self.GetRandomVector(7.0))
			V.Add(way.GetWorldLocation())
			pFleet.Randomise()
			pFleet.SetPosition(V)
		else:
			pWay = self.GetChildByName('ATP_Dock_Queue')
			pFleet.AssignAI( [ AI_PATH+'.ATP_PositionByCirclingAI' , pWay , self , self.ET_ARRIVED_AT_QUEUE , 15.0],TRUE)		

		## Iterate over the ships
		for pShip in pFleet.GetShips():
			assert pShip.State == NORMAL	## valid state
			self.AssignSlot(pShip)
			pShip.SetState(ENTERING)

			## Modify the state
			self.SetSlotState(pShip,Starbase.TO_ENTERPOOL)			
			
		## debug
		# debug(__name__+": DockUs: AI: "+str(pFleet)+": ATP_DockAI to ATP_Dock_Queue")
	
	def ArrivedAtEnterQueue(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return
	
		## Set the ship in the queue
		self.EnterQueue.append(pShip.ID)
	
		## Modify the state
		self.SetSlotState(pShip,Starbase.AT_ENTERPOOL)
	
		## debug
		# debug(__name__+": ArrivedAtEnterQueue: "+str(pShip)+": Arrived at dockqueue")
	
		## Force a predock trial
		self.PreDock(pShip)	
			

	def PreDock(self,pShip=None):
		if self.EnterTrafficLight==Starbase.GREEN:
			## Find a ship
			if not self.EnterQueue:
				return Starbase.EMPTY

			## Give the player an advantage
			self.PutPlayerOnTop()

			pShip=GetByID(self.EnterQueue.pop(0))
			if not pShip:
				self.PreDock()
			
			##Set the light to orange
			self.EnterTrafficLight = Starbase.ORANGE

			## Modify the state
			self.SetSlotState(pShip,Starbase.TO_ENTERSLOT)

			##Assign to AI to move in
			pShip.AssignAI([AI_PATH+".ATP_MoveAI",self.GetChildByName("ATP_Dock_Slot"),self,self.ET_PREENTER_DONE],TRUE)

			## debug
			# debug(__name__+": PreDock: AI: "+str(pShip)+": ATP_DockAI, sending to Enterlight")


		elif  self.EnterTrafficLight==Starbase.RED or self.EnterTrafficLight==Starbase.ORANGE:
			##Stop the ship
			if pShip:
				pShip.AssignAI([AI_PATH+".ATP_HaltAI"],TRUE)
				#debug(__name__+": PreDock: "+str(pShip)+": has to wait at the dockqueue")
		else:
			raise RuntimeError

		return Starbase.FULL	

	def PreEnterDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		##Occupy the slot
		self.EnterSlot = pShip.ID

		## Modify the state
		self.SetSlotState(pShip,Starbase.AT_ENTERSLOT )

		##Set the light to red
		self.EnterTrafficLight = Starbase.RED

		## debug
		# debug(__name__+": PreEnterdone: "+str(pShip)+": Arrived at Enterlight")

		##Force an effectivedock trial
		self.EffectiveDock(pShip)
		
	def EffectiveDock(self,pShip=None):
		if self.MainTrafficLight == Starbase.GREEN:
			##Check if the starbase is not full
			if self.GetNumShips()>=self.NumDocks:
				self.EnterTrafficLight = Starbase.RED
				return Starbase.EMPTY

			## Ship on route, don't do anything
			if self.EnterTrafficLight == Starbase.ORANGE:
				return Starbase.EMPTY

			##Switch the entry light to green and Force a predock trial
			if self.EnterTrafficLight==Starbase.RED or self.EnterTrafficLight==Starbase.GREEN:
				self.EnterTrafficLight = Starbase.GREEN
				self.PreDock()
		
			##Find a ship
			pShip=GetByID(self.EnterSlot)
			if not pShip:
				return Starbase.EMPTY
			self.EnterSlot=None
				
			## Swicth the light to RED
			self.MainTrafficLight	= Starbase.RED

			## Modify the state
			self.SetSlotState(pShip,Starbase.IN_MAIN)
		
			## Mark the ship as inside the starbase and but do not yet update its fleet
			# pShip.SetHolder(self)
						
			##Disable collisions to be sure:
			pShip.GetNode().EnableCollisionsWith(self.GetNode(),FALSE)
			self.GetNode().EnableCollisionsWith(pShip.GetNode(),FALSE)

			##Assign AI to move in:
			pShip.AssignAI([AI_PATH+".ATP_DockAI",self.GetChildByName("ATP_Dock_Start_A"),self,self.ET_ENTER_DONE],TRUE)

			## debug
			# debug(__name__+": EffectiveDock: AI: "+str(pShip)+": ATP_DockAI")
	
		elif  self.MainTrafficLight==Starbase.RED:
			##Stop the ship
			if pShip:
				pShip.AssignAI([AI_PATH+".ATP_StayAI"],TRUE)
				# debug(__name__+": "+str(pShip)+": has to wait at the front main queue")

		else:
			raise RuntimeError

		return Starbase.FULL
	
	def InternalEnterDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		## Find a free spot
		slot=self.GetSlot(pShip)

		## Modify the state
		self.SetSlotState(pShip,Starbase.IN_SHIP)

		## Assign AI to move to the assigned spot:
		pPos = self.GetChildByName("ATP_Rot_"+str(self.NumDocks-1))
		pDock = self.GetChildByName("ATP_Rot_"+str(slot))
		pShip.AssignAI([AI_PATH+".ATP_MoveAIWCA",pPos,self,self.ET_DOCK_REACHED,pDock],TRUE)


		## debug
		# debug(__name__+": Enterdone: "+str(pShip)+": Sending to slot "+str(slot)+", using ATP_DockAI")

		## Allow a new ship:
		self.MainTrafficLight=Starbase.GREEN
		trial=self.EffectiveUndock()

		if trial==Starbase.EMPTY:
			## The queue was empty or busy, try the other queue
			trial=self.EffectiveDock()
			
			if trial==Starbase.EMPTY:
				## Both queues were empty or busy
				self.MainTrafficLight=Starbase.GREEN
				#debug(__name__+": Nobody ready to enter/leave now")
				return Starbase.EMPTY

		return Starbase.FULL

	def DockReached(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return	
	
		## Slot
		slot = self.GetSlot(pShip)
		
		## Assign AI to move to the assigned spot:
		pShip.AssignAI([AI_PATH+".ATP_DockPreciseAI",self.GetChildByName("ATP_Dock_"+str(slot)),self,self.ET_DOCKING_DONE],TRUE)

		## debug
		# debug(__name__+": Dock Reached: "+str(pShip)+": Sending to slot "+str(slot)+", using ATP_DockAI")

	def DockingDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		## Modify the state
		self.SetSlotState(pShip,Starbase.AT_DOCK)

		## The ship is sound and safe at the location, set it to sleep
		pShip.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],TRUE)

		## Change the ship state
		self.EnterDone(pShip)		

		## debug
		debug(__name__+": DockingDone: "+str(pShip)+" to sleep...")

			
	## Exit handlers
	#####################################	
	def ConceptualExitFleet(self,pFleet):
		## Conceptually enter the ships
		for pShip in pFleet.GetShips():
			assert pShip.State == INSIDE	## valid state
			pShip.SetState(EXITING)
			if self.fExitDelay:
				self.AddDelay("DelayedExitDone",self.fExitDelay,pShip,self)
			else:
				self.ExitDone(pShip)

	def RenderedExitFleet(self,pFleet):
		# debug(__name__+": UndockUs: "+str(pFleet))

		##Set the ships in the queue
		for pShip in pFleet.GetShips():
			assert pShip.State == INSIDE	## valid state
			pShip.SetState(EXITING)
			self.ExitQueue.append(pShip.ID)

			## Modify the state
			self.SetSlotState(pShip,Starbase.AT_EXITPOOL)
				
		## Force a predock trial
		self.PreUndock()
		 

	def PreUndock(self,pShip=None):
		if self.ExitTrafficLight==Starbase.GREEN:
			## Find a ship
			if not self.ExitQueue:
				return Starbase.EMPTY

			## Give the player an advantage
			self.PutPlayerOnTop()

			pShip = GetByID(self.ExitQueue.pop(0))
			if not pShip:
				self.PreUndock()
		
			## Modify the state
			self.SetSlotState(pShip,Starbase.TO_EXITSLOT)

			##Set the light to orange
			self.ExitTrafficLight = Starbase.ORANGE

			## Get the slot
			slot = self.GetSlot(pShip)
		
			## debuf-g
			# debug(__name__+": Sending "+str(pShip)+" to ExitLight")

			## Assign to AI to move out
			pRot = self.GetChildByName("ATP_Rot_"+str(slot))
			pShip.AssignAI([AI_PATH+".ATP_DockPreciseAI",pRot,self,self.ET_LEAVEDOCK_DONE,pRot],TRUE)
	
		elif  self.ExitTrafficLight==Starbase.RED or self.ExitTrafficLight == Starbase.ORANGE:
			##Stop the ship
			if pShip:
				pShip.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],TRUE)
				# debug(__name__+": Holding "+str(pShip)+" to its slot")
		else:
			raise RuntimeError

	def LeaveDockDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		## Get the slot
		slot = self.GetSlot(pShip)

		##Assign to AI to move out
		pRot = self.GetChildByName("ATP_Rot_"+str(slot))
		pShip.AssignAI([AI_PATH+".ATP_MoveAIWCA",pRot,self,self.ET_PREEXIT_DONE],TRUE)

	def PreExitDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		##Occupy the slot
		self.ExitSlot = pShip.ID

		## Modify the state
		self.SetSlotState(pShip,Starbase.AT_EXITSLOT)

		## Set the exit light to red
		self.ExitTrafficLight = Starbase.RED

		## debug
		# debug(__name__+": PreExitDone: "+str(pShip)+": Arrived At Main Light")

		##Force an effectiveundock trial
		self.EffectiveUndock(pShip)		

	def EffectiveUndock(self,pShip=None):
		if self.MainTrafficLight == Starbase.GREEN:
			## Ship on route, don't do anything
			if self.ExitTrafficLight == Starbase.ORANGE:
				return Starbase.EMPTY

			##Switch the entry light to green and Force a predock trial
			if self.ExitTrafficLight==Starbase.RED or self.ExitTrafficLight==Starbase.GREEN:
				self.ExitTrafficLight = Starbase.GREEN
				self.PreUndock()
		
			##Find a ship
			pShip=GetByID(self.ExitSlot)
			if not pShip:
				return Starbase.EMPTY
			self.ExitSlot=None

			## Modify the state
			self.SetSlotState(pShip,Starbase.IN_MAIN)
				
			##Swicth the light to RED
			self.MainTrafficLight	= Starbase.RED
		
			##Mark the ship as outside the starbase and but do not yet update its fleet
			# pShip.SetHolder(self.GetHolder())
							
			##Disable collisions to be sure:
			pShip.GetNode().EnableCollisionsWith(self.GetNode(),FALSE)
			self.GetNode().EnableCollisionsWith(pShip.GetNode(),FALSE)

			##Assign AI to move out:
			pShip.AssignAI([AI_PATH+".ATP_MoveAIWCA",self.GetChildByName("ATP_Undock_Start_A"),self,self.ET_EXIT_DONE],TRUE)

			## debug
			#debug(__name__+": EffectiveUndock: AI: "+str(pShip)+": ATP_DockAI")
	
		elif  self.MainTrafficLight==Starbase.RED:
			##Stop the ship
			if pShip:
				pShip.AssignAI([AI_PATH+".ATP_StayAI"],TRUE)
				#debug(__name__+": "+str(pShip)+" has to wait before the Inside Main Light")
		else:
			raise RuntimeError
	
	def InternalExitDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		## Assign AI to move to the assigned spot:
		pShip.AssignAI([AI_PATH+".ATP_MoveAI",self.GetChildByName("ATP_Undock_Queue"),self,self.ET_UNDOCKING_DONE],TRUE)

		## debug
		# debug(__name__+": Exitdone: "+str(pShip)+": Arrived Outside")

		## Modify the state
		self.SetSlotState(pShip,Starbase.OUTSIDE)

		## Allow a new ship:
		self.MainTrafficLight=Starbase.GREEN
		trial=self.EffectiveDock()
		
		if trial==Starbase.EMPTY:
			##The queue was empty, try the other queue
			trial=self.EffectiveUndock()
			
			if trial==Starbase.EMPTY:
				self.MainTrafficLight=Starbase.GREEN
				debug(__name__+": Nobody ready/present to leave/enter")
				return Starbase.EMPTY
		return Starbase.FULL

	def UndockingDone(self,gEvent):
		## Decode event
		pEvent = DecodeEvent(gEvent)
		pShip = pEvent.GetSource()
		if not pShip:
			return

		## The ship is sound and safe at the location, totally release it
		pShip.AssignAI()

		## Unassign the slot
		self.UnassignSlot(pShip)

		## End call
		self.ExitDone(pShip)

		## debug
		debug(__name__+": UndockingDone: "+str(pShip)+": Sound and safe?")

	def DelayedExitDone(self,gEvent):
		## Decode the event
		pEvent = DecodeEvent(gEvent)
		pShip =  pEvent.GetSource()
		if not pShip:
			return

		## Unassign the slot
		self.UnassignSlot(pShip)

		## Handler
		self.ExitDone(pShip)
							
	

	## Slot functions
	######################################################
	def SetSlotState(self,pShip,iState):
		for slot in self.Slots.keys():
			if self.Slots[slot][0]==pShip.ID:
				self.Slots[slot] = (pShip.ID , iState)

	def GetSlotState(self,pShip):
		for slot in self.Slots.keys():
			if self.Slots[slot][0]==pShip.ID:
				return self.Slots[slot][1]

	def GetSlot(self,pShip):
		for slot in self.Slots.keys():
			if self.Slots[slot][0] == pShip.ID:
				return slot
		return None

	def SwapSlots(self,pShipA,pShipB):
		## Find the two slots
		slotA = None
		slotB = None
		for slot in self.Slots.keys():
			if self.Slots[slot][0] == pShipA.ID:
				slotA = slot
			if self.Slots[slot][0] == pShipB.ID:
				slotB = slot
		if not (slotA and slotB):
			return
	
		## Swap
		self.Slots[slotA] , self.Slots[slotB] = self.Slots[slotB] , self.Slots[slotA]
			
		
	def AssignSlot(self,pShip):
		freeSlot = -1

		## What order of slots
		keys = self.Slots.keys()		
		keys.sort()

		if self.IsRendered():
			## In rendered state, send ship to the lower numbers
			pass
		else:
			## In unrendered state, send ship to the higher numbers
			keys.reverse()
		
		## Find a free slot
		for slot in keys:
			if self.Slots[slot][0] == 0:
				freeSlot = slot
				self.Slots[slot] = (pShip.ID , Starbase.AT_DOCK)
				#debug("Assigned Slot "+str(slot)+" to "+pShip.GetName())
				break		
		if freeSlot == -1:
			## Found none
			raise RuntimeError

		return freeSlot

	def UnassignSlot(self,pShip):
		for slot in self.Slots.keys():
			pOtherID = self.Slots[slot][0]
			if pShip.ID == pOtherID:
				self.Slots[slot] = (0,0)
				return

	def PutPlayerOnTop(self):
		## Put playerfleet on top
		ExitQueue = []
		for ID in self.ExitQueue:
			pShip = GetByID(ID)
			if pShip:
				if pShip.GetFleet().ID == PLAYER_FLEET_ID:
					ExitQueue.insert(0,ID)
				else:
					ExitQueue.append(ID)
		self.ExitQueue = ExitQueue[:]
		
		## Put playerfleet on top
		EnterQueue = []
		for ID in self.EnterQueue:
			pShip = GetByID(ID)
			if pShip:
				if pShip.GetFleet().ID == PLAYER_FLEET_ID:
					EnterQueue.insert(0,ID)
				else:
					EnterQueue.append(ID)
		self.EnterQueue = EnterQueue[:] 
	

	## Waypoints
	###################################################
	def GenerateWaypoints(self):
		pSet = self.GetNode().GetContainingSet()
		
		T_0 = ("ATP_Dock_Start_A"  ,"ATP_Dock_Start_B"  ,"ATP_Dock_End_A"  ,"ATP_Dock_End_B")
		T_1 = ("ATP_Undock_Start_A","ATP_Undock_Start_B","ATP_Undock_End_A","ATP_Undock_End_B")
		T_2 = ("ATP_Dock_Queue"    ,)
		T_3 = ("ATP_Undock_Queue"  ,)
		T_4 = ("ATP_Dock_Slot"	   ,)
		T_5 = ("ATP_Undock_Slot"   ,)
		T_6 = ("ATP_Crosshair"   ,)
		T   = ( T_0 , T_1 , T_2 , T_3, T_4 ,T_5, T_6)

		for t in T:
			pWaypoint=None
			for s in t:
				Prev     = pWaypoint
				pWaypoint = Waypoint(s,self,bAttach = FALSE)
				pWaypoint.GetNode().SetSpeed(5.0)
				pWaypoint.GetNode().SetStatic(FALSE)
				vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(self.GetNode(),s)
				#PositionObjectFromLocalInfo(pWaypoint.GetNode(),vPos,vFwd,vUp)
				PositionObjectFromInfo(pWaypoint.GetNode(),self.Node,vPos,vFwd,vUp)
				if Prev:
					Prev.GetNode().InsertAfterObj(pWaypoint.GetNode())
		
	def GenerateDockpoints(self):
		pSet = self.GetNode().GetContainingSet()
		
		f=240.0/self.NumDocks
		for num in range(0,self.NumDocks):		
			
			pWaypoint = Waypoint("ATP_Dock_"+str(num),self,bAttach = FALSE)
			pWaypoint.GetNode().SetSpeed(5.0)
			pWaypoint.GetNode().SetStatic(FALSE)
			vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(self.GetNode(),"ATP_Dock_Pos")
			PositionObjectFromInfo(pWaypoint.GetNode(),self.Node,vPos,vFwd,vUp,60.0+num*f)
				
		Prev = None
		f=250.0/self.NumDocks
		for num in range(0,self.NumDocks):		
			pWaypoint = Waypoint("ATP_Rot_"+str(self.NumDocks-num-1),self,bAttach = FALSE)
			pWaypoint.GetNode().SetSpeed(10.0)
			pWaypoint.GetNode().SetStatic(FALSE)
			vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(self.GetNode(),"ATP_Rot_Pos")
			PositionObjectFromInfo(pWaypoint.GetNode(),self.Node,vPos,vFwd,vUp,55.0+(self.NumDocks-num-1)*f)
			if Prev:
				Prev.GetNode().InsertAfterObj(pWaypoint.GetNode())
			Prev = pWaypoint

		#Attach ATP_Undock_Slot to it:
		if Prev:
			Prev.GetNode().InsertAfterObj(self.GetChildByName("ATP_Undock_Slot").GetNode())

	def Randomise(self):
		i = self.NumDocks

		## Free the slots
		for i in range(0,self.NumDocks):
			self.Slots[i]= (0,0)
		freeslots = self.NumDocks
		bFull = FALSE

		for pFleet in self.GetFleets():
			
			if pFleet.State in (INSIDE,ENTERING,REPAIR,BUILDING):

				iShips = pFleet.GetNumShips()
				if freeslots - iShips < 0:
					bFull = TRUE
				freeslots = freeslots - iShips
 			
				if not bFull:
					for pShip in pFleet.GetShips():
						self.AssignSlot(pShip)
						pShip.Randomise()
						slot=self.GetSlot(pShip)
						w = self.GetChildByName("ATP_Dock_"+str(slot)).GetNode()
						W = w.GetWorldLocation()
						pShip.SetPosition(W)
						pShip.GetNode().AlignToVectors(w.GetWorldForwardTG(),w.GetWorldUpTG())
				else:
					self.RandomiseFromList((pFleet,))

			elif pFleet.State == NORMAL:
				self.RandomiseFromList((pFleet,))

			elif pFleet.State == INTERCEPTING:
				self.RandomiseFromList((pFleet,))

			elif pFleet.State == EXITING:
				self.RandomiseFromList((pFleet,))

			elif pFleet.State == WARPING:	## Singular case
				pass

			else:
				raise RuntimeError
	
		## Heuristal solution to force rotation alignment on the starbase
		way=self.GetChildByName("ATP_Crosshair").GetNode()
		W = way.GetWorldLocation()
		self.SetPosition(W)
		V=way.GetWorldForwardTG()
		V.Scale(1.0)
		self.GetNode().AlignToVectors(V,way.GetWorldUpTG())

		##Other stuff

	def Render(self,pSet):
		## Solarsystem
		pSolar = self.GetSolar()

		## Rendered already?
		preRendered = self.IsRendered()

		## Base class function
		Ship.Render(self,pSet)
	
		## Extra's
		if not preRendered:
			## Make the waypoints
			self.GenerateWaypoints()
			self.GenerateDockpoints()	

			## Add Some handlers
			self.AddHandler(self.ET_ARRIVED_AT_QUEUE,	"ArrivedAtEnterQueue"	)
			self.AddHandler(self.ET_PREENTER_DONE,		"PreEnterDone"		)
			self.AddHandler(self.ET_ENTER_DONE,		"InternalEnterDone"	)		
			self.AddHandler(self.ET_DOCKING_DONE,		"DockingDone"		)
			self.AddHandler(self.ET_LEAVEDOCK_DONE,		"LeaveDockDone"		)		
			self.AddHandler(self.ET_PREEXIT_DONE,		"PreExitDone"		)
			self.AddHandler(self.ET_EXIT_DONE,		"InternalExitDone"	)
			self.AddHandler(self.ET_UNDOCKING_DONE,		"UndockingDone"		)
			self.AddHandler(self.ET_DOCK_PLAYER,		"DockPlayer"		)
			self.AddHandler(self.ET_UNDOCK_PLAYER,		"UndockPlayer"		)
			self.AddHandler(self.ET_DOCK_REACHED,		"DockReached"		)

			## Reset lights
			self.EnterTrafficLight	= Starbase.GREEN
			self.ExitTrafficLight	= Starbase.GREEN
			self.MainTrafficLight	= Starbase.GREEN			
		
	def DockPlayer(self,gEvent):
		GetPlayerFleet().Voyage(self,bInside = TRUE)

	def UndockPlayer(self,gEvent):
		GetPlayerFleet().Voyage(self,bInside = FALSE)	

	def Unrender(self):
		if self.Node:
			## Remove some handlers
			self.RemoveHandler(self.ET_ARRIVED_AT_QUEUE,	"ArrivedAtEnterQueue"	)
			self.RemoveHandler(self.ET_PREENTER_DONE,	"PreEnterDone"		)
			self.RemoveHandler(self.ET_ENTER_DONE,		"InternalEnterDone"	)		
			self.RemoveHandler(self.ET_DOCKING_DONE,	"DockingDone"		)
			self.RemoveHandler(self.ET_LEAVEDOCK_DONE,	"LeaveDockDone"		)
			self.RemoveHandler(self.ET_PREEXIT_DONE,	"PreExitDone"		)
			self.RemoveHandler(self.ET_EXIT_DONE,		"InternalExitDone"	)
			self.RemoveHandler(self.ET_UNDOCKING_DONE,	"UndockingDone"		)
			self.RemoveHandler(self.ET_DOCK_PLAYER,		"DockPlayer"		)
			self.RemoveHandler(self.ET_UNDOCK_PLAYER,	"UndockPlayer"		)
			self.RemoveHandler(self.ET_DOCK_REACHED,	"DockReached"		)			

		Ship.Unrender(self)
	
	def CanWarp(self):
		return FALSE

	def AssignAI(self,kArgs=None,force=FALSE):
		if kArgs is None:
			kArgs=[]
		kArgs=kArgs[:]

		#debug("Assigning AI for "+self.sName)

		## Own AI
		Ship.AssignAI(self,kArgs,force)

		## Children AI
		for pFleet in self.GetFleets():
			if pFleet.State in (INSIDE,BUILDING,REPAIR):
				pFleet.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],FALSE)			
			elif pFleet.State == NORMAL:
				pFleet.AssignAI()
			elif pFleet.State == INTERCEPTING:
				pass
			elif pFleet.State == ENTERING:
				pFleet.AssignAI([AI_PATH+".ATP_StayAI",App.ShipClass.GREEN_ALERT],FALSE)
			elif pFleet.State == EXITING:
				pFleet.AssignAI()
			elif pFleet.State == WARPING:
				pass
			else:
				raise RuntimeError

def PositionObjectFromInfo(pObject,pLocalInfoObject, vPos, vFwd, vUp,Z=0.0):
	M=App.TGMatrix3()
	M.MakeIdentity()
	M.MakeZRotation(toRad(Z))
	vWorldPos = pLocalInfoObject.GetWorldLocation()
	mWorldRot = pLocalInfoObject.GetWorldRotation()
	mWorldRot = M.MultMatrixLeft(mWorldRot)
	
	vPos = copyVector(vPos)
	vFwd = copyVector(vFwd)
	vUp  = copyVector(vUp)

	vPos.MultMatrixLeft( mWorldRot )
	vPos.Add(vWorldPos)
	vFwd.MultMatrixLeft( mWorldRot )
	vUp.MultMatrixLeft( mWorldRot )

	# Move the waypoint to this position/orientation.
	GetByNode(pObject).SetPosition(vPos)
	pObject.AlignToVectors(vFwd, vUp)
	pObject.UpdateNodeOnly()


