import App
import BaseAI
import math

e0 = App.TGPoint3()
e0.SetXYZ(0.0,0.0,0.0)
eZ = App.TGPoint3()
eZ.SetXYZ(0.0,0.0,1.0)

half_sqrt3 = math.sqrt(3.0)/2.0

class ATP_PositionByCircle(BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		## Parent class init first.
		BaseAI.BaseAI.__init__(self, pCodeAI)

		## Set default values for parameters that have them.
		self.SetupDefaultParams( self.SetPrecision )
		self.SetRequiredParams (	( 'pOrbitted',    'SetOrbitted'    ),
						( 'pDestination', 'SetDestination' ) 	)
		self.SetExternalFunctions( ('SetTarget','SetDestination') )

		## Save a reference to our module, so the module isn't
		## unloaded unexpectedly.
		self.pModule = __import__(__name__)

		## Own params
		self.BU = copyVector(eZ)

	## The object we're circling
	def SetOrbitted(self,pOrbitted):
		self.pOrbitted = pOrbitted

	## The object we are going to
	def SetDestination(self,pDestination):
		self.pDestination = pDestination

	## How precise do we want to be
	def SetPrecision(self,fDistanceCloseEnough = 3.0,fDotCloseEnough = 0.9):
		self.fDistanceCloseEnough	= fDistanceCloseEnough
		self.fDotCloseEnough		= fDotCloseEnough
	
	def GetNextUpdateTime(self):
		return 0.5

	def GetStatusInfo(self):
		return ''

	## The real stuff
	def Update(self):
		## Involved ship
		pShip = self.pCodeAI.GetShip()
		
		## The three involved points
		B = self.pOrbitted.GetWorldLocation()
		P = pShip.GetWorldLocation()
		D = self.pDestination.GetWorldLocation()

		## The three difference vectors
		BP = copyVector(P)
		BP.Subtract(B)
		BD = copyVector(D)
		BD.Subtract(B)
		PD = copyVector(D)
		PD.Subtract(P)

		## Distances
		d = BD.Length()	## radial distance
		e = BP.Length() ## radial distance
		g = PD.Length()	## real distance
	
		## Unitize
		BD.Unitize()
		BP.Unitize()
		
		## Tangent distance needed to cover
		BDtemp = copyVector(BD)
		BDtemp.Subtract(BP)
		f = BDtemp.Length() ## tangent distance

		# print 'radial:',d-e,'\tglobal:',g,'\ttangent:',f

		## Are we close enough ?
		if g > self.fDistanceCloseEnough:
			## Scale accordingly			
			pImpulse = pShip.GetImpulseEngineSubsystem()
			v_max	 = pImpulse.GetMaxSpeed()					
		
			### Tangent movement
			## Normal on the 'spanned' plane			
			BU = BP.Cross(BD)
			if BU.Length() <= 0.01:
				BU = copyVector(eZ)
			BU.Unitize()			
			
			## Needed speed vector for an orbitting from P to D, with centre in B
			VT = BU.Cross(BP)
			VT.Unitize()
			vt = min(3.5*v_max,f/self.GetNextUpdateTime())
			VT.Scale(vt)

			### Radial movement
			VR = copyVector(BP)
			VR.Unitize()
			if d > e:
				vr = min(v_max,(d-e)/self.GetNextUpdateTime())
			else:
				vr = -min(v_max,(e-d)/self.GetNextUpdateTime())
			VR.Scale(vr)
		
			## Summed velocity
			VV = copyVector(VT)
			VV.Add(VR)			

			## What speed do we want ?
			vv = VV.Length()

			## Alignment to the speed
			VV.Unitize()
			pShip.TurnTowardOrientation(VV,BU)

			## How well is our current orientation to the desired velocity ?
			F = pShip.GetWorldForwardTG()
			k = VV.Dot(F)

			## Fuzzy modification
			k = max(0,-1.0+2.0*k)
			
			## Selected speed
			v_select = min( k * v_max , vv )

			## Set our speed
			pShip.SetSpeed(v_select, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )					

			## Still busy
			return App.ArtificialIntelligence.US_ACTIVE

		else:
			# print 'Last refinement'

			## No translate speed
			pShip.SetSpeed(0.0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )

			## Angle with destination
			F = self.pDestination.GetWorldForwardTG()			
			E = pShip.GetWorldForwardTG()

			## Cos of angle with the destination
			a = E.Dot(F)

			if a > self.fDotCloseEnough:
				## We have arrived
				return App.ArtificialIntelligence.US_DONE
			else:
				## Too seperated, turn toward it
				U = self.pDestination.GetWorldUpTG()
				pShip.TurnTowardOrientation(F,U)
			
				## Still busy
				return App.ArtificialIntelligence.US_ACTIVE


def copyVector(V):
	U = App.TGPoint3()
	U.Set(V)
	return U