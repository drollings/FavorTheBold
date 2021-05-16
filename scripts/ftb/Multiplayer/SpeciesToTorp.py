import App

# types for initializing torps create from C.
UNKNOWN = 0
DISRUPTOR = 1
PHOTON = 2
QUANTUM = 3
ANTIMATTER = 4
CARDTORP = 5
KLINGONTORP = 6
POSITRON = 7
PULSEDISRUPT = 8
FUSIONBOLT = 9
CARDASSIANDISRUPTOR = 10
KESSOKDISRUPTOR = 11
PHASEDPLASMA = 12
POSITRON2 = 13
PHOTON2 = 14
ROMULANCANNON = 15
ANTIMATTERBURST = 16
BFIGHTERDISRUPTOR = 17
BREENDAMPER = 18
BREENTORPEDO = 19
CARDPLASMABURST = 20
CARDTORPEDO = 21
CLASS1PULSEPHASER = 22
FASTKLINGONTORPEDO = 23
HEAVYPULSEPOLARON = 24
KLINGONFASTPLASMABURST = 25
KLINGONPLASMABURST = 26
KLINGONTORPEDO = 27
KLINGONTRIPLETORPEDO = 28
MICROCARDTORPEDO = 29
MICROPHOTONTORPEDO = 30
MICROPOLARONTORPEDO = 31
MK10DISRUPTOR = 32
MK12DISRUPTOR = 33
MK12PULSEDISRUPTOR = 34
MK18DISRUPTOR = 35
MK21DISRUPTOR = 36
MK5PHOTONTORPEDO = 37
MK5PHOTONTORPEDOB = 38
MK5PHOTONTORPEDOM = 39
MK5PHOTONTORPEDOS = 40
MK6PHOTONTORPEDO = 41
MK6PULSEDISRUPTOR = 42
PDPULSEPOLARON = 43
POLARONTORPEDO = 44
PULSEPHASER = 45
PULSEPOLARON = 46
QUANTUMTORPEDO = 47
ROMPLASMABURST = 48
ROMTORPEDO = 49
TRICOBALT = 50
VALDOREBLAST = 51
VALDOREHEAVYBLAST = 52
MK3PHOTONTORPEDO = 53
MK3PHOTONTORPEDOB = 54
MK3PHOTONTORPEDOM = 55
MK3PHOTONTORPEDOS = 56
MK4PHOTONTORPEDO = 57
MK4PHOTONTORPEDOB = 58
MK4PHOTONTORPEDOM = 59
MK4PHOTONTORPEDOS = 60
MAX_TORPS = 61

# Setup tuples
kSpeciesTuple = ((UNKNOWN, None),
	(DISRUPTOR, "Disruptor"),
	(PHOTON, "PhotonTorpedo"),
	(QUANTUM, "QuantumTorpedo"),
	(ANTIMATTER, "AntimatterTorpedo"),
	(CARDTORP, "CardassianTorpedo"),
	(KLINGONTORP, "KlingonTorpedo"),
	(POSITRON, "PositronTorpedo"),
	(PULSEDISRUPT, "PulseDisruptor"),
	(FUSIONBOLT, "FusionBolt"),
	(CARDASSIANDISRUPTOR, "CardassianDisruptor"),
	(KESSOKDISRUPTOR, "KessokDisruptor"),
	(PHASEDPLASMA, "PhasedPlasma"),
	(POSITRON2, "Positron2"),
	(PHOTON2, "PhotonTorpedo2"),
	(ROMULANCANNON, "RomulanCannon"),
	(ANTIMATTERBURST, 'Antimatter'),
	(BFIGHTERDISRUPTOR, 'BFighterDisruptor'),
	(BREENDAMPER, 'BreenDamper'),
	(BREENTORPEDO, 'BreenTorpedo'),
	(CARDPLASMABURST, 'CardPlasmaBurst'),
	(CARDTORPEDO, 'CardTorpedo'),
	(CLASS1PULSEPHASER, 'Class1PulsePhaser'),
	(FASTKLINGONTORPEDO, 'FastKlingonTorpedo'),
	(HEAVYPULSEPOLARON, 'HeavyPulsePolaron'),
	(KLINGONFASTPLASMABURST, 'KlingonFastPlasmaBurst'),
	(KLINGONPLASMABURST, 'KlingonPlasmaBurst'),
	(KLINGONTORPEDO, 'KlingonTorpedo'),
	(KLINGONTRIPLETORPEDO, 'KlingonTripleTorpedo'),
	(MICROCARDTORPEDO, 'MicroCardTorpedo'),
	(MICROPHOTONTORPEDO, 'MicroPhotonTorpedo'),
	(MICROPOLARONTORPEDO, 'MicroPolaronTorpedo'),
	(MK10DISRUPTOR, 'Mk10Disruptor'),
	(MK12DISRUPTOR, 'Mk12Disruptor'),
	(MK12PULSEDISRUPTOR, 'Mk12PulseDisruptor'),
	(MK18DISRUPTOR, 'Mk18Disruptor'),
	(MK21DISRUPTOR, 'Mk21Disruptor'),
	(MK5PHOTONTORPEDO, 'Mk5PhotonTorpedo'),
	(MK5PHOTONTORPEDOB, 'Mk5PhotonTorpedoB'),
	(MK5PHOTONTORPEDOM, 'Mk5PhotonTorpedoM'),
	(MK5PHOTONTORPEDOS, 'Mk5PhotonTorpedoS'),
	(MK6PHOTONTORPEDO, 'Mk6PhotonTorpedo'),
	(MK6PULSEDISRUPTOR, 'Mk6PulseDisruptor'),
	(PDPULSEPOLARON, 'PDPulsePolaron'),
	(POLARONTORPEDO, 'PolaronTorpedo'),
	(PULSEPHASER, 'PulsePhaser'),
	(PULSEPOLARON, 'PulsePolaron'),
	(QUANTUMTORPEDO, 'QuantumTorpedo'),
	(ROMPLASMABURST, 'RomPlasmaBurst'),
	(ROMTORPEDO, 'RomTorpedo'),
	(TRICOBALT, 'Tricobalt'),
	(VALDOREBLAST, 'ValdoreBlast'),
	(VALDOREHEAVYBLAST, 'ValdoreHeavyBlast'),
	(MK3PHOTONTORPEDO, 'Mk3PhotonTorpedo'),
	(MK3PHOTONTORPEDOM, 'Mk3PhotonTorpedoM'),
	(MK3PHOTONTORPEDOS, 'Mk3PhotonTorpedoS'),
	(MK4PHOTONTORPEDO, 'Mk4PhotonTorpedo'),
	(MK4PHOTONTORPEDOM, 'Mk4PhotonTorpedoM'),
	(MK4PHOTONTORPEDOS, 'Mk4PhotonTorpedoS'),
	(MAX_TORPS, None))

def CreateTorpedoFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [1]

	pTorp = App.Torpedo_Create (pcScript)
	return pTorp

def GetScriptFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [1]

def InitObject (self, iType):
	# Get the script
	pcScript = GetScriptFromSpecies (iType)
	if (pcScript == None):
		return 0

	mod = __import__("Tactical.Projectiles." + pcScript)
	mod.Create(self)

	self.UpdateNodeOnly ()

	return 1;	# This is Python, not C!

