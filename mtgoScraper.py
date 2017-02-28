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
deckNamesDict = {"Afinity": ["Mox Opal", "others" ], 'Eldrazi Tron': [],}



url = "http://magic.wizards.com/en/articles/archive/mtgo-standings/competitive-modern-constructed-league-2017-02-22"
html = urllib.request.urlopen(url)
soup = bs(html, 'html.parser')

allDecks = []

for decklist in soup.find('div', class_='decklists'):
	oneDeck = Deck()
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

# for deck in allDecks:
# 	print ()
# 	print ('Next Deck')
# 	print ('Main Board')
# 	for card in deck.getMB():
# 		print (card.name, ' - ', card.number)
# 	print ()
# 	print ('Sideboard')
# 	for card in deck.getSB():
# 		print (card.name, ' - ', card.number)


   


