
from blackjack_deck import Deck

q = True
while q:
	deal = input("Want to be dealt in? y/n\n")
	if deal.lower() == 'y':

		
		# Creat instance of Deck class called deck, shuffle deck, deal hand to player and dealer.
		deck = Deck()
		deck.shuffle_deck()
		player = deck.deal_player_hand()
		dealer = deck.deal_dealer_hand()
		# Display player hand and one of dealer's cards.
		print("You were dealt the following cards: {}".format(player))
		
		print("Dealer is showing one of their cards: {}".format(dealer[0]))

		# Player has the option to hit or stay
		while True:
			hit = input("Do you want to hit? 'y' or 'n' ")
			if hit == 'y' and deck.get_player_total()<=21:
				deck.player_hit_me()
				
				print("You were dealt the following card: {}".format(player[-1]))
				print("Your current total: {}".format(deck.get_player_total()))
			else:
				break	

		# Display player deck and total
		player_total = deck.get_player_total()
		print("Your hand: {}".format(player))
		print(player_total)

		# Dealer tries to beat player
		dealer_total = deck.optimize_dealer()

		# Display dealer hand and total
		print("The dealer hand: {}".format(dealer))
		print(dealer_total)

		# Declare Winner!
		if player_total > dealer_total and player_total <= 21:
			print("Player wins with a score of {} over dealer score of {}".format(player_total, dealer_total))
		elif dealer_total > 21:
			print("Player wins with a score of {}. Dealer went over 21".format(player_total))
		elif player_total > 21:
			print("Dealer wins with a score of {}. Player went over 21".format(dealer_total))			
		else:
			print("Dealer wins with a score of {} vs. player score of {}".format(dealer_total, player_total))	

	else:
		q = False


