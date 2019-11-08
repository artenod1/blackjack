from random import shuffle


class Deck:
	def __init__(self):
		suit = ['Heart', 'Diamond', 'Spade', 'Club']
		card = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
		self.deck = []
		self.player_hand = []
		self.dealer_hand = []
		self.player_total = 0
		self.dealer_total = 0
		for s in suit:
			for c in card:
				self.deck.append((s,c))


	def __repr__(self):
		return "Deck of {} cards".format(len(self.deck))	


	def shuffle_deck(self):
		"""Return the deck of cards in random order"""
		shuffle(self.deck)
		return self.deck

	def deal_player_hand(self):
		"""Deal two cards to the player"""
		self.player_hand = self.deck[0:2]
		self.deck = self.deck[2::]
		return self.player_hand		
			

	def deal_dealer_hand(self):
		"""Deal two cards to the dealer"""
		self.dealer_hand = self.deck[0:2]
		self.deck = self.deck[2::]
		return self.dealer_hand

	def player_hit_me(self):
		"""Add one card from deck to player hand and remove same card from deck."""
		self.player_hand.append(self.deck[0])
		self.deck = self.deck[1::]
		return self.player_hand	

	def dealer_hit_me(self):
		"""Add one card from deck to dealer hand and remove same card from deck."""
		self.dealer_hand.append(self.deck[0])
		self.deck = self.deck[1::]
		return self.dealer_hand						

	def get_player_total(self):
		"""Calculate player total from current player hand"""
		self.player_total = 0
		for i in range(len(self.player_hand)):
			if self.player_hand[i][-1] in 'KQJ':
				self.player_total += 10
			elif self.player_hand[i][-1] == 'A':
				self.player_total += int(input('1 or 11 for your Ace?\n' ))	
			else:
				self.player_total += int(self.player_hand[i][-1])	
		return self.player_total	

	def get_dealer_total(self):
		"""Calculate dealer total from current dealer hand"""
		self.dealer_total = 0
		for i in range(len(self.dealer_hand)):
			if self.dealer_hand[i][-1] in 'KQJ':
				self.dealer_total += 10
			elif self.dealer_hand[i][-1] == 'A':
				if self.dealer_total + 11 in range(16,22):
					self.dealer_total += 11
				else:
					self.dealer_total += 1		
			else:
				self.dealer_total += int(self.dealer_hand[i][-1])	
		return self.dealer_total		

	def optimize_dealer(self):
		"""Function optimizes dealer hand to beat player total"""
		self.dealer_total = self.get_dealer_total()
		if self.dealer_total < self.player_total and self.player_total <= 21:
			self.dealer_hit_me()
			return self.optimize_dealer()
		else:
			return self.get_dealer_total()