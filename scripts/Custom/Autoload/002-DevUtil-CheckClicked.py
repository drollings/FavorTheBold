# This used to be in LaunchShipHandlers, by Sleight42.



#######################
# What does this thing do? asked by Defiant
# maybe also Deprecated?
#######################
# Looks to me like a utility function for development, not regular use.
# Pretty nifty if you ask me.  We should put this in its own plugin.  -Dasher42
def TargetListClicked( pObject, pEvent):
	casts = [App.TGEventHandlerObject_Cast, \
			 App.ShipClass_Cast, \
			 App.ShipSubsystem_Cast, \
			 App.TGPane_Cast, \
			 App.TGButton_Cast, \
			 App.TGTextButton_Cast, \
			 App.STMenu_Cast, \
			 App.STButton_Cast, \
			 App.TGIntEvent_Cast,\
			 App.TGBoolEvent_Cast,\
			 App.TGObjPtrEvent_Cast,\
			 App.TGCharEvent_Cast,\
			 App.TGShortEvent_Cast,\
			 App.TGFloatEvent_Cast,\
			 App.TGStringEvent_Cast]
	for cast in casts:
		obj = cast( pObject)
		if( obj != None):
			print "TargetListClicked pObject is a",obj
	for cast in casts:
		obj = cast( pEvent)
		if( obj != None):
			print "TargetListClicked pEvent is a",obj
			if( cast == App.TGIntEvent_Cast):
				print "TGIntEvent val", str( obj.GetInt())
	for cast in casts:
		obj = cast( pEvent.GetDestination())
		if( obj != None):
			print "TargetListClicked pEvent.GetDestination() is a",obj
	for cast in casts:
		obj = cast( pEvent.GetSource())
		if( obj != None):
			print "TargetListClicked pEvent.GetSource() is a",obj


