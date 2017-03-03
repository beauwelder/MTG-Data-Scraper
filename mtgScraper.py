from bs4 import BeautifulSoup as bs
import urllib.request

class Card(object):
	def __init__(self):
		self.name = ''
		self.number = 0

class Deck(object):
	def __init__(self):
		self.deckName = ''
		self.dateWon = ''
		self.cards = []
		self.mainBoard = []
		self.sideBoard = []
		# self.creatures = []
		# self.instants = []
		# self.sorceries = []
		# self.planeswalkers = []
		# self.artifacts = []
		# self.enchantments = []
		# self.lands = []

	def getDeckName(self):
		return self.deckName

	def getDateWon(self):
		return self.dateWon

	def getCards(self):
		return self.cards

	def getMB(self):
		return self.mainBoard

	def getSB(self):
		return self.sideBoard

	# def getCreatures(self):
	# 	return self.creatures

	# def getInstants(self):
	# 	return self.instants

	# def getSorceries(self):
	# 	return self.sorceries

	# def getPlainswalkers(self):
	# 	return self.planeswalkers

	# def getArtifacts(self):
	# 	return self.artifacts

	# def getEnchanments(self):
	# 	return self.enchantments

	# def getLands(self):
	# 	return self.lands


#Dictionary of known decks
deckNames = {"Afinity": ["Mox Opal", "Darksteel Citadel", "Arcbound Ravager", "Vault Skirge", "Blinkmoth Nexus"], 
             "Eldrazi Tron": ["Urza's Tower", "Eldrazi Temple", "Wastes", "Thought-Knot Seer"], 
             "Death's Shadow Jund": ["Death's Shadow", "Street Wraith", "Tarmogoyf", "Traverse the Ulvenwald", "Thoughtseize"], 
             "Abzan Midrange": ["Liliana of the Veil", "Path to Exile", "Lingering Souls", "Tarmogoyf"], 
             "Jund Midrange": ["Liliana of the Veil", "Lighting Bolt", "Tarmogory", "Raging Ravine"], 
             "Bant Eldrazi": ["Eldrazi Temple", "Noble Hierarch", "Ancient Stirrings", "Path to Exile", "Thought-Knot Seer"], 
             "RG Valakut": ["Primeval Titan", "Summoner's Pact", "Valakut, the Molten Pinnacle"], 
             "Burn": ["Goblin Guide", "Eidolon of the Great Revel", "Lava Spike"],
             "Tron": ["Urza's Tower", "Sylvan Scrying", "Ancient Stirrings", "Chromatic Star"],
             "Grixis": ["Tasigur, the Golden Fang", "Serum Visions", "Lightning Bolt"],
             "Merfolk": ["Aether Vial", "Cursecatcher", "Lord of Atlantis"],
             "Abzan Company": ["Viscera Seer", "Kitchen Finks", "Collected Company", "Gavony Township"],
             "Dredge": ["Narcomoeba", "Cathartic Reunion", "Conflagrate", "Prized Amalgam"],
             "Gifts Storm": ["Grapeshot", "Gifts Ungiven" "Past in Flames", "Baral, Chief of Compliance"],
             "Ad Nauseam": ["Simian Spirit Guide", "Angel's Grace", "Ad Nauseam"],
             "Infect": ["Glistener Elf", "Noble Hierarch", "Inkmoth Nexus", "Vines of Vastwood"],
             "Knightfall": ["Knight of the Reliquary", "Retreat to Coralhelm", "Noble Hierarch"],
             "Amulet Titan": ["Azusa, Lost but Seeking", "Primeval Titan", "Amulet of Vigot", "Sakura-Tribe Scout"],
             "Goryo's Vengeance": ["Goryo's Vengeance", "Griselbrand", "Simian Spirit Guide"],
             "Eldrazi & Taxes": ["Eldrazi Temple", "Aether Vial", "Thalia, Guardian of Thraben", "Eldrazi Displacer"],
             "Lantern Control": ["Code Shredder", "Lantern of Insight", "Ensnaring Bridge", "Mox Opal"],
             "Sun and Moon": ["Chalice of the Void", "Ensnaring Bridge", "Blood Moon", "Nahiri, the Harbinger"],
             "Bring to Light Scapeshift": ["Bring to Light", "Scapeshift", "Sakura-Tribe Elder"],
             "Jeskai": ["Snapcaster Mage", "Lightning Bolt", "Path to Exile"],
             "Elves": ["Heritage Druid", "Nettle Sentinel", "Elvish Archdruid", "Ezuri, Renegade Leader"],
             "Cheerios": ["Puresteel Paladin", "Sram, Senior Edificer", "Grapeshot", "Retract"],
             "Copy Cat": ["Saheeli Rai", "Felidar Guardian"],
             "Bant Spirits": ["Collected Company", "Selfless Spirit", "Drogskol Captain", "Spell Queller"],
             "Skred": ["Koth of the Hammer", "Skred", "Scrying Sheets"],
             "8 Rack": ["The Rack", "Skrieking Affliction", "Mutavault", "Smallpox"],
             "Soul Sisters": ["Serra Ascendant", "Soul Warden", "Ajani's Pridemate"],
             "Bogles": ["Slippery Bogle", "Daybreak Coronet", "Ethereal Armor"],
             "Living End": ["Deadshot Minotaur", "Living End", "Violent Outburst"]}


#for date in range(1)
url = "http://magic.wizards.com/en/articles/archive/mtgo-standings/competitive-modern-constructed-league-2017-02-22"
html = urllib.request.urlopen(url)
soup = bs(html, 'html.parser')

allDecks = []

for decklist in soup.find('div', class_='decklists'):
	oneDeck = Deck()
	oneDeck.dateWon = "2017-02-22"
	for mb in decklist.find_all('div', class_='sorted-by-overview-container sortedContainer'):
		for card in mb.find_all('span', class_='row'):
			oneCard = Card()
			cardCount = card.find('span', class_='card-count')
			cardName = card.find('span', class_='card-name')
			oneCard.number = cardCount.get_text()
			oneCard.name = cardName.get_text()
			oneDeck.cards.append(oneCard)
			oneDeck.mainBoard.append(oneCard)
	for sb in decklist.find_all('div', class_='sorted-by-sideboard-container'):
		for card in sb.find_all('span', class_='row'):
			oneCard = Card()
			cardCount = card.find('span', class_='card-count')
			cardName = card.find('span', class_='card-name')
			oneCard.number = cardCount.get_text()
			oneCard.name = cardName.get_text()
			oneDeck.cards.append(oneCard)
			oneDeck.sideBoard.append(oneCard)
	allDecks.append(oneDeck)

for deck in allDecks:
	print()
	print("Date Won: ", deck.getDateWon())
	print ()
	print ('Next Deck')
	print ('Main Board')
	for card in deck.getMB():
		print (card.name, ' - ', card.number)
	print ()
	print ('Sideboard')
	for card in deck.getSB():
		print (card.name, ' - ', card.number)


   


