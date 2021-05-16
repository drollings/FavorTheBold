# Foundation Icons Extension 20030406 for Bridge Commander
# Written April 6, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import Foundation

print 'Outdated Foundation, installing WeaponIcons extensions'


def InitializeIcons(kIcons, type):
	try:
		for i in Foundation.dIcons[type]:
			i(kIcons)
	except KeyError:
		pass



# In order to make new icons, you should have a script like the below appended
# to a list in the dIcons dictionary.
def WidePhasers(kIcons):
	# Dasher's all-around icon support
	kTextureHandle = kIcons.LoadIconTexture('Data/Icons/PhaserArcsWide.tga')
	kIcons.SetIconLocation(550, kTextureHandle, 0, 0, 126, 70)
	kIcons.SetIconLocation(555, kTextureHandle, 1, 71, 49, 29)

	kTextureHandle = kIcons.LoadIconTexture('Data/Icons/PhaserFieldsWide.tga')
	kIcons.SetIconLocation(551, kTextureHandle, 2, 2, 83, 59)
	kIcons.SetIconLocation(552, kTextureHandle, 2, 60, 83, 54)

	kIcons.SetIconLocation(556, kTextureHandle, 93, 24, 36, 25)
	kIcons.SetIconLocation(557, kTextureHandle, 93, 24, 34, 22)

	# Invisible ones
	kIcons.SetIconLocation(374, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(520, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(375, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(522, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(523, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(560, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(561, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(562, kTextureHandle, 40, 30, 1, 1)
	kIcons.SetIconLocation(380, kTextureHandle, 40, 30, 1, 1)



Foundation.InitializeIcons = InitializeIcons
Foundation.dIcons = { 'Weapon': [ WidePhasers ] }





