import math


######################################################################################
# Used for testing in small modules.  Comment out import App, instantiate this as App.




class point:
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		self.x = x
		self.y = y
		self.z = z
	def Set(self, pt):
		self.x = pt.x
		self.y = pt.y
		self.z = pt.z
	def SetTranslateXYZ(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def Add(self, pt):
		self.x = self.x + pt.x
		self.y = self.y + pt.y
		self.z = self.z + pt.z
	def Subtract(self, pt):
		self.x = self.x - pt.x
		self.y = self.y - pt.y
		self.z = self.z - pt.z
	def Unitize(self):

		x = self.x * self.x
		y = self.y * self.y
		z = self.z * self.z
		return math.sqrt(x + y + z)

	def SetStatic(self, num):
		pass

	def SetXYZ(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def AlignToVectors(self, a, b):
		pass
	def SetSpeed(self, num):
		pass
	def Update(self, num):
		pass
	def SetupDamage(self, a, b):
		pass
	def AddNebulaSphere(self, x, y, z, diameter):
		pass

	def UpdateNodeOnly(self):
		pass
	def GetWorldLocation(self):
		return self
	def SetAtmosphereRadius(self, r):
		pass


class ship(point):
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		point.__init__(self, x, y, z)

class set:
	def __init__(self):
		self.list = {}
	def AddObjectToSet(self, obj, name):
		self.list[name] = obj
	def DeleteObjectFromSet(self, name):
		del self.list[name]
	def GetName(self):
		return 'Test'



def PrintPt(pt):
	return '(%2.5f %2.5f %2.5f)' % (pt.x, pt.y, pt.z)


class EventManager:
	def __init__(self):
		pass

	def AddBroadcastPythonFuncHandler(self, key, game, name):
		print 'Registering', key, game, "'" + name + "'"
		print FoundationTriggers.__dict__.keys()

	def RemoveBroadcastHandler(self, key, game, name):
		print 'Removing', key, game, "'" + name + "'"
		print FoundationTriggers.__dict__.keys()



class DummyApp:
	def __init__(self):
		self.seqIssued = {}
		self.counter = 0
		self.g_kSystemWrapper = point()
		self.g_kSystemWrapper.GetRandomNumber = self.GetRandomNumber
		self.TGPoint3 = point
		self.g_kEventManager = EventManager()
	def __getattr__(self, name):
		if self.seqIssued.has_key(name):	return self.seqIssued[name]
		self.seqIssued[name] = self.counter
		self.counter = self.counter + 1
		return self.counter - 1

	def GetRandomNumber(self, num):
		import random
		return num * random.random()
	def Game_GetCurrentGame(self):
		return None

	def Sun_Create(self, d, a, f, b, fl):
		return point()
	def Planet_Create(self, d, m):
		return point()
	def Ship_Create(self, x, y, z):
		return point(x, y, z)
	def Set_Create(self):
		return set()
	def Waypoint_Create(self, x, y, z):
		return point(x, y, z)
	def MetaNebula_Create(self, r, g, b, x1, x2, s1, s2):
		return point(0, 0, 0)
	def UtopiaModule_GetNextEventType(self):
		return self.__getattr__('')
