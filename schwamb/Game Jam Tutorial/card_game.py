# Holds all the functions for the logic/gameplay of a computerized version of Up & Down the River
import random
from game_graphics import *

##### get_n_players() #####
# get_n_players asks the user for the number of players
#
# Parameters:
# Returns:
#     n_players: the number of players
def get_n_players():
    n_players = int(input("How many people are playing?"))
    return n_players

def get_player_names(n_players):
    player_names = []
    for i in range(n_players):
        if i == 0:
            player_names.append(input("What is the 1st player's name?"))
        elif i == 1:
            player_names.append(input("What is the 2nd player's name?"))
        elif i == 2:
            player_names.append(input("What is the 3rd player's name?"))
        else:
            player_names.append(input(f"What is the {i+1}th player's name?"))
    return player_names

def calculate_first_deal(n_players):
    n_cards = 52 // n_players
    return n_cards

def deal_cards(n_cards,player_names):
    n_players = len(player_names)
    deck = ['Ace of Diamonds','King of Diamonds','Queen of Diamonds','Jack of Diamonds','10 of Diamonds','9 of Diamonds','8 of Diamonds',
               '7 of Diamonds','6 of Diamonds','5 of Diamonds','4 of Diamonds','3 of Diamonds','2 of Diamonds',
               'Ace of Clubs','King of Clubs','Queen of Clubs','Jack of Clubs','10 of Clubs','9 of Clubs','8 of Clubs',
               '7 of Clubs','6 of Clubs','5 of Clubs','4 of Clubs','3 of Clubs','2 of Clubs',
               'Ace of Hearts','King of Hearts','Queen of Hearts','Jack of Hearts','10 of Hearts','9 of Hearts','8 of Hearts',
               '7 of Hearts','6 of Hearts','5 of Hearts','4 of Hearts','3 of Hearts','2 of Hearts',
               'Ace of Spades','King of Spades','Queen of Spades','Jack of Spades','10 of Spades','9 of Spades','8 of Spades',
               '7 of Spades','6 of Spades','5 of Spades','4 of Spades','3 of Spades','2 of Spades']
    hands = dict()
    for player in player_names:
        hands[player] = []
        for j in range(n_cards):
            card_index = random.randint(0,len(deck)-1)
            card = deck[card_index]
            deck.pop(card_index)
            hands[player].append(card)
        hands[player] = sort_hand(hands[player])

    if len(deck)>0:
        last_card_index = random.randint(0,len(deck)-1)
        last_card = deck[last_card_index]
        _, trump_suit = last_card.split(' of ')
    else:
        trump_suit = "Spades"
    return hands, trump_suit

def get_bids(player_names,hands,n_cards):
    bids = dict()
    for player in player_names:
        show_cards(hands,player)
        bids[player] = int(input("How many tricks is " + player + " bidding? "))
        while player == player_names[-1] and sum(bids.values()) == n_cards:
            invalid_bid = n_cards - sum(list(bids.values())[:-1])
            bids[player] = int(input("Invalid bid! You cannot bid "+str(invalid_bid)+". Try again: "))
    show_bids(sum(bids.values()),n_cards)

    return bids

def get_last_bid(player_names,hands,n_cards):
    bids = dict()
    for player in player_names:
        cards_to_show = []
        for player2 in player_names:
            if player != player2:
                cards_to_show.append(hands[player2][0])
        show_final_cards(cards_to_show,player)
        bids[player] = int(input("How many tricks is " + player + " bidding? "))
        while player == player_names[-1] and sum(bids.values()) == n_cards:
            invalid_bid = n_cards - sum(list(bids.values())[:-1])
            bids[player] = int(input("Invalid bid! You cannot bid "+str(invalid_bid)+". Try again: "))
    show_bids(sum(bids.values()),n_cards)

    return bids

def play_round(player_order,hands,trump_suit):
    tricks = dict()
    for player in player_order:
        tricks[player] = 0
    trump_broken = False
    while len(hands[player_order[0]]) > 1:
        led_suit = ""
        played_cards = []
        for player in player_order:
            if player == player_order[0]:
                leader = True
            else:
                leader = False
            show_cards(hands,player)
            card = play_card(hands[player],trump_suit,led_suit,trump_broken,leader)
            clear_text_output()
            _, card_suit = card.split(' of ')
            if leader:
                led_suit = card_suit
            if card_suit == trump_suit:
                trump_broken = True
            hands[player].remove(card)
            played_cards.append(card)
            show_trick(played_cards)
        winner = calculate_winner(played_cards,player_order,trump_suit,led_suit)
        tricks[winner] += 1
        show_tricks_won(tricks)
        player_order = rotate_player_order(player_order,winner)
    played_cards = []
    played_cards.append(hands[player_order[0]][0])
    _, led_suit = hands[player_order[0]][0].split(' of ')
    for player in player_order[1:]:
        played_cards.append(hands[player][0])
    show_trick(played_cards)
    winner = calculate_winner(played_cards,player_order,trump_suit,led_suit)
    tricks[winner] += 1
    show_tricks_won(tricks)
    return tricks

def play_card(hand, trump_suit, led_suit, trump_broken=False, leader=True):
    card = input("Which card would you like to play? ")
    while card not in hand:
        card = input("Invalid card. Please pick a card in your hand. ")
    _, card_suit = card.split(' of ')
    while card_suit == trump_suit and trump_broken == False and leader == True and not all(trump_suit in card for card in hand):
        card = input("Cannot play a "+trump_suit[:-1]+" as "+trump_suit+" have not been broken yet. Please choose a different card.")
        _, card_suit = card.split(' of ')
    while card_suit != led_suit and leader == False and any(led_suit in card for card in hand):
        card = input("Must play a "+led_suit[:-1]+". Please choose a different card.")
        _, card_suit = card.split(' of ')
    return card

def calculate_winner(played_cards,player_names,trump_suit,led_suit):
    max_val = 0
    winner = ""
    for card in played_cards:
        card_val, card_suit = get_card_value(card)
        if card_suit == trump_suit:
            card_val += 15
        elif card_suit != led_suit:
            card_val = 0
        if card_val > max_val:
            max_val = card_val
            winner_idx = played_cards.index(card)
            winner = player_names[winner_idx]
    return winner

def rotate_player_order(player_order,winner):
    winner_idx = player_order.index(winner)
    player_order = player_order[winner_idx:] + player_order[:winner_idx]
    return player_order

def sort_hand(hand):
    sorted_hand = []
    for card in hand:
        card_val, card_suit = get_card_value(card)
        added = False
        for sorted_card in sorted_hand:
            sorted_card_val, sorted_card_suit = get_card_value(sorted_card)
            if compare_suits(card_suit, sorted_card_suit) < 0:
                sorted_hand.insert(sorted_hand.index(sorted_card),card)
                added = True
                break
            elif compare_suits(card_suit, sorted_card_suit) == 0:
                if card_val > sorted_card_val:
                    sorted_hand.insert(sorted_hand.index(sorted_card),card)
                    added = True
                    break
        if not added:
            sorted_hand.append(card)
    return sorted_hand

def get_card_value(card_str):
    card_char, card_suit = card_str.split(' of ')
    if len(card_char) > 2:
        if card_char[0] == 'A':
            card_val = 14
        elif card_char[0] == 'K':
            card_val = 13
        elif card_char[0] == 'Q':
            card_val = 12
        else:
            card_val = 11
    else:
        card_val = int(card_char)
    return card_val, card_suit 

def compare_suits(suit1, suit2):
    suit_ranks = {'Diamonds': 0, 'Clubs': 1, 'Hearts': 2, 'Spades': 3}
    diff = suit_ranks[suit1] - suit_ranks[suit2]
    return diff