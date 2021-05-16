Sun Apr 04 15:51:45 2004
import App
g_kModifierTable = ((1.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 3.0, 1.0))

def GetModifier(iAttackerClass, iKilledClass):
    kModTable = g_kModifierTable[iAttackerClass]
    return kModTable[iKilledClass]

+++ okay decompyling Modifier.pyc 
Sun Apr 04 15:51:45 2004
