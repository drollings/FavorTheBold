import App
import Registry


g_species = Registry.Registry()

# types for initializing objects create from C.
UNKNOWN = g_species.Register("Neutral", (None, 0, "Neutral", 0))
AKIRA = g_species.Register("Akira", ("Akira", App.SPECIES_AKIRA, "Federation", 1))
AMBASSADOR = g_species.Register("Ambassador", ("Ambassador", App.SPECIES_AMBASSADOR, "Federation", 1))
GALAXY = g_species.Register("Galaxy", ("Galaxy", App.SPECIES_GALAXY, "Federation", 1))
NEBULA = g_species.Register("Nebula", ("Nebula" , App.SPECIES_NEBULA, "Federation", 1))
SOVEREIGN = g_species.Register("Sovereign", ("Sovereign" , App.SPECIES_SOVEREIGN, "Federation", 1))
BIRDOFPREY = g_species.Register("BirdOfPrey", ("BirdOfPrey", App.SPECIES_BIRD_OF_PREY, "Klingon", 1))
VORCHA = g_species.Register("Vorcha", ("Vorcha" , App.SPECIES_VORCHA, "Klingon", 1))
WARBIRD = g_species.Register("Warbird", ("Warbird" , App.SPECIES_WARBIRD, "Romulan", 1))
MARAUDER = g_species.Register("Marauder", ("Marauder" , App.SPECIES_MARAUDER, "Ferengi", 1))
GALOR = g_species.Register("Galor", ("Galor" , App.SPECIES_GALOR, "Cardassian", 1))
KELDON = g_species.Register("Keldon", ("Keldon" , App.SPECIES_KELDON, "Cardassian", 1))

FTB_AKIRA = g_species.Register('FTB_Akira', ('FTB_Akira', App.SPECIES_AKIRA, 'Federation', 1))
FTB_AMBASSADOR = g_species.Register('FTB_Ambassador', ('FTB_Ambassador', App.SPECIES_AKIRA, 'Federation', 1))
FTB_BAKRUS = g_species.Register('FTB_Bakrus', ('FTB_Bakrus', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_BAJORANASSAULTCRAFT = g_species.Register('FTB_BajoranAssaultCraft', ('FTB_BajoranAssaultCraft', App.SPECIES_AKIRA, 'Bajoran', 1))
FTB_BREENFIGHTER = g_species.Register('FTB_BreenFighter', ('FTB_BreenFighter', App.SPECIES_AKIRA, 'Breen', 1))
FTB_BREENFRIGATE = g_species.Register('FTB_BreenFrigate', ('FTB_BreenFrigate', App.SPECIES_AKIRA, 'Breen', 1))
FTB_BREENMPWG = g_species.Register('FTB_BreenMPWG', ('FTB_BreenMPWG', App.SPECIES_AKIRA, 'Breen', 1))
FTB_BREL = g_species.Register('FTB_Brel', ('FTB_Brel', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_CERBERUS = g_species.Register('FTB_Cerberus', ('FTB_Cerberus', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_CHURCHILL = g_species.Register('FTB_Churchill', ('FTB_Churchill', App.SPECIES_AKIRA, 'Federation', 1))
FTB_CUDGEL = g_species.Register('FTB_Cudgel', ('FTB_Cudgel', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_CONSTITUTION = g_species.Register('FTB_Constitution', ('FTB_Constitution', App.SPECIES_AKIRA, 'Federation', 1))
FTB_CONSTITUTIONMK2 = g_species.Register('FTB_ConstitutionMk2', ('FTB_ConstitutionMk2', App.SPECIES_AKIRA, 'Federation', 1))
FTB_CONSTITUTIONTRN = g_species.Register('FTB_ConstitutionMk2', ('FTB_ConstitutionMk2', App.SPECIES_AKIRA, 'Federation', 1))
FTB_CONSTELLATION = g_species.Register('FTB_Constellation', ('FTB_Constellation', App.SPECIES_AKIRA, 'Federation', 1))
FTB_DANUBE = g_species.Register('FTB_Danube', ('FTB_Danube', App.SPECIES_AKIRA, 'Federation', 1))
FTB_DEFIANT = g_species.Register('FTB_Defiant', ('FTB_Defiant', App.SPECIES_AKIRA, 'Federation', 1))
FTB_DDERIDEX = g_species.Register('FTB_Dderidex', ('FTB_Dderidex', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_DEVASTATOR = g_species.Register('FTB_Devastator', ('FTB_Devastator', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_DOMINATOR = g_species.Register('FTB_Dominator', ('FTB_Dominator', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_DREADNAUGHT = g_species.Register('FTB_Dreadnaught', ('FTB_Dreadnaught', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_DDREADNAUGHT = g_species.Register('FTB_DDreadnaught', ('FTB_DDreadnaught', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_DVERIX = g_species.Register('FTB_Dverix', ('FTB_Dverix', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_ENSLAVER = g_species.Register('FTB_Enslaver', ('FTB_Enslaver', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_EXIMIUS = g_species.Register('FTB_Eximius', ('FTB_Eximius', App.SPECIES_AKIRA, 'Federation', 1))
FTB_EXCELSIOR = g_species.Register('FTB_Excelsior', ('FTB_Excelsior', App.SPECIES_AKIRA, 'Federation', 1))
FTB_EXCELSIORMK2 = g_species.Register('FTB_Excelsior_Mk2', ('FTB_Excelsior_Mk2', App.SPECIES_AKIRA, 'Federation', 1))
FTB_FERENGISHUTTLE = g_species.Register('FTB_FerengiShuttle', ('FTB_FerengiShuttle', App.SPECIES_AKIRA, 'Ferengi', 1))
FTB_GALAXY = g_species.Register('FTB_Galaxy', ('FTB_Galaxy', App.SPECIES_AKIRA, 'Federation', 1))
FTB_GALAXYMK2 = g_species.Register('FTB_Galaxy_Mk2', ('FTB_Galaxy_Mk2', App.SPECIES_AKIRA, 'Federation', 1))
FTB_GALAXY_SAUCER = g_species.Register('FTB_Galaxy_Saucer', ('FTB_Galaxy_Saucer', App.SPECIES_AKIRA, 'Federation', 1))
FTB_GALAXY_DRIVE = g_species.Register('FTB_Galaxy_Drive', ('FTB_Galaxy_Drive', App.SPECIES_AKIRA, 'Federation', 1))
FTB_GALOR = g_species.Register('FTB_Galor', ('FTB_Galor', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_GROUMAL = g_species.Register('FTB_Groumal', ('FTB_Groumal', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_HIDEKI = g_species.Register('FTB_Hideki', ('FTB_Hideki', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_HIROGEN = g_species.Register('FTB_Hirogen', ('FTB_Hirogen', App.SPECIES_AKIRA, 'Hirogen', 1))
FTB_HORDA = g_species.Register('FTB_Horda', ('FTB_Horda', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_INSIDIOUS = g_species.Register('FTB_Insidious', ('FTB_Insidious', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_INTREPID = g_species.Register('FTB_Intrepid', ('FTB_Intrepid', App.SPECIES_AKIRA, 'Federation', 1))
FTB_KAREMMAN = g_species.Register('FTB_Karemman', ('FTB_Karemman', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_KELDON = g_species.Register('FTB_Keldon', ('FTB_Keldon', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_KIMAL = g_species.Register('FTB_Kimal', ('FTB_Kimal', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_KTINGA = g_species.Register('FTB_Ktinga', ('FTB_Ktinga', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_KVORT = g_species.Register('FTB_Kvort', ('FTB_Kvort', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_LAKOTA = g_species.Register('FTB_Lakota', ('FTB_Lakota', App.SPECIES_AKIRA, 'Federation', 1))
FTB_LEVIATHAN = g_species.Register('FTB_Leviathan', ('FTB_Leviathan', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_MEDITERRANEAN = g_species.Register('FTB_Mediterranean', ('FTB_Mediterranean', App.SPECIES_AKIRA, 'Federation', 1))
FTB_MIRANDA = g_species.Register('FTB_Miranda', ('FTB_Miranda', App.SPECIES_AKIRA, 'Federation', 1))
FTB_MIRADORN = g_species.Register('FTB_Miradorn', ('FTB_Miradorn', App.SPECIES_AKIRA, 'Miradorn', 1))
FTB_NEBULA = g_species.Register('FTB_Nebula', ('FTB_Nebula', App.SPECIES_AKIRA, 'Federation', 1))
FTB_NEGHVAR = g_species.Register('FTB_Neghvar', ('FTB_Neghvar', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_NEWORLEANS = g_species.Register('FTB_NewOrleans', ('FTB_NewOrleans', App.SPECIES_AKIRA, 'Federation', 1))
FTB_NOREXAN = g_species.Register('FTB_Norexan', ('FTB_Norexan', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_NORWAY = g_species.Register('FTB_Norway', ('FTB_Norway', App.SPECIES_AKIRA, 'Federation', 1))
FTB_NOVA = g_species.Register('FTB_Nova', ('FTB_Nova', App.SPECIES_AKIRA, 'Federation', 1))
FTB_OBERTH = g_species.Register('FTB_Oberth', ('FTB_Oberth', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PACKRAT = g_species.Register('FTB_Packrat', ('FTB_Packrat', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PEREGRINE = g_species.Register('FTB_Peregrine', ('FTB_Peregrine', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PROSPECTOR = g_species.Register('FTB_Prospector', ('FTB_Prospector', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PROMETHEUS = g_species.Register('FTB_Prometheus', ('FTB_Prometheus', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PROMETHEUS_A = g_species.Register('FTB_Prometheus_A', ('FTB_Prometheus_A', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PROMETHEUS_B = g_species.Register('FTB_Prometheus_B', ('FTB_Prometheus_B', App.SPECIES_AKIRA, 'Federation', 1))
FTB_PROMETHEUS_C = g_species.Register('FTB_Prometheus_C', ('FTB_Prometheus_C', App.SPECIES_AKIRA, 'Federation', 1))
FTB_RAIDER = g_species.Register('FTB_Raider', ('FTB_Raider', App.SPECIES_AKIRA, 'Federation', 1))
FTB_RRDEREX = g_species.Register('FTB_RRDerex', ('FTB_RRDerex', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_SABER = g_species.Register('FTB_Saber', ('FTB_Saber', App.SPECIES_AKIRA, 'Federation', 1))
FTB_SCIMITAR = g_species.Register('FTB_Scimitar', ('FTB_Scimitar', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_SDS = g_species.Register('FTB_SDS', ('FTB_SDS', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_SHELLEY = g_species.Register('FTB_Shelley', ('FTB_Shelley', App.SPECIES_AKIRA, 'Federation', 1))
FTB_SOVEREIGN = g_species.Register('FTB_Sovereign', ('FTB_Sovereign', App.SPECIES_AKIRA, 'Federation', 1))
FTB_SOVEREIGNMK2 = g_species.Register('FTB_SovereignMk2', ('FTB_SovereignMk2', App.SPECIES_AKIRA, 'Federation', 1))
FTB_SOYUZ = g_species.Register('FTB_Soyuz', ('FTB_Soyuz', App.SPECIES_AKIRA, 'Federation', 1))
FTB_STEAMRUNNER = g_species.Register('FTB_Steamrunner', ('FTB_Steamrunner', App.SPECIES_AKIRA, 'Federation', 1))
FTB_STINGER = g_species.Register('FTB_Stinger', ('FTB_Stinger', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_HORDA = g_species.Register('FTB_Horda', ('FTB_Horda', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_TOSD7 = g_species.Register('FTB_TOSD7', ('FTB_TOSD7', App.SPECIES_AKIRA, 'Klingon', 1))
FTB_TPRIEX = g_species.Register('FTB_TPriex', ('FTB_TPriex', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_TPRIEXDRONE = g_species.Register('FTB_TPriexDrone', ('FTB_TPriexDrone', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_TAMARIAN = g_species.Register('FTB_Tamarian', ('FTB_Tamarian', App.SPECIES_AKIRA, 'Tamarian', 1))
FTB_TRAMMION = g_species.Register('FTB_Trammion', ('FTB_Trammion', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_TYPE9 = g_species.Register('FTB_Type9', ('FTB_Type9', App.SPECIES_AKIRA, 'Federation', 1))
FTB_VAKOR = g_species.Register('FTB_Vakor', ('FTB_Vakor', App.SPECIES_AKIRA, 'Cardassian', 1))
FTB_VALDORE = g_species.Register('FTB_Valdore', ('FTB_Valdore', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_VIRULENT = g_species.Register('FTB_Virulent', ('FTB_Virulent', App.SPECIES_AKIRA, 'Dominion', 1))
FTB_VORCHA = g_species.Register('FTB_Vorcha', ('FTB_Vorcha', App.SPECIES_AKIRA, 'Klingon', 1))

FTB_NEPTUNE = g_species.Register('FTB_Neptune', ('FTB_Neptune', App.SPECIES_AKIRA, 'Human', 1))
FTB_NX01 = g_species.Register('FTB_NX01', ('FTB_NX01', App.SPECIES_AKIRA, 'Human', 1))
FTB_ENTDRAGON = g_species.Register('FTB_ENTDRAGON', ('FTB_ENTDRAGON', App.SPECIES_AKIRA, 'Romulan', 1))
FTB_D5 = g_species.Register('FTB_D5', ('FTB_D5', App.SPECIES_AKIRA, 'Klingon', 1))

FTB_DKYR = g_species.Register('FTB_DKYR', ('FTB_DKYR', App.SPECIES_AKIRA, 'Vulcan', 1))
FTB_SHRAN = g_species.Register('FTB_SHRAN', ('FTB_SHRAN', App.SPECIES_AKIRA, 'Vulcan', 1))
FTB_SURAK = g_species.Register('FTB_SURAK', ('FTB_SURAK', App.SPECIES_AKIRA, 'Vulcan', 1))
FTB_VAHKIAS = g_species.Register('FTB_VAHKIAS', ('FTB_VAHKIAS', App.SPECIES_AKIRA, 'Vulcan', 1))

MAX_FLYABLE_SHIPS = FTB_NX01 + 1

CARDHYBRID = g_species.Register("CardHybrid", ("CardHybrid", App.SPECIES_CARDHYBRID, "Cardassian", 1))
KESSOKHEAVY = g_species.Register("KessokHeavy", ("KessokHeavy" , App.SPECIES_KESSOK_HEAVY, "Kessok", 1))
KESSOKLIGHT = g_species.Register("KessokLight", ("KessokLight" , App.SPECIES_KESSOK_LIGHT, "Kessok", 1))
SHUTTLE = g_species.Register("Shuttle", ("Shuttle" , App.SPECIES_SHUTTLE, "Federation", 1))
CARDFREIGHTER = g_species.Register("CardFreighter", ("CardFreighter", "Cardassian Freighter" , App.SPECIES_CARDFREIGHTER, "Cardassian", 1))
FREIGHTER = g_species.Register("Freighter", ("Freighter" , App.SPECIES_FREIGHTER, "Federation", 1))
TRANSPORT = g_species.Register("Transport", ("Transport" , App.SPECIES_TRANSPORT, "Federation", 1))
SPACEFACILITY = g_species.Register("SpaceFacility", ("SpaceFacility" , App.SPECIES_SPACE_FACILITY, "Federation", 1))
COMMARRAY = g_species.Register("CommArray", ("CommArray" , App.SPECIES_COMMARRAY, "Federation", 1))
COMMLIGHT = g_species.Register("CommLight", ("CommLight", App.SPECIES_COMMLIGHT, "Cardassian", 1))
DRYDOCK = g_species.Register("DryDock", ("DryDock" , App.SPECIES_DRYDOCK, "Federation", 1))
PROBE = g_species.Register("Probe", ("Probe" , App.SPECIES_PROBE, "Federation", 1))
DECOY = g_species.Register("Decoy", ("Decoy" , App.SPECIES_PROBETYPE2, "Federation", 1))
SUNBUSTER = g_species.Register("Sunbuster", ("Sunbuster" , App.SPECIES_SUNBUSTER, "Kessok", 1))
CARDOUTPOST = g_species.Register("CardOutpost", ("CardOutpost" , App.SPECIES_CARD_OUTPOST, "Cardassian", 1))
CARDSTARBASE = g_species.Register("CardStarbase", ("CardStarbase" , App.SPECIES_CARD_STARBASE, "Cardassian", 1))
CARDSTATION = g_species.Register("CardStation", ("CardStation" , App.SPECIES_CARD_STATION, "Cardassian", 1))
FEDOUTPOST = g_species.Register("FedOutpost", ("FedOutpost" , App.SPECIES_FED_OUTPOST, "Federation", 1))
FEDSTARBASE = g_species.Register("FedStarbase", ("FedStarbase" , App.SPECIES_FED_STARBASE, "Federation", 1))
ASTEROID = g_species.Register("Asteroid", ("Asteroid" , App.SPECIES_ASTEROID, "Neutral", 1))
ASTEROID1 = g_species.Register("Asteroid1", ("Asteroid1" , App.SPECIES_ASTEROID, "Neutral", 1))
ASTEROID2 = g_species.Register("Asteroid2", ("Asteroid2" , App.SPECIES_ASTEROID, "Neutral", 1))
ASTEROID3 = g_species.Register("Asteroid3", ("Asteroid3" , App.SPECIES_ASTEROID, "Neutral", 1))
AMAGON = g_species.Register("Amagon", ("Amagon", App.SPECIES_ASTEROID, "Cardassian", 1))
BIRANUSTATION = g_species.Register("BiranuStation", ("BiranuStation", App.SPECIES_SPACE_FACILITY, "Neutral", 1))
ENTERPRISE = g_species.Register("Enterprise", ("Enterprise", App.SPECIES_SOVEREIGN, "Federation", 1))
GERONIMO = g_species.Register("Geronimo", ("Geronimo", App.SPECIES_AKIRA, "Federation", 1))
PEREGRINE = g_species.Register("Peregrine", ("Peregrine", App.SPECIES_NEBULA, "Federation", 1))
ASTEROIDH1 = g_species.Register("Asteroidh1", ("Asteroidh1" , App.SPECIES_ASTEROID, "Neutral", 1))
ASTEROIDH2 = g_species.Register("Asteroidh2", ("Asteroidh2" , App.SPECIES_ASTEROID, "Neutral", 1))
ASTEROIDH3 = g_species.Register("Asteroidh3", ("Asteroidh3" , App.SPECIES_ASTEROID, "Neutral", 1))
ESCAPEPOD = g_species.Register("Escapepod", ("Escapepod" , App.SPECIES_ESCAPEPOD, "Neutral", 1))
KESSOKMINE = g_species.Register("KessokMine", ("KessokMine" , App.SPECIES_KESSOKMINE, "Kessok", 1))
BORGCUBE = g_species.Register("BorgCube", ("BorgCube", App.SPECIES_BORG,  "Borg", 1))
MAX_SHIPS = BORGCUBE + 1


def GetShipFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_SHIPS):
#		print ("Species out of range")
		return None

	pSpecTuple = g_species._arrayList[iSpecies]
	pcScript = pSpecTuple [0]

	ShipScript = __import__("ftb.ships." + pcScript)
	ShipScript.LoadModel ()
	return ShipScript.GetShipStats ()

def GetScriptFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_SHIPS):
		return None

	pSpecTuple = g_species._arrayList[iSpecies]
	return pSpecTuple [0]


# This function is called from code to fill in the spec of
# an object that has been serialized over the net.
def InitObject (self, iType):
	kStats = GetShipFromSpecies (iType)
	if (kStats == None):
		# Failed.  Unknown type. Bail.
		return 0

	# Now that we have the stats, initialize the objects.
	# Initialize the ship's model.
	self.SetupModel (kStats['Name'])

	# Load hardpoints.
	pPropertySet = self.GetPropertySet()
	mod = __import__("ftb.ships.hp." + kStats['HardpointFile'])

	App.g_kModelPropertyManager.ClearLocalTemplates ()
	reload (mod)

	mod.LoadPropertySet(pPropertySet)

	self.SetupProperties()

	self.UpdateNodeOnly()

	return 1

def CreateShip (iType):
	# Get ship stats
	kStats = GetShipFromSpecies (iType)

	if (kStats == None):
		# Failed.  Unknown type. Bail.
		return None

#	print ("Creating " + kStats['Name'] + "\n")
	pShip = App.ShipClass_Create (kStats['Name'])

	sModule = "ftb.ships." + kSpeciesTuple [iType][0]
#	print ("*** Setting script module " + sModule)
	pShip.SetScript(sModule)

	# Load hardpoints.
	pPropertySet = pShip.GetPropertySet()
	mod = __import__("ftb.ships.hp." + kStats['HardpointFile'])

	App.g_kModelPropertyManager.ClearLocalTemplates ()
	reload(mod)

	mod.LoadPropertySet(pPropertySet)

	pShip.SetupProperties()

	pShip.UpdateNodeOnly()

	pShip.SetNetType (iType)

	return pShip

def GetIconNum (iSpecies):
	pSpecTuple = g_species._arrayList[iSpecies]
	iNum = pSpecTuple [1]

	return iNum

def GetSideFromSpecies (iSpecies):
	pSpecTuple = g_species._arrayList[iSpecies]
	pcSide = pSpecTuple [2]

	return pcSide

def GetClassFromSpecies (iSpecies):
	pSpecTuple = g_species._arrayList[iSpecies]
	iClass = pSpecTuple [3]

	return iClass