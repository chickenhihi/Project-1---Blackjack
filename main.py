from art import logo
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def current_score(list_cards):
    '''Returns the sum of the cards'''
    sum = 0 
    n = 0 #number of appearances of A
    for card in list_cards:
        if card == 11:
            n += 1  
    for card in list_cards:
        sum += card
    while n != 0 and sum > 21:
        sum -= 10
        n -= 1
    return sum

def play_game():
    print(logo)
    
    your_cards = []
    your_cards.append(deal_card())
    your_cards.append(deal_card())
    your_score = current_score(your_cards)
    print(f"    Your cards: {your_cards}, current score: {your_score}")

    dealer_card = []
    dealer_card.append(deal_card())
    dealer_card.append(deal_card())
    print(f"    Computer's first card is {dealer_card[0]}")
    dealer_score = current_score(dealer_card)

    while your_score <= 21:
        play = input("Type 'y' to get another card, type 'n' to pass: ")
        if play == 'y' :
            your_cards.append(deal_card())
            your_score = current_score(your_cards)
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            print(f"    Computer's first card is {dealer_card[0]}")
        elif play == 'n':
            while dealer_score < 17:
                dealer_card.append(deal_card())
                dealer_score = current_score(dealer_card)
            print(f"    Your final hand: {your_cards}, final score: {your_score}")
            print(f"    Computer's final hand: {dealer_card}, final score: {dealer_score}")
            if your_score > dealer_score or dealer_score > 21:
                print("You win !")
            elif your_score == dealer_score:
                print("Draw !")
            else:
                print("You lose !")
            break
        if your_score > 21:
            print("You lose !")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()