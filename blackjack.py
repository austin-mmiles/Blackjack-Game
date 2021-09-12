from random import betavariate
from game_components import *

player = Player(100)
bet = 0

game_finished = False
while not game_finished:
    while True:
        print("Welcome to BlackJack!")
        playing = input("Would you like to play a hand? (Y/N): ")
        if playing.lower() not in ['y', 'n']:
            print("Invalid option")
        elif playing.lower() == 'n':
            game_finished = True
            print("Come back next time")
            break
        else:
            player.hand = Hand()
            player.wallet += bet
            bet = 0
            dealer = Dealer()
            while True:
                wager_amount = int(
                    input("Enter wager amount (current balance: {}): ". format(player.wallet)))
                if wager_amount <= player.wallet:
                    player.wallet -= wager_amount
                    break
            break

    if game_finished == True:
        break

    for card in range(2):
        dealer.deal(player)
        dealer.deal(dealer)

    dealer.print_opening_hand()
    busted = False
    blackjack = False
    end_turn = False
    while not end_turn:
        if player.hand.hand_value() == 21:
            print("BlackJack!")
            blackjack = True
            end_turn = True
        elif player.hand.hand_value() > 21:
            print("Busted!")
            player.print_hand()
            busted = True
            end_turn = True
        else:
            player.print_hand()
            player_decision = input(
                "Would you like to Hit ('H') or Stand ('S')")
            if player_decision.lower() == 'h':
                dealer.deal(player)
                print("Your card is ", player.hand.cards_in_hand[-1])
            elif player_decision.lower() == 's':
                end_turn = True
            else:
                print("Invalid Choice! Try again")

    while dealer.hand.hand_value() < 17 and not busted and not blackjack:
        print("Dealer will draw card...")
        dealer.deal(dealer)
        print("Dealer draws {}".format(dealer.hand.cards_in_hand[-1]))

    dealer_hand_value = dealer.hand.hand_value()
    player_hand_value = player.hand.hand_value()

    if busted:
        print("Dealer wins")
        input("Press any Key to Continue")
    elif blackjack:
        bet = wager_amount * 2.5
        print("Winner Winner Chicken Dinnner!")
    elif dealer_hand_value > 21 or dealer_hand_value < player_hand_value:
        bet = wager_amount * 2
        print("Winner!")
        input("Press any Key to Continue")
    elif dealer_hand_value == player_hand_value:
        bet = wager_amount
        print("Its a push!")
        input("Press any Key to Continue")
    elif dealer_hand_value > player_hand_value:
        print("Dealer wins")
        input("Press any Key to Continue")
