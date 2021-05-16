import App
from ATP_Object import *

sAnimPath     = 'Custom.AdvancedTechnologies.Data.Universe.ATP_Animations.'
sDatabasePath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Databases/ATP_MainDatabase.tgl'

sATPHeadPath = 'scripts/Custom/AdvancedTechnologies/Data/Universe/Gfx/Characters/Heads/'

				
class Character(UniverseElement):
	pDatabase = None

	dAnimationModes = { 	'Speak'	:		App.CharacterAction.AT_SPEAK_LINE,		
				'Talk' :		App.CharacterAction.AT_SAY_LINE,
				'TalkAfterTurn' :	App.CharacterAction.AT_SAY_LINE_AFTER_TURN 	}

	def __init__(self,ID=0):
		## Upper class
		UniverseElement.__init__(self,ID)

		## Own attr
		self.sHeadType = ''
		self.sBodyType = ''
		self.sLoc = ''
		self.bStanding = FALSE
		self.dAnimations = {}
		self.dLines = {}
		self.pSequence = None		

	def Bind(self,pBridge,sName,sHeadType,sBodyType,sLoc):
		## Move
		self.Move(pBridge)

		## How to construct the character		
		self.sHeadType = sHeadType[:]
		self.sBodyType = sBodyType[:]
		self.sLoc = sLoc[:]

		## Fixed name ?
		if not sName:
			sName = self.GetRace().GetCharacterName()
		self.sName = sName[:]

	def Render(self,pSet):
		#debug('begin rendering character '+self.sName)
		
		if not self.Node:					
			
			## Gfx files
			pHeadType = dHeads[self.sHeadType]
			pBodyType = dBodies[self.sBodyType]		
			sBaseHeadTexture = pHeadType.GetBaseHeadTexture()
			sHeadNif = pHeadType.GetHeadNif()
			sBodyTexture = pBodyType.GetBodyTexture()
			sBodyNif = pBodyType.GetBodyNif()
			iSize = pBodyType.GetSize()
			
			## Correct gender ?
			iGender = pHeadType.GetGender()
			iGenderBis = pBodyType.GetGender()
			assert iGender == iGenderBis			

			#debug('LoadMOdel character '+self.sName)
			#debug(' sBodyNif:'+sBodyNif)
			#debug(' sHeadNif:'+sHeadNif)

			## Preload
			App.g_kModelManager.LoadModel(sBodyNif, 'Bip01')
			App.g_kModelManager.LoadModel(sHeadNif, None)
			
			#debug('Create character '+self.sName)

			## Create the character
			Node = App.CharacterClass_Create(sBodyNif,sHeadNif)

			## Save it
			self.Node = Node
	
			#debug('Texture character '+self.sName)
			#debug(' sBodyTexture: '+sBodyTexture)
			#debug(' sBaseHeadTexture: '+sBaseHeadTexture +'_head.tga')

			## Textures
			Node.ReplaceBodyAndHead(sBodyTexture , sBaseHeadTexture +'_head.tga')

			#debug('Adding to set character '+self.sName)

			## Add the character to the set
			pSet.AddObjectToSet(Node,self.sName)
			pLight = pSet.GetLight('ambientlight1')
			pLight.AddIlluminatedObject(Node)
	
			#debug('Set params character '+self.sName)

			## Setup the character configuration
			Node.SetSize(iSize)
			Node.SetGender(iGender)
			Node.SetStanding(self.bStanding)
			Node.SetRandomAnimationChance(0.2)
			Node.SetBlinkChance(0.2)
			Node.SetCharacterName(self.sName)

			#debug('Add anim character '+self.sName)

			## Animations
			self.AddAnimation('TurnStation', 'Bridge.Characters.CommonAnimations.GlanceLeft')
			self.AddAnimation('BackStation', 'Bridge.Characters.CommonAnimations.Standing')

			#debug('Complex character '+self.sName)
			if pHeadType.IsComplex():
				## Blinking
				Node.AddFacialImage('Blink0', sBaseHeadTexture + '_head_blink1.tga')
				Node.AddFacialImage('Blink1', sBaseHeadTexture + '_head_blink2.tga')
				Node.AddFacialImage('Blink2', sBaseHeadTexture + '_head_eyesclosed.tga')
				Node.SetBlinkStages(3)

				## Mouth
				Node.AddFacialImage('SpeakA', sBaseHeadTexture + '_head_a.tga')
				Node.AddFacialImage('SpeakE', sBaseHeadTexture + '_head_e.tga')
				Node.AddFacialImage('SpeakU', sBaseHeadTexture + '_head_u.tga')
				Node.SetAnimatedSpeaking(1)

			## Configure for the Generic bridge
			Node.ClearAnimations()
			#Node.SetDatabase('')

			#debug('Set loc '+self.sName)

			## Some random animations
			self.AddRandomAnimation( sAnimPath +'Breathe')
			# self.AddRandomAnimation('Bridge.Characters.CommonAnimations.Blast')

			## Where to place it
			sShortLoc = str(self.ID) + '_' + 'STANDING'
			Node.SetLocation(sShortLoc)

			#debug('Effec loc character '+self.sName)
			#debug(' loc: '+self.sLoc)

			## Effectively put it
			pSequence = App.TGSequence_Create()
			App.g_kAnimationManager.LoadAnimation(self.sLoc,sShortLoc)
			pSequence.AddAction(App.TGAnimPosition_Create(Node.GetAnimNode(),sShortLoc))
			pSequence.Play()

			

		#debug('end rendering character '+self.sName)

	def Unrender(self):
		#debug('begin unrendering character '+self.sName)
		
		## Unload animations
		kAM = App.g_kAnimationManager
		for key in self.dAnimations.keys():
			kAM.FreeAnimation(key)
		self.dAnimations = {}

		## Baseclass
		UniverseElement.Unrender(self)

		#debug('end unrendering character '+self.sName)

	def AddRandomAnimation(self,sPath):
		self.Node.AddRandomAnimation(sPath)
		
	def AddAnimation(self,sName,sPath):
		sShort = str(self.ID) + '_' + sName
		self.Node.AddAnimation(sShort,sPath)		

	def AddSingleAnimation(self,sName,sPath):
		sShort = str(self.ID) + '_' + sName
		App.g_kAnimationManager.LoadAnimation(sPath,sShort)
		self.dAnimations[sShort] = None


	## Commands
	################################
	def SpeakAction(self,sTextRef,sMode = 'Speak',bTurnback = TRUE):
		## Talk action
		if dLines.has_key(sTextRef):
			pAction = App.CharacterAction_Create(self.Node, Character.dAnimationModes[sMode] , sTextRef , 'Captain' , bTurnback , Character.pDatabase)
		else:
			pAction = App.CharacterAction_Create(self.Node, Character.dAnimationModes[sMode] , sTextRef , 'Captain' , bTurnback )
		return pAction	

	def Speak(self,sTextRef,sMode = 'Speak',bTurnback = TRUE):
		if self.pSequence:
			return ## busy
		self.pSequence = App.TGSequence_Create()

		## Speak action
		self.pSequence.AppendAction( self.SpeakAction(sTextRef,sMode,bTurnback) )

		## Unload action
		self.pSequence.AppendAction( self.UnloadAction() )		

		## Play
		self.pSequence.Play()

	def SayYesAction(self):
		sEffCharName = g_dNameToCharacterName[self.sName]
		sTextRef = sEffCharName + 'Yes' + str(self.GetRandomInt(1,5))
		return self.SpeakAction(sTextRef)
	
	def SayYes(self):
		sEffCharName = g_dNameToCharacterName[self.sName]
		sTextRef = sEffCharName + 'Yes' + str(self.GetRandomInt(1,5))
		self.Speak(sTextRef)

	## Unload
	###############################"
	def UnloadAction(self):
		pAction = App.TGScriptAction_Create(__name__,'Unload', self.ID)
		return pAction

	def Unload(self):
		if self.pSequence:
			self.pSequence.Destroy()
		self.pSequence = None


g_dNameToCharacterName = { 	'Helm' : 	'Kiska',
				'Commander' :	'Saffi',
				'Engineer' : 	'Brex',
				'Tactical' : 	'Felix',
				'Science' : 	'Miguel'
			 }

def Unload(pAction,ID):
	pCharacter = GetByID(ID)
	if pCharacter:
		pCharacter.Unload()
	return 0


def SynchroniseWithGame():
	## Get the playerbridge
	pBridge = GetPlayerBridge()

	## Create the characters
	### Helm		
	pCharacter = Character()
	pCharacter.Bind(pBridge,'Helm','','','')
	pCharacter.Node = App.CharacterClass_GetObject(pBridge.Node,'Helm')

	### Commander		
	pCharacter = Character()
	pCharacter.Bind(pBridge,'Commander','','','')
	pCharacter.Node = App.CharacterClass_GetObject(pBridge.Node,'XO')

	### Security		
	pCharacter = Character()
	pCharacter.Bind(pBridge,'Tactical','','','')
	pCharacter.Node = App.CharacterClass_GetObject(pBridge.Node,'Tactical')

	### Engineer	
	pCharacter = Character()
	pCharacter.Bind(pBridge,'Engineer','','','')
	pCharacter.Node = App.CharacterClass_GetObject(pBridge.Node,'Engineer')

	### Science		
	pCharacter = Character()
	pCharacter.Bind(pBridge,'Science','','','')
	pCharacter.Node = App.CharacterClass_GetObject(pBridge.Node,'Science')

	## Update the database
	pGame = GetGame().Node
	Character.pDatabase = App.g_kLocalizationManager.Load(sDatabasePath)
	
	## Loop through all voice lines that we want to preload, and load them.
	for sLine in dLines.keys():
		pGame.LoadDatabaseSoundInGroup(Character.pDatabase, sLine, 'BridgeGeneric')


dLines = {	'TargetImpulseDisabled':0,
		'SelfLifeSupportDisabled':0,
		'SelfWarpDisabled':0,
		'SelfSensorsDisabled':0,
		'SelfTorpedoesDisabled':0,
		'SelfShieldsOnline':0,
		'SelfTractorDisabled':0,
		'TargetWarpDisabled':0,
		'TargetTractorDisabled':0,
		'SelfWarpOnline':0,
		'TargetPhasersDisabled':0,
		'SelfPowerDisabled':0,
		'SelfLifeSupportOnline':0,
		'TargetSensorsDisabled':0,
		'SelfSensorsOnline':0,
		'SelfPhasersDisabled':0,
		'SelfTractorsFire':0,
		'SelfImpulseOnline':0,	
		'SelfImpulseDisabled':0,
		'SelfShieldsDisabled':0,
		'TargetTorpedoesDisabled':0,
		'TargetShieldsDisabled':0,
		'TargetPowerDisabled':0,
		'SelfTractorsStop':0,
		'Dock_Init':0,
		'Dock_ACK':0,
		'CaptainOnTheBridge':0		}


class HeadType:
	sGenderToiGender = { 	'M' :  App.CharacterClass.MALE,
				'F':  App.CharacterClass.FEMALE 	}

	def __init__(self,sFolder,sHeadNif,sHeadTexture,sGender,bComplex):
		## Attrs
		self.bComplex = bComplex
		self.sFolder = sFolder
		self.sHeadNif = sHeadNif
		self.sHeadTexture = sHeadTexture
		self.iGender =  HeadType.sGenderToiGender[sGender]

	def IsComplex(self):
		return self.bComplex

	def GetHeadNif(self):
		return self.sFolder + '/' + self.sHeadNif

	def GetBaseHeadTexture(self):
		return self.sFolder + '/' + self.sHeadTexture

	def GetGender(self):
		return self.iGender


dHeads = {	'Andorian' :	HeadType(	'data/Models/Characters/Heads/HeadAndorian', ## **** Red
					  	'andorian_head.nif',
					 	'verata',
						'M',
						TRUE
					 ) ,

		'Boolean' :	HeadType(	'data/Models/Characters/Heads/HeadBrex', ## Yellow
					  	'brex_head.nif',
					 	'brex',
						'M',
						TRUE
					 ) ,

		'Tpol' :	HeadType(	sATPHeadPath + 'Tpol',
					  	'Tpol_head.nif',
					 	'Tpol',
						'F',
						TRUE
					 ) ,

		'Cardassian1' : HeadType(	'data/Models/Characters/Heads/HeadCard',
					  	'cardassian_head.nif',
					 	'card_capt',
						'M',
						TRUE
					 ) ,

		'Cardassian2' : HeadType(	'data/Models/Characters/Heads/HeadCard',
					  	'cardassian_head.nif',
					 	'card_prison_cmdr',
						'M',
						FALSE
					 ) ,

		'Cardassian3' : HeadType(	'data/Models/Characters/Heads/HeadCard',
					  	'cardassian_head.nif',
					 	'havar',
						'M',
						TRUE
					 ) ,

		'Cardassian4' : HeadType(	'data/Models/Characters/Heads/HeadCard',
					  	'cardassian_head.nif',
					 	'matan',
						'M',
						TRUE
					 ) ,

		'Cardassian5' : HeadType(	'data/Models/Characters/Heads/HeadCard',
					  	'cardassian_head.nif',
					 	'sek',
						'M',
						TRUE
					 ) ,

		'Human1' : 	HeadType(	'data/Models/Characters/Heads/HeadData',	##**** Red
					  	'data_head.nif',
					 	'soto',
						'M',
						TRUE
					 ) ,

		'Human2' :	 HeadType(	'data/Models/Characters/Heads/HeadData',	##**** Red
					  	'data_head.nif',
					 	'yi',
						'M',
						TRUE
					 ) ,

		'Human3' :	 HeadType(	'data/Models/Characters/Heads/HeadData',	##* Yellow
					  	'data_head.nif',
					 	'male_ensignC',
						'M',
						FALSE
					 ) ,

		'Human4' :	 HeadType(	'data/Models/Characters/Heads/HeadData',	##* Red
					  	'data_head.nif',
					 	'male_ensignD',
						'M',
						FALSE
					 ) ,

		'Felix' :	 HeadType(	'data/Models/Characters/Heads/HeadFelix',	##** Yellow
					  	'Felix_head.nif',
					 	'felix',
						'M',
						TRUE
					 ) ,
		
		'Human5' :	 HeadType(	'data/Models/Characters/Heads/HeadPicard',##*** YEllow
					  	'Picard_head.nif',
					 	'willis',
						'M',
						TRUE
					 ) ,

		'Human6' :	 HeadType(	'data/Models/Characters/Heads/HeadFem3',	##**** Red
					  	'fem3_head.nif',
					 	'haley',
						'F',
						TRUE
					 ) ,

		'Human7' :	 HeadType(	'data/Models/Characters/Heads/HeadFem3',	##**** Red
					  	'fem3_head.nif',
					 	'zeiss',
						'F',
						TRUE
					 ) ,

		'Human8' :	 HeadType(	'data/Models/Characters/Heads/HeadFem3',	##* Yellow
					  	'fem3_head.nif',
					 	'female_ensignB',
						'F',
						FALSE
					 ) ,

		'Human24' :	 HeadType(	'data/Models/Characters/Heads/HeadFem4',	##* Yellow
					  	'fem4_head.nif',
					 	'female_ensignC',
						'F',
						FALSE
					 ) ,

		'Human9' :	 HeadType(	'data/Models/Characters/Heads/HeadFem4',	##* Red
					  	'fem4_head.nif',
					 	'female_ensignD',
						'F',
						FALSE
					 ) ,

		
		'Human10' :	 HeadType(	'data/Models/Characters/Heads/HeadLiu',	##***** Red
					  	'liu_head.nif',
					 	'liu',
						'F',
						TRUE
					 ) ,

		'Human11' :	 HeadType(	'data/Models/Characters/Heads/HeadLiu',	##* Yellow
					  	'liu_head.nif',
					 	'female_ensignA',
						'F',
						FALSE
					 ) ,

		'Human12' :	 HeadType(	'data/Models/Characters/Heads/HeadLiu',	##**** Red
					  	'liu_head.nif',
					 	'liu',
						'F',
						FALSE
					 ) ,

		'Human13' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'dawson',
						'M',
						TRUE
					 ) ,

		'Human14' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##*** Red
					  	'miguel_head.nif',
					 	'graff',
						'M',
						TRUE
					 ) ,
		
		'Human15' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'jadeja',
						'M',
						TRUE
					 ) ,

		'Human16' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##* Yellow
					  	'miguel_head.nif',
					 	'male_ensignB',
						'M',
						FALSE
					 ) ,

		'Human17' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'male_ensignE',
						'M',
						FALSE
					 ) ,

		'Human18' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'male_ensignF',
						'M',
						FALSE
					 ) ,

		'Human19' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'martin',
						'M',
						TRUE
					 ) ,

		'Human20' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**** Red
					  	'miguel_head.nif',
					 	'mccray',
						'M',
						TRUE
					 ) ,

		'Human21' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##CIV Red
					  	'miguel_head.nif',
					 	'soams',
						'M',
						TRUE
					 ) ,

		'Human22' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##CIV Red
					  	'miguel_head.nif',
					 	'takahara',
						'M',
						TRUE
					 ) ,

		
		'Human23' :	 HeadType(	'data/Models/Characters/Heads/HeadPicard',##* YEllow
					  	'Picard_head.nif',
					 	'male_ensignA',
						'M',
						FALSE
					 ) ,

		'Miguel' :	 HeadType(	'data/Models/Characters/Heads/HeadMiguel',##**. Blue
					  	'miguel_head.nif',
					 	'miguel',
						'M',
						TRUE
					 ) ,

		
		'Picard' :	 HeadType(	'data/Models/Characters/Heads/HeadPicard',##**** Red
					  	'Picard_head.nif',
					 	'picard',
						'M',
						TRUE
					 ) ,	

		'Romulan1' :	 HeadType(	'data/Models/Characters/Heads/HeadFemRomulan',
					  	'femromulan_head.nif',
					 	'vlin',
						'F',
						TRUE
					 ) ,

		'Romulan2' :	 HeadType(	'data/Models/Characters/Heads/HeadRomulan',
					  	'romulan_head.nif',
					 	'barel',
						'M',
						TRUE
					 ) ,

		'Romulan3' :	 HeadType(	'data/Models/Characters/Heads/HeadRomulan',
					  	'romulan_head.nif',
					 	'saalek',
						'M',
						TRUE
					 ) ,

		'Romulan4' :	 HeadType(	'data/Models/Characters/Heads/HeadRomulan',
					  	'romulan_head.nif',
					 	'terik',
						'M',
						TRUE
					 ) ,

		'Romulan5' :	 HeadType(	sATPHeadPath + 'RomulanFemale',
					  	'femromulan_head.nif',
					 	'romfem1',
						'F',
						FALSE
					 ) ,

		'Ferengi' :	 HeadType(	'data/Models/Characters/Heads/HeadFerengi',
					  	'ferengi_head.nif',
					 	'praag',
						'M',
						TRUE
					 ) ,

		'Kessok' :	 HeadType(	'data/Models/Characters/Heads/HeadKessok',
					  	'kessok_head.nif',
					 	'kessok',
						'M',
						FALSE
					 ) ,

		'Kiska' :	 HeadType(	'data/Models/Characters/Heads/HeadKiska',
					  	'kiska_head.nif',
					 	'kiska',
						'F',
						TRUE
					 ) ,

		'Saffi' :	 HeadType(	'data/Models/Characters/Heads/HeadSaffi',
					  	'saffi_head.nif',
					 	'saffi',
						'F',
						TRUE
					 ) ,

		'Klingon1' :	 HeadType(	'data/Models/Characters/Heads/HeadKlingon',
					  	'klingon_head.nif',
					 	'kartok',
						'M',
						TRUE
					 ) ,

		
		'Klingon2' :	 HeadType(	'data/Models/Characters/Heads/HeadKlingon',
					  	'klingon_head.nif',
					 	'korbus',
						'M',
						TRUE
					 )

	}



class BodyType:
	sGenderToiGender = { 	'M' :  App.CharacterClass.MALE,
				'F':  App.CharacterClass.FEMALE 	}
	sSizeToiSize	 = {	'small'  : App.CharacterClass.SMALL,
				'medium' : App.CharacterClass.MEDIUM,
				'large'  : App.CharacterClass.LARGE	}

	def __init__(self,sBodyNif,sBodyTexture,sSize,sGender):
			
		## Attrs
		self.sBodyNif = sBodyNif
		self.sBodyTexture = sBodyTexture
		self.iSize = BodyType.sSizeToiSize[sSize]
		self.iGender = BodyType.sGenderToiGender[sGender]

	def GetBodyTexture(self):
		return self.sBodyTexture[:]

	def GetBodyNif(self):
		return self.sBodyNif[:]

	def GetGender(self):
		return self.iGender

	def GetSize(self):
		return self.iSize


dBodies = {	'Cardassian' : 		BodyType(	'data/Models/Characters/Bodies/BodyCardassian/BodyCardassian.nif',
							'data/Models/Characters/Bodies/BodyCardassian/Cardassian_body.tga',
							'medium',
							'M'
						),

		'HumanScienceFemale' : 	BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyFemS/FedFemTeal_body.tga',
							'small',
							'F'
						),

		'StarfleetOfficerFemale' : BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyFemS/FedFemRed_body.tga',
							'small',
							'F'
						),

		'StarfleetScienceFemale' : BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyFemS/FedFemTeal_body.tga',
							'medium',
							'F'
						),

		'StarfleetTacticalFemale' : BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyFemS/FedFemGold_body.tga',
							'small',
							'F'
						),

		'StarfleetAdmiralFemale' : BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedAdmiral_body.tga',
							'small',
							'F'
						),

		'StarfleetScienceMale' : BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedTeal_body.tga',
							'medium',
							'M'
						),

		'StarfleetOfficerMale' : BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedRed_body.tga',
							'medium',
							'M'
						),

		'StarfleetTacticalMale' : BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedGold_body.tga',
							'medium',
							'M'
						),

		'StarfleetAdmiralMale' : BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedAdmiral_body.tga',
							'medium',
							'M'
						),

		'RomulanMale' :		BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/Romulan_body.tga',
							'medium',
							'M'
						),

		'RomulanFemale' :	BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/Romulan_body.tga',
							'small',
							'F'
						),

		'Male' :		BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedCivilan_body.tga',
							'medium',
							'M'
						),

		'Female' :		BodyType(	'data/Models/Characters/Bodies/BodyFemM/BodyFemM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/FedFemCivilan_body.tga',
							'small',
							'F'
						),

		'Ferengi' :		BodyType(	'data/Models/Characters/Bodies/BodyMaleM/BodyMaleM.nif',
							'data/Models/Characters/Bodies/BodyMaleM/Ferengi_body.tga',
							'medium',
							'M'
						),	

		'Kessok' : 		BodyType(	'data/Models/Characters/Bodies/BodyKessok/BodyKessok.nif',
							'data/Models/Characters/Bodies/BodyKessok/kessok_body.tga',
							'large',
							'M'
						),
		
		'Klingon' : 		BodyType(	'data/Models/Characters/Bodies/BodyKlingon/BodyKlingon.nif',
							'data/Models/Characters/Bodies/BodyKessok/Klingon_body.tga',
							'large',
							'M'
						)

	}
	
		

